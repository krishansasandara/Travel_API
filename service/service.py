from datetime import datetime
from typing import Optional, List

from models.destination import DestinationCreate, DestinationResponse


class DestinationService:

    def __init__(self):
        self.destination: dict[int, dict] = {}
        self.count: int = 0

    def create_destination(self,create_data: DestinationCreate) -> DestinationResponse:

        for dest in self.destination.values():
            if dest["name"] == create_data.name:
                raise ValueError(f"Destination {create_data.name} already exists")

        dest_id = self.count

        new_destination = {
            "name" : create_data.name,
            "city" : create_data.city,
            "province" : create_data.province,
            "category" : create_data.category,
            "description" : create_data.description,
            "entry_fee" : create_data.entry_fee,
            "rating" : create_data.rating,
            "is_unesco" : create_data.is_unesco,
            "tags" : create_data.tags,
            "created_at" : datetime.now().isoformat(),
            "updated_at" : datetime.now().isoformat()
        }
        self.destination[dest_id] = new_destination
        self.count += 1
        return DestinationResponse(**new_destination) #DestinationResponse(name = new_destination["name"]

    def get_destination(self,dest_id: int) -> Optional[DestinationResponse]:
        if dest_id not in self.destination:
            return None
        return DestinationResponse(**self.destination[dest_id])

    def get_all_destination(self) -> List[DestinationResponse]:
        destination : List[DestinationResponse] = []

        for dest in self.destination.values():
            destination.append(DestinationResponse(**dest))

        return destination