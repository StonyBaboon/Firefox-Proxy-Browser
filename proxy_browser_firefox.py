from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import sys

# Function to get the proxy from the user
def get_proxy():
    proxy_address = input("Please enter the proxy address (e.g., proxy_ip:proxy_port): ")
    return proxy_address

# Function to get the proxy type from the user
def get_proxy_type():
    print("Choose the proxy type:")
    print("1. SOCKS4")
    print("2. SOCKS5")
    print("3. HTTP")
    print("4. HTTPS")
    choice = input("Enter 1, 2, 3, or 4: ")
    
    if choice == '1':
        return 'socks4'
    elif choice == '2':
        return 'socks5'
    elif choice == '3':
        return 'http'
    elif choice == '4':
        return 'https'
    else:
        print("Invalid option. Using HTTP as the default.")
        return 'http'

# Debug function
def debug_print(message):
    if debug_mode:
        print(f"[DEBUG] {message}")

# Initialize debug mode variable
debug_mode = len(sys.argv) > 1 and sys.argv[1] == 'debug'

# Get the proxy address and proxy type
proxy_address = get_proxy()
proxy_type = get_proxy_type()

# Set Firefox options
firefox_options = Options()
firefox_options.headless = False  # If you want the Firefox window to be visible

# Configure the proxy according to the user's choice
if proxy_type == 'socks4':
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'socksProxy': proxy_address,
        'socksVersion': 4,  # Setting SOCKS4 version
        'sslProxy': proxy_address  # Proxy for SSL traffic
    })
elif proxy_type == 'socks5':
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'socksProxy': proxy_address,
        'socksVersion': 5,  # Setting SOCKS5 version
        'sslProxy': proxy_address
    })
elif proxy_type == 'https':
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': proxy_address,
        'sslProxy': proxy_address  # HTTPS uses the HTTP proxy for SSL traffic
    })
else:  # HTTP as default
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': proxy_address,
        'sslProxy': proxy_address  # For HTTPS as well
    })

# Apply proxy settings to Firefox
firefox_options.proxy = proxy

# Initialize the geckodriver service
service = Service('C:/geckodriver/geckodriver.exe')  # Make sure the path is correct

try:
    debug_print("Starting the Firefox driver...")
    driver = webdriver.Firefox(service=service, options=firefox_options)

    debug_print("Waiting 5 seconds before accessing the website...")
    time.sleep(5)  # Wait before accessing the website

    debug_print("Accessing myip.com to check the proxy...")
    driver.get('https://www.myip.com')  # Test the proxy by accessing this site

    debug_print("The browser will remain open. Close it manually to finish.")
    input("Press Enter to close the browser...")  # Wait for the user to press Enter to close

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Make sure to close the browser
    if 'driver' in locals():
        debug_print("Closing the Firefox driver...")
        driver.quit()
