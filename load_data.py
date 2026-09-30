import pandas as pd
import sqlite3
import os

# -------------------------------------------------
# PharmaSense AI - Load Excel Dataset into SQLite
# -------------------------------------------------

EXCEL_FILE = "data/PharmaSense_synthetic_dataset.xlsx"
DATABASE_FILE = "pharmasense.db"

# Check whether the Excel file exists
if not os.path.exists(EXCEL_FILE):
    print("❌ Excel file not found!")
    print(f"Expected file: {EXCEL_FILE}")
    exit()

# Connect to SQLite database
conn = sqlite3.connect(DATABASE_FILE)

# Tables required for PharmaSense AI
tables = [
    "compounds",
    "clinical_trials",
    "trial_sites",
    "lab_results",
    "adverse_events",
    "research_documents",
    "agent_interaction_logs"
]

print("\nLoading PharmaSense AI dataset...\n")

for table in tables:
    df = pd.read_excel(EXCEL_FILE, sheet_name=table)

    # Load the dataframe into SQLite
    df.to_sql(table, conn, if_exists="replace", index=False)

    print(f"✅ {table}: {len(df)} records loaded")

conn.close()

print("\n🎉 PharmaSense database created successfully!")
print(f"Database file: {DATABASE_FILE}")