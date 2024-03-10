from geocoders.geocoder import Geocoder
from api import API


# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:
        """
            TODO:
            - Делать запросы к API для каждой area
            - Для каждого ответа формировать полный адрес
        """

        address = API.get_area(area_id).name
        id = str(area_id)

        while API.get_area(area_id).parent_id is not None:
            area_id = API.get_area(area_id).parent_id
            address = API.get_area(area_id).name + ', ' + address
        address = id + ',"' + address + '"'
        return address