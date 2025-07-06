# Resume Analyzer – Python Project by Shivam Dubey 

# Important industry skills list
#I am Vishal. I have experience in python, communication, teamwork, and data analysis. I worked on projects using github and sql. My strengths include problem solving and leadership.


important_skills = [
    "python", "communication", "teamwork", "leadership", "sql",
    "problem solving", "critical thinking", "html", "css", "javascript",
    "machine learning", "data analysis", "github", "project management"
]

# Ask user to paste entire resume in one go
resume_text = input("Paste your entire resume content in one line (no Enter in between):\n").lower()

# Analyze skills
present_skills = []
missing_skills = []

for skill in important_skills:
    if skill in resume_text:
        present_skills.append(skill)
    else:
        missing_skills.append(skill)

# Display results
print("\nResume Analysis Report")
print("-" * 25)
print(f"Skills Found ({len(present_skills)}): {', '.join(present_skills)}")
print(f"Skills Missing ({len(missing_skills)}): {', '.join(missing_skills)}")

# Word count check
word_count = len(resume_text.split())
print(f"\nWord Count: {word_count}")
if word_count < 100:
    print("Your resume seems too short. Try adding more content.")
elif word_count > 500:
    print("Your resume might be too long. Try keeping it more concise.")
else:
    print("Resume length looks fine.")

# Skill score
score = (len(present_skills) / len(important_skills)) * 100
print(f"\nResume Skill Score: {round(score, 2)} / 100")

# Suggestion
if score > 80:
    print("Excellent. Your resume looks strong.")
elif score > 50:
    print("Good. But there is room for improvement.")
else:
    print("Needs improvement. Add more relevant skills and details.")
