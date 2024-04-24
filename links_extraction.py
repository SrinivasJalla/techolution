import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin


def extract_links_and_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    toctree_div = soup.find('div', class_='toctree-wrapper compound')
    
    links = []
    
    if toctree_div:
        link_tags = toctree_div.find_all('a', class_='reference internal')
        
        for tag in link_tags:
            relative_url = tag.get('href')
            full_url = urljoin(url, relative_url)
            text = tag.text
            links.append({'link': full_url, 'text': text})
            
    return links

def write_to_csv(links, filename='extracted_links.csv'):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['link', 'text']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for link in links:
            writer.writerow(link)
            
            
url = "https://packaging.python.org/en/latest/guides/section-install/"
extracted_links = extract_links_and_text(url)
write_to_csv(extracted_links)