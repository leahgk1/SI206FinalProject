import os
import sys
import subprocess
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    print("=" * 80)
    print("SI 206 FINAL PROJECT: TRAVEL DATA ANALYSIS".center(80))
    print("=" * 80)
    print()

def print_menu():
    print("\nMAIN MENU")
    print("1. Collect Attraction Data (Yelp API)")
    print("2. Analyze Attraction Data & Generate Visualizations")
    print("3. Weather Data Operations")
    print("4. Booking.com Web Scraping")
    print("5. Exit")
    print()

def run_script(script_path):
    print(f"\nRunning {script_path}...\n")
    result = subprocess.run([sys.executable, script_path], capture_output=False)
    if result.returncode == 0:
        print(f"\nSuccessfully ran {script_path}")
    else:
        print(f"\nError running {script_path}")
    
    input("\nPress Enter to continue...")

def weather_submenu():
    clear_screen()
    print("\nWEATHER DATA OPERATIONS")
    print("1. Create Weather Database Tables")
    print("2. Analyze Weather Data")
    print("3. Back to Main Menu")
    
    choice = input("\nEnter your choice (1-3): ")
    
    if choice == "1":
        run_script("openweatherdata/create_weather_db.py")
    elif choice == "2":
        run_script("openweatherdata/analyze_weather.py")
    elif choice == "3":
        return
    else:
        print("Invalid choice. Please try again.")
        time.sleep(1)
        weather_submenu()

def main():
    while True:
        print_header()
        print_menu()
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            run_script("tripadvisordata/collect_attractions.py")
        elif choice == "2":
            run_script("tripadvisordata/analyze_attractions.py")
        elif choice == "3":
            weather_submenu()
        elif choice == "4":
            run_script("booking_scraper.py")
        elif choice == "5":
            print("\nThank you for using the Travel Data Analysis program!")
            print("Exiting...\n")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
