from fastapi import FastAPI, HTTPException
import os
import psycopg2
from pydantic import BaseModel
from typing import List

app = FastAPI()

DATABASE_HOST = os.getenv("API_DB_HOST", "localhost")
DATABASE_PORT = os.getenv("API_DB_PORT", "5432")
DATABASE_NAME = os.getenv("API_DB_NAME", "api")
DATABASE_USER = os.getenv("API_DB_USER", "apiuser")
DATABASE_PASS = os.getenv("API_DB_PASS", "apipass")

DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

class Animal(BaseModel):
    id: int
    name: str
    check_in_date: str
    check_out_date: str
    status: str

@app.get("/animals", response_model=List[Animal])
async def get_animals():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animals;")
    animals = cursor.fetchall()
    conn.close()
    return [{"id": id, "name": name, "check_in_date": check_in, "check_out_date": check_out, "status": status} 
            for id, name, check_in, check_out, status in animals]

@app.post("/animals", response_model=Animal)
async def create_animal(animal: Animal):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO animals (name, check_in_date, check_out_date, status) VALUES (%s, %s, %s, %s) RETURNING id;",
                   (animal.name, animal.check_in_date, animal.check_out_date, animal.status))
    animal_id = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    animal.id = animal_id
    return animal

@app.delete("/animals/{animal_id}", response_model=dict)
async def delete_animal(animal_id: int):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM animals WHERE id = %s;", (animal_id,))
    conn.commit()
    conn.close()
    return {"message": "Animal deleted"}
