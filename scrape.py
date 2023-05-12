from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup webdriver
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.get('https://unisat.io/brc20/Oshi')

# Wait for the user to manually pass the Cloudflare check
input("Press Enter after you have manually passed the Cloudflare check...")

# Now let's wait until the supply and holder count elements are present
wait = WebDriverWait(driver, 10)

supply_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div/table/tbody/tr[4]/td/div/span')))
holder_count_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div/table/tbody/tr[22]/td/div/span')))

# Extract and print the text of the elements
supply = supply_element.text.replace(",", "")
holder_count = holder_count_element.text.replace(",", "")

print(f"Supply: {supply}")
print(f"Holder count: {holder_count}")

# Close the browser
driver.quit()
