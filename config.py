from dotenv import load_dotenv
import os
import streamlit as st


ENV = os.getenv("ENVIRONMENT", "dev")

if ENV == "prod":
    load_dotenv(".env.prod")
else:
    load_dotenv(".env.dev")

BASE_URL = os.getenv("BASE_URL") or st.secrets["BASE_URL"]