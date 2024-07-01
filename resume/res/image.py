from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def scrape_website(url):
    # Set up the Chrome WebDriver
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Open the URL
    driver.get(url)

    # Wait for the page to fully load
    time.sleep(3)  # Adjust the sleep time if necessary

    # Get the page source and parse it with BeautifulSoup
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find all elements with the specific class name
    elements = soup.find_all(class_='styles_JDC__dang-inner-html__h0K4t')

    # Extract and print the text content
    for element in elements:
        text_content = element.get_text(strip=True)
        return(f"Text Content: {text_content}")
        print("-" * 40)

    # Close the WebDriver
    driver.quit()

# URL of the website to scrape
url = 'https://www.naukri.com/job-listings-software-developer-sap-cpq-rohde-schwarz-india-pvt-limited-new-delhi-bengaluru-5-to-10-years-220324500587?src=companyPageJobsDesk&sid=17198420477038137&xp=1&px=1'  # Replace with the actual URL
class_name = 'styles_JDC__dang-inner-html__h0K4t'  # Replace with the actual class name

