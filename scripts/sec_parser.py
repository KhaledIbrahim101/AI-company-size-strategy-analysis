# sec_parser.py
import os
import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.sec.gov/Archives/edgar/data"
HEADERS = {'User-Agent': 'MBA-Thesis-Researcher/1.0'}

def download_10k(cik, accession_number, save_dir="sec_filings"):
    accession_formatted = accession_number.replace("-", "")
    url = f"{BASE_URL}/{cik}/{accession_formatted}/{accession_number}-index.htm"
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text, 'html.parser')

    doc_link = None
    for row in soup.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) > 3 and "10-K" in cols[0].text:
            doc_link = "https://www.sec.gov" + cols[2].a['href']
            break

    if doc_link:
        doc = requests.get(doc_link, headers=HEADERS)
        os.makedirs(save_dir, exist_ok=True)
        with open(os.path.join(save_dir, f"{cik}_{accession_number}.html"), 'w', encoding='utf-8') as f:
            f.write(doc.text)
        print(f"Downloaded {accession_number}")
    else:
        print("10-K document not found.")

# Example usage
# download_10k("0000320193", "0000320193-23-000105")
