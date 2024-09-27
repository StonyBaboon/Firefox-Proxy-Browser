import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import WebDriverException

def start_browser_with_proxy(proxy_address, proxy_type, debug=False):
    try:
        if debug:
            print("[DEBUG] Starting Firefox driver...")

        options = Options()
        options.headless = False  # Do not run in headless mode, so we can see the browser

        proxy = Proxy()

        if proxy_type == 1:  # SOCKS4
            proxy.proxy_type = ProxyType.MANUAL
            proxy.socksProxy = proxy_address
            proxy.socksVersion = 4
        elif proxy_type == 2:  # HTTP/HTTPS
            proxy.proxy_type = ProxyType.MANUAL
            proxy.httpProxy = proxy_address
            proxy.sslProxy = proxy_address
        elif proxy_type == 3:  # SOCKS5
            proxy.proxy_type = ProxyType.MANUAL
            proxy.socksProxy = proxy_address
            proxy.socksVersion = 5

        capabilities = webdriver.DesiredCapabilities.FIREFOX
        proxy.add_to_capabilities(capabilities)

        driver = webdriver.Firefox(options=options, desired_capabilities=capabilities)

        if debug:
            print("[DEBUG] Waiting 5 seconds before accessing myip.com...")
        time.sleep(5)

        if debug:
            print("[DEBUG] Accessing myip.com to verify the proxy...")
        driver.get("https://www.myip.com/")

        time.sleep(10)  # Wait to see the result

    except WebDriverException as e:
        print(f"An error occurred: {e}")
    finally:
        if 'driver' in locals():
            if debug:
                print("[DEBUG] Closing Firefox driver...")
            driver.quit()

if __name__ == "__main__":
    proxy_address = input("Please enter the proxy address (e.g., proxy_ip:proxy_port): ")

    print("Choose the proxy type:")
    print("1. SOCKS4")
    print("2. HTTP/HTTPS")
    print("3. SOCKS5")
    proxy_type = int(input("Enter 1, 2, or 3: "))

    debug_mode = input("Enable debug mode? (y/n): ").strip().lower() == 'y'

    start_browser_with_proxy(proxy_address, proxy_type, debug=debug_mode)
