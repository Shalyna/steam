from bs4 import BeautifulSoup
import requests
import re


def get_games():
    price_list = []
    html_text = requests.get("https://store.steampowered.com/search/?filter=topsellers").text
    soup = BeautifulSoup(html_text, "lxml")
    game_results = soup.find_all("a", class_ = "search_result_row")
    for game in game_results:
        price = game.find("div", class_ = "discount_final_price")
        if price is None:
            price = 0000
            price_list.append(price)
        else:
            price = price.text
            price = price.strip("$")
            price = re.sub("[.]", "", price)
            price = int(price)
            price_list.append(price)
        
        price_list.sort()
        
    print(price_list)
    
get_games()
