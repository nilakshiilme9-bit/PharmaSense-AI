from src.database import get_connection


# Function #1
def get_trial_count():
    """Return the total number of clinical trials."""
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM clinical_trials")
        return cursor.fetchone()[0]
    finally:
        connection.close()

def get_trials_by_status(status):
    """Return clinical trials matching a given status."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT trial_id, compound_id, trial_phase,
                   therapeutic_area, sponsor, status
            FROM clinical_trials
            WHERE status = ?
            """,
            (status,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


def get_trials_by_phase(trial_phase):
    """Return clinical trials matching a given trial phase."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT trial_id, compound_id, trial_phase,
                   therapeutic_area, sponsor, status
            FROM clinical_trials
            WHERE trial_phase = ?
            """,
            (trial_phase,)
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_trials_by_therapeutic_area(therapeutic_area):
    """Return clinical trials matching a therapeutic area."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT trial_id, compound_id, trial_phase,
                   therapeutic_area, sponsor, status
            FROM clinical_trials
            WHERE therapeutic_area = ?
            """,
            (therapeutic_area,)
        )

        return cursor.fetchall() 

    finally:
        connection.close()  

def get_trials_by_sponsor(sponsor):
    """Return clinical trials matching a given sponsor."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT trial_id, compound_id, trial_phase,
                   therapeutic_area, sponsor, status
            FROM clinical_trials
            WHERE sponsor = ?
            """,
            (sponsor,)
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_enrollment_data():
    """Return planned and actual enrollment for all clinical trials."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT trial_id, target_enrollment, actual_enrollment
            FROM clinical_trials
            """
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_enrollment_performance():
    """Return enrollment target, actual enrollment, and enrollment percentage."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                trial_id,
                target_enrollment,
                actual_enrollment,
                ROUND(
                    (CAST(actual_enrollment AS REAL) / target_enrollment) * 100,
                    2
                ) AS enrollment_percentage
            FROM clinical_trials
            """
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_trial_status_summary():
    """Return the number of trials for each trial status."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT status, COUNT(*) AS trial_count
            FROM clinical_trials
            GROUP BY status
            ORDER BY trial_count DESC
            """
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_trial_phase_summary():
    """Return the number of trials for each trial phase."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT trial_phase, COUNT(*) AS trial_count
            FROM clinical_trials
            GROUP BY trial_phase
            ORDER BY trial_phase
            """
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_trials_by_compound(compound_id):
    """Return clinical trials for a specific compound."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT trial_id, compound_id, trial_phase,
                   therapeutic_area, sponsor, status
            FROM clinical_trials
            WHERE compound_id = ?
            """,
            (compound_id,)
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_trials_by_sponsor(sponsor):
    """Return clinical trials sponsored by a given organization."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT trial_id, compound_id, trial_phase,
                   therapeutic_area, sponsor, status
            FROM clinical_trials
            WHERE sponsor = ?
            """,
            (sponsor,)
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_trials_by_start_date(start_date):
    """Return clinical trials starting on or after a given date."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT trial_id, compound_id, trial_phase,
                   therapeutic_area, sponsor, start_date, status
            FROM clinical_trials
            WHERE start_date >= ?
            ORDER BY start_date
            """,
            (start_date,)
        )

        return cursor.fetchall()

    finally:
        connection.close()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM clinical_trials")
        count = cursor.fetchone()[0]
        return count

    finally:
        connection.close()

def get_trials_by_date_range(start_date, end_date):
    """Return clinical trials starting within a given date range."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT trial_id, compound_id, trial_phase,
                   therapeutic_area, sponsor, start_date, status
            FROM clinical_trials
            WHERE start_date BETWEEN ? AND ?
            ORDER BY start_date
            """,
            (start_date, end_date)
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_trial_details(trial_id):
    """Return complete details of a specific clinical trial."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM clinical_trials
            WHERE trial_id = ?
            """,
            (trial_id,)
        )

        return cursor.fetchone()

    finally:
        connection.close()

def get_trial_sites(trial_id):
    """Return all sites associated with a specific clinical trial."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM trial_sites
            WHERE trial_id = ?
            """,
            (trial_id,)
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_site_summary():
    """Return a summary of trial sites grouped by country."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT country,
                   COUNT(*) AS site_count,
                   SUM(enrollment_count) AS total_enrollment
            FROM trial_sites
            GROUP BY country
            ORDER BY site_count DESC
            """
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_trials_by_site_status(site_status):
    """Return trial sites matching a given site status."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT site_id, trial_id, site_name,
                   country, principal_investigator,
                   enrollment_count, site_status
            FROM trial_sites
            WHERE site_status = ?
            """,
            (site_status,)
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_trials_by_country(country):
    """Return trial sites located in a given country."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT site_id, trial_id, site_name,
                   country, principal_investigator,
                   enrollment_count, site_status
            FROM trial_sites
            WHERE country = ?
            """,
            (country,)
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_trial_enrollment_summary():
    """Return target and actual enrollment for all clinical trials."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT trial_id,
                   target_enrollment,
                   actual_enrollment,
                   ROUND(
                       (actual_enrollment * 100.0) /
                       NULLIF(target_enrollment, 0),
                       2
                   ) AS enrollment_percentage
            FROM clinical_trials
            ORDER BY trial_id
            """
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_active_trials():
    """Return all currently active or recruiting clinical trials."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT trial_id, compound_id, trial_phase,
                   therapeutic_area, sponsor,
                   start_date, status
            FROM clinical_trials
            WHERE status IN ('Recruiting', 'Active, not recruiting')
            ORDER BY start_date
            """
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_trials_by_phase_and_status(trial_phase, status):
    """Return clinical trials matching a specific phase and status."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT trial_id, compound_id, trial_phase,
                   therapeutic_area, sponsor,
                   start_date, status
            FROM clinical_trials
            WHERE trial_phase = ?
              AND status = ?
            ORDER BY start_date
            """,
            (trial_phase, status)
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_trials_by_therapeutic_area_and_status(therapeutic_area, status):
    """Return clinical trials matching a therapeutic area and status."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT trial_id, compound_id, trial_phase,
                   therapeutic_area, sponsor,
                   start_date, status
            FROM clinical_trials
            WHERE therapeutic_area = ?
              AND status = ?
            ORDER BY start_date
            """,
            (therapeutic_area, status)
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_trial_completion_rate():
    """Return the percentage of clinical trials that are completed."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                COUNT(*) AS total_trials,
                SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END)
                    AS completed_trials
            FROM clinical_trials
            """
        )

        total_trials, completed_trials = cursor.fetchone()

        completion_rate = round(
            (completed_trials * 100.0) / total_trials,
            2
        )

        return total_trials, completed_trials, completion_rate

    finally:
        connection.close()

def get_trials_by_sponsor_and_status(sponsor, status):
    """Return clinical trials matching a sponsor and status."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT trial_id, compound_id, trial_phase,
                   therapeutic_area, sponsor,
                   start_date, status
            FROM clinical_trials
            WHERE sponsor = ?
              AND status = ?
            ORDER BY start_date
            """,
            (sponsor, status)
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_trials_by_date_and_status(start_date, status):
    """Return clinical trials starting on or after a date with a given status."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT trial_id, compound_id, trial_phase,
                   therapeutic_area, sponsor,
                   start_date, status
            FROM clinical_trials
            WHERE start_date >= ?
              AND status = ?
            ORDER BY start_date
            """,
            (start_date, status)
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_average_enrollment_performance():
    """Return the average enrollment performance across all trials."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT ROUND(
                AVG(
                    (actual_enrollment * 100.0) /
                    NULLIF(target_enrollment, 0)
                ),
                2
            )
            FROM clinical_trials
            """
        )

        return cursor.fetchone()[0]

    finally:
        connection.close()

def get_trials_with_low_enrollment(threshold=50):
    """Return trials with enrollment performance below a given percentage."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT trial_id,
                   compound_id,
                   trial_phase,
                   therapeutic_area,
                   target_enrollment,
                   actual_enrollment,
                   ROUND(
                       (actual_enrollment * 100.0) /
                       NULLIF(target_enrollment, 0),
                       2
                   ) AS enrollment_percentage
            FROM clinical_trials
            WHERE
                (actual_enrollment * 100.0) /
                NULLIF(target_enrollment, 0) < ?
            ORDER BY enrollment_percentage ASC
            """,
            (threshold,)
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_over_enrolled_trials():
    """Return clinical trials where actual enrollment exceeds the target."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT trial_id,
                   compound_id,
                   trial_phase,
                   therapeutic_area,
                   target_enrollment,
                   actual_enrollment,
                   ROUND(
                       (actual_enrollment * 100.0) /
                       NULLIF(target_enrollment, 0),
                       2
                   ) AS enrollment_percentage
            FROM clinical_trials
            WHERE actual_enrollment > target_enrollment
            ORDER BY enrollment_percentage DESC
            """
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_trial_duration():
    """Return the duration of each clinical trial in days."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT trial_id,
                   compound_id,
                   trial_phase,
                   therapeutic_area,
                   start_date,
                   planned_end_date,
                   actual_end_date,
                   CAST(
                       JULIANDAY(
                           COALESCE(actual_end_date, planned_end_date)
                       ) - JULIANDAY(start_date)
                       AS INTEGER
                   ) AS duration_days
            FROM clinical_trials
            ORDER BY duration_days DESC
            """
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_average_trial_duration():
    """Return the average duration of clinical trials in days."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT ROUND(
                AVG(
                    JULIANDAY(
                        COALESCE(actual_end_date, planned_end_date)
                    ) - JULIANDAY(start_date)
                ),
                2
            )
            FROM clinical_trials
            """
        )

        return cursor.fetchone()[0]

    finally:
        connection.close()

def get_trials_by_phase_enrollment():
    """Return enrollment statistics grouped by clinical trial phase."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT trial_phase,
                   COUNT(*) AS trial_count,
                   SUM(target_enrollment) AS total_target_enrollment,
                   SUM(actual_enrollment) AS total_actual_enrollment,
                   ROUND(
                       AVG(
                           (actual_enrollment * 100.0) /
                           NULLIF(target_enrollment, 0)
                       ),
                       2
                   ) AS average_enrollment_percentage
            FROM clinical_trials
            GROUP BY trial_phase
            ORDER BY trial_phase
            """
        )

        return cursor.fetchall()

    finally:
        connection.close()

def get_trials_by_therapeutic_area_enrollment():
    """Return enrollment statistics grouped by therapeutic area."""
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT therapeutic_area,
                   COUNT(*) AS trial_count,
                   SUM(target_enrollment) AS total_target_enrollment,
                   SUM(actual_enrollment) AS total_actual_enrollment,
                   ROUND(
                       AVG(
                           (actual_enrollment * 100.0) /
                           NULLIF(target_enrollment, 0)
                       ),
                       2
                   ) AS average_enrollment_percentage
            FROM clinical_trials
            GROUP BY therapeutic_area
            ORDER BY therapeutic_area
            """
        )
        return cursor.fetchall()
    finally:
        connection.close()

def get_top_enrolled_trials(limit=10):
    """Return clinical trials with the highest actual enrollment."""
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT trial_id,
                   compound_id,
                   trial_phase,
                   therapeutic_area,
                   actual_enrollment
            FROM clinical_trials
            ORDER BY actual_enrollment DESC
            LIMIT ?
            """,
            (limit,)
        )
        return cursor.fetchall()
    finally:
        connection.close()

def get_top_enrolled_trials(limit=10):
    """Return clinical trials with the highest actual enrollment."""
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT trial_id,
                   compound_id,
                   trial_phase,
                   therapeutic_area,
                   actual_enrollment
            FROM clinical_trials
            ORDER BY actual_enrollment DESC
            LIMIT ?
            """,
            (limit,)
        )
        return cursor.fetchall()
    finally:
        connection.close()

def get_lowest_enrolled_trials(limit=10):
    """Return clinical trials with the lowest actual enrollment."""
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT trial_id,
                   compound_id,
                   trial_phase,
                   therapeutic_area,
                   actual_enrollment
            FROM clinical_trials
            ORDER BY actual_enrollment ASC
            LIMIT ?
            """,
            (limit,)
        )
        return cursor.fetchall()
    finally:
        connection.close()

def get_trial_status_by_therapeutic_area():
    """Return trial counts grouped by therapeutic area and status."""
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT therapeutic_area,
                   status,
                   COUNT(*) AS trial_count
            FROM clinical_trials
            GROUP BY therapeutic_area, status
            ORDER BY therapeutic_area, trial_count DESC
            """
        )
        return cursor.fetchall()
    finally:
        connection.close()

def get_average_enrollment_by_therapeutic_area():
    """Return average actual enrollment grouped by therapeutic area."""
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT therapeutic_area,
                   COUNT(*) AS trial_count,
                   ROUND(AVG(actual_enrollment), 2) AS average_actual_enrollment
            FROM clinical_trials
            GROUP BY therapeutic_area
            ORDER BY average_actual_enrollment DESC
            """
        )
        return cursor.fetchall()
    finally:
        connection.close()
def get_enrollment_excess():
    """Return trials where actual enrollment exceeded target enrollment."""
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT trial_id,
                   compound_id,
                   target_enrollment,
                   actual_enrollment,
                   (actual_enrollment - target_enrollment) AS excess_enrollment
            FROM clinical_trials
            WHERE actual_enrollment > target_enrollment
            ORDER BY excess_enrollment DESC
            """
        )
        return cursor.fetchall()
    finally:
        connection.close()

# Function #37
def get_enrollment_shortfall(threshold=50):
    """Return trials where actual enrollment is below target by a given threshold."""
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT trial_id,
                   compound_id,
                   target_enrollment,
                   actual_enrollment,
                   (target_enrollment - actual_enrollment) AS shortfall
            FROM clinical_trials
            WHERE (target_enrollment - actual_enrollment) >= ?
            ORDER BY shortfall DESC
            """,
            (threshold,)
        )
        return cursor.fetchall()
    finally:
        connection.close()


# Function #38
def get_trials_by_sponsor_enrollment():
    """Return enrollment statistics grouped by sponsor."""
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT sponsor,
                   COUNT(*) AS trial_count,
                   SUM(target_enrollment) AS total_target_enrollment,
                   SUM(actual_enrollment) AS total_actual_enrollment,
                   ROUND(
                       AVG(
                           (actual_enrollment * 100.0) /
                           NULLIF(target_enrollment, 0)
                       ),
                       2
                   ) AS average_enrollment_percentage
            FROM clinical_trials
            GROUP BY sponsor
            ORDER BY average_enrollment_percentage DESC
            """
        )
        return cursor.fetchall()
    finally:
        connection.close()


# Function #39
def get_trials_by_phase_and_therapeutic_area():
    """Return trial counts grouped by phase and therapeutic area."""
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT trial_phase,
                   therapeutic_area,
                   COUNT(*) AS trial_count
            FROM clinical_trials
            GROUP BY trial_phase, therapeutic_area
            ORDER BY trial_phase, therapeutic_area
            """
        )
        return cursor.fetchall()
    finally:
        connection.close()


# Function #40
def get_trial_enrollment_variance():
    """Return enrollment difference and percentage difference for each trial."""
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT trial_id,
                   compound_id,
                   target_enrollment,
                   actual_enrollment,
                   (actual_enrollment - target_enrollment) AS enrollment_difference,
                   ROUND(
                       ((actual_enrollment - target_enrollment) * 100.0) /
                       NULLIF(target_enrollment, 0),
                       2
                   ) AS enrollment_variance_percentage
            FROM clinical_trials
            ORDER BY enrollment_variance_percentage DESC
            """
        )
        return cursor.fetchall()
    finally:
        connection.close()

# Function #41
def trial_data_analyst_agent(query_type, value=None, value2=None):
    """Route an agent request to the appropriate trial analysis function."""

    # Functions #1–#10
    if query_type == "count":
        return get_trial_count()

    elif query_type == "status":
        return get_trials_by_status(value)

    elif query_type == "phase":
        return get_trials_by_phase(value)

    elif query_type == "therapeutic_area":
        return get_trials_by_therapeutic_area(value)

    elif query_type == "sponsor":
        return get_trials_by_sponsor(value)

    elif query_type == "enrollment":
        return get_enrollment_data()

    elif query_type == "enrollment_performance":
        return get_enrollment_performance()

    elif query_type == "status_summary":
        return get_trial_status_summary()

    elif query_type == "phase_summary":
        return get_trial_phase_summary()

    elif query_type == "compound":
        return get_trials_by_compound(value)

    # Functions #11–#20
    elif query_type == "start_date":
        return get_trials_by_start_date(value)

    elif query_type == "date_range":
        return get_trials_by_date_range(value, value2)

    elif query_type == "trial_details":
        return get_trial_details(value)

    elif query_type == "trial_sites":
        return get_trial_sites(value)

    elif query_type == "site_summary":
        return get_site_summary()

    elif query_type == "site_status":
        return get_trials_by_site_status(value)

    elif query_type == "country":
        return get_trials_by_country(value)

    elif query_type == "enrollment_summary":
        return get_trial_enrollment_summary()

    elif query_type == "active_trials":
        return get_active_trials()

    elif query_type == "phase_status":
        return get_trials_by_phase_and_status(value, value2)

    # Functions #21–#30
    elif query_type == "area_status":
        return get_trials_by_therapeutic_area_and_status(value, value2)

    elif query_type == "completion_rate":
        return get_trial_completion_rate()

    elif query_type == "sponsor_status":
        return get_trials_by_sponsor_and_status(value, value2)

    elif query_type == "date_status":
        return get_trials_by_date_and_status(value, value2)

    elif query_type == "average_enrollment_performance":
        return get_average_enrollment_performance()

    elif query_type == "low_enrollment":
        return get_trials_with_low_enrollment(value)

    elif query_type == "over_enrolled":
        return get_over_enrolled_trials()

    elif query_type == "trial_duration":
        return get_trial_duration()

    elif query_type == "average_trial_duration":
        return get_average_trial_duration()

    elif query_type == "phase_enrollment":
        return get_trials_by_phase_enrollment()

    # Functions #31–#40
    elif query_type == "area_enrollment":
        return get_trials_by_therapeutic_area_enrollment()

    elif query_type == "top_enrolled":
        return get_top_enrolled_trials(value)

    elif query_type == "lowest_enrolled":
        return get_lowest_enrolled_trials(value)

    elif query_type == "status_by_area":
        return get_trial_status_by_therapeutic_area()

    elif query_type == "average_enrollment_by_area":
        return get_average_enrollment_by_therapeutic_area()

    elif query_type == "enrollment_excess":
        return get_enrollment_excess()

    elif query_type == "enrollment_shortfall":
        return get_enrollment_shortfall(value)

    elif query_type == "sponsor_enrollment":
        return get_trials_by_sponsor_enrollment()

    elif query_type == "phase_therapeutic_area":
        return get_trials_by_phase_and_therapeutic_area()

    elif query_type == "enrollment_variance":
        return get_trial_enrollment_variance()

    else:
        return "Invalid query type."

if __name__ == "__main__":

    print("Completion Rate:", trial_data_analyst_agent("completion_rate"))

    print("Active Oncology Trials:", len(
        trial_data_analyst_agent(
            "area_status",
            "Oncology",
            "Active, not recruiting"
        )
    ))

    print("Low Enrollment Trials:", len(
        trial_data_analyst_agent("low_enrollment", 50)
    ))

    print("Over Enrolled Trials:", len(
        trial_data_analyst_agent("over_enrolled")
    ))

    print("Average Trial Duration:", trial_data_analyst_agent(
        "average_trial_duration"
    ))

    print("Phase Enrollment:", len(
        trial_data_analyst_agent("phase_enrollment")
    ))

    print("Therapeutic Area Enrollment:", len(
        trial_data_analyst_agent("area_enrollment")
    ))

    print("Top Enrolled Trials:", len(
        trial_data_analyst_agent("top_enrolled", 10)
    ))

    print("Lowest Enrolled Trials:", len(
        trial_data_analyst_agent("lowest_enrolled", 10)
    ))

    print("Enrollment Excess:", len(
        trial_data_analyst_agent("enrollment_excess")
    ))

    print("Enrollment Shortfall:", len(
        trial_data_analyst_agent("enrollment_shortfall", 50)
    ))

    print("Sponsor Enrollment:", len(
        trial_data_analyst_agent("sponsor_enrollment")
    ))

    print("Phase & Therapeutic Area:", len(
        trial_data_analyst_agent("phase_therapeutic_area")
    ))

    print("Enrollment Variance:", len(
        trial_data_analyst_agent("enrollment_variance")
    ))