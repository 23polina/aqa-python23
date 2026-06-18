import requests


class ApiClient:
    def __init__(self, base_url):
        self.url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def get_request(self, endpoint: str):
        return requests.get(f"{self.url}{endpoint}", timeout=5)

    def post_request(self, endpoint: str, body: dict):
        return requests.post(f"{self.url}{endpoint}", json=body, headers=self.headers, timeout=5)

    def put_request(self, endpoint: str, body: dict, token=None):
        headers_cookies = self.headers.copy()
        if token:
            headers_cookies["Cookie"] = f"token={token}"
        return requests.put(f"{self.url}{endpoint}", json=body, headers=headers_cookies, timeout=5)

    def patch_request(self, endpoint: str, body: dict, token=None):
        headers_cookies = self.headers.copy()
        if token:
            headers_cookies["Cookie"] = f"token={token}"
        return requests.patch(f"{self.url}{endpoint}",
                              json=body, headers=headers_cookies, timeout=5)

    def delete_request(self, endpoint: str, token=None):
        headers_cookies = self.headers.copy()
        if token:
            headers_cookies["Cookie"] = f"token={token}"
        return requests.delete(f"{self.url}{endpoint}", headers=headers_cookies, timeout=5)
