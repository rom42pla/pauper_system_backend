import os
import uvicorn
from os.path import join, exists

from scripts import utils
# from models.bots import ScemoBot
from routers import root

env_filepath = join(".", "conf.env")

if __name__ == "__main__":
    # eventually read environmental variables from file
    if exists(env_filepath):
        utils.export_env(env_filepath)

    # runs the server
    uvicorn.run(root.app)
