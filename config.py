from dotenv import load_dotenv
import os
import streamlit as st


ENV = os.getenv("ENVIRONMENT", "dev")

if ENV == "prod":
    load_dotenv(".env.prod")
else:
    load_dotenv(".env.dev")

BASE_URL = st.secrets["BASE_URL"] or os.getenv("BASE_URL")