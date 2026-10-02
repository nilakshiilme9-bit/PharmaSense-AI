"""
PharmaSense-AI - Router / Planner Agent

This agent identifies which PharmaSense agent should handle
a user's natural-language question.
"""


def route_query(question):
    """
    Determine which agent should handle the user's question.

    Returns:
        A dictionary containing the selected agent,
        query type, and reason.
    """

    question = question.lower().strip()

    # ---------------------------------------------------------
    # Clinical Trial Queries
    # ---------------------------------------------------------

    trial_keywords = [
        "trial",
        "trials",
        "clinical trial",
        "clinical trials",
        "enrollment",
        "enrolment",
        "recruiting",
        "phase i",
        "phase ii",
        "phase iii",
        "phase iv",
        "sponsor",
        "therapeutic area",
        "trial status",
        "trial duration"
    ]

    if any(keyword in question for keyword in trial_keywords):
        return {
            "agent": "Trial Query Agent",
            "query_type": "clinical_trial",
            "reason": "The question is related to clinical trial data."
        }

    # ---------------------------------------------------------
    # Literature / Document Queries
    # ---------------------------------------------------------

    literature_keywords = [
        "literature",
        "research paper",
        "research papers",
        "document",
        "documents",
        "publication",
        "publications",
        "author",
        "literature review",
        "regulatory briefing",
        "research document"
    ]

    if any(keyword in question for keyword in literature_keywords):
        return {
            "agent": "Literature Research Agent",
            "query_type": "literature",
            "reason": "The question is related to research documents or literature."
        }

    # ---------------------------------------------------------
    # Adverse Event Queries
    # ---------------------------------------------------------

    adverse_event_keywords = [
        "adverse event",
        "adverse events",
        "side effect",
        "side effects",
        "safety event",
        "safety events",
        "seriousness",
        "severity",
        "causality",
        "fatal event",
        "high priority event"
    ]

    if any(keyword in question for keyword in adverse_event_keywords):
        return {
            "agent": "Adverse Event Triage Agent",
            "query_type": "adverse_event",
            "reason": "The question is related to adverse events or safety."
        }

    # ---------------------------------------------------------
    # Compound Queries
    # ---------------------------------------------------------

    compound_keywords = [
        "compound",
        "compounds",
        "chemical class",
        "molecular weight",
        "toxicity",
        "target protein",
        "mechanism of action",
        "discovery phase",
        "similar compound",
        "similar compounds"
    ]

    if any(keyword in question for keyword in compound_keywords):
        return {
            "agent": "Compound Similarity Agent",
            "query_type": "compound",
            "reason": "The question is related to pharmaceutical compounds."
        }

    # ---------------------------------------------------------
    # Report Generation Queries
    # ---------------------------------------------------------

    report_keywords = [
        "report",
        "research summary",
        "summary report",
        "generate report",
        "create report",
        "prepare report",
        "final report"
    ]

    if any(keyword in question for keyword in report_keywords):
        return {
            "agent": "Report Writer Agent",
            "query_type": "report",
            "reason": "The user requested a research report or summary."
        }

    # ---------------------------------------------------------
    # Unknown Query
    # ---------------------------------------------------------

    return {
        "agent": "Unknown",
        "query_type": "unknown",
        "reason": "The question could not be mapped to a PharmaSense agent."
    }


def router_planner_agent(question):
    """
    Main Router / Planner Agent function.

    This function receives a user question and returns
    the appropriate PharmaSense agent.
    """

    return route_query(question)


# ============================================================
# COMPLETE TEST
# ============================================================

if __name__ == "__main__":

    print("\n" + "=" * 70)
    print("ROUTER / PLANNER AGENT TEST")
    print("=" * 70)

    test_questions = [
        "How many clinical trials are completed?",
        "How many Phase III trials are recruiting?",
        "Find oncology literature documents.",
        "How many serious adverse events are there?",
        "Find compounds targeting ALK.",
        "Generate a research report.",
        "What is the weather today?"
    ]

    for question in test_questions:

        result = router_planner_agent(question)

        print("\nQuestion:")
        print(question)

        print("Selected Agent:")
        print(result["agent"])

        print("Query Type:")
        print(result["query_type"])

        print("Reason:")
        print(result["reason"])

        print("-" * 70)

    print("\n" + "=" * 70)
    print("ROUTER / PLANNER AGENT TEST COMPLETED")
    print("=" * 70)