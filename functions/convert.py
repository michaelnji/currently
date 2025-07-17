import requests

def convert_currency(api_key, from_currency, to_currency, amount):
    """
    Convert currency using the UnirateAPI
    """

    import requests

    base_url = "https://api.unirateapi.com/api"
    url = f"{base_url}/convert"
    
    params = {
        "api_key": api_key,
        "from": from_currency,
        "to": to_currency,
        "amount": amount
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        jsonData = response.json()
        return {
            "from_": jsonData.get("from"),
            "to": jsonData.get("to"),
            "amount": jsonData.get("amount"),
            "result": jsonData.get("result")
        }
    else:
        raise Exception(f"[{response.status_code}] API request failed: {response.text}")