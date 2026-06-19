# Decision Prediction Engine

## Vision

A web application that allows users to define arbitrary decision problems,
create custom predictors, enter historical observations, and automatically
train/evaluate machine learning models to predict future outcomes.

Examples:
- Should I accept this job?
- Should I buy this?
- Will this project succeed?

The system is generic and should not contain hardcoded predictors.

## Current Architecture

decision-prediction-engine/
│
├── backend/
│   └── app/
│       ├── main.py
│       ├── models/
│       ├── training/
│       ├── prediction/
│       └── database/
│
├── frontend/
├── data/
├── notebooks/
└── tests/

## Tech Stack

- Python
- FastAPI
- Uvicorn
- SQLite (initially)
- SQLAlchemy
- scikit-learn

## Roadmap

Phase 0 - Environment Setup (DONE)
This phase involved creating the intial architecture along with creating a virtual environment with the appropriate packages.
Phase 1 - Data Model Design
Phase 2 - Database Layer
Phase 3 - API Layer
Phase 4 - First End-to-End Workflow
Phase 5 - Data Processing Pipeline
Phase 6 - Single Model Training
Phase 7 - Model Comparison Engine
Phase 8 - Prediction Engine
Phase 9 - Explainability
Phase 10 - Frontend

## Decisions Made

- User-defined predictors
- User-defined decision categories
- Support both classification and regression
- Automatic model comparison
- FastAPI backend
- Focus on ML/statistics learning
