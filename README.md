# Feedback Fusion UI

A Streamlit-based frontend for collecting product feedback, evaluating it using a language model (Flan-T5-base), and classifying it as positive or negative using an LLM-powered sentiment analysis system.

![alt text](image-1.png)

# Features

- Collects user feedback on products.
- Integrates with FastAPI backend and MongoDB.
- Uses Flan-T5-base model to classify feedback sentiment
- Clean UI built with Streamlit in Python.

# Tech Stack

- **Frontend**: Streamlit (Python)
- **Backend**: FastAPI (connected via API)
- **Model**: Flan-T5-base (LLM for sentiment analysis)
- **Database**: MongoDB

# Project Structure

feedback-fusion-frontend/
├── app.py                   # Main Streamlit app
├── service/
│   ├── productApi.py        # Fetch product details from backend
│   └── feedbackApi.py       # Send feedback data to backend
├── model/
│   └── FeedbackModel.py     # Feedback data model using Pydantic
└── README.md


# Installation

- Clone the repository

Install the dependencies
- pip install streamlit pydantic

Run the application
- streamlit run app.py
