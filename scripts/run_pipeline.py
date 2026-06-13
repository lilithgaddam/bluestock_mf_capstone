import os

os.system("python scripts/clean_nav_history.py")
os.system("python scripts/clean_transactions.py")
os.system("python scripts/clean_scheme_performance.py")
os.system("python scripts/create_database.py")

print("Pipeline completed successfully")