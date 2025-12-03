# app/config.py
import os
import hvac

VAULT_ADDR = os.getenv("VAULT_ADDR")
VAULT_TOKEN = os.getenv("VAULT_TOKEN")

# Créer le client Vault
client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)

# Lire les secrets depuis Vault
secret_response = client.secrets.kv.v2.read_secret_version(
    path="fastapi",  # juste le nom du secret sous le mount point
    mount_point="secret"  # mount point par défaut dans dev mode
)
secrets = secret_response['data']['data']

DB_USERNAME = secrets.get("DB_USERNAME")
DB_PASSWORD = secrets.get("DB_PASSWORD")
DB_HOST = secrets.get("DB_HOST")
DB_NAME = secrets.get("DB_NAME")

# Connection string (not used for a real connection)
DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
