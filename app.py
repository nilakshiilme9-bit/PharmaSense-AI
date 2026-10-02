"""
PharmaSense-AI
Professional Streamlit User Interface
"""

import streamlit as st

from src.app import process_user_query


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="PharmaSense-AI",
    page_icon="💊",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 0px;
    }

    .subtitle {
        font-size: 20px;
        color: #666666;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 25px;
        font-weight: 600;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .agent-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #f5f7fa;
        margin-bottom: 10px;
    }

    .footer {
        text-align: center;
        color: #777777;
        margin-top: 40px;
        padding: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">💊 PharmaSense-AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered Pharmaceutical Research Assistant</div>',
    unsafe_allow_html=True
)

st.write(
    "Analyze clinical trials, research literature, adverse events, "
    "pharmaceutical compounds, and generate research reports using "
    "a multi-agent architecture."
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("💊 PharmaSense-AI")

st.sidebar.markdown("### Available Agents")

st.sidebar.markdown(
    """
    🔬 **Trial Data Analyst**

    📚 **Literature Research Agent**

    ⚠️ **Adverse Event Triage Agent**

    🧪 **Compound Similarity Agent**

    📝 **Report Writer Agent**

    🧭 **Router / Planner Agent**
    """
)

st.sidebar.divider()

st.sidebar.info(
    "The Router / Planner Agent identifies the type of user "
    "question and sends it to the appropriate specialized agent."
)


# ============================================================
# PROJECT OVERVIEW
# ============================================================

st.markdown(
    '<div class="section-title">📊 PharmaSense-AI Overview</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Clinical Trials",
        "110"
    )

with col2:
    st.metric(
        "Research Documents",
        "250"
    )

with col3:
    st.metric(
        "Adverse Events",
        "500"
    )

with col4:
    st.metric(
        "Compounds",
        "150"
    )


# ============================================================
# KEY ANALYTICS
# ============================================================

st.markdown(
    '<div class="section-title">📈 Key Analytics</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Completed Trials",
        "39"
    )

with col2:
    st.metric(
        "Phase III Trials",
        "31"
    )

with col3:
    st.metric(
        "Recruiting Phase III",
        "7"
    )

with col4:
    st.metric(
        "Completion Rate",
        "35.45%"
    )


# ============================================================
# ENROLLMENT ANALYTICS
# ============================================================

st.markdown(
    '<div class="section-title">👥 Enrollment Analytics</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average Enrollment Performance",
        "70.86%"
    )

with col2:
    st.metric(
        "Low Enrollment Trials",
        "29"
    )

with col3:
    st.metric(
        "Over-Enrolled Trials",
        "6"
    )


# ============================================================
# TRIAL PHASE DISTRIBUTION
# ============================================================

st.markdown(
    '<div class="section-title">🔬 Clinical Trial Phase Distribution</div>',
    unsafe_allow_html=True
)

phase_data = {
    "Phase I": 37,
    "Phase II": 33,
    "Phase III": 31,
    "Phase IV": 9
}

st.bar_chart(phase_data)


# ============================================================
# TRIAL STATUS DISTRIBUTION
# ============================================================

st.markdown(
    '<div class="section-title">📋 Clinical Trial Status</div>',
    unsafe_allow_html=True
)

status_data = {
    "Completed": 39,
    "Active not recruiting": 29,
    "Recruiting": 27,
    "Terminated": 9,
    "Suspended": 6
}

st.bar_chart(status_data)


# ============================================================
# RESEARCH QUESTION SECTION
# ============================================================

st.markdown(
    '<div class="section-title">🔍 Research Assistant</div>',
    unsafe_allow_html=True
)

st.write(
    "Ask a question about clinical trials, literature, adverse events, "
    "compounds, or request a complete research report."
)


# ============================================================
# EXAMPLE QUESTIONS
# ============================================================

example_questions = [
    "How many clinical trials are completed?",
    "How many Phase III trials are recruiting?",
    "How many oncology documents are there?",
    "How many mild adverse events are there?",
    "Find compounds targeting ALK.",
    "Generate a research report."
]

selected_example = st.selectbox(
    "Choose an example question:",
    ["Select a question"] + example_questions
)


# ============================================================
# USER QUESTION
# ============================================================

question = st.text_input(
    "Enter your research question:",
    placeholder="Example: How many Phase III trials are recruiting?"
)


# ============================================================
# USE EXAMPLE
# ============================================================

if selected_example != "Select a question":

    if st.button("Use Selected Example"):

        st.session_state["question"] = selected_example

        st.rerun()


# Restore selected question after rerun

if "question" in st.session_state:

    if not question:

        question = st.session_state["question"]


# ============================================================
# ANALYZE BUTTON
# ============================================================

if st.button("🔍 Analyze", type="primary"):

    if not question.strip():

        st.warning(
            "Please enter a research question."
        )

    else:

        with st.spinner(
            "PharmaSense-AI is analyzing your question..."
        ):

            response = process_user_query(question)


        # ====================================================
        # SUCCESS MESSAGE
        # ====================================================

        st.success(
            "Analysis completed successfully."
        )


        # ====================================================
        # ROUTING INFORMATION
        # ====================================================

        st.markdown(
            '<div class="section-title">🧭 Agent Routing</div>',
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Selected Agent",
                response["selected_agent"]
            )

        with col2:

            st.metric(
                "Query Type",
                response["query_type"]
            )


        # ====================================================
        # ROUTING REASON
        # ====================================================

        with st.expander("🧭 Why was this agent selected?"):

            st.write(
                response["reason"]
            )


        # ====================================================
        # RESULT
        # ====================================================

        st.markdown(
            '<div class="section-title">📊 Analysis Result</div>',
            unsafe_allow_html=True
        )

        result = response["result"]


        # ----------------------------------------------------
        # STRING RESULT
        # ----------------------------------------------------

        if isinstance(result, str):

            st.text(result)


        # ----------------------------------------------------
        # LIST RESULT
        # ----------------------------------------------------

        elif isinstance(result, list):

            st.write(
                f"Found **{len(result)} result(s)**."
            )

            st.dataframe(
                result,
                use_container_width=True
            )


        # ----------------------------------------------------
        # DICTIONARY RESULT
        # ----------------------------------------------------

        elif isinstance(result, dict):

            st.json(result)


        # ----------------------------------------------------
        # OTHER RESULT
        # ----------------------------------------------------

        else:

            st.write(result)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div class="footer">

    **PharmaSense-AI**  
    Multi-Agent Pharmaceutical Research Assistant

    <br>

    Clinical Trials • Literature • Adverse Events • Compounds

    </div>
    """,
    unsafe_allow_html=True
)
