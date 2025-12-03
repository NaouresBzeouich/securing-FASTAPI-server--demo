# app/services/db_service.py

from app.config import DATABASE_URL

class FakeDatabaseConnection:
    def __init__(self):
        self.connection_url = DATABASE_URL

    def connect(self):
        # Simulated DB connection
        print(f"[FAKE-DB] Connecting to database at: {self.connection_url}")
        return True

    def get_status(self):
        return {
            "status": "connected",
            "url": self.connection_url,
        }

# Instantiate a fake database client
db_client = FakeDatabaseConnection()
