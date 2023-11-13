import requests
import pandas as pd
from datetime import datetime

def fetch_data_and_save_to_csv(api_endpoint, csv_filename):
    response = requests.get(api_endpoint)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df.to_csv(csv_filename, index=False)
        print(f"Data saved to {csv_filename}")
    else:
        print(f"Failed to retrieve data from {api_endpoint}: {response.status_code}")


endpoints = {
    "311_Service_Requests": "https://data.cityofnewyork.us/resource/erm2-nwe9.json",
    "Restaurant_Inspection_Results": "https://data.cityofnewyork.us/resource/43nn-pn8j.json"
}


current_date = datetime.now().strftime("%Y-%m-%d")

for name, endpoint in endpoints.items():
    csv_filename = f"{name}_{current_date}.csv"
    fetch_data_and_save_to_csv(endpoint, csv_filename)