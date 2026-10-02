from src.agents.trial_data_analyst import trial_data_analyst_agent


def process_trial_query(question):
    """Process a natural-language clinical trial query."""

    question = question.lower().strip()

    # Recruiting Phase III trials
    if "recruiting" in question and (
        "phase iii" in question or "phase 3" in question
    ):
        return len(
            trial_data_analyst_agent(
                "phase_status",
                "Phase III",
                "Recruiting"
            )
        )

    # Phase III trials
    elif "phase iii" in question or "phase 3" in question:
        return len(
            trial_data_analyst_agent(
                "phase",
                "Phase III"
            )
        )

    # Low enrollment trials
    elif "low enrollment" in question:
        return len(
            trial_data_analyst_agent(
                "low_enrollment",
                50
            )
        )

    # Over-enrolled trials
    elif "over enrolled" in question or "over-enrolled" in question:
        return len(
            trial_data_analyst_agent(
                "over_enrolled"
            )
        )

    # Average trial duration
    elif (
        "average trial duration" in question
        or "average duration" in question
    ):
        return trial_data_analyst_agent(
            "average_trial_duration"
        )

    # Average enrollment performance
    elif "average enrollment performance" in question:
        return trial_data_analyst_agent(
            "average_enrollment_performance"
        )

    # Top enrolled trials
    elif "top" in question and "enrolled" in question:
        return trial_data_analyst_agent(
            "top_enrolled",
            10
        )

    # India trials
    elif "india" in question:
        return len(
            trial_data_analyst_agent(
                "country",
                "India"
            )
        )

    # Trials starting in 2025
    elif "2025" in question:
        return len(
            trial_data_analyst_agent(
                "start_date",
                "2025-01-01"
            )
        )

    # Oncology trials
    elif "oncology" in question:
        return len(
            trial_data_analyst_agent(
                "therapeutic_area",
                "Oncology"
            )
        )

    # Completed trials
    elif "completed" in question:
        return len(
            trial_data_analyst_agent(
                "status",
                "Completed"
            )
        )

    # Active trials
    elif "active" in question:
        return len(
            trial_data_analyst_agent(
                "active_trials"
            )
        )

    # Trials by sponsor
    elif "sponsor" in question or "sponsored" in question:
        return len(
            trial_data_analyst_agent(
                "sponsor",
                "PharmaSense Global R&D"
            )
        )

    # Trials by therapeutic area
    elif "therapeutic area" in question:
        return len(
            trial_data_analyst_agent(
                "therapeutic_area",
                "Oncology"
            )
        )

    # Trials by status
    elif "status" in question:
        return len(
            trial_data_analyst_agent(
                "status",
                "Completed"
            )
        )

    # Total number of trials
    elif "how many" in question and "trial" in question:
        return trial_data_analyst_agent(
            "count"
        )

    else:
        return "Sorry, I could not understand the trial query."
    
if __name__ == "__main__":

    print("Phase 3 Trials:", process_trial_query(
        "How many Phase 3 trials are there?"
    ))

    print("Recruiting Phase 3 Trials:", process_trial_query(
        "How many recruiting Phase 3 trials are there?"
    ))

    print("Low Enrollment Trials:", process_trial_query(
        "How many low enrollment trials are there?"
    ))

    print("Over-Enrolled Trials:", process_trial_query(
        "How many over-enrolled trials are there?"
    ))

    print("Average Duration:", process_trial_query(
        "What is the average duration?"
    ))

    print("Average Enrollment Performance:", process_trial_query(
        "What is the average enrollment performance?"
    ))

    print("India Trials:", process_trial_query(
        "How many trials are in India?"
    ))

    print("Oncology Trials:", process_trial_query(
        "How many oncology trials are there?"
    ))

    print("Completed Trials:", process_trial_query(
        "How many completed trials are there?"
    ))

    print("Total Trials:", process_trial_query(
        "How many clinical trials are there?"
    ))

    print("Average Trial Duration:", process_trial_query(
        "What is the average trial duration?"
    ))

    print("Global R&D Trials:", process_trial_query(
        "How many trials are sponsored by Global R&D?"
    ))

    print("Oncology Therapeutic Area:", process_trial_query(
        "How many trials are in the Oncology therapeutic area?"
    ))

    print("Completed Status Trials:", process_trial_query(
        "How many trials have Completed status?"
    ))