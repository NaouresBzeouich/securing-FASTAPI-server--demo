import requests

vault_addr = "http://127.0.0.1:8200"
token = "myroot"
path = "secret/data/fastapi"

data = {
    "data": {
        "DB_USERNAME": "admin",
        "DB_PASSWORD": "supersecret123",
        "DB_HOST": "localhost",
        "DB_NAME": "my_fake_database"
    }
}

headers = {"X-Vault-Token": token}
response = requests.post(f"{vault_addr}/v1/{path}", json=data, headers=headers)
print(response.json())
