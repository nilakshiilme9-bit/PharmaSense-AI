"""
PharmaSense-AI Backend Application Controller
"""

from src.agents.router_planner_agent import router_planner_agent
from src.agents.trial_query_agent import process_trial_query
from src.agents.literature_research_agent import literature_research_agent
from src.agents.adverse_event_triage_agent import adverse_event_triage_agent
from src.agents.compound_similarity_agent import compound_similarity_agent
from src.agents.report_writer_agent import report_writer_agent


# ============================================================
# MAIN USER QUERY PROCESSOR
# ============================================================

def process_user_query(question):
    """
    Process a user question through the Router/Planner Agent
    and send it to the appropriate specialized agent.
    """

    # --------------------------------------------------------
    # STEP 1: ROUTE THE QUESTION
    # --------------------------------------------------------

    routing = router_planner_agent(question)

    selected_agent = routing.get("agent")
    query_type = routing.get("query_type")
    reason = routing.get("reason")

    # --------------------------------------------------------
    # STEP 2: TRIAL QUERY AGENT
    # --------------------------------------------------------

    if selected_agent == "Trial Query Agent":

        result = process_trial_query(question)

        return {
            "selected_agent": selected_agent,
            "query_type": query_type,
            "reason": reason,
            "result": result
        }

    # --------------------------------------------------------
    # STEP 3: LITERATURE RESEARCH AGENT
    # --------------------------------------------------------

    elif selected_agent == "Literature Research Agent":

        question_lower = question.lower()

        if "oncology" in question_lower:

            result = literature_research_agent(
                "search",
                "Oncology"
            )

        elif "literature review" in question_lower:

            result = literature_research_agent(
                "type",
                "Literature Review"
            )

        elif "safety" in question_lower:

            result = literature_research_agent(
                "tag",
                "Safety"
            )

        elif "count" in question_lower or "how many" in question_lower:

            result = literature_research_agent(
                "count"
            )

        else:

            result = literature_research_agent(
                "count"
            )

        return {
            "selected_agent": selected_agent,
            "query_type": query_type,
            "reason": reason,
            "result": result
        }

    # --------------------------------------------------------
    # STEP 4: ADVERSE EVENT TRIAGE AGENT
    # --------------------------------------------------------

    elif selected_agent == "Adverse Event Triage Agent":

        question_lower = question.lower()

        if "mild" in question_lower:

            result = adverse_event_triage_agent(
                "severity",
                "Mild"
            )

        elif "severe" in question_lower:

            result = adverse_event_triage_agent(
                "severity",
                "Severe"
            )

        elif "serious" in question_lower:

            result = adverse_event_triage_agent(
                "seriousness",
                "Serious"
            )

        elif "high priority" in question_lower:

            result = adverse_event_triage_agent(
                "high_priority"
            )

        else:

            result = adverse_event_triage_agent(
                "count"
            )

        return {
            "selected_agent": selected_agent,
            "query_type": query_type,
            "reason": reason,
            "result": result
        }

    # --------------------------------------------------------
    # STEP 5: COMPOUND SIMILARITY AGENT
    # --------------------------------------------------------

    elif selected_agent == "Compound Similarity Agent":

        question_lower = question.lower()

        if "alk" in question_lower:

            result = compound_similarity_agent(
                "target",
                "ALK"
            )

        elif "approved" in question_lower:

            result = compound_similarity_agent(
                "discovery_phase",
                "Approved"
            )

        elif "cardiology" in question_lower:

            result = compound_similarity_agent(
                "therapeutic_area",
                "Cardiology"
            )

        else:

            result = compound_similarity_agent(
                "count"
            )

        return {
            "selected_agent": selected_agent,
            "query_type": query_type,
            "reason": reason,
            "result": result
        }

    # --------------------------------------------------------
    # STEP 6: REPORT WRITER AGENT
    # --------------------------------------------------------

    elif selected_agent == "Report Writer Agent":

        # ====================================================
        # CLINICAL TRIAL RESULTS
        # ====================================================

        trial_results = [
            f"Total Clinical Trials: "
            f"{process_trial_query('How many clinical trials are there?')}",

            f"Completed Trials: "
            f"{process_trial_query('How many clinical trials are completed?')}",

            f"Phase III Trials: "
            f"{process_trial_query('How many Phase III trials are there?')}",

            f"Recruiting Phase III Trials: "
            f"{process_trial_query('How many Phase III trials are recruiting?')}",

            f"Average Enrollment Performance: "
            f"{process_trial_query('What is the average enrollment performance?')}",

            f"Average Trial Duration: "
            f"{process_trial_query('What is the average trial duration?')}"
        ]

        # ====================================================
        # LITERATURE RESULTS
        # ====================================================

        literature_results = [
            f"Total Research Documents: "
            f"{literature_research_agent('count')}",

            f"Oncology Documents: "
            f"{len(literature_research_agent('search', 'Oncology'))}",

            f"Literature Reviews: "
            f"{len(literature_research_agent('type', 'Literature Review'))}",

            f"Safety Tagged Documents: "
            f"{len(literature_research_agent('tag', 'Safety'))}"
        ]

        # ====================================================
        # ADVERSE EVENT RESULTS
        # ====================================================

        adverse_event_results = [
            f"Total Adverse Events: "
            f"{adverse_event_triage_agent('count')}",

            f"Mild Events: "
            f"{len(adverse_event_triage_agent('severity', 'Mild'))}",

            f"Non-serious Events: "
            f"{len(adverse_event_triage_agent('seriousness', 'Non-serious'))}",

            f"High Priority Events: "
            f"{len(adverse_event_triage_agent('high_priority'))}"
        ]

        # ====================================================
        # COMPOUND RESULTS
        # ====================================================

        compound_results = [
            f"Total Compounds: "
            f"{compound_similarity_agent('count')}",

            f"Cardiology Compounds: "
            f"{len(compound_similarity_agent('therapeutic_area', 'Cardiology'))}",

            f"ALK Targeting Compounds: "
            f"{len(compound_similarity_agent('target', 'ALK'))}",

            f"Approved Compounds: "
            f"{len(compound_similarity_agent('discovery_phase', 'Approved'))}"
        ]

        # ====================================================
        # GENERATE COMPLETE REPORT
        # ====================================================

        result = report_writer_agent(
            title="PharmaSense-AI Research Report",
            trial_results=trial_results,
            literature_results=literature_results,
            adverse_event_results=adverse_event_results,
            compound_results=compound_results,
            conclusion=(
                "The report summarizes clinical trial activity, "
                "research literature, adverse events, and "
                "pharmaceutical compound information."
            )
        )

        return {
            "selected_agent": selected_agent,
            "query_type": query_type,
            "reason": reason,
            "result": result
        }

    # --------------------------------------------------------
    # STEP 7: UNKNOWN QUERY
    # --------------------------------------------------------

    else:

        return {
            "selected_agent": selected_agent,
            "query_type": query_type,
            "reason": reason,
            "result": (
                "Sorry, I could not determine the appropriate "
                "agent for this question."
            )
        }


# ============================================================
# BACKEND TEST
# ============================================================

if __name__ == "__main__":

    print("=" * 70)
    print("PHARMASENSE-AI BACKEND APPLICATION TEST")
    print("=" * 70)

    test_questions = [
        "How many clinical trials are completed?",
        "How many Phase III trials are recruiting?",
        "How many oncology documents are there?",
        "How many mild adverse events are there?",
        "Find compounds targeting ALK.",
        "Generate a research report."
    ]

    for question in test_questions:

        print("\n" + "-" * 70)
        print("QUESTION:", question)
        print("-" * 70)

        response = process_user_query(question)

        print("Selected Agent:", response["selected_agent"])
        print("Query Type:", response["query_type"])
        print("Reason:", response["reason"])
        print("Result:")

        if isinstance(response["result"], list):

            print(
                "Number of results:",
                len(response["result"])
            )

            print(
                response["result"][:3]
            )

        else:

            print(response["result"])

    print("\n" + "=" * 70)
    print("PHARMASENSE-AI BACKEND APPLICATION TEST COMPLETED")
    print("=" * 70)