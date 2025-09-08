import requests
import time

class FipeAPIClient:
    BASE_URL = "https://fipe.parallelum.com.br/api/v2"

    def __init__(self, api_key=None):
        self.api_key = api_key
        self.headers = {}
        if self.api_key:
            self.headers['X-Subscription-Token'] = self.api_key

    def _make_request(self, endpoint, retries=3, backoff_factor=1):
        url = f"{self.BASE_URL}/{endpoint}"
        for i in range(retries):
            try:
                response = requests.get(url, headers=self.headers)
                response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"Error making request to FIPE API: {e}")
                if i < retries - 1:
                    time.sleep(backoff_factor * (2 ** i))
                else:
                    return None

    def get_brands(self, vehicle_type):
        # vehicle_type can be 'cars', 'motos', 'caminhoes'
        endpoint = f"{vehicle_type}/brands"
        return self._make_request(endpoint)

    def get_models(self, vehicle_type, brand_code):
        endpoint = f"{vehicle_type}/brands/{brand_code}/models"
        return self._make_request(endpoint)

    def get_years(self, vehicle_type, brand_code, model_code):
        endpoint = f"{vehicle_type}/brands/{brand_code}/models/{model_code}/years"
        return self._make_request(endpoint)

    def get_price(self, vehicle_type, brand_code, model_code, year_code):
        endpoint = f"{vehicle_type}/brands/{brand_code}/models/{model_code}/years/{year_code}"
        return self._make_request(endpoint)