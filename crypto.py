from requests import get
from json import loads, dumps

# Define API key here
API_KEY = "3A8F4370-B2E7-49A9-879C-D54777EAC4E7"

base_url = "https://rest.coinapi.io"

symbol_id = "BINANCE_SPOT_BTC_USDT"

# Define endpoint url here
# endpoint_url = base_url + "/v1/trades/latest"
endpoint_url = base_url + f"/v1/ohlcv/{symbol_id}/latest"

# Define header elements here
url_headers = {"authorization": API_KEY}

# Define URL parameters here
url_parameters = {
    # URL parameter to filter asset results based on asset ID
#     "filter_symbol_id": "BITSTAPM_;BINANCE_SPOT_",
#     "filter_exchange_id":"ECB;COINBASE;BINANCE",
#     "filter_asset_id": "BTC;ETH"
    #   "limit":"25",
    #   "filter_symbol_id": "BINANCE_",
    #   "include_id":True
    "period_id":"1HRS",
    "include_empty_items": True,
    "limit":100
 }

# Function to make API call to CoinAPI
def make_api_call(url, headers, params):
    # Making GET request
    res = get(url=url, headers=headers, params=params)

    # Checking if API returns any errors in the response
    if res.status_code != 200:
        # Printing custom status error message
        print(res)
        return

    # Printing custom header elements header element
    print(res.headers)

    # Printing a clean JSON response
    print("\nJSON Response:")
    parsed_json = loads(res.content)
    formatted_json = dumps(parsed_json, indent=4)
    print(formatted_json)

# Calling API
make_api_call(endpoint_url, url_headers, url_parameters)