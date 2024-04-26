import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def root():
    return {"message": "Hello World"}

@app.get("/getwaterleveldatas")
async def get_water_level_datas():
    pass

@app.post("/setValveStatus")
async def set_valve_status():
    pass
if __name__ == '__main__':
    #debug mode
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
    print("running")