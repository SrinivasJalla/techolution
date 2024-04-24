import os
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

           

def read_csv_file(csv_filename):
    df = pd.read_csv(csv_filename)
    return df

csv_filename = 'extracted_links.csv'
data_frame = read_csv_file(csv_filename)
links = data_frame['link']
text = data_frame['text']

filename_counter = 1

for link, text in zip(links, text):
    url = link
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    article = soup.find('article', role='main')
    
    filename = f"filename{filename_counter}.csv"
    filename_counter += 1
    
    directory = 'downloaded_data'
    os.makedirs(directory, exist_ok=True)
    
    with open(os.path.join(directory, filename), 'w', newline='') as csvfile:
        fieldnames = ['heading', 'sub_heading', 'code']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        if article:
            sections = article.find_all('section')
            for section in sections:
                section_id = section.get('id')
                section_name = section.find('h2').text.strip() if section.find('h2') else ""
                
                inner_section = soup.find('section', id=section_id)
                if inner_section:
                    h2_tag = inner_section.find('h2')
                    heading = h2_tag.text.strip() if h2_tag else ""
                    
                    h3_tag = inner_section.find('h3')
                    sub_heading = h3_tag.text.strip() if h3_tag else ""
                    
                    pre_element = inner_section.find('pre')
                    code = pre_element.text.strip() if pre_element else ""
                    
                    writer.writerow({'heading': heading, 'sub_heading': sub_heading, 'code': code})





