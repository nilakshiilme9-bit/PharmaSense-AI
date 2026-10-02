from src.database import get_connection


# ============================================================
# Function 1: Get total number of compounds
# ============================================================

def get_compound_count():
    """Return the total number of compounds."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM compounds"
        )

        return cursor.fetchone()[0]

    finally:
        connection.close()


# ============================================================
# Function 2: Get compound details
# ============================================================

def get_compound_details(compound_id):
    """Return complete details of a compound."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                compound_id,
                compound_name,
                chemical_class,
                therapeutic_area,
                target_protein,
                mechanism_of_action,
                discovery_phase,
                molecular_weight_da,
                solubility_mg_ml,
                toxicity_score,
                lead_scientist,
                synthesis_date,
                created_at
            FROM compounds
            WHERE compound_id = ?
            """,
            (compound_id,)
        )

        return cursor.fetchone()

    finally:
        connection.close()


# ============================================================
# Function 3: Search compounds by name
# ============================================================

def search_compounds(keyword):
    """Search compounds by compound name."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        search_pattern = f"%{keyword}%"

        cursor.execute(
            """
            SELECT
                compound_id,
                compound_name,
                chemical_class,
                therapeutic_area,
                target_protein,
                mechanism_of_action,
                discovery_phase,
                molecular_weight_da,
                solubility_mg_ml,
                toxicity_score
            FROM compounds
            WHERE compound_name LIKE ?
            ORDER BY compound_name
            """,
            (search_pattern,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 4: Get compounds by therapeutic area
# ============================================================

def get_compounds_by_therapeutic_area(therapeutic_area):
    """Return compounds belonging to a therapeutic area."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                compound_id,
                compound_name,
                chemical_class,
                therapeutic_area,
                target_protein,
                mechanism_of_action,
                discovery_phase,
                molecular_weight_da,
                solubility_mg_ml,
                toxicity_score
            FROM compounds
            WHERE therapeutic_area = ?
            ORDER BY compound_name
            """,
            (therapeutic_area,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 5: Get compounds by chemical class
# ============================================================

def get_compounds_by_chemical_class(chemical_class):
    """Return compounds belonging to a chemical class."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                compound_id,
                compound_name,
                chemical_class,
                therapeutic_area,
                target_protein,
                mechanism_of_action,
                discovery_phase,
                molecular_weight_da,
                solubility_mg_ml,
                toxicity_score
            FROM compounds
            WHERE chemical_class = ?
            ORDER BY compound_name
            """,
            (chemical_class,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 6: Get compounds by target protein
# ============================================================

def get_compounds_by_target(target_protein):
    """Return compounds associated with a target protein."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                compound_id,
                compound_name,
                chemical_class,
                therapeutic_area,
                target_protein,
                mechanism_of_action,
                discovery_phase,
                molecular_weight_da,
                solubility_mg_ml,
                toxicity_score
            FROM compounds
            WHERE target_protein = ?
            ORDER BY compound_name
            """,
            (target_protein,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 7: Get compounds by mechanism of action
# ============================================================

def get_compounds_by_mechanism(mechanism):
    """Return compounds matching a mechanism of action."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        search_pattern = f"%{mechanism}%"

        cursor.execute(
            """
            SELECT
                compound_id,
                compound_name,
                chemical_class,
                therapeutic_area,
                target_protein,
                mechanism_of_action,
                discovery_phase,
                molecular_weight_da,
                solubility_mg_ml,
                toxicity_score
            FROM compounds
            WHERE mechanism_of_action LIKE ?
            ORDER BY compound_name
            """,
            (search_pattern,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 8: Get compounds by discovery phase
# ============================================================

def get_compounds_by_discovery_phase(discovery_phase):
    """Return compounds belonging to a discovery phase."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                compound_id,
                compound_name,
                chemical_class,
                therapeutic_area,
                target_protein,
                mechanism_of_action,
                discovery_phase,
                molecular_weight_da,
                solubility_mg_ml,
                toxicity_score
            FROM compounds
            WHERE discovery_phase = ?
            ORDER BY compound_name
            """,
            (discovery_phase,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 9: Get compounds within molecular-weight range
# ============================================================

def get_compounds_by_molecular_weight(min_weight, max_weight):
    """Return compounds within a molecular-weight range."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                compound_id,
                compound_name,
                chemical_class,
                therapeutic_area,
                target_protein,
                mechanism_of_action,
                discovery_phase,
                molecular_weight_da,
                solubility_mg_ml,
                toxicity_score
            FROM compounds
            WHERE molecular_weight_da BETWEEN ? AND ?
            ORDER BY molecular_weight_da
            """,
            (min_weight, max_weight)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 10: Get compounds by toxicity threshold
# ============================================================

def get_compounds_by_toxicity(max_toxicity):
    """Return compounds with toxicity score at or below a threshold."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                compound_id,
                compound_name,
                chemical_class,
                therapeutic_area,
                target_protein,
                mechanism_of_action,
                discovery_phase,
                molecular_weight_da,
                solubility_mg_ml,
                toxicity_score
            FROM compounds
            WHERE toxicity_score <= ?
            ORDER BY toxicity_score
            """,
            (max_toxicity,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 11: Find similar compounds using shared attributes
# ============================================================

def find_similar_compounds(compound_id):
    """
    Find compounds that share chemical class, therapeutic area,
    target protein, or mechanism of action with the given compound.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                chemical_class,
                therapeutic_area,
                target_protein,
                mechanism_of_action
            FROM compounds
            WHERE compound_id = ?
            """,
            (compound_id,)
        )

        reference = cursor.fetchone()

        if reference is None:
            return []

        chemical_class, therapeutic_area, target_protein, mechanism = reference

        cursor.execute(
            """
            SELECT
                compound_id,
                compound_name,
                chemical_class,
                therapeutic_area,
                target_protein,
                mechanism_of_action,
                discovery_phase,
                molecular_weight_da,
                solubility_mg_ml,
                toxicity_score
            FROM compounds
            WHERE compound_id != ?
              AND (
                    chemical_class = ?
                    OR therapeutic_area = ?
                    OR target_protein = ?
                    OR mechanism_of_action = ?
              )
            ORDER BY compound_name
            """,
            (
                compound_id,
                chemical_class,
                therapeutic_area,
                target_protein,
                mechanism
            )
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 12: Compound Similarity Agent Dispatcher
# ============================================================

def compound_similarity_agent(query_type, value=None, value2=None):
    """Route a compound research request to the appropriate function."""

    if query_type == "count":
        return get_compound_count()

    elif query_type == "details":
        return get_compound_details(value)

    elif query_type == "search":
        return search_compounds(value)

    elif query_type == "therapeutic_area":
        return get_compounds_by_therapeutic_area(value)

    elif query_type == "chemical_class":
        return get_compounds_by_chemical_class(value)

    elif query_type == "target":
        return get_compounds_by_target(value)

    elif query_type == "mechanism":
        return get_compounds_by_mechanism(value)

    elif query_type == "discovery_phase":
        return get_compounds_by_discovery_phase(value)

    elif query_type == "molecular_weight":
        return get_compounds_by_molecular_weight(value, value2)

    elif query_type == "toxicity":
        return get_compounds_by_toxicity(value)

    elif query_type == "similar":
        return find_similar_compounds(value)

    else:
        return "Invalid query type."


# ============================================================
# Complete Testing
# ============================================================

if __name__ == "__main__":

    print("\n========== COMPOUND SIMILARITY AGENT TEST ==========\n")

    # Read actual database values for reliable testing
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT DISTINCT therapeutic_area
            FROM compounds
            WHERE therapeutic_area IS NOT NULL
            ORDER BY therapeutic_area
            """
        )
        therapeutic_areas = [
            row[0] for row in cursor.fetchall()
        ]

        cursor.execute(
            """
            SELECT DISTINCT chemical_class
            FROM compounds
            WHERE chemical_class IS NOT NULL
            ORDER BY chemical_class
            """
        )
        chemical_classes = [
            row[0] for row in cursor.fetchall()
        ]

        cursor.execute(
            """
            SELECT DISTINCT target_protein
            FROM compounds
            WHERE target_protein IS NOT NULL
            ORDER BY target_protein
            """
        )
        target_proteins = [
            row[0] for row in cursor.fetchall()
        ]

        cursor.execute(
            """
            SELECT DISTINCT discovery_phase
            FROM compounds
            WHERE discovery_phase IS NOT NULL
            ORDER BY discovery_phase
            """
        )
        discovery_phases = [
            row[0] for row in cursor.fetchall()
        ]

        cursor.execute(
            """
            SELECT
                MIN(molecular_weight_da),
                MAX(molecular_weight_da)
            FROM compounds
            """
        )
        min_weight, max_weight = cursor.fetchone()

        cursor.execute(
            """
            SELECT
                MIN(toxicity_score)
            FROM compounds
            """
        )
        min_toxicity = cursor.fetchone()[0]

    finally:
        connection.close()

    # Function 1
    print(
        "1. Total Compounds:",
        get_compound_count()
    )

    # Function 2
    reference_compound = get_compound_details("CMP-0001")
    print(
        "2. CMP-0001 Details:",
        reference_compound
    )

    # Function 3
    search_result = search_compounds("RX")
    print(
        "3. Compounds containing 'RX':",
        len(search_result)
    )

    # Function 4
    if therapeutic_areas:
        area_result = get_compounds_by_therapeutic_area(
            therapeutic_areas[0]
        )
        print(
            f"4. Compounds in '{therapeutic_areas[0]}':",
            len(area_result)
        )

    # Function 5
    if chemical_classes:
        class_result = get_compounds_by_chemical_class(
            chemical_classes[0]
        )
        print(
            f"5. Compounds in chemical class '{chemical_classes[0]}':",
            len(class_result)
        )

    # Function 6
    if target_proteins:
        target_result = get_compounds_by_target(
            target_proteins[0]
        )
        print(
            f"6. Compounds targeting '{target_proteins[0]}':",
            len(target_result)
        )

    # Function 7
    mechanism_result = get_compounds_by_mechanism("inhibitor")
    print(
        "7. Compounds with 'inhibitor' mechanism:",
        len(mechanism_result)
    )

    # Function 8
    if discovery_phases:
        phase_result = get_compounds_by_discovery_phase(
            discovery_phases[0]
        )
        print(
            f"8. Compounds in '{discovery_phases[0]}' discovery phase:",
            len(phase_result)
        )

    # Function 9
    midpoint = (min_weight + max_weight) / 2

    weight_result = get_compounds_by_molecular_weight(
        min_weight,
        midpoint
    )

    print(
        "9. Compounds in lower molecular-weight range:",
        len(weight_result)
    )

    # Function 10
    toxicity_result = get_compounds_by_toxicity(
        min_toxicity
    )

    print(
        "10. Compounds at minimum toxicity score:",
        len(toxicity_result)
    )

    # Function 11
    similar_result = find_similar_compounds(
        "CMP-0001"
    )

    print(
        "11. Compounds similar to CMP-0001:",
        len(similar_result)
    )

    # Function 12
    dispatcher_result = compound_similarity_agent(
        "count"
    )

    print(
        "12. Dispatcher Compound Count:",
        dispatcher_result
    )

    print("\n========== TEST COMPLETED ==========\n")