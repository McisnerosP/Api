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







# class Dato(BaseModel):
#     valor:str

# # @info_api.post("/site")
# # def api_site(varibale:Sites):
# #     return get(f'https://inventory-restapi-h36rii5v2q-ue.a.run.app/infopersite/"{varibale.name}"').json()
# @info_api.post("/site/")
# async def api_site(val:Dato):
#     return get(f'https://inventory-restapi-h36rii5v2q-ue.a.run.app/infopersite/"{val.valor}"').json()
   
# @info_api.get("/site/{item}")
# def search(item:str):
#     print(item)
#     print("as there")
#     return post(f'https://inventory-restapi-h36rii5v2q-ue.a.run.app/infopersite/"{" ":item}')
#     print(item)
#     print("hello there")

