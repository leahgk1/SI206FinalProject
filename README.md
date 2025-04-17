# SI 206 Final Project: APIs, SQL, and Visualizations

## Project Overview
This project collects data from various APIs, stores it in an SQLite database, and creates visualizations to analyze the data.

### Project Components

#### Yelp API Component
The Yelp API component collects information about attractions in different cities, stores the data in a database, and creates visualizations to analyze the data.

#### Weather API Component (existing)
The Weather API component collects weather data for different cities and analyzes it.

#### Booking.com Web Scraping Component (existing)
The Booking.com component scrapes hotel price data from the website.

## Setup Instructions

### Requirements
Install the required packages:
```
pip install requests matplotlib pandas seaborn beautifulsoup4
```

### Running the Code

#### 1. Collecting Attraction Data
Run the following command to collect attraction data for a city:
```
python tripadvisordata/collect_attractions.py
```
You will be prompted to enter a city name. The script will collect up to 100 attractions for the city, limiting each API call to 25 items.

Run this script multiple times with different cities to build up your database.

#### 2. Analyzing Attraction Data
Run the following command to analyze the collected attraction data:
```
python tripadvisordata/analyze_attractions.py
```
This will generate visualizations in a 'visualizations' folder and create a text file with analysis results.

#### 3. Weather Data Collection & Analysis (existing functionality)
To set up weather data tables:
```
python openweatherdata/create_weather_db.py
```

To analyze weather data:
```
python openweatherdata/analyze_weather.py
```

#### 4. Booking.com Web Scraping (existing functionality)
To scrape hotel data:
```
python booking_scraper.py
```

## Project Structure
- `tripadvisordata/`: Contains Yelp API related code
  - `collect_attractions.py`: Collects attraction data from Yelp API
  - `analyze_attractions.py`: Analyzes attraction data and creates visualizations
- `openweatherdata/`: Contains weather API related code
- `visualizations/`: Contains generated visualization images
- `travel_project.db`: SQLite database with all collected data

## Database Structure
The database contains several tables:
- `cities`: Information about cities
- `attractions`: Information about attractions in cities
- `weather`: Weather information for cities

## Authors
- Leah Kim
- Sam Kim
- Sean Park
