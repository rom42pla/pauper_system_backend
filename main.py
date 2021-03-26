import uvicorn
from os.path import join, exists

from fastapi import FastAPI

from routers import misc
from scripts import utils

env_filepath = join(".", "conf.env")

app = FastAPI()

app.include_router(misc.router)


@app.get("/")
async def root():
    return {"message": "Welcome to Pauper System Backend! Check /docs for documentation!"}


if __name__ == "__main__":
    # eventually read environmental variables from file
    if exists(env_filepath):
        utils.export_env(env_filepath)

    uvicorn.run(app=app)