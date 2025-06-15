import requests
import streamlit as st
from model.FeedbackModel import userFeedback

def addUserFeedback(userFeedback: userFeedback):
    try:
        response = requests.post("http://127.0.0.1:8000/model/generation", json = userFeedback.dict())
        if response.status_code == 200:
            return response.json()
        else:
            return "Something went wrong :("
    except Exception as e:
        return {"error": str(e)}
    