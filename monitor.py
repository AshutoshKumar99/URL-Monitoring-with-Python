import requests
import time

# ANSI escape codes for coloring the output
GREEN = '\033[92m'  # Green for sign-in detected
RED = '\033[91m'    # Red for errors or the next run message
YELLOW = '\033[93m' # Yellow for other status codes or warnings
RESET = '\033[0m'   # Reset color

def check_signin_page(url):
    try:
        response = requests.get(url)
       
        #response = requests.get(url, timeout=0.001) Simulate a Timeout Error, Set a very low timeout to trigger a timeout error

        if response.status_code == 200:
            print(f"{url}: {YELLOW}Page is up, but no sign-in page detected.{RESET}")
        elif response.status_code == 401:
            # Treat 401 as sign-in page detected
            print(f"{url}: {GREEN}Sign-in page detected.{RESET}")
        else:
            print(f"{url}: {YELLOW}Returned status code {response.status_code} (No sign-in page detected).{RESET}")

    except requests.exceptions.RequestException as e:
        print(f"{url}: {RED}An error occurred: {e}{RESET}")

# List of URLs to monitor
urls = [
    "https://amer-staging.spectrum.precisely.com/rest/SearchbyEntityID_v1/results.json?Data.ENTITY_ID=285928234&Data.Country=USA",
    "https://mastercard-graph.spectrum.precisely.com/rest/SearchbyEntityID_v1/results.json?Data.ENTITY_ID=285928234&Data.Country=USA",
    "https://mastercard-uat-graph.spectrum.precisely.com/rest/SearchbyEntityID_v1/results.json?Data.ENTITY_ID=285928234&Data.Country=USA",
    "https://amer.spectrum.precisely.com/rest/MC_Match_Search/results.json?Data.Merchant_Name=RADIO SHACK&Data.City=ROCHESTER&Data.State_Province=NY&Data.Postal_Code=146261632&Option.max_results=10"
    "#https://nonexistentwebsite.com" # Invalid domain to simulate server down,(Connection Refused) Error
]

while True:
    for url in urls:
        check_signin_page(url)

    print(f"{RED}Next run will be after 20 minute...{RESET}")
    time.sleep(1200)  # Wait for 20 minutes before running again
