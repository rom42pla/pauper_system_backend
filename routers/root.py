from fastapi import FastAPI

from routers import misc

app = FastAPI()


app.include_router(misc.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}