import requests
from bs4 import BeautifulSoup
import pandas as pd

# Wikipedia page URL
url = "https://en.wikipedia.org/wiki/Comma-separated_values"

# Get HTML content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the first table with class 'wikitable'
table = soup.find("table", {"class": "wikitable"})

# Parse table
rows = table.find_all("tr")
data = []

for row in rows:
    cols = row.find_all(["td", "th"])
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

# Convert to DataFrame
df = pd.DataFrame(data[1:], columns=data[0])

# Save CSV locally
df.to_csv("cars.csv", index=False)

print("CSV saved successfully!")
