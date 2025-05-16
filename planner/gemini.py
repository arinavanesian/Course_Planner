import google.generativeai as genai
from django.conf import settings
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

model = genai.GenerativeModel('gemini-1.5-pro')

def generate_recommendation(student, available_courses):
    prompt = f"""
    As an AUA MS in CIS academic advisor, create a personalized course plan for:
    - Student: {student.name}
    - Concentration: {student.get_concentration_display()}
    - Completed Courses: {list(student.completed_courses.values_list('code', flat=True))}
    
    Degree Requirements:
    - 30 core credits + 1 ENV credit
    - 12 concentration credits
    - 6 free electives
    
    Available Courses:
    {available_courses}
    
    Provide:
    1. Recommended courses for next semester (3-5 courses)
    2. Justification for each recommendation
    3. Warnings about missing prerequisites
    4. Workload estimation (low/medium/high)
    """
    # In planner/gemini.py, temporarily add:
    print("API Key:", os.getenv('GEMINI_API_KEY'))  # Should show your key
    response = model.generate_content("Test prompt")
    print("Gemini Response:", response.text)
    response = model.generate_content(prompt)
    return response.text
