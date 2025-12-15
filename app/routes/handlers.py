from flask import render_template, url_for, redirect, request, session
from pyresparser import ResumeParser
from app.services.recommend_service import RecommendSkills
from app.utils.resume_utils import calculate_resume_score, pdf_reader, fetch_yt_video
from app.models.courses import resume_videos, interview_videos
from werkzeug.utils import secure_filename
import tempfile
import os
import re
import random


def index_handler():
    return render_template('index.html')


def resume_upload_handler():
    return render_template('resume_upload.html')


def upload_resume_handler():
    if 'resume_file' not in request.files:
        return "No file part"
    pdf_file = request.files['resume_file']
    if pdf_file.filename == '':
        return "No selected file"
    if pdf_file and pdf_file.filename.endswith('.pdf'):
        try:
            filename = secure_filename(pdf_file.filename)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(pdf_file.read())
                tmp_path = tmp.name
            resume_parser = ResumeParser(tmp_path)
            resume_data = resume_parser.get_extracted_data()
            session['current_file_path'] = tmp_path
            session['resume_data'] = resume_data
            action = request.form.get('action')
            if action == 'analyze':
                return redirect(url_for('main.analyse'))
            elif action == 'recommend':
                return redirect(url_for('main.recommender'))
        except Exception as e:
            return f"Error processing file: {e}"
    return "Invalid file format. Please upload a PDF."


def analyse_handler():
    resume_data = session.get('resume_data')
    current_file_path = session.get('current_file_path')
    if not resume_data or not current_file_path or not os.path.exists(current_file_path):
        return "Session expired or file missing", 400
    user_skills = resume_data.get('skills', [])
    field, skills, courses = RecommendSkills().recommend_skills_and_courses(user_skills, num_courses=5)
    resume_text = pdf_reader(file_path=current_file_path)
    score, tips = calculate_resume_score(resume_text)
    if os.path.exists(current_file_path):
        os.remove(current_file_path)
    return render_template('analyse.html', resume_data=resume_data, field=field, skills=skills, courses=courses, score=score, tips=tips)


def extract_video_id(link):
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex, link)
    return match.group(1) if match else None


def recommender_handler():
    resume_vid = random.choice(resume_videos)
    interview_vid = random.choice(interview_videos)
    resume_title = fetch_yt_video(resume_vid)
    interview_title = fetch_yt_video(interview_vid)
    resume_id = extract_video_id(resume_vid)
    interview_id = extract_video_id(interview_vid)
    return render_template("recommend.html", resume_title=resume_title, interview_title=interview_title, resume_link=resume_vid, interview_link=interview_vid, resume_id=resume_id, interview_id=interview_id)
