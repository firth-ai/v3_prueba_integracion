from fastapi import FastAPI, Body
from pydantic import BaseModel
from fastapi.responses import JSONResponse

class UserDescription(BaseModel):
    user_description: str

app = FastAPI(title="v3_prueba_integracion")
app.version = "v3"

@app.post("/process")
async def process_input(data: UserDescription = Body(...)):
    response = {
        "user_description": data.user_description,
        "codes_col": "prueba_integracion_exitosa"
    }
    return JSONResponse(content=response)