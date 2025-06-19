import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")  # Or use "gemini-1.5-pro"

# Read tasks from file
def read_tasks(filepath):
    with open(filepath, "r") as f:
        return f.read()

# Summarize and prioritize tasks using Gemini
def summarize_tasks(tasks):
    prompt = f"""
You are a smart task planning agent.
Given a list of tasks, categorize them into 3 priority buckets:
- High Priority
- Medium Priority
- Low Priority

Tasks:
{tasks}

Return the response in this format:
High Priority:
- task 1
- task 2

Medium Priority:
- task 1
- task 2

Low Priority:
- task 1
- task 2
"""
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    task_text = read_tasks("tasks.txt")
    summary = summarize_tasks(task_text)
    print("\nTask Summary\n")
    print("-" * 30)
    print(summary)
