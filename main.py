from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
import pandas as pd
from models import Recipe, RecipeUpdateRequest
from typing import List, Optional, Union

app = FastAPI()

df = pd.read_csv('dataset//epi_r.csv')
df = df.filter(['title', 'rating', 'calories', 'protein', 'fat', 'sodium', 'almond', 'dairy', 'pork'])

db: List[Recipe] = []

for index, row in df.iterrows():
    db.append(Recipe(
        id=uuid4(),
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
        return {"Error": "This title is already in the database!"}
    else:
        db.append(recipe)
        return f"Recipe '{recipe.title}' has successfully been added!"


@app.delete('/api/v1/recipes/{recipe_id}')
async def delete_recipe(recipe_id: UUID):
    for recipe in db:
        if recipe.id == recipe_id:
            db.remove(recipe)
            return f"The recipe with the ID: {recipe_id} has been deleted"
    raise HTTPException(
        status_code=404,
        detail=f"{recipe_id} does not exist"
    )


@app.put('/api/v1/recipes/{recipe_id}')
async def update_recipe(recipe_update: RecipeUpdateRequest, recipe_id: UUID):
    for recipe in db:
        if recipe.id == recipe_id:
            for x in recipe_update.__dict__:
                if recipe_update.__dict__[x] != None:
                    print(recipe_update.__dict__[x])
                    setattr(recipe, str(x), recipe_update.__dict__[x])
            return "Successfully updated!"

    raise HTTPException(
        status_code=404,
        detail=f"Recipe ID '{recipe_id}' does not exist"
    )

@app.get("/api/v1/recipes/filter")
async def read_item(
        id: Optional[UUID] = uuid4(),
        title: Union[str, None] = None,
        rating: Union[str, None] = None,
        calories: Union[str, None] = None,
        protein: Union[str, None] = None,
        fat: Union[str, None] = None,
        sodium: Union[str, None] = None,
        almond: Union[str, None] = None,
        dairy: Union[str, None] = None,
        pork: Union[str, None] = None,
):
    params = locals().copy()
    del params['id']




