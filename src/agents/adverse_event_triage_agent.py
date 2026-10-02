from src.database import get_connection


# ============================================================
# Function 1: Get total number of adverse events
# ============================================================

def get_event_count():
    """Return the total number of adverse events."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM adverse_events"
        )

        return cursor.fetchone()[0]

    finally:
        connection.close()


# ============================================================
# Function 2: Get adverse events by severity
# ============================================================

def get_events_by_severity(severity):
    """Return adverse events matching a severity level."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                event_id,
                trial_id,
                site_id,
                patient_code,
                event_date,
                adverse_event_term,
                severity,
                seriousness,
                causality_assessment,
                outcome,
                reported_by
            FROM adverse_events
            WHERE severity = ?
            ORDER BY event_date DESC
            """,
            (severity,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 3: Get adverse events by seriousness
# ============================================================

def get_events_by_seriousness(seriousness):
    """Return adverse events matching a seriousness category."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                event_id,
                trial_id,
                site_id,
                patient_code,
                event_date,
                adverse_event_term,
                severity,
                seriousness,
                causality_assessment,
                outcome,
                reported_by
            FROM adverse_events
            WHERE seriousness = ?
            ORDER BY event_date DESC
            """,
            (seriousness,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 4: Get adverse events by trial
# ============================================================

def get_events_by_trial(trial_id):
    """Return adverse events associated with a clinical trial."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                event_id,
                trial_id,
                site_id,
                patient_code,
                event_date,
                adverse_event_term,
                severity,
                seriousness,
                causality_assessment,
                outcome,
                reported_by
            FROM adverse_events
            WHERE trial_id = ?
            ORDER BY event_date DESC
            """,
            (trial_id,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 5: Get adverse events by site
# ============================================================

def get_events_by_site(site_id):
    """Return adverse events reported from a specific site."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                event_id,
                trial_id,
                site_id,
                patient_code,
                event_date,
                adverse_event_term,
                severity,
                seriousness,
                causality_assessment,
                outcome,
                reported_by
            FROM adverse_events
            WHERE site_id = ?
            ORDER BY event_date DESC
            """,
            (site_id,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 6: Search adverse events by term
# ============================================================

def search_adverse_events(keyword):
    """Search adverse events by adverse-event term."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        search_pattern = f"%{keyword}%"

        cursor.execute(
            """
            SELECT
                event_id,
                trial_id,
                site_id,
                patient_code,
                event_date,
                adverse_event_term,
                severity,
                seriousness,
                causality_assessment,
                outcome,
                reported_by
            FROM adverse_events
            WHERE adverse_event_term LIKE ?
            ORDER BY event_date DESC
            """,
            (search_pattern,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 7: Get events by causality assessment
# ============================================================

def get_events_by_causality(causality):
    """Return adverse events matching a causality assessment."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                event_id,
                trial_id,
                site_id,
                patient_code,
                event_date,
                adverse_event_term,
                severity,
                seriousness,
                causality_assessment,
                outcome,
                reported_by
            FROM adverse_events
            WHERE causality_assessment = ?
            ORDER BY event_date DESC
            """,
            (causality,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 8: Get events by outcome
# ============================================================

def get_events_by_outcome(outcome):
    """Return adverse events matching an outcome."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                event_id,
                trial_id,
                site_id,
                patient_code,
                event_date,
                adverse_event_term,
                severity,
                seriousness,
                causality_assessment,
                outcome,
                reported_by
            FROM adverse_events
            WHERE outcome = ?
            ORDER BY event_date DESC
            """,
            (outcome,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 9: Get recent adverse events
# ============================================================

def get_recent_adverse_events(limit=10):
    """Return the most recently reported adverse events."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                event_id,
                trial_id,
                site_id,
                patient_code,
                event_date,
                adverse_event_term,
                severity,
                seriousness,
                causality_assessment,
                outcome,
                reported_by
            FROM adverse_events
            ORDER BY event_date DESC
            LIMIT ?
            """,
            (limit,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 10: Get adverse events by date range
# ============================================================

def get_events_by_date_range(start_date, end_date):
    """Return adverse events within a specified date range."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                event_id,
                trial_id,
                site_id,
                patient_code,
                event_date,
                adverse_event_term,
                severity,
                seriousness,
                causality_assessment,
                outcome,
                reported_by
            FROM adverse_events
            WHERE event_date BETWEEN ? AND ?
            ORDER BY event_date DESC
            """,
            (start_date, end_date)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 11: Get high-priority adverse events
# ============================================================

def get_high_priority_events():
    """
    Return events that require higher-priority review.

    An event is considered high priority when it is marked
    serious or has a severe/life-threatening/fatal severity.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                event_id,
                trial_id,
                site_id,
                patient_code,
                event_date,
                adverse_event_term,
                severity,
                seriousness,
                causality_assessment,
                outcome,
                reported_by
            FROM adverse_events
            WHERE
                LOWER(seriousness) = 'serious'
                OR LOWER(severity) IN (
                    'severe',
                    'life-threatening',
                    'fatal'
                )
            ORDER BY event_date DESC
            """
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 12: Adverse Event Triage Agent Dispatcher
# ============================================================

def adverse_event_triage_agent(query_type, value=None, value2=None):
    """Route an adverse-event request to the appropriate function."""

    if query_type == "count":
        return get_event_count()

    elif query_type == "severity":
        return get_events_by_severity(value)

    elif query_type == "seriousness":
        return get_events_by_seriousness(value)

    elif query_type == "trial":
        return get_events_by_trial(value)

    elif query_type == "site":
        return get_events_by_site(value)

    elif query_type == "search":
        return search_adverse_events(value)

    elif query_type == "causality":
        return get_events_by_causality(value)

    elif query_type == "outcome":
        return get_events_by_outcome(value)

    elif query_type == "recent":
        return get_recent_adverse_events(value)

    elif query_type == "date_range":
        return get_events_by_date_range(value, value2)

    elif query_type == "high_priority":
        return get_high_priority_events()

    else:
        return "Invalid query type."


# ============================================================
# Complete Testing
# ============================================================

if __name__ == "__main__":

    print("\n========== ADVERSE EVENT TRIAGE AGENT TEST ==========\n")

    # Get actual values from the database so the tests
    # do not depend on guessed severity/seriousness names.

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT DISTINCT severity
            FROM adverse_events
            WHERE severity IS NOT NULL
            ORDER BY severity
            """
        )

        severity_values = [
            row[0] for row in cursor.fetchall()
        ]

        cursor.execute(
            """
            SELECT DISTINCT seriousness
            FROM adverse_events
            WHERE seriousness IS NOT NULL
            ORDER BY seriousness
            """
        )

        seriousness_values = [
            row[0] for row in cursor.fetchall()
        ]

        cursor.execute(
            """
            SELECT DISTINCT causality_assessment
            FROM adverse_events
            WHERE causality_assessment IS NOT NULL
            ORDER BY causality_assessment
            """
        )

        causality_values = [
            row[0] for row in cursor.fetchall()
        ]

        cursor.execute(
            """
            SELECT DISTINCT outcome
            FROM adverse_events
            WHERE outcome IS NOT NULL
            ORDER BY outcome
            """
        )

        outcome_values = [
            row[0] for row in cursor.fetchall()
        ]

    finally:
        connection.close()

    # Function 1
    print(
        "1. Total Adverse Events:",
        get_event_count()
    )

    # Function 2
    if severity_values:
        severity_result = get_events_by_severity(
            severity_values[0]
        )
        print(
            f"2. Events with severity '{severity_values[0]}':",
            len(severity_result)
        )

    # Function 3
    if seriousness_values:
        seriousness_result = get_events_by_seriousness(
            seriousness_values[0]
        )
        print(
            f"3. Events with seriousness '{seriousness_values[0]}':",
            len(seriousness_result)
        )

    # Function 4
    trial_result = get_events_by_trial("TRL-0001")
    print(
        "4. Events for TRL-0001:",
        len(trial_result)
    )

    # Function 5
    site_result = get_events_by_site("SITE-0001")
    print(
        "5. Events for SITE-0001:",
        len(site_result)
    )

    # Function 6
    search_result = search_adverse_events("headache")
    print(
        "6. Events containing 'headache':",
        len(search_result)
    )

    # Function 7
    if causality_values:
        causality_result = get_events_by_causality(
            causality_values[0]
        )
        print(
            f"7. Events with causality '{causality_values[0]}':",
            len(causality_result)
        )

    # Function 8
    if outcome_values:
        outcome_result = get_events_by_outcome(
            outcome_values[0]
        )
        print(
            f"8. Events with outcome '{outcome_values[0]}':",
            len(outcome_result)
        )

    # Function 9
    recent_result = get_recent_adverse_events(5)
    print(
        "9. Recent Adverse Events:",
        len(recent_result)
    )

    # Function 10
    date_result = get_events_by_date_range(
        "2025-01-01",
        "2025-12-31"
    )
    print(
        "10. Events in 2025:",
        len(date_result)
    )

    # Function 11
    priority_result = get_high_priority_events()
    print(
        "11. High-Priority Events:",
        len(priority_result)
    )

    # Function 12
    dispatcher_result = adverse_event_triage_agent(
        "count"
    )
    print(
        "12. Dispatcher Event Count:",
        dispatcher_result
    )

    print("\n========== TEST COMPLETED ==========\n")