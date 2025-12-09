import PyPDF2
from yt_dlp import YoutubeDL


def calculate_resume_score(resume_text):
    tips = []
    score = 0

    if 'Objective' in resume_text:
        score += 20
        tips.append(("[+] Awesome! You have added Objective", True))
    else:
        tips.append(("[-] Please add your career objective, it will give your career intention to the recruiters.", False))

    if 'Declaration' in resume_text:
        score += 20
        tips.append(("[+] Awesome! You have added Declaration", True))
    else:
        tips.append(("[-] Please add a Declaration. It gives assurance that the information is accurate.", False))

    if 'Hobbies' in resume_text or 'Interests' in resume_text:
        score += 20
        tips.append(("[+] Awesome! You have added your Hobbies", True))
    else:
        tips.append(("[-] Please add Hobbies or Interests. They show your personality to recruiters.", False))

    if 'Achievements' in resume_text:
        score += 20
        tips.append(("[+] Awesome! You have added your Achievements", True))
    else:
        tips.append(("[-] Please add Achievements. They show you're capable of excelling in a role.", False))

    if 'Projects' in resume_text:
        score += 20
        tips.append(("[+] Awesome! You have added your Projects", True))
    else:
        tips.append(("[-] Please add Projects. It shows relevant practical work.", False))

    return score, tips


def pdf_reader(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text


def fetch_yt_video(link):
    ydl_opts = {}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=False)
        return info['title']
