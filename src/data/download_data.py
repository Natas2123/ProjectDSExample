# download_data.py
import requests

url = "https://gist.githubusercontent.com/javierIA/bc3a0167e9f3085019382976d4abf315/raw/990a37420be156cb9c7e2829092d948ba7f2acc1/RH_bruto.csv"
response = requests.get(url)

with open("./data/raw/RH_bruto.csv", "wb") as f:
    f.write(response.content)
