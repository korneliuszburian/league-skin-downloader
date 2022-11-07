import urllib.request
import zipfile
import os.path
import requests
from bs4 import BeautifulSoup

def get_filtered_links(url, filter):
    """Returns a list of links that match a filter"""
    links = []
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features='lxml')
    
    for tag in soup.find_all('a'):
        links.append(tag.get('href'))

    for link in links:
        if link.endswith(filter):
            correct_link = link
            break
        
    return correct_link

def extract_zip_file(zip_file, filter, destination):
    """Extracts a zip file to a destination folder"""
    with zipfile.ZipFile(zip_file[0], 'r') as zip_ref:
        for y in zip_ref.namelist():
            if y.startswith(filter):
                zip_ref.extractall(destination)
                os.startfile(destination + y)
        
output_path = 'C:/Users/username/Desktop/'
retrieved_file = urllib.request.urlretrieve(get_filtered_links(('http://leagueskin.net/p/download-mod-skin-2020-chn'), '.zip'))
extract_zip_file(retrieved_file, 'LOLPRO', output_path)
