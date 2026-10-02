"""
PharmaSense-AI - Report Writer Agent

This agent converts results from different PharmaSense agents
into a structured research report.
"""


def format_section(title, content):
    """Create a formatted report section."""

    if content is None:
        content = "No information available."

    return f"\n## {title}\n{content}\n"


def format_list(items):
    """Convert a list of items into a readable bullet list."""

    if not items:
        return "No information available."

    if isinstance(items, (str, int, float)):
        return str(items)

    result = []

    for item in items:
        if isinstance(item, tuple):
            result.append("- " + " | ".join(str(value) for value in item))
        elif isinstance(item, dict):
            result.append(
                "- " + ", ".join(
                    f"{key}: {value}"
                    for key, value in item.items()
                )
            )
        else:
            result.append(f"- {item}")

    return "\n".join(result)


def generate_report(
    title,
    trial_results=None,
    literature_results=None,
    adverse_event_results=None,
    compound_results=None,
    conclusion=None
):
    """
    Generate a structured research report from agent results.

    Parameters:
        title: Report title.
        trial_results: Results from Trial Data Analyst.
        literature_results: Results from Literature Research Agent.
        adverse_event_results: Results from Adverse Event Triage Agent.
        compound_results: Results from Compound Similarity Agent.
        conclusion: Optional final conclusion.

    Returns:
        A formatted research report as a string.
    """

    report = []

    report.append("=" * 70)
    report.append(title.upper())
    report.append("=" * 70)

    report.append(
        format_section(
            "1. Clinical Trial Analysis",
            format_list(trial_results)
        )
    )

    report.append(
        format_section(
            "2. Literature Research",
            format_list(literature_results)
        )
    )

    report.append(
        format_section(
            "3. Adverse Event Analysis",
            format_list(adverse_event_results)
        )
    )

    report.append(
        format_section(
            "4. Compound Analysis",
            format_list(compound_results)
        )
    )

    if conclusion is None:
        conclusion = (
            "The report combines clinical trial, literature, "
            "adverse event, and compound analysis results "
            "provided by the PharmaSense-AI agents."
        )

    report.append(
        format_section(
            "5. Conclusion",
            conclusion
        )
    )

    report.append("\n" + "=" * 70)
    report.append("END OF REPORT")
    report.append("=" * 70)

    return "\n".join(report)


def report_writer_agent(
    title,
    trial_results=None,
    literature_results=None,
    adverse_event_results=None,
    compound_results=None,
    conclusion=None
):
    """
    Main Report Writer Agent function.

    This function receives results from different agents
    and generates one structured research report.
    """

    return generate_report(
        title=title,
        trial_results=trial_results,
        literature_results=literature_results,
        adverse_event_results=adverse_event_results,
        compound_results=compound_results,
        conclusion=conclusion
    )


# ============================================================
# COMPLETE TEST
# ============================================================

if __name__ == "__main__":

    print("\n" + "=" * 70)
    print("REPORT WRITER AGENT TEST")
    print("=" * 70)

    # Sample results from Trial Data Analyst
    trial_results = [
        ("Total Clinical Trials", 110),
        ("Completed Trials", 39),
        ("Phase III Trials", 31),
        ("Recruiting Phase III Trials", 7),
        ("Average Enrollment Performance", "70.86%"),
        ("Average Trial Duration", "511.5 days")
    ]

    # Sample results from Literature Research Agent
    literature_results = [
        ("Total Research Documents", 250),
        ("Oncology Documents", 37),
        ("Literature Reviews", 44),
        ("Safety Tagged Documents", 131)
    ]

    # Sample results from Adverse Event Triage Agent
    adverse_event_results = [
        ("Total Adverse Events", 500),
        ("Mild Events", 284),
        ("Non-serious Events", 457),
        ("High Priority Events", 67)
    ]

    # Sample results from Compound Similarity Agent
    compound_results = [
        ("Total Compounds", 150),
        ("Cardiology Compounds", 26),
        ("ALK Targeting Compounds", 7),
        ("Approved Compounds", 10),
        ("Similar Compounds to CMP-0001", 36)
    ]

    # Generate report
    report = report_writer_agent(
        title="PharmaSense-AI Clinical Research Summary",

        trial_results=trial_results,

        literature_results=literature_results,

        adverse_event_results=adverse_event_results,

        compound_results=compound_results,

        conclusion=(
            "The PharmaSense-AI analysis combines clinical trial, "
            "research literature, adverse event, and compound data "
            "into a single structured research summary."
        )
    )

    # Display report
    print(report)

    print("\n" + "=" * 70)
    print("REPORT WRITER AGENT TEST COMPLETED")
    print("=" * 70)