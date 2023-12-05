from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
import os

app = FastAPI()

class Item(BaseModel):
    key: str
    value: str

# Подключение к PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="your_database",
    user="your_username",
    password="your_password")

cursor = conn.cursor()

@app.post("/set")
async def set_item(item: Item):
    try:
        cursor.execute("INSERT INTO key_value (key, value) VALUES (%s, %s)", (item.key, item.value))
        conn.commit()
        return {"message": "Item added successfully"}
    except:
        conn.rollback()
        raise HTTPException(status_code=500, detail="Error saving item")

@app.get("/get/{key}")
async def get_item(key: str):
    cursor.execute("SELECT value FROM key_value WHERE key = %s", (key,))
    result = cursor.fetchone()
    if result:
        return {"value": result[0]}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
