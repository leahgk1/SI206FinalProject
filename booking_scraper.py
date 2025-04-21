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
def scrape_booking(url, city_num):
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
    # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
    #lets try to make this into a dictionary

        hotel_list = []
    # # save contents to a file
    # with open('orlando.html', 'w', encoding='utf-8') as file:
    #     file.write(o_soup.prettify())


    # Find the hotel listings
        for listings in soup.find_all('h3', class_='f6431b446c e6208ee469 d0caee4251'):
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
                cities_hotels[cities[city_num]][hotel_name] = d[hotel_name]
            else:
                continue
            #if hotel name does not exist, create a new entry
    #Extract hotel names and prices

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
scrape_booking(Orlando_url, 1)




# Miami scrape
Miami_url = "https://www.booking.com/searchresults.html?ss=Miami&ssne=Miami&ssne_untouched=Miami&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20023181&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
miami_response = requests.get(Miami_url)
scrape_booking(Miami_url, 2)




# Boston scrape
Boston_url = "https://www.booking.com/searchresults.html?ss=Boston&ssne=Boston&ssne_untouched=Boston&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20061717&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
boston_response = requests.get(Boston_url)
scrape_booking(Boston_url, 3)



# Washington D.C. scrape
Washington_D_C_url = "https://www.booking.com/searchresults.html?ss=Downtown+D.C.&ssne=Downtown+D.C.&ssne_untouched=Downtown+D.C.&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=928&dest_type=district&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
washington_response = requests.get(Washington_D_C_url)
scrape_booking(Washington_D_C_url, 4)




# Philadelphia scrape
Philadelphia_url = "https://www.booking.com/searchresults.html?ss=Philadelphia&ssne=Philadelphia&ssne_untouched=Philadelphia&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20111994&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
philadelphia_response = requests.get(Philadelphia_url)
scrape_booking(Philadelphia_url, 5)




# Atlanta scrape
Atlanta_url = "https://www.booking.com/searchresults.html?ss=Atlanta&ssne=Atlanta&ssne_untouched=Atlanta&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20024809&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
atlanta_response = requests.get(Atlanta_url)
scrape_booking(Atlanta_url, 6)





# Charleston scrape
Charleston_url = "https://www.booking.com/searchresults.html?ss=Charleston&ssne=Charleston&ssne_untouched=Charleston&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20115955&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
charleston_response = requests.get(Charleston_url)
scrape_booking(Charleston_url, 7)




# Savannah scrape
Savannah_url = "https://www.booking.com/searchresults.html?ss=Savannah&ssne=Savannah&ssne_untouched=Savannah&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20029490&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
savannah_response = requests.get(Savannah_url)
scrape_booking(Savannah_url, 8)




# Richmond scrape
Richmond_url = "https://www.booking.com/searchresults.html?ss=Richmond&ssne=Richmond&ssne_untouched=Richmond&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20141027&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
richmond_response = requests.get(Richmond_url)
scrape_booking(Richmond_url, 9)



# Charlotte scrape
Charlotte_url = "https://www.booking.com/searchresults.html?ss=Charlotte&ssne=Charlotte&ssne_untouched=Charlotte&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20091627&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
charlotte_response = requests.get(Charlotte_url)
scrape_booking(Charlotte_url, 10)




# Cleveland scrape
Cleveland_url = "https://www.booking.com/searchresults.html?ss=Cleveland&ssne=Cleveland&ssne_untouched=Cleveland&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20097630&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
cleveland_response = requests.get(Cleveland_url)
scrape_booking(Cleveland_url, 11)




# Baltimore scrape
Baltimore_url = "https://www.booking.com/searchresults.html?ss=Baltimore&ssne=Baltimore&ssne_untouched=Baltimore&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20053799&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
baltimore_response = requests.get(Baltimore_url)
scrape_booking(Baltimore_url, 12)




# Pittsburgh scrape
Pittsburgh_url = "https://www.booking.com/searchresults.html?ss=Pittsburgh&ssne=Pittsburgh&ssne_untouched=Pittsburgh&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20112087&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
pittsburgh_response = requests.get(Pittsburgh_url)
scrape_booking(Pittsburgh_url, 13)



# Detroit scrape
Detroit_url = "https://www.booking.com/searchresults.html?ss=Detroit&ssne=Detroit&ssne_untouched=Detroit&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20064402&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
detroit_response = requests.get(Detroit_url)
scrape_booking(Detroit_url, 14)




# Jacksonville scrape
Jacksonville_url = "https://www.booking.com/searchresults.html?ss=Jacksonville&ssne=Jacksonville&ssne_untouched=Jacksonville&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20022757&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
jacksonville_response = requests.get(Jacksonville_url)
scrape_booking(Jacksonville_url, 15)




# Indianapolis scrape
Indianapolis_url = "https://www.booking.com/searchresults.html?ss=Indianapolis&ssne=Indianapolis&ssne_untouched=Indianapolis&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20037880&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
indianapolis_response = requests.get(Indianapolis_url)
scrape_booking(Indianapolis_url, 16)




# Hartford scrape
Hartford_url = "https://www.booking.com/searchresults.html?ss=Hartford&ssne=Hartford&ssne_untouched=Hartford&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20018898&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
hartford_response = requests.get(Hartford_url)
scrape_booking(Hartford_url, 17)



# Cincinnati scrape
Cincinnati_url = "https://www.booking.com/searchresults.html?ss=Cincinnati&ssne=Cincinnati&ssne_untouched=Cincinnati&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20097593&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
cincinnati_response = requests.get(Cincinnati_url)
scrape_booking(Cincinnati_url, 18)




# Providence scrape
Providence_url = "https://www.booking.com/searchresults.html?ss=Providence&ssne=Providence&ssne_untouched=Providence&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20115245&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
providence_response = requests.get(Providence_url)
scrape_booking(Providence_url, 19)


# Columbus scrape
Columbus_url = "https://www.booking.com/searchresults.html?ss=Columbus&ssne=Columbus&ssne_untouched=Columbus&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20097699&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
columbus_response = requests.get(Columbus_url)
scrape_booking(Columbus_url, 20)




# Raleigh scrape
Raleigh_url = "https://www.booking.com/searchresults.html?ss=Raleigh&ssne=Raleigh&ssne_untouched=Raleigh&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20094466&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
raleigh_response = requests.get(Raleigh_url)
scrape_booking(Raleigh_url, 21)





# Buffalo scrape
Buffalo_url = "https://www.booking.com/searchresults.html?ss=Buffalo&ssne=Buffalo&ssne_untouched=Buffalo&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20085250&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
buffalo_response = requests.get(Buffalo_url)
scrape_booking(Buffalo_url, 22)



# Augusta scrape
Augusta_url = "https://www.booking.com/searchresults.html?ss=Augusta&ssne=Augusta&ssne_untouched=Augusta&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20024822&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
augusta_response = requests.get(Augusta_url)
scrape_booking(Augusta_url, 23)



# Tampa scrape
Tampa_url = "https://www.booking.com/searchresults.html?ss=Tampa&ssne=Tampa&ssne_untouched=Tampa&label=gen173nr-1FCAEoggI46AdIM1gEaJsCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKn79S_BsACAdICJDMyNGI3MTM1LWNmMGItNDY2NS1iN2RjLTVmZjk1OWMxNzFmYtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20024246&dest_type=city&checkin=2025-05-01&checkout=2025-05-03&group_adults=2&no_rooms=1&group_children=0"
tampa_response = requests.get(Tampa_url)
scrape_booking(Tampa_url, 24)


def make_json_file(cities_hotel):
    with open('hotel_prices.json', 'w') as file:
        json.dump(cities_hotels, file, indent=4)

#main
if __name__ == "__main__":
    
    make_json_file(cities_hotels)
