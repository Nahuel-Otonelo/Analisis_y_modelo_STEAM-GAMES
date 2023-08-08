from fastapi import FastAPI

from funciones import gener, juegosna, specsna, earlyaccesna, sentimentna

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Bienvenido!"}



@app.get("/genero/{years}")
async def genero(year: str):
    result = gener(year)
    return result


@app.get("/juegos/{years}")
async def juegos(year: str):
    result = juegosna(year)
    return result


@app.get("/specs/{years}")
async def specs(year: str):
    result = specsna(year)
    return result



@app.get("/earlyacces/{years}")
async def earlyacces(year: str):
    result = earlyaccesna(year)
    return result


@app.get("/sentiment/{years}")
async def earlyacces(year: str):
    result = sentimentna(year)
    return result




