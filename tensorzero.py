import requests

def get_status() -> bool:
    try:
        resp = requests.get("https://api.tensorzero.com/status")
        return resp.json()['status'] == 'ok'
    except:
        return False
