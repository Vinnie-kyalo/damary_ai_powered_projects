import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def evaluate_application(resume_text, job_description):
    prompt = f"""
    Evaluate this job application:

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Return structured result with:
    - score (0-100)
    - strengths
    - weaknesses
    - recommendations
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content