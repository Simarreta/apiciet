#hace esto para usar FastAPI como instancia del objeto
from fastapi import FastAPI, Path
import httpx

app=FastAPI()
#ahora ya puedo usar las funciones de la instancia FastApi como los gets, por ejemplo

## amazon.com/create-user
## GET -> para obtener o devolver una información
## POST -> para crear algo nuevo en la database
## PUT -> para actualizar la database
## DELETE -> para borrar algo

students={
    1:{
        'first':"John",
        'last':'Doe',
        'age':25
        },
}


## hago la función para obtener información de la url
@app.get("/")
def index():
    return {"name": "First Data"}

## esta función es para ver la información del estudiante indicando el número del estudiante version 1
##@app.get("/get-student/{student_id}")
## def get_student(student_id: int):
##    return students[student_id]


##gt -> greater than
##lt -> lesser than
##gte -> great or equal
##lte -> lower or equal


## Per ara no va
# @app.get("/get-student/{student_id}")
# def get_student(student_id: int =Path(None, description="The ID of the student you want to view", gt=0, lt=3)):
#    return students[student_id]


@app.get("/productos/{codigo_barras}")
async def obtener_producto(codigo_barras: str):
    url = f"https://world.openfoodfacts.org/api/v0/product/{codigo_barras}.json"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        json_data = response.json()
        processed_text = process_product(json_data)
        return {"processed_text": processed_text}
    
def process_product(json_data):
    allergens = json_data["product"]["allergens"]+json_data["product"]["allergens_from_ingredients"]+json_data["product"]["allergens_from_user"]
    allergens_hierarchy =json_data["product"]["allergens_hierarchy"]
    for allergen in allergens_hierarchy:
       allergens= allergens+","+allergen

    allergens_tags =json_data["product"]["allergens_tags"]
    for allergen_tag in allergens_tags:
        allergens= allergens+","+allergen_tag

    processed_text= allergens.replace("en:","")
    return processed_text
