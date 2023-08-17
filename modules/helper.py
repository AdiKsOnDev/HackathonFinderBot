import lxml
from bs4 import BeautifulSoup
from selenium import webdriver

URL = 'https://lablab.ai/event'
HEADERS = {

    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'

} 

def check_for_hackathons(url, headers):
    """_summary_
    """
    # Request the html code of the page
    driver = webdriver.Chrome()
    driver.get(url)

    # 'Cook' the soup 
    soup = BeautifulSoup(driver.page_source, 'lxml')

    # Create the list of available Hackathons
    hackathon_cards = soup.find(
            'div', 
            {
                'class': 'card-animation card-border card-shadow relative flex h-full flex-col overflow-hidden rounded-lg bg-white'
            }
        )

    return hackathon_cards.prettify()

if __name__ == "__main__":
    print(check_for_hackathons(url=URL, headers=HEADERS))