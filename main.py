from fastapi import FastAPI
from dotenv import load_dotenv
from routes.auth import auth_routes
from routes.user_api import info_api
app= FastAPI("Autho")
app.include_router(auth_routes)
app.include_router(info_api)
load_dotenv()