from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(title="Secure FastAPI Server - TP3 DevSecOps")

# Import models
from app.models.item import Item
from app.models.user import User

@app.get("/")
def read_root():
    return {"message": "Welcome to the Secure FastAPI Server - TP3 DevSecOps"}

# ----------- 1. Health check -----------
@app.get("/health")
def health():
    return {"status": "ok"}


# ----------- 2. Get server info -----------
@app.get("/info")
def info():
    return {
        "app": "it's just a test server for DevSecOps TP3",
        "version": "1.0.0"
    }


# ----------- 3. Return environment-based secret (for K8s secret demo) -----------
@app.get("/secret")
def get_secret():
    secret_value = os.getenv("APP_SECRET", "no-secret-provided")
    return {"secret": secret_value}


# ----------- 4. Create item (POST) -----------
@app.post("/items")
def create_item(item: Item):
    return {
        "message": "Item created",
        "item": item
    }


# ----------- 5. Update item (PUT) -----------
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {
        "message": "Item updated",
        "item_id": item_id,
        "new_data": item
    }


# ----------- 6. get item (Get) -----------
@app.get("/item/{item_id}")
def get_item(item_id: int):
    return {
        "message": "Item retrieved",
        "item_id": item_id,
    }

# ----------- 7. get user (Get) -----------
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "message": "User retrieved",
        "user_id": user_id,
    }

# ----------- 8. Create user (POST) -----------
@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created",
        "user": user
    }

# ----------- 9. Return secrets from Vault (DB credentials) -----------
from app.config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME
@app.get("/secrets")
def get_secrets():
    return {
        "DB_USERNAME": DB_USERNAME, 
        "DB_PASSWORD": DB_PASSWORD,
        "DB_HOST": DB_HOST,
        "DB_NAME": DB_NAME
        }
