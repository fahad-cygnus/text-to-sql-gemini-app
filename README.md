# SQL Query Generator with Google Gemini

This project is a Streamlit application that utilizes the Google Gemini model to convert English questions into SQL queries. It retrieves data from a SQLite database based on the generated SQL queries.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Code Explanation](#code-explanation)

## Prerequisites

Before you begin, ensure you have the following installed:
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
- Python 3.10

## Setup Instructions

1. **Create a Conda Environment**

   To set up the environment for Python and install the necessary packages, run the following commands in your terminal:

   ```bash
   conda create -p venv python==3.10 -y
   conda activate venv/
   ```

2. **Install Required Packages**

   Inside the activated environment, install the required packages by running:

   ```bash
   pip install -r requirements.txt
   ```

3. **Create Database Tables and Insert Values**

   To create the necessary database tables and insert initial values, execute the following command:

   ```bash
   python sql.py
   ```

## Running the Application

To run the Streamlit application, use the following command:

```bash
streamlit run app.py
```

This will start the application, and you can access it in your web browser.

## Code Explanation

### `app.py`

- **Imports and Configuration**: The application imports necessary libraries, loads environment variables, and configures the Google Gemini API key.
  
- **Function `get_gemini_response`**: This function takes a question and a prompt, uses the Gemini model to generate a SQL query based on the input question.

- **Function `read_sql_query`**: This function connects to the SQLite database, executes the provided SQL query, and returns the results.

- **Streamlit Interface**: The application sets up a simple user interface where users can input their questions. Upon submission, it generates a SQL query and retrieves data from the database.

### `sql.py`

- **Database Connection**: This script connects to a SQLite database and creates a table named `STUDENT` with columns for `NAME`, `CLASS`, `SECTION`, and `MARKS`.

- **Inserting Records**: It inserts several records into the `STUDENT` table for demonstration purposes.

- **Displaying Records**: After inserting the records, it retrieves and prints all entries from the `STUDENT` table.

## Conclusion

This project demonstrates how to leverage the Google Gemini model to convert natural language questions into SQL queries and retrieve data from a SQLite database. Follow the setup instructions to get started and explore the functionality of the application.