```bash
import requests
import time
from tabulate import tabulate

subdomains = [
    'awesomeweb1.com',
    'awesomeweb2.com',
    'awesomeweb3.com',
    # Add more subdomains here
]

# Function to check the status of a subdomain
def check_status(subdomain):
    try:
        response = requests.get(f"http://{awesomeweb}", timeout=5)
        status = "Up" if response.status_code == 200 else "Down"
    except requests.ConnectionError:
        status = "Down"
    return subdomain, status

# Function to display the status in tabular format
def display_status(subdomain_status):
    headers = ["Subdomain", "Status"]
    print(tabulate(subdomain_status, headers=headers, tablefmt="grid"))

# Main loop to check status every minute
if __name__ == "__main__":
    while True:
        subdomain_status = []
        for subdomain in subdomains:
            result = check_status(subdomain)
            subdomain_status.append(result)

        display_status(subdomain_status)
        print("Checking again in 1 minute...")
        time.sleep(60)
```
