from fastapi import APIRouter
from pydantic import BaseModel
from requests import get
from middlewares.verify_token_route import VerifyTokenRoute

info_api = APIRouter(route_class=VerifyTokenRoute)






@info_api.get("/inventory")
def api_inventory():
    return get('https://inventory-restapi-h36rii5v2q-ue.a.run.app/inventariolist').json()