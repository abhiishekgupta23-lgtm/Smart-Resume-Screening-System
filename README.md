# Smart Resume Screening System

## Overview

This project is an AI-powered Resume Screening System that matches resumes against a Job Description (JD) using TF-IDF and Cosine Similarity.

## Features

* Resume Skill Extraction
* Job Description Analysis
* TF-IDF Based Matching
* Cosine Similarity Scoring
* Matched Skills Identification
* Missing Skills Detection
* FastAPI Endpoint

## Tech Stack

* Python
* FastAPI
* Scikit-Learn
* TF-IDF Vectorizer

## Installation

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python -m uvicorn app.main:app --reload
```

## API Endpoint

POST /match-resume

### Sample Request

```json
{
  "job_description": "Looking for Python FastAPI SQL Machine Learning developer",
  "resume_text": "I know Python SQL Pandas Machine Learning"
}
```

### Sample Response

```json
{
  "match_score": 41.12,
  "matched_skills": ["python", "sql", "machine learning"],
  "missing_skills": ["fastapi"],
  "explanation": "Candidate matches 3 required skills and is missing 1 skills."
}
```

## Approach

1. Extract skills from Job Description and Resume.
2. Convert both texts into TF-IDF vectors.
3. Calculate Cosine Similarity between vectors.
4. Generate Match Score, Matched Skills, Missing Skills and Explanation.


# Smart-Resume-Screening-System