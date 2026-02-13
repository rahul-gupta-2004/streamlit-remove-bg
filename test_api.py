import requests

url = "https://background-remover-api.onrender.com"

# Test if API is reachable
try:
    r = requests.get(f"{url}/docs", timeout=5)
    print(f"API is live! Status: {r.status_code}")
    print(f"URL: {url}")
except Exception as e:
    print(f"API not reachable: {e}")