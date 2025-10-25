# Very small Nova Poshta stub (real implementation should use requests/httpx and cache results)
from app.config import settings

class NovaPoshtaClient:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or settings.NP_API_KEY

    def find_cities(self, query: str):
        # Placeholder: return demo city
        return [{"Ref": "demo-city-ref", "Description": "Kyiv"}]

    def get_warehouses(self, city_ref: str):
        return [{"Ref": "wh-1", "Description": "Central branch"}]
