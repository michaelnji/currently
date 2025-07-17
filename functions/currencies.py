def fetchCurrencies(api_key):
    """
    Convert currency using the UnirateAPI
    """

    import requests

    base_url = "https://api.unirateapi.com/api"
    url = f"{base_url}/currencies"
    
    params = {
        "api_key": api_key,
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"[{response.status_code}] API request failed: {response.text}")