
import json
import re
from langchain_ollama import ChatOllama
from prompts import SYSTEM_PROMPT

llm = ChatOllama(
    model="llama3.2",
    temperature=0,
    format="json"
)

def generate_with_agent(requirement):

    prompt = f"""
    {SYSTEM_PROMPT}

    Analyze this software requirement:
    {requirement}

    Return ONLY valid JSON.
    Do not include markdown or explanations.
    """

    response = llm.invoke(prompt)
    content = response.content.strip()

    if not content:
        raise ValueError("AI returned an empty response.")

    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        match = re.search(r'\{.*\}', content, re.DOTALL)

        if not match:
            raise ValueError(
                f"AI did not return valid JSON: {content[:300]}"
            )

        data = json.loads(match.group())

    if not isinstance(data, dict):
        raise ValueError("AI response must be a JSON object.")

    return data
