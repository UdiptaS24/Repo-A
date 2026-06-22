from fastapi import FastAPI
import os
app = FastAPI()
from dotenv import load_dotenv
load_dotenv()

secret1 = os.getenv("ENV_1")