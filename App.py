from flask import Flask, render_template, url_for, redirect, request , session
from pyresparser import ResumeParser
from Utils import RecommendSkills , calculate_resume_score , pdf_reader , fetch_yt_video
import PyPDF2 
from werkzeug.utils import secure_filename
import tempfile
from Courses import resume_videos , interview_videos
import os  
import re
import random 
app = Flask(__name__)
app.secret_key = "kyahisecrethai"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume_upload')
def resume_upload():
    return render_template('resume_upload.html')


@app.route('/upload_resume', methods=['POST'])
def upload_resume():
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
                return redirect(url_for('analyse'))
            elif action == 'recommend':
                return redirect(url_for('recommender'))

        except Exception as e:
            return f"Error processing file: {e}"

    return "Invalid file format. Please upload a PDF."

# @app.route('/upload_resume', methods=['POST'])
# def upload_resume():
#     if 'resume_file' not in request.files:
#         return "No file part", 400

#     resume_file = request.files['resume_file']

#     if resume_file.filename == '':
#         return "No selected file", 400

#     if resume_file:
#         os.makedirs('uploads', exist_ok=True)
#         filename = secure_filename(resume_file.filename)
#         file_path = os.path.join('uploads', filename)
#         resume_file.save(file_path)

#         resume_data = ResumeParser(file_path).get_extracted_data()

#         # Save everything to session
#         session['current_file_path'] = file_path
#         session['filename'] = filename
#         session['resume_data'] = resume_data

#         return redirect(url_for('analyse'))

@app.route('/analyse')
def analyse():
    resume_data = session.get('resume_data')
    current_file_path = session.get('current_file_path')

    if not resume_data or not current_file_path or not os.path.exists(current_file_path):
        return "Session expired or file missing", 400

    user_skills = resume_data.get('skills', [])
    field, skills, courses = RecommendSkills().recommend_skills_and_courses(user_skills, num_courses=5)

    resume_text = pdf_reader(file_path=current_file_path)
    score, tips = calculate_resume_score(resume_text)

    # Optional: delete file after analysis
    if os.path.exists(current_file_path):
        os.remove(current_file_path)

    return render_template('analyse.html', resume_data=resume_data, field=field, skills=skills, courses=courses, score=score, tips=tips)

def extract_video_id(link):
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex, link)
    return match.group(1) if match else None

@app.route('/recommender')
def recommender():
    resume_vid = random.choice(resume_videos)
    interview_vid = random.choice(interview_videos)

    resume_title = fetch_yt_video(resume_vid)
    interview_title = fetch_yt_video(interview_vid)

    resume_id = extract_video_id(resume_vid)
    interview_id = extract_video_id(interview_vid)

    return render_template("recommend.html",
                           resume_title=resume_title,
                           interview_title=interview_title,
                           resume_link=resume_vid,
                           interview_link=interview_vid,
                           resume_id=resume_id,
                           interview_id=interview_id)


if __name__ == '__main__':
    app.run(debug=True)