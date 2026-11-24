# AI Test Case Generator Agent

## Project Overview
The AI Test Case Generator Agent is an AI-powered web application that automatically generates software test cases from plain-English requirements.

It uses a local Large Language Model (LLM) through Ollama to understand software requirements and generate positive, negative, and edge-case test scenarios.

## Features
- Enter software requirements in natural language.
- AI-powered requirement understanding.
- Generate positive, negative, and edge-case scenarios.
- Generate test steps, preconditions, test data and expected results.
- Assign High, Medium and Low priorities.
- Edit and delete generated test cases.
- Save test case history using SQLite.
- View previously saved test cases.
- Export test cases as CSV.
- Validate AI-generated JSON responses.

## Technologies Used
- Python
- Streamlit
- Ollama
- Llama 3.2
- LangChain
- SQLite
- Pandas

## Project Structure

```text
ai-test-case-generator-agent/
│
├── app.py
├── agent.py
├── test_case_generator.py
├── prompts.py
├── database.py
├── export_utils.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Open the project folder

```bash
cd ai-test-case-generator-agent
```

### 3. Create a virtual environment

```bash
py -m venv venv
```

### 4. Activate the environment

Windows:

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Install and start Ollama

Download Ollama from https://ollama.com/

Pull the model:

```bash
ollama pull llama3.2
```

### 7. Run the application

```bash
streamlit run app.py
```

## Application Workflow

1. Enter a software requirement.
2. Click Generate Test Cases.
3. AI analyzes the requirement.
4. Test scenarios are generated.
5. Review, edit or delete test cases.
6. Save test cases in SQLite.
7. Download results as CSV.

## Example Requirement

A user should be able to register using name, email and password.

## Expected Output

The application generates structured test cases covering valid registration, invalid inputs and other relevant scenarios.

## Project Purpose

This project demonstrates the use of Agentic AI, local LLM integration and software testing automation.

**Developed as part of the Xpert Champs AI Engineering Internship.**