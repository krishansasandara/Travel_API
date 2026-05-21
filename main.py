from typing import List

from fastapi import FastAPI
from starlette import status
from starlette.exceptions import HTTPException

from models.destination import DestinationResponse, DestinationCreate
from service.service import DestinationService

app = FastAPI(title="Sri Lanka Travel Assistant API")
destination_service = DestinationService()

@app.post("/destination",response_model=DestinationResponse,status_code=status.HTTP_201_CREATED)
def create_destination(destination: DestinationCreate) -> DestinationResponse:

    try:
        return destination_service.create_destination(destination)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(e))

@app.get(f"/destination")
def get_all_destination() -> List[DestinationResponse]:
    return destination_service.get_all_destination()

@app.get("/destination/{dest_id}")
def get_destination_by_id(dest_id : int):
    destination = destination_service.get_destination(dest_id)

    if  destination:
        return destination
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = "Destination Not found")


