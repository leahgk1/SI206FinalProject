import requests
import re
from bs4 import BeautifulSoup
import json


cities = [
    "New York City", "Orlando", "Miami", "Boston", "Washington D.C.",
    "Philadelphia", "Atlanta", "Charleston", "Savannah", "Richmond",
    "Charlotte", "Cleveland", "Baltimore", "Pittsburgh", "Detroit",
    "Jacksonville", "Indianapolis", "Hartford", "Cincinnati", "Providence",
    "Columbus", "Raleigh", "Buffalo", "Augusta", "Tampa"
]
cities_hotels = {
    "New York City": {   
    },
    "Orlando": {
    },
    "Miami": {
    },
    "Boston": {
    },
    "Washington D.C.": {
    },
    "Philadelphia": {
    },
    "Atlanta": {
    },
    "Charleston": {
    },
    "Savannah": {
    },
    "Richmond": {
    },
    "Charlotte": {
    },
    "Cleveland": {
    },
    "Baltimore": {
    },
    "Pittsburgh": {
    },
    "Detroit": {
    },
    "Jacksonville": {
    },
    "Indianapolis": {
    },
    "Hartford": {
    },
    "Cincinnati": {
    },
    "Providence": {
    },
    "Columbus": {
    },
    "Raleigh": {
    },
    "Buffalo": {
    },
    "Augusta": {
    },
    "Tampa": {
    }
}
# URL of the webpage to scrape
url = "https://www.expedia.com/Hotel-Search?destination=Manhattan%2C%20New%20York%2C%20New%20York%2C%20United%20States%20of%20America&regionId=129440&latLong=40.783062%2C-73.971252&d1=2025-05-01&startDate=2025-05-01&d2=2025-05-03&endDate=2025-05-03&adults=2&rooms=1&isInvalidatedDate=false&upsellingNumNightsAdded=&theme=&userIntent=&semdtl=&upsellingDiscountTypeAdded=&useRewards=false&sort=RECOMMENDED&children=&mapBounds=&pwaDialog="
Manhattan_url = "https://www.booking.com/searchresults.html?ss=Manhattan%2C+New+York%2C+New+York%2C+United+States&map=1&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKV59S_BsACAdICJDJhMmUxZWM4LTgyZTktNDcyNy1hMWJiLTMyMTAxN2FhNTdhMNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=929&dest_type=district&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=eaf0664a5e58079d&ac_meta=GhBlYWYwNjY0YTVlNTgwNzlkIAAoATICZW46BW1hbmhhQABKAFAA&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0#map_opened"
# Send a GET request to the URL

# Manhattan
response = requests.get(Manhattan_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('expedia.html', 'w', encoding='utf-8') as file:
    #     file.write(soup.prettify())
    # Find the hotel listings
    for listings in soup.find_all('span', class_='bui-card__title'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('div', class_='bui-price-display__value bui-f-color-constructive')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[0]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices

    

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
#orlando scrape
Orlando_url = "https://www.booking.com/searchresults.html?ss=Orlando%2C+Florida%2C+United+States&ssne=Tampa&ssne_untouched=Tampa&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20023488&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=71f09aa541290557&ac_meta=GhA3MWYwOWFhNTQxMjkwNTU3IAAoATICZW46B09ybGFuZG9AAEoAUAA%3D&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0#map_opened"
orlando_response = requests.get(Orlando_url)
# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    o_soup = BeautifulSoup(orlando_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # # save contents to a file
    # with open('orlando.html', 'w', encoding='utf-8') as file:
    #     file.write(o_soup.prettify())


    # Find the hotel listings
    for listings in o_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[1]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices



# Miami scrape
Miami_url = "https://www.booking.com/searchresults.html?ss=Miami&ssne=Miami&ssne_untouched=Miami&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20023181&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
miami_response = requests.get(Miami_url)
# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    m_soup = BeautifulSoup(miami_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('miami.html', 'w', encoding='utf-8') as file:
    #     file.write(m_soup.prettify())
    # Find the hotel listings
    for listings in m_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[2]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices



# Boston scrape
Boston_url = "https://www.booking.com/searchresults.html?ss=Boston&ssne=Boston&ssne_untouched=Boston&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20061717&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
boston_response = requests.get(Boston_url)
# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    b_soup = BeautifulSoup(boston_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('boston.html', 'w', encoding='utf-8') as file:
    #     file.write(b_soup.prettify())
    # Find the hotel listings
    for listings in b_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[3]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices


# Washington D.C. scrape
Washington_D_C_url = "https://www.booking.com/searchresults.html?ss=Downtown+D.C.&ssne=Downtown+D.C.&ssne_untouched=Downtown+D.C.&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=928&dest_type=district&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
washington_response = requests.get(Washington_D_C_url)
# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    w_soup = BeautifulSoup(washington_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('washington.html', 'w', encoding='utf-8') as file:
    #     file.write(w_soup.prettify())
    # Find the hotel listings
    for listings in w_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[4]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices


# Philadelphia scrape
Philadelphia_url = "https://www.booking.com/searchresults.html?ss=Philadelphia&ssne=Philadelphia&ssne_untouched=Philadelphia&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20111994&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
philadelphia_response = requests.get(Philadelphia_url)
# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    p_soup = BeautifulSoup(philadelphia_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('philadelphia.html', 'w', encoding='utf-8') as file:
    #     file.write(p_soup.prettify())
    # Find the hotel listings
    for listings in p_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[5]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices



# Atlanta scrape
Atlanta_url = "https://www.booking.com/searchresults.html?ss=Atlanta&ssne=Atlanta&ssne_untouched=Atlanta&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20024809&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
atlanta_response = requests.get(Atlanta_url)
if response.status_code == 200:
    # Parse the HTML content of the page
    a_soup = BeautifulSoup(atlanta_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('atlanta.html', 'w', encoding='utf-8') as file:
    #     file.write(a_soup.prettify())
    # Find the hotel listings
    for listings in a_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[6]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices



# Charleston scrape
Charleston_url = "https://www.booking.com/searchresults.html?ss=Charleston&ssne=Charleston&ssne_untouched=Charleston&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20115955&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
charleston_response = requests.get(Charleston_url)
if response.status_code == 200:
    # Parse the HTML content of the page
    c_soup = BeautifulSoup(charleston_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('charleston.html', 'w', encoding='utf-8') as file:
    #     file.write(c_soup.prettify())
    # Find the hotel listings
    for listings in c_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[7]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices


# Savannah scrape
Savannah_url = "https://www.booking.com/searchresults.html?ss=Savannah&ssne=Savannah&ssne_untouched=Savannah&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20029490&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
savannah_response = requests.get(Savannah_url)
if response.status_code == 200:
    # Parse the HTML content of the page
    s_soup = BeautifulSoup(savannah_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('savannah.html', 'w', encoding='utf-8') as file:
    #     file.write(s_soup.prettify())
    # Find the hotel listings
    for listings in s_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[8]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices


# Richmond scrape
Richmond_url = "https://www.booking.com/searchresults.html?ss=Richmond&ssne=Richmond&ssne_untouched=Richmond&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20141027&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
richmond_response = requests.get(Richmond_url)
if response.status_code == 200:
    # Parse the HTML content of the page
    r_soup = BeautifulSoup(richmond_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('richmond.html', 'w', encoding='utf-8') as file:
    #     file.write(r_soup.prettify())
    # Find the hotel listings
    for listings in r_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[9]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices


# Charlotte scrape
Charlotte_url = "https://www.booking.com/searchresults.html?ss=Charlotte&ssne=Charlotte&ssne_untouched=Charlotte&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20091627&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
charlotte_response = requests.get(Charlotte_url)
if response.status_code == 200:
    # Parse the HTML content of the page
    char_soup = BeautifulSoup(charlotte_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('charlotte.html', 'w', encoding='utf-8') as file:
    #     file.write(char_soup.prettify())
    # Find the hotel listings
    for listings in char_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[10]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices


# Cleveland scrape
Cleveland_url = "https://www.booking.com/searchresults.html?ss=Cleveland&ssne=Cleveland&ssne_untouched=Cleveland&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20097630&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
cleveland_response = requests.get(Cleveland_url)
if response.status_code == 200:
    # Parse the HTML content of the page
    cleve_soup = BeautifulSoup(cleveland_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('cleveland.html', 'w', encoding='utf-8') as file:
    #     file.write(cleve_soup.prettify())
    # Find the hotel listings
    for listings in cleve_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[11]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices


# Baltimore scrape
Baltimore_url = "https://www.booking.com/searchresults.html?ss=Baltimore&ssne=Baltimore&ssne_untouched=Baltimore&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20053799&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
baltimore_response = requests.get(Baltimore_url)
if response.status_code == 200:
    # Parse the HTML content of the page
    balt_soup = BeautifulSoup(baltimore_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('baltimore.html', 'w', encoding='utf-8') as file:
    #     file.write(balt_soup.prettify())
    # Find the hotel listings
    for listings in balt_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[12]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices


# Pittsburgh scrape
Pittsburgh_url = "https://www.booking.com/searchresults.html?ss=Pittsburgh&ssne=Pittsburgh&ssne_untouched=Pittsburgh&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20112087&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
pittsburgh_response = requests.get(Pittsburgh_url)
if response.status_code == 200:
    # Parse the HTML content of the page
    pitts_soup = BeautifulSoup(pittsburgh_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('pittsburgh.html', 'w', encoding='utf-8') as file:
    #     file.write(pitts_soup.prettify())
    # Find the hotel listings
    for listings in pitts_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[13]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices


# Detroit scrape
Detroit_url = "https://www.booking.com/searchresults.html?ss=Detroit&ssne=Detroit&ssne_untouched=Detroit&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20064402&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
detroit_response = requests.get(Detroit_url)
if response.status_code == 200:
    # Parse the HTML content of the page
    det_soup = BeautifulSoup(detroit_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('detroit.html', 'w', encoding='utf-8') as file:
    #     file.write(det_soup.prettify())
    # Find the hotel listings
    for listings in det_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[14]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices


# Jacksonville scrape
Jacksonville_url = "https://www.booking.com/searchresults.html?ss=Jacksonville&ssne=Jacksonville&ssne_untouched=Jacksonville&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20022757&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
jacksonville_response = requests.get(Jacksonville_url)
if response.status_code == 200:
    # Parse the HTML content of the page
    jack_soup = BeautifulSoup(jacksonville_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('jacksonville.html', 'w', encoding='utf-8') as file:
    #     file.write(jack_soup.prettify())
    # Find the hotel listings
    for listings in jack_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[15]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices


# Indianapolis scrape
Indianapolis_url = "https://www.booking.com/searchresults.html?ss=Indianapolis&ssne=Indianapolis&ssne_untouched=Indianapolis&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20037880&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
indianapolis_response = requests.get(Indianapolis_url)
if response.status_code == 200:
    # Parse the HTML content of the page
    in_soup = BeautifulSoup(indianapolis_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('indianapolis.html', 'w', encoding='utf-8') as file:
    #     file.write(in_soup.prettify())
    # Find the hotel listings
    for listings in in_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[16]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices


# Hartford scrape
Hartford_url = "https://www.booking.com/searchresults.html?ss=Hartford&ssne=Hartford&ssne_untouched=Hartford&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20018898&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
hartford_response = requests.get(Hartford_url)
if response.status_code == 200:
    # Parse the HTML content of the page
    hart_soup = BeautifulSoup(hartford_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('hartford.html', 'w', encoding='utf-8') as file:
    #     file.write(hart_soup.prettify())
    # Find the hotel listings
    for listings in hart_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[17]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices


# Cincinnati scrape
Cincinnati_url = "https://www.booking.com/searchresults.html?ss=Cincinnati&ssne=Cincinnati&ssne_untouched=Cincinnati&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20097593&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
cincinnati_response = requests.get(Cincinnati_url)
if response.status_code == 200:
    # Parse the HTML content of the page
    cin_soup = BeautifulSoup(cincinnati_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('cincinnati.html', 'w', encoding='utf-8') as file:
    #     file.write(cin_soup.prettify())
    # Find the hotel listings
    for listings in cin_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[18]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices


# Providence scrape
Providence_url = "https://www.booking.com/searchresults.html?ss=Providence&ssne=Providence&ssne_untouched=Providence&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20115245&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
providence_response = requests.get(Providence_url)
if response.status_code == 200:
    # Parse the HTML content of the page
    prov_soup = BeautifulSoup(providence_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('providence.html', 'w', encoding='utf-8') as file:
    #     file.write(prov_soup.prettify())
    # Find the hotel listings
    for listings in prov_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[19]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices


# Columbus scrape
Columbus_url = "https://www.booking.com/searchresults.html?ss=Columbus&ssne=Columbus&ssne_untouched=Columbus&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20097699&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
columbus_response = requests.get(Columbus_url)
if response.status_code == 200:
    # Parse the HTML content of the page
    col_soup = BeautifulSoup(columbus_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('columbus.html', 'w', encoding='utf-8') as file:
    #     file.write(col_soup.prettify())
    # Find the hotel listings
    for listings in col_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[20]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices


# Raleigh scrape
Raleigh_url = "https://www.booking.com/searchresults.html?ss=Raleigh&ssne=Raleigh&ssne_untouched=Raleigh&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20094466&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
raleigh_response = requests.get(Raleigh_url)
if response.status_code == 200:
    # Parse the HTML content of the page
    ral_soup = BeautifulSoup(raleigh_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('raleigh.html', 'w', encoding='utf-8') as file:
    #     file.write(ral_soup.prettify())
    # Find the hotel listings
    for listings in ral_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[21]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices



# Buffalo scrape
Buffalo_url = "https://www.booking.com/searchresults.html?ss=Buffalo&ssne=Buffalo&ssne_untouched=Buffalo&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20085250&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
buffalo_response = requests.get(Buffalo_url)
if response.status_code == 200:
    # Parse the HTML content of the page
    buff_soup = BeautifulSoup(buffalo_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('buffalo.html', 'w', encoding='utf-8') as file:
    #     file.write(buff_soup.prettify())
    # Find the hotel listings
    for listings in buff_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[22]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices


# Augusta scrape
Augusta_url = "https://www.booking.com/searchresults.html?ss=Augusta&ssne=Augusta&ssne_untouched=Augusta&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20024822&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
augusta_response = requests.get(Augusta_url)
if response.status_code == 200:
    # Parse the HTML content of the page
    aug_soup = BeautifulSoup(augusta_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('augusta.html', 'w', encoding='utf-8') as file:
    #     file.write(aug_soup.prettify())
    # Find the hotel listings
    for listings in aug_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[23]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices


# Tampa scrape
Tampa_url = "https://www.booking.com/searchresults.html?ss=Tampa&ssne=Tampa&ssne_untouched=Tampa&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20024246&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
tampa_response = requests.get(Tampa_url)
if response.status_code == 200:
    # Parse the HTML content of the page
    tamp_soup = BeautifulSoup(tampa_response.text, 'html.parser')
    #lets try to make this into a dictionary

    hotel_list = []
    # save contents to a file
    # with open('tampa.html', 'w', encoding='utf-8') as file:
    #     file.write(tamp_soup.prettify())
    # Find the hotel listings
    for listings in tamp_soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
        # Extract hotel names
        
        hotel_name = listings.get_text(strip=True)
        if re.search(r'\w+', hotel_name):
            #if name is empty break the loop
            if hotel_name == '':
                break
            hotel_list.append(hotel_name)
            # Extract hotel prices
            d = {}
            # d[hotel_name] = 
            price = listings.find_next('span', class_='f6431b446c e6208ee469')
            if price:
                hotel_price = price.get_text(strip=True)
                #this needs to return the price only not the '$'
                h_price = re.search(r'\d+(?:\.\d{2})?', hotel_price).group()
                d[hotel_name] = float(h_price)
            else:
                continue
        if hotel_name in hotel_list:
            #if hotel name already exists, append the price to the list
            cities_hotels[cities[24]][hotel_name] = d[hotel_name]
        else:
            continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices

# Step 2: Write to a JSON file
with open('hotel_prices.json', 'w') as file:
    json.dump(cities_hotels, file, indent=4)
