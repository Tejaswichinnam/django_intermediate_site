import requests
from bs4 import BeautifulSoup

def scrape_flipkart():
    url = "https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DApple"
    headers = {"User-Agent": "Mozilla/5.0"}  
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    names = [i.get_text() for i in soup.find_all('div', class_="KzDlHZ")[2:20]]
    prices = [i.get_text() for i in soup.find_all('div', class_="Nx9bqj _4b5DiR")[2:20]]
    links = ["https://www.flipkart.com" + i['href'] for i in soup.find_all('a', class_="CGtC98")[2:20]]
    images = [i['src'] for i in soup.find_all('img', class_="DByuf4")[2:20]]

    return zip(names, prices, links, images)
