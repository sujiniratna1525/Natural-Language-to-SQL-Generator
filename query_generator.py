import requests

def generate_sql(question):

    prompt = f"""
Convert the user question into SQL query.

Database: student
Table: students

Columns:
id
name

Rules:
1. Return ONLY SQL query.
2. explanation.
3. No markdown.
4. No extra text.

Question:
{question}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma:2b",
            "prompt": prompt,
            "stream": False
        }
    )

    sql_query = response.json()["response"]

    sql_query = sql_query.replace("```sql", "")
    sql_query = sql_query.replace("```", "")
    sql_query = sql_query.replace("**", "")
    sql_query = sql_query.strip()

    return sql_query