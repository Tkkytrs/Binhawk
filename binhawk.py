import requests
from bs4 import BeautifulSoup
from colorama import Fore
# Random numbers
import pyfiglet
import random
import time
def display_bin_info(data):
    #rint("BIN:")
    for bin_info in data['bins']:
        print(f"{Fore.RED}BIN:  {Fore.CYAN}{bin_info['bin']}")
        time.sleep(0.05)
        print(f"{Fore.GREEN}→{Fore.YELLOW} TYPE:  {Fore.CYAN}{bin_info['type']}")
        time.sleep(0.05)
        print(f"{Fore.GREEN}→ {Fore.YELLOW}LEVEL:  {Fore.CYAN}{bin_info['level']}")
        time.sleep(0.05)
        print(f"{Fore.GREEN}→ {Fore.YELLOW}BRAND: {Fore.CYAN} {bin_info['brand']}")
        time.sleep(0.05)
        print(f"{Fore.GREEN}→{Fore.YELLOW} BANK:  {Fore.CYAN}{bin_info['bank']}")
        time.sleep(0.05)
        print(f"{Fore.GREEN}→ {Fore.YELLOW}COUNTRY: {Fore.CYAN} {bin_info['country']}")
        print("\n")

print(Fore.CYAN+pyfiglet.figlet_format("tkkytrs"))
print(Fore.YELLOW+"OWNER @TKKYTRS")
print(Fore.YELLOW+"TOOL: BINNER")
print(Fore.YELLOW+"ANY PROBLEM @TKKYTRSP < DM HERE")
print("\n\n")
time.sleep(3)
print(Fore.RED+"FINDING BINS")

# Generate 100 random 5-digit numbers
random_numbers = [str(random.randint(10000, 99999)) for _ in range(100)]

# Add prefix '5' to the first 50 numbers and '4' to the rest
modified_numbers = ['5' + num if i < 50 else '4' + num for i, num in enumerate(random_numbers)]

# Prepare the numbers for the URL
numbers_for_url = '%0D%0A'.join(modified_numbers)

# URL for BIN search
url = f'https://bins.ws/search?bins={numbers_for_url}&bank=&country='

# Make the request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Extract HTML content
    html_content = response.text

    # Data list to store extracted information
    data = []

    # Use BeautifulSoup to find the table directly within the HTML body
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table', class_='dataframe')

    # Check if the table was found
    if table:
        # Extract rows from the table
        rows = table.find_all('tr')

        if len(rows) > 1:  # Check if there are rows in the table
            for row in rows[1:]:
                columns = row.find_all('td')
                if len(columns) == 6:  # Ensure there are enough columns
                    data.append({
                        'bin': columns[0].text.strip(),
                        'type': columns[1].text.strip(),
                        'level': columns[2].text.strip(),
                        'brand': columns[3].text.strip(),
                        'bank': columns[4].text.strip(),
                        'country': columns[5].text.strip()
                    })

            # Convert data to JSON format
            json_data = {'bins': data}

            # Print or return the JSON data
            #print(json_data)
            display_bin_info(json_data)
        else:
            print("No data rows found in the table.")
    else:
        print("Table not found within HTML body.")
else:
    print(f"Request failed with status code {response.status_code}")
