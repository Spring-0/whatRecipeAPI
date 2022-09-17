from fastapi import FastAPI
import pandas as pd
#  from fastapi import Response
from models import Recipe
from typing import List

app = FastAPI()

df = pd.read_csv('dataset//epi_r.csv')
df = df.filter(['title', 'rating', 'calories', 'protein', 'fat', 'sodium', 'almond', 'dairy', 'pork'])

db: List[Recipe] = []

for index, row in df.iterrows():
    db.append(Recipe(
        title=row['title'],
        rating=row['rating'],
        calories=row['calories'],
        protein=row['protein'],
        fat=row['fat'],
        sodium=row['sodium'],
        almond=row['almond'],
        dairy=row['dairy'],
        pork=row['pork']
    ))


@app.get("/")
async def root():
    return "Welcome, please refer to 'docs_that_dont_exist_yet.com' to get started"


@app.get("/api/v1/recipes")
async def fetch_all_recipes():
    return db
    #  return Response(df.to_json(orient='records'), media_type='application/json')


@app.post('/api/v1/recipes')
async def upload_recipe(recipe: Recipe):
    if recipe in db:
        return {"Error: ": "This title is already in the database!"}
    else:
        db.append(recipe)
        return f"Recipe '{recipe.title}' has successfully been added!"
