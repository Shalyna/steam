from bs4 import BeautifulSoup
import requests
import re
import time


def get_games():
    html_text = requests.get("https://store.steampowered.com/search/?filter=topsellers").text
    soup = BeautifulSoup(html_text, "lxml")
    game_results = soup.find_all("a", class_ = "search_result_row")
    
    for game in game_results:
        price = game.find("div", class_ = "discount_final_price")
        if price is None:
            price = 0000
        else:
            price = price.text

        title = game.find("span", class_ = "title").text
        release = game.find("div", class_ = "search_released").text
        link = game['href']

        print(f"Title: {title}\nRelease: {release}\nPrice: {price}\nMore Info: {link}\n")

    
if __name__ == "__main__":
    while True:
        get_games()
        time.sleep(600)