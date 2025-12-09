import random
from app.models.courses import (
    ds_course, web_course, android_course, 
    ios_course, uiux_course
)

ds_keyword = ['tensorflow', 'keras', 'pytorch', 'machine learning', 'deep learning', 'flask', 'streamlit']
web_keyword = ['react', 'django', 'node js', 'react js', 'php', 'laravel', 'magento', 'wordpress',
               'javascript', 'angular js', 'c#', 'flask']
android_keyword = ['android', 'android development', 'flutter', 'kotlin', 'xml', 'kivy']
ios_keyword = ['ios', 'ios development', 'swift', 'cocoa', 'cocoa touch', 'xcode']
uiux_keyword = ['ux', 'adobe xd', 'figma', 'zeplin', 'balsamiq', 'ui', 'prototyping', 'wireframes', 'storyframes',
                'adobe photoshop', 'photoshop', 'editing', 'adobe illustrator', 'illustrator', 'adobe after effects',
                'after effects', 'adobe premier pro', 'premier pro', 'adobe indesign', 'indesign', 'wireframe',
                'solid', 'grasp', 'user research', 'user experience']


class RecommendSkills:
    def __init__(self):
        pass

    def get_random_courses(self, course_list, n):
        random.shuffle(course_list)
        return course_list[:n]

    def recommend_skills_and_courses(self, user_skills, num_courses=5):
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
