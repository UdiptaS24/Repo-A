from fastapi import FastAPI
import httpx
import os
app = FastAPI()
from dotenv import load_dotenv
load_dotenv()

secret1 = os.getenv("ENV_1")
secret2 = os.getenv("ENV_2")