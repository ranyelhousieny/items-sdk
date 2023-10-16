import requests

class ItemsAPI:
    def __init__(self, base_url="http://127.0.0.1:8000"):
        self.base_url = base_url

    def create_item(self, name: str, price: float, description: str = None) -> dict:
        data = {
            "name": name,
            "price": price
        }
        if description:
            data["description"] = description
        response = requests.post(f"{self.base_url}/items/", json=data)
        response.raise_for_status()
        return response.json()

    def get_items(self) -> list:
        response = requests.get(f"{self.base_url}/items/")
        response.raise_for_status()
        return response.json()

    def get_item(self, item_id: int) -> dict:
        response = requests.get(f"{self.base_url}/items/{item_id}")
        response.raise_for_status()
        return response.json()

    def update_item(self, item_id: int, name: str, price: float, description: str = None) -> dict:
        data = {
            "name": name,
            "price": price
        }
        if description:
            data["description"] = description
        response = requests.put(f"{self.base_url}/items/{item_id}", json=data)
        response.raise_for_status()
        return response.json()

    def delete_item(self, item_id: int) -> dict:
        response = requests.delete(f"{self.base_url}/items/{item_id}")
        response.raise_for_status()
        return response.json()
