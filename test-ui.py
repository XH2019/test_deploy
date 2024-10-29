# -*- coding: utf-8 -*-
"""ui.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1emOL9AYrdn_Q3wqwaEblkEjce6-O2mJN
"""
import os
import streamlit as st
import requests

st.title("Resume-Job Description Matcher")

resume = st.text_area("Paste your resume here")
job_description = st.text_area("Paste the job description here")

if st.button("Match"):
    if resume and job_description:
        #api_endpoint = os.environ.get('API_ENDPOINT')  # Get the API endpoint
        api_endpoint = st.secrets["API_ENDPOINT"] # Get the API endpoint
        # Error handling in case the environment variable is not set
        if api_endpoint is None:
            st.error("API endpoint not found. Please check your configuration.")
        else:
            try:
                response = requests.post(f'{api_endpoint}/test', data={'resume': resume, 'job_description': job_description})
                response.raise_for_status()  # Raise an exception for bad status codes
                result = response.json()
                st.write(f"Match Score: {result['score']}")
                # ... display gap analysis ...
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to the API: {e}")
    else:
        st.write("Please enter both a resume and a job description.")
