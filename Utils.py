import random 
from Courses import ds_course, web_course, android_course, ios_course, uiux_course 
import PyPDF2
from yt_dlp import YoutubeDL  # use yt_dlp instead of youtube_dl if using updated version


ds_keyword = ['tensorflow', 'keras', 'pytorch', 'machine learning', 'deep learning', 'flask', 'streamlit']
web_keyword = ['react', 'django', 'node js', 'react js', 'php', 'laravel', 'magento', 'wordpress',
               'javascript', 'angular js', 'c#', 'flask']
android_keyword = ['android', 'android development', 'flutter', 'kotlin', 'xml', 'kivy']
ios_keyword = ['ios', 'ios development', 'swift', 'cocoa', 'cocoa touch', 'xcode']
uiux_keyword = ['ux', 'adobe xd', 'figma', 'zeplin', 'balsamiq', 'ui', 'prototyping', 'wireframes', 'storyframes',
                'adobe photoshop', 'photoshop', 'editing', 'adobe illustrator', 'illustrator', 'adobe after effects',
                'after effects', 'adobe premier pro', 'premier pro', 'adobe indesign', 'indesign', 'wireframe',
                'solid', 'grasp', 'user research', 'user experience']


class RecommendSkills : 
      def __init__(self):
            pass 


      def get_random_courses(self , course_list, n):
            random.shuffle(course_list)
            return course_list[:n]
      

      def recommend_skills_and_courses(self , user_skills, num_courses=5):
            user_skills_lower = [skill.lower() for skill in user_skills]

            for skill in user_skills_lower:
                  if skill in ds_keyword:
                        return (
                        'Data Science',
                        ['Data Visualization', 'Predictive Analysis', 'Statistical Modeling', 'Data Mining',
                        'Clustering & Classification', 'Data Analytics', 'Quantitative Analysis', 'Web Scraping',
                        'ML Algorithms', 'Keras', 'Pytorch', 'Probability', 'Scikit-learn', 'Tensorflow', "Flask", 'Streamlit'],
                              self.get_random_courses(ds_course, num_courses)
                        )

                  elif skill in web_keyword:
                        return (
                        'Web Development',
                        ['React', 'Django', 'Node JS', 'React JS', 'PHP', 'Laravel', 'Magento', 'WordPress',
                        'JavaScript', 'Angular JS', 'C#', 'Flask', 'SDK'],
                              self.get_random_courses(web_course, num_courses)
                        )

                  elif skill in android_keyword:
                        return (
                        'Android Development',
                        ['Android', 'Android development', 'Flutter', 'Kotlin', 'XML', 'Java', 'Kivy',
                        'GIT', 'SDK', 'SQLite'],
                              self.get_random_courses(android_course, num_courses)
                        )

                  elif skill in ios_keyword:
                        return (
                        'iOS Development',
                        ['iOS', 'iOS Development', 'Swift', 'Cocoa', 'Cocoa Touch', 'Xcode',
                        'Objective-C', 'SQLite', 'Plist', 'StoreKit', "UI-Kit", 'AV Foundation', 'Auto-Layout'],
                              self.get_random_courses(ios_course, num_courses)
                        )

                  elif skill in uiux_keyword:
                        return (
                        'UI-UX Development',
                        ['UI', 'User Experience', 'Adobe XD', 'Figma', 'Zeplin', 'Balsamiq', 'Prototyping', 'Wireframes',
                        'Storyframes', 'Adobe Photoshop', 'Editing', 'Illustrator', 'After Effects',
                        'Premier Pro', 'Indesign', 'Wireframe', 'Solid', 'Grasp', 'User Research'],
                              self.get_random_courses(uiux_course, num_courses)
                        )

            return ('General', [], [])  



def calculate_resume_score(resume_text):
    tips = []
    score = 0

    # 1. Objective
    if 'Objective' in resume_text:
        score += 20
        tips.append(("[+] Awesome! You have added Objective", True))
    else:
        tips.append(("[-] Please add your career objective, it will give your career intention to the recruiters.", False))

    # 2. Declaration
    if 'Declaration' in resume_text:
        score += 20
        tips.append(("[+] Awesome! You have added Declaration", True))
    else:
        tips.append(("[-] Please add a Declaration. It gives assurance that the information is accurate.", False))

    # 3. Hobbies / Interests
    if 'Hobbies' in resume_text or 'Interests' in resume_text:
        score += 20
        tips.append(("[+] Awesome! You have added your Hobbies", True))
    else:
        tips.append(("[-] Please add Hobbies or Interests. They show your personality to recruiters.", False))

    # 4. Achievements
    if 'Achievements' in resume_text:
        score += 20
        tips.append(("[+] Awesome! You have added your Achievements", True))
    else:
        tips.append(("[-] Please add Achievements. They show you're capable of excelling in a role.", False))

    # 5. Projects
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