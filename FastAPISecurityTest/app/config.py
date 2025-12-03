# app/config.py

# ❌ Fake secrets (insecure version BEFORE Vault)
DB_USERNAME = "admin"
DB_PASSWORD = "supersecret123"
DB_HOST = "localhost"
DB_NAME = "my_fake_database"

# Connection string (not used for a real connection)
DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
