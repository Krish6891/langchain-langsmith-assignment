"""
LangChain + OpenAI + LangSmith Example

Author: Gopalakrishnan
Python: 3.11+
"""

import os
import sys

from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI


# -----------------------------------------------------
# Load environment variables
# -----------------------------------------------------
load_dotenv()


# -----------------------------------------------------
# Read API Keys
# -----------------------------------------------------
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")


# -----------------------------------------------------
# Validate API Keys
# -----------------------------------------------------
if not GOOGLE_API_KEY:
    print("\nERROR")
    print("GOOGLE_API_KEY not found.")
    print("Please add it to your .env file.\n")
    sys.exit()

if not LANGSMITH_API_KEY:
    print("\nERROR")
    print("LANGSMITH_API_KEY not found.")
    print("Please add it to your .env file.\n")
    sys.exit()


# -----------------------------------------------------
# Create Prompt
# -----------------------------------------------------
prompt = ChatPromptTemplate.from_template(
    "{question}"
)


# -----------------------------------------------------
# Create Google Generative AI Model
# -----------------------------------------------------
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


# -----------------------------------------------------
# Output Parser
# -----------------------------------------------------
parser = StrOutputParser()


# -----------------------------------------------------
# Build Chain
# -----------------------------------------------------
chain = prompt | model | parser


# -----------------------------------------------------
# User Input
# -----------------------------------------------------
question = input("Enter your prompt: ")


# -----------------------------------------------------
# Invoke Chain
# -----------------------------------------------------
response = chain.invoke(
    {
        "question": question
    }
)


# -----------------------------------------------------
# Print Response
# -----------------------------------------------------
print("\nAI Response:\n")
print(response)