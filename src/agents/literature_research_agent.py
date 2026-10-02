from src.database import get_connection


# ============================================================
# Function 1: Get total number of research documents
# ============================================================

def get_document_count():
    """Return the total number of research documents."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM research_documents"
        )

        return cursor.fetchone()[0]

    finally:
        connection.close()


# ============================================================
# Function 2: Search documents by keyword
# ============================================================

def search_documents(keyword):
    """Search research documents by keyword in title, text, or tags."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        search_pattern = f"%{keyword}%"

        cursor.execute(
            """
            SELECT
                doc_id,
                compound_id,
                trial_id,
                doc_type,
                title,
                author,
                date,
                tags
            FROM research_documents
            WHERE title LIKE ?
               OR full_text LIKE ?
               OR tags LIKE ?
            ORDER BY date DESC
            """,
            (
                search_pattern,
                search_pattern,
                search_pattern
            )
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 3: Get documents by document type
# ============================================================

def get_documents_by_type(doc_type):
    """Return research documents matching a document type."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                doc_id,
                compound_id,
                trial_id,
                doc_type,
                title,
                author,
                date,
                tags
            FROM research_documents
            WHERE doc_type = ?
            ORDER BY date DESC
            """,
            (doc_type,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 4: Get documents by compound ID
# ============================================================

def get_documents_by_compound(compound_id):
    """Return research documents associated with a compound."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                doc_id,
                compound_id,
                trial_id,
                doc_type,
                title,
                author,
                date,
                tags
            FROM research_documents
            WHERE compound_id = ?
            ORDER BY date DESC
            """,
            (compound_id,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 5: Get documents by trial ID
# ============================================================

def get_documents_by_trial(trial_id):
    """Return research documents associated with a clinical trial."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                doc_id,
                compound_id,
                trial_id,
                doc_type,
                title,
                author,
                date,
                tags
            FROM research_documents
            WHERE trial_id = ?
            ORDER BY date DESC
            """,
            (trial_id,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 6: Get documents by author
# ============================================================

def get_documents_by_author(author):
    """Return research documents written by a specific author."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                doc_id,
                compound_id,
                trial_id,
                doc_type,
                title,
                author,
                date,
                tags
            FROM research_documents
            WHERE author = ?
            ORDER BY date DESC
            """,
            (author,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 7: Get documents within a date range
# ============================================================

def get_documents_by_date_range(start_date, end_date):
    """Return research documents within a specified date range."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                doc_id,
                compound_id,
                trial_id,
                doc_type,
                title,
                author,
                date,
                tags
            FROM research_documents
            WHERE date BETWEEN ? AND ?
            ORDER BY date DESC
            """,
            (start_date, end_date)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 8: Get documents containing a specific tag
# ============================================================

def get_documents_by_tag(tag):
    """Return research documents containing a specific tag."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        search_pattern = f"%{tag}%"

        cursor.execute(
            """
            SELECT
                doc_id,
                compound_id,
                trial_id,
                doc_type,
                title,
                author,
                date,
                tags
            FROM research_documents
            WHERE tags LIKE ?
            ORDER BY date DESC
            """,
            (search_pattern,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 9: Get recent documents
# ============================================================

def get_recent_documents(limit=10):
    """Return the most recent research documents."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                doc_id,
                compound_id,
                trial_id,
                doc_type,
                title,
                author,
                date,
                tags
            FROM research_documents
            ORDER BY date DESC
            LIMIT ?
            """,
            (limit,)
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 10: Get document details
# ============================================================

def get_document_details(doc_id):
    """Return complete details of a research document."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                doc_id,
                compound_id,
                trial_id,
                doc_type,
                title,
                author,
                date,
                full_text,
                tags
            FROM research_documents
            WHERE doc_id = ?
            """,
            (doc_id,)
        )

        return cursor.fetchone()

    finally:
        connection.close()


# ============================================================
# Function 11: Search documents by keyword and document type
# ============================================================

def search_documents_by_type(keyword, doc_type):
    """Search documents by keyword and document type."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        search_pattern = f"%{keyword}%"

        cursor.execute(
            """
            SELECT
                doc_id,
                compound_id,
                trial_id,
                doc_type,
                title,
                author,
                date,
                tags
            FROM research_documents
            WHERE
                (
                    title LIKE ?
                    OR full_text LIKE ?
                    OR tags LIKE ?
                )
                AND doc_type = ?
            ORDER BY date DESC
            """,
            (
                search_pattern,
                search_pattern,
                search_pattern,
                doc_type
            )
        )

        return cursor.fetchall()

    finally:
        connection.close()


# ============================================================
# Function 12: Literature Research Agent Dispatcher
# ============================================================

def literature_research_agent(query_type, value=None, value2=None):
    """Route a literature research request to the appropriate function."""

    # Basic document queries
    if query_type == "count":
        return get_document_count()

    elif query_type == "search":
        return search_documents(value)

    elif query_type == "type":
        return get_documents_by_type(value)

    # Compound and trial queries
    elif query_type == "compound":
        return get_documents_by_compound(value)

    elif query_type == "trial":
        return get_documents_by_trial(value)

    # Author and date queries
    elif query_type == "author":
        return get_documents_by_author(value)

    elif query_type == "date_range":
        return get_documents_by_date_range(value, value2)

    # Tag and recent document queries
    elif query_type == "tag":
        return get_documents_by_tag(value)

    elif query_type == "recent":
        return get_recent_documents(value)

    # Individual document
    elif query_type == "details":
        return get_document_details(value)

    # Combined search
    elif query_type == "search_by_type":
        return search_documents_by_type(value, value2)

    else:
        return "Invalid query type."


# ============================================================
# Complete Testing
# ============================================================

if __name__ == "__main__":

    print("\n========== LITERATURE RESEARCH AGENT TEST ==========\n")

    # Function 1
    print(
        "1. Total Research Documents:",
        get_document_count()
    )

    # Function 2
    oncology_documents = search_documents("Oncology")
    print(
        "2. Oncology Documents:",
        len(oncology_documents)
    )

    # Function 3
    literature_reviews = get_documents_by_type(
        "Literature Review"
    )
    print(
        "3. Literature Reviews:",
        len(literature_reviews)
    )

    # Function 4
    compound_documents = get_documents_by_compound(
        "CMP-0067"
    )
    print(
        "4. Documents for CMP-0067:",
        len(compound_documents)
    )

    # Function 5
    trial_documents = get_documents_by_trial(
        "TRL-0087"
    )
    print(
        "5. Documents for TRL-0087:",
        len(trial_documents)
    )

    # Function 6
    author_documents = get_documents_by_author(
        "Steven Davis"
    )
    print(
        "6. Documents by Steven Davis:",
        len(author_documents)
    )

    # Function 7
    date_documents = get_documents_by_date_range(
        "2025-01-01",
        "2025-12-31"
    )
    print(
        "7. Documents in 2025:",
        len(date_documents)
    )

    # Function 8
    safety_documents = get_documents_by_tag(
        "Safety"
    )
    print(
        "8. Documents with Safety tag:",
        len(safety_documents)
    )

    # Function 9
    recent_documents = get_recent_documents(5)
    print(
        "9. Recent Documents:",
        len(recent_documents)
    )

    # Function 10
    document_details = get_document_details(
        "DOC-00095"
    )
    print(
        "10. DOC-00095 Details:",
        document_details
    )

    # Function 11
    oncology_reviews = search_documents_by_type(
        "Oncology",
        "Literature Review"
    )
    print(
        "11. Oncology Literature Reviews:",
        len(oncology_reviews)
    )

    # Function 12
    dispatcher_result = literature_research_agent(
        "type",
        "Literature Review"
    )
    print(
        "12. Dispatcher Literature Reviews:",
        len(dispatcher_result)
    )

    print("\n========== TEST COMPLETED ==========\n")