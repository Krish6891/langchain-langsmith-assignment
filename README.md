# 🚀 LangChain + Gemini + LangSmith Application

A beginner-friendly Python project demonstrating how to build an AI application using **LangChain**, **Google Gemini**, and **LangSmith**.

---

# 📌 Project Overview

This project demonstrates:

- LangChain Prompt Templates
- Google Gemini API Integration
- LangSmith Tracing
- Environment Variable Management
- Secure API Key Handling
- Python Best Practices

---

# 🛠 Technologies Used

- Python 3.11+
- LangChain
- Google Gemini API
- LangSmith
- python-dotenv

---

# 📂 Project Structure

```
LangChain-LangSmith-App/
│
├── main.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/Krish6891/langchain-langsmith-assignment.git
```

Move into the project

```bash
cd langchain-langsmith-assignment
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Install Packages

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure Environment Variables

Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_API_KEY

LANGSMITH_API_KEY=YOUR_LANGSMITH_API_KEY

LANGSMITH_TRACING=true

LANGSMITH_PROJECT=LangChain_Assignment
```

---

# ▶ Run the Project

```bash
python main.py
```

---

# 📸 Sample Output

```
Enter your prompt:
What is LangChain?

AI Response:

LangChain is a framework that simplifies the development of AI-powered applications by connecting language models with prompts, tools, memory, and external data.
```

---

# 📊 LangSmith

This project supports automatic tracing using LangSmith.

You can view:

- Prompt
- AI Response
- Execution Time
- Token Usage
- Complete Trace

---

# 👨‍💻 Author

**N. Gopalakrishnan**

GitHub:
https://github.com/Krish6891

---

# ⭐ If you found this project useful, don't forget to Star the repository.