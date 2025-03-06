from dotenv import load_dotenv
load_dotenv() ## load all the environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

## Configure our API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to Load Google Gemini Model and provide SQL Query as response
def get_gemini_response(question,prompt):
  model=genai.GenerativeModel('gemini-2.0-flash')
  response=model.generate_content([prompt[0], question])
  return response.text

## Function to retrieve query from the SQL Database
def read_sql_query(sql,db):
  conn=sqlite3.connect(db)
  cur=conn.cursor()
  cur.execute(sql)
  rows=cur.fetchall()
  conn.commit()
  conn.close()
  for row in rows:
    print(row)
  return rows

## Define your Prompt
prompt=[
   """
You are an expert in converting English questions to SQL query! The SQL database has the name STUDENT and has the following colums - NAME, CLASS, SECTION and MARKS \n\nFor example, \nExample 1 - How many entries of records are present?, the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ; \nExample 2 - Tell me all the students studying in Data Science class?, the SQL command will be something like this SELECT * FROM STUDENT where CLASS="Data Science"; also the sql code shoud not have ``` in beginning or end and sql word in the output
   """
]

## Streamlit App
st.set_page_config(page_title="Gemini Model 2.0 Flash")
st.header("Gemini App To Retrieve SQL Data via Text (Natural Language to SQL Query)")
question=st.text_input("Enter your prompt in Natural Language: ", key="input")
submit=st.button("Ask the question")

## if submit is clicked
if submit:
  response=get_gemini_response(question,prompt)
  print(response)
  st.subheader("NL (Your Prompt) to SQL Query")
  st.markdown(f'<h5 style="color: green;">{response}</h4>', unsafe_allow_html=True)
  data=read_sql_query(response,"student.db")
  st.markdown('<hr >', unsafe_allow_html=True)
  st.subheader("The Response from Database via SQL Query")
  for row in data:
    print(row)
    st.markdown(f'<h5 style="color: green;">{row}</h4>', unsafe_allow_html=True)