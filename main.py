from fastapi import FastAPI

from app.schemas import ResumeRequest
from app.skill_extractor import extract_skills
from app.matcher import calculate_similarity

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Resume Screening API Running"
    }

@app.post("/match-resume")
def match_resume(data: ResumeRequest):

    jd_skills = extract_skills(
        data.job_description
    )

    resume_skills = extract_skills(
        data.resume_text
    )

    matched_skills = sorted(list(
        set(jd_skills) &
        set(resume_skills)
    ))

    missing_skills = sorted(list(
        set(jd_skills) -
        set(resume_skills)
    ))

    score = calculate_similarity(
        data.job_description,
        data.resume_text
    )

    if score >= 70:
        explanation = (
            f"Strong match. Candidate possesses "
            f"{', '.join(matched_skills)}. "
            f"Missing skills: {', '.join(missing_skills)}."
        )

    elif score >= 40:
        explanation = (
            f"Moderate match. Candidate has "
            f"{', '.join(matched_skills)} but lacks "
            f"{', '.join(missing_skills)}."
        )

    else:
        explanation = (
            "Low match. Resume does not align well "
            "with the job description."
        )

    return {
        "match_score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "explanation": explanation
    }