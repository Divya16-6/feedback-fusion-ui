import requests
import streamlit as st
from model.FeedbackModel import userFeedback
from config import BASE_URL

def addUserFeedback(userFeedback: userFeedback):
    try:
        response = requests.post(f"{BASE_URL}/model/generation", json = userFeedback.dict())
        if response.status_code == 200:
            return response.json()
        else:
            return "Something went wrong :("
    except Exception as e:
        return {"error": str(e)}
    