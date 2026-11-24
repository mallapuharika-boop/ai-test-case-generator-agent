
import json

REQUIRED_FIELDS = [
    "id",
    "title",
    "scenario",
    "preconditions",
    "steps",
    "test_data",
    "expected_result",
    "priority"
]

def validate_test_cases(data):
    if not isinstance(data, dict):
        raise ValueError("Invalid AI response format.")

    cases = data.get("test_cases")

    if not isinstance(cases, list) or not cases:
        raise ValueError("No test cases generated.")

    for case in cases:
        if not isinstance(case, dict):
            raise ValueError("Invalid test case.")

        for field in REQUIRED_FIELDS:
            if not case.get(field):
                raise ValueError(f"Missing field: {field}")

        if case["priority"] not in ["High", "Medium", "Low"]:
            raise ValueError("Invalid priority.")

        if case["scenario"] not in ["Positive", "Negative", "Edge"]:
            raise ValueError("Invalid scenario type.")

    return data

def generate_test_cases(requirement, agent_function):
    if not requirement or not requirement.strip():
        raise ValueError("Please enter a software requirement.")

    result = agent_function(requirement)
    return validate_test_cases(result)
