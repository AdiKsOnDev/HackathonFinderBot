import json

import lxml
from bs4 import BeautifulSoup
from selenium import webdriver

URL = 'https://lablab.ai/event'

def get_hackathons(url):
    """Gets the list of upcoming Hackathons

    Args:
        url (str): The url of 'LabLabAI'

    Returns:
        Dictionary: The dictionary containing 'name': 'url' of upcoming Hackathons
    """    

    hackathons = {}

    # Get the html code of the page
    driver = webdriver.Chrome()
    driver.get(url)

    # 'Cook' the soup 
    soup = BeautifulSoup(driver.page_source, 'lxml')

    # Find the list of available Hackathons
    hackathon_cards = soup.find_all(
            'div', 
            {
                'class': 'card-animation card-border card-shadow relative flex h-full flex-col overflow-hidden rounded-lg bg-white'
            }
        )
    
    for card in hackathon_cards:
        on_going = card.find('span')

        # Check if the Hackathon is finished
        if on_going.string == "Register":
            hackathon_name = card.find('h2').string
            hackathon_url = "https://lablab.ai" + card.find('a')['href']

            hackathons[hackathon_name] = hackathon_url

            print(hackathon_url)
    
    with open("hackathons.json", "w") as outfile:
        json.dump(hackathons, outfile)
    
    return hackathons

if __name__ == "__main__":
    get_hackathons(url=URL)