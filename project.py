import chromedriver_autoinstaller
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Automatically install the correct version of ChromeDriver
chromedriver_autoinstaller.install()

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open a website

driver.get("https://www.espn.com/olympics/summer/2024/medals")
print(driver.title)  # Print the title of the page
time.sleep(5)
# Name,ID,Class Name,Tag

try:
    elements = driver.find_elements(By.XPATH, '//*[contains(@class, "medals") and contains(@class, "olympics") and contains(@class, "has-team-logos")]')
    for element in elements:
        print(element.text)
except Exception as e:
    print("Error:", e)

# Close the WebDriver
#//*[@id="medals olympics has-team-logos]/tbody/tr/td[1]"

driver.quit()

