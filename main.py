from bs4 import BeautifulSoup
import requests

def get_games():
    html_text = requests.get("https://store.steampowered.com/search/?filter=topsellers").text
    soup = BeautifulSoup(html_text, "lxml")
    game_results = soup.find_all("a", class_ = "search_result_row")
    for game in game_results:
        price = game.find("div", class_ = "discount_final_price")
        if price is None:
            price = "$00.00"
        else:
            price = price.text
        # if "$" in price:
        #     price.strip("$")
        #     if "." in price:
        #         dollars, cents = price.split(".")
        #         if len(dollars) >= 3:

        title = game.find("span", class_ = "title").text
        release = game.find("div", class_ = "search_released").text


        # image = game_results.find("div", class_ = "search_capsule").img
        # review = game_results.find("span", class_ = "search_review_summary")
        print(f"Title: {title}\nRelease: {release}\nPrice: {price}")
        # print(price)
    
get_games()

# <a href="https://store.steampowered.com/app/730/CounterStrike_2/?snr=1_7_7_7000_150_1" data-ds-appid="730" data-ds-itemkey="App_730" data-ds-tagids="[1663,1774,3859,3878,19,5711,5055]" data-ds-descids="[2,5]" data-ds-crtrids="[4]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:730,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )"
# class="search_result_row ds_collapse_flag  app_impression_tracked" data-search-page="1" data-gpnav="item" data-ds-steam-deck-compat-handled="true">
#             <div class="col search_capsule"><img src="https://cdn.cloudflare.steamstatic.com/steam/apps/730/capsule_sm_120.jpg?t=1696011820" srcset="https://cdn.cloudflare.steamstatic.com/steam/apps/730/capsule_sm_120.jpg?t=1696011820 1x, https://cdn.cloudflare.steamstatic.com/steam/apps/730/capsule_231x87.jpg?t=1696011820 2x"></div>
#             <div class="responsive_search_name_combined">
#                 <div class="col search_name ellipsis">
#                     <span class="title">Counter-Strike 2</span>
#                     <div>
#                                                 <span class="platform_img win"></span><span class="platform_img linux"></span>                                            </div>
#                 </div>
#                 <div class="col search_released responsive_secondrow">Aug 21, 2012</div>
#                 <div class="col search_reviewscore responsive_secondrow">
#                                             <span class="search_review_summary positive" data-tooltip-html="Very Positive<br>88% of the 7,590,882 user reviews for this game are positive.">
# 								</span>
#                                     </div>


#                 <div class="col search_price_discount_combined responsive_secondrow" data-price-final="1499">
#                     <div class="col search_discount_and_price responsive_secondrow">
#                         <div class="discount_block search_discount_block no_discount" data-price-final="1499" data-bundlediscount="0" data-discount="0"><div class="discount_prices"><div class="discount_final_price">$14.99</div></div></div>                    </div>
#                 </div>
#             </div>


#             <div style="clear: left;"></div>
#         </a>