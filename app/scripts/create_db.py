from app.database.database import DatabaseManager

db = DatabaseManager()

db.create_tables()

print("Database initialized successfully.")
