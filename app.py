
import streamlit as st
import pandas as pd

from agent import generate_with_agent
from database import create_tables, save_history, get_history
from test_case_generator import generate_test_cases
from export_utils import export_to_csv

st.set_page_config(
    page_title="AI Test Case Generator",
    page_icon="🧪",
    layout="wide"
)

create_tables()

st.title("🧪 AI Test Case Generator Agent")
st.write("Generate software test cases automatically using AI.")

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select Page",
    ["Generate Test Cases", "History"]
)

if page == "Generate Test Cases":

    st.header("Enter Software Requirement")

    requirement = st.text_area(
        "Describe your software feature:",
        placeholder="Example: A user should be able to register using name, email and password.",
        height=150
    )

    if st.button("Generate Test Cases", type="primary"):

        if not requirement.strip():
            st.warning("Please enter a software requirement.")

        else:
            try:
                with st.spinner("AI is generating test cases..."):
                    result = generate_test_cases(
                        requirement,
                        generate_with_agent
                    )

                st.session_state["cases"] = result["test_cases"]
                st.session_state["requirement"] = requirement
                st.success("Test cases generated successfully!")

            except Exception as e:
                st.error(f"Generation failed: {e}")

    if "cases" in st.session_state:

        st.subheader("Generated Test Cases")

        edited_cases = st.data_editor(
            pd.DataFrame(st.session_state["cases"]),
            num_rows="dynamic",
            use_container_width=True,
            key="test_editor"
        )

        st.session_state["cases"] = edited_cases.to_dict(
            orient="records"
        )

        if st.button("Save Test Cases"):
            save_history(
                st.session_state["requirement"],
                st.session_state["cases"]
            )
            st.success("Test cases saved successfully!")

        csv_data = export_to_csv(st.session_state["cases"])

        st.download_button(
            "Download CSV",
            data=csv_data,
            file_name="test_cases.csv",
            mime="text/csv"
        )

        if st.button("Clear Results"):
            del st.session_state["cases"]
            st.rerun()

elif page == "History":

    st.header("Previous Test Case History")

    history = get_history()

    if history:
        for record in history:
            with st.expander(
                f"History #{record[0]} - {record[1]}"
            ):
                import json
                cases = json.loads(record[2])

                st.write("Created:", record[3])
                st.dataframe(
                    pd.DataFrame(cases),
                    use_container_width=True
                )
    else:
        st.info("No saved history available yet.")

st.divider()
st.caption("AI Test Case Generator Agent | Xpert Champs")
