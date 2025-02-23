from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import BASE_URL
class DynamicPage():
    def __init__(self,driver):
        self.driver=driver
        self.url=BASE_URL

    def open_example(self, example_id=1):
        example_url=f"{self.url}/{example_id}"
        self.driver.get(example_url)

    def start_loading(self):
        self.driver.find_element(By.XPATH,"//button[contains(text(),'Start')]").click()

    def wait_for_loading_to_finish(self):
        WebDriverWait(self.driver,10).until(
            EC.invisibility_of_element_located((By.ID,"loading"))
        )

    def get_final_text(self):
        element=WebDriverWait(self.driver,10).until(
            EC.visibility_of_all_elements_located((By.ID,"finish"))
        )
        return element[0].text
