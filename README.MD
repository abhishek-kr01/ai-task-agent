# 🧠 AI Task Planner Agent using Gemini API

This project is a simple yet powerful **AI agent** that reads a list of tasks from a `.txt` file and uses **Google's Gemini API** to intelligently categorize them into:

- ✅ High Priority
- ⚠️ Medium Priority
- 💤 Low Priority

It simulates how an intelligent assistant would prioritize your to-do list using Generative AI!

---

## 🚀 Demo Output

### 🔹 Input (`tasks.txt`):

```

Fix login bug
Buy groceries
Respond to HR email
Prepare for presentation
Call Mom
Schedule dentist appointment

```

### 🔸 Output (Terminal):

```

## Task Summary

High Priority:

* Fix login bug
* Prepare for presentation

Medium Priority:

* Respond to HR email
* Schedule dentist appointment

Low Priority:

* Buy groceries
* Call Mom

```

---

## 💡 Features

- 📥 Reads plain-text task lists
- 🤖 Uses Gemini LLM to prioritize tasks contextually
- 🔐 Secure API key handling using `.env`
- 🧠 Acts as a smart agent with zero manual rules

---

## 🛠️ Tech Stack

- Python 3.8+
- [Google Gemini API](https://ai.google.dev/)
- `google-generativeai` SDK
- `python-dotenv` for environment variable management

---

## 📦 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/abhishek-kr01/ai-task-agent.git
   cd ai-task-agent
   ```

````

2. **Create `.env` file**

   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

   > ⚠️ *Never share your real API key publicly.*

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the agent**

   ```bash
   python task_agent.py
   ```

---

ai-task-agent/
├── task_agent.py         # Main script
├── tasks.txt             # Your task input file
├── .env.example          # Template for env file (no key included)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

```

---

## ✍️ How It Works

* The script reads tasks from `tasks.txt`
* Sends them to Gemini API with a smart prompt
* Outputs a categorized list based on priority buckets
* Acts as a beginner-friendly AI agent in action

---

## 📌 Sample Use Cases

* Personal daily task prioritization
* Lightweight intelligent assistant demos
* GenAI + LLM learning projects

---

## 🙋‍♂️ Author

**Abhishek Kumar**
AI Explorer | Full Stack Developer
🌐 [LinkedIn](https://www.linkedin.com/in/abhishek-kumar-6202249339ak/)
🐙 [GitHub](https://github.com/abhishek-kr01)

---

## 📣 Feedback & Contributions

Have suggestions or ideas to extend this agent (e.g., voice input, deadlines, GUI)?
Feel free to open an issue or pull request!

````

---

### ✅ Also Create These Two Extra Files in Your Repo:

**`.env.example`**

```env
# Copy this file and rename to .env
GEMINI_API_KEY=your_api_key_here
```

**`requirements.txt`**

```txt
google-generativeai
python-dotenv
```
