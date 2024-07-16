from fastapi import FastAPI

app = FastAPI()

@app.get("/return_1")
async def return_1():
    return {"value": 1}

@app.get("/return_2")
async def return_2():
    return {"value": 2}

@app.get("/return_3")
async def return_3():
    return {"value": 3}

@app.get("/return_4")
async def return_4():
    return {"value": 4}
