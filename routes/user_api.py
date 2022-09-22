from fastapi import APIRouter
from pydantic import BaseModel
from requests import get
from middlewares.verify_token_route import VerifyTokenRoute
from os import getenv
from dotenv import load_dotenv

info_api = APIRouter(route_class=VerifyTokenRoute)
load_dotenv()

@info_api.get("/inventory")
def api_inventory():
    # return get('https://inventory-restapi-h36rii5v2q-ue.a.run.app/inventariolist').json()
    return get(f"{getenv('LINK_INVENTARIO')}").json()



