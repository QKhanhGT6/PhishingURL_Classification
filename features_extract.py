from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse, urljoin
import re
import numpy as np

def count_self_references(url, soup):
    """
    Count the number of internal (self-referencing) links on the page.
    """
    domain = urlparse(url).netloc
    self_ref_count = 0

    for link in soup.find_all('a', href=True):
        href = urljoin(url, link['href'])
        if domain in urlparse(href).netloc:  # Check if the link belongs to the same domain
            self_ref_count += 1

    return self_ref_count

def check_social_links(soup):
    social_sites = ['facebook.com', 'twitter.com', 'linkedin.com', 'instagram.com', 'youtube.com', 'pinterest.com']
    has_social_net = 0

    for link in soup.find_all('a', href=True):
        if any(social in link['href'] for social in social_sites):  # Check if the link contains a social site domain
            has_social_net = 1
            break

    return has_social_net

def extract_features(url):

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    features = [
        50, #"URLSimilarityIndex"
        len(re.findall(r'[^\w/:]', url)),  # NoOfOtherSpecialCharsInURL
        round(len(re.findall(r'[^\w/:]', url)) / len(url), 2),  # SpacialCharRatioInURL rounded to 2 decimals
        1 if urlparse(url).scheme == 'https' else 0,  # IsHTTPS
        len(html.split('\n')),  # LineOfCode
        50, #"DomainTitleMatchScore"
        50, #"URLTitleMatchScore"
        1 if soup.find('meta', attrs={"name": "viewport"}) else 0,  # IsResponsive
        1 if soup.find('meta', attrs={"name": "description"}) else 0,  # HasDescription
        check_social_links(soup), #"HasSocialNet"
        1 if soup.find('button') or soup.find('input', attrs={"type": "submit"}) else 0,  # HasSubmitButton
        1 if "©" in html or "copyright" in html.lower() else 0,  # HasCopyrightInfo
        len(soup.find_all('img')),  # NoOfImage
        len(soup.find_all('script')),  # NoOfJS
        count_self_references(url, soup) #"NoOfSelfRef"
    ]

    return [np.array(features)]