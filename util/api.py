import requests 

base_url = 'https://api.worldbank.org/v2/'

def get_wb_data(endpoint, params={}):
    url = base_url + endpoint
    parameters = params | {'format': 'json'} # Extend the parameters to keep response in json format

    response = requests.get(url, parameters)

    if response.status_code == 200:
        data = response.json()
    else:
        return response
    return data[1]