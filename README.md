
# Firefox Proxy Browser

## Project Overview

This Python script allows users to open a Firefox browser with a proxy connection to verify if the proxy is working by accessing `myip.com`. The user can choose between different types of proxies (SOCKS4, SOCKS5, HTTP/HTTPS).

The project also includes a batch script that helps in setting up the environment by installing Python, `pip`, necessary dependencies, and the `geckodriver`. However, it is recommended to install everything manually for better control.

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
   - [Manual Installation](#manual-installation)
   - [Automated Installation using `.bat`](#automated-installation-using-bat)
3. [Running the Python Script](#running-the-python-script)
4. [Notes and Troubleshooting](#notes-and-troubleshooting)

## Requirements

Before running the script, ensure you have the following installed:

- **Python** (version 3.7 or later)
- **pip** (Python's package manager)
- **geckodriver** (for Selenium WebDriver to work with Firefox)
- **Mozilla Firefox** (must be installed on the system)
- **Selenium** (Python package)

## Installation

### Manual Installation

1. **Step 1: Install Python**
   - Go to the official [Python website](https://www.python.org/downloads/) and download Python (version 3.7 or later).
   - Install Python and check the option **"Add Python to PATH"** during installation.

2. **Step 2: Install pip**
   - If not already installed, open a terminal (Command Prompt or PowerShell) and run:
     ```bash
     python -m ensurepip --upgrade
     ```

3. **Step 3: Install Selenium package**
   - In the terminal, install Selenium by running:
     ```bash
     pip install selenium
     ```

4. **Step 4: Download and install `geckodriver`**
   - Go to the [geckodriver releases page](https://github.com/mozilla/geckodriver/releases) and download the latest version for your OS (e.g., Windows, macOS, Linux).
   - Extract the `geckodriver` executable and move it to a directory (e.g., `C:\geckodriver\` for Windows).
   - Add this directory to your **system PATH**:
     - **Windows**: Follow [this guide](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/) to add the folder where `geckodriver.exe` is located to the system environment variable `PATH`.

### Automated Installation using `.bat`

If you prefer automated installation, follow these steps:

1. Run the provided **`install_all_dependencies.bat`** file:
   - This script will automatically:
     - Install Python (if not already installed).
     - Install `pip` (if not already installed).
     - Install the `selenium` package using `pip`.
     - Download `geckodriver`, extract it to `C:\geckodriver`, and add it to the system `PATH`.
   - Simply double-click the `.bat` file, or run it via the Command Prompt with:
     ```cmd
     install_all_dependencies.bat
     ```

## Running the Python Script

Once all dependencies are installed:

1. Open the terminal (Command Prompt, PowerShell, etc.).
2. Navigate to the directory where the Python script (`proxy_browser_firefox.py`) is located.
3. Run the script using the following command:
   ```bash
   python proxy_browser_firefox.py
   ```

4. You will be prompted to enter the proxy address and proxy type:
   - Enter the proxy address in the format `ip:port` (e.g., `138.124.0.40:64742`).
   - Choose the proxy type:
     - `1` for **SOCKS4**
     - `2` for **HTTP/HTTPS**
     - `3` for **SOCKS5**

5. The script will open Firefox, connect to the proxy, and attempt to access `myip.com` to verify the proxy connection.

## Notes and Troubleshooting

- **Firefox Version**: Ensure that your version of Firefox is compatible with the installed `geckodriver`. Update Firefox if necessary.
- **geckodriver Location**: If the script fails with an error about the driver, ensure `geckodriver.exe` is installed in the correct location (`C:\geckodriver\` for Windows) and is added to your system `PATH`.
- **Proxy Errors**: If the script fails to connect to `myip.com`, double-check that the proxy details are correct, and try with another proxy.
- **Debug Mode**: To troubleshoot issues, you can enable debug mode in the script by typing `y` when prompted:
   ```bash
   Enable debug mode? (y/n): y
   ```

## Future Improvements

- Add more advanced error handling for different types of proxies.
- Add support for rotating proxy lists.

## Support

If you encounter any issues with the script or installation process, please open an issue or request support.
