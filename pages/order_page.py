from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from locator.locator import Locator

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
    def fill_order_form(self, name, surname, address, metro, phone):
        self.driver.find_element(*Locator.name_input).send_keys(name)
        self.driver.find_element(*Locator.surname_input).send_keys(surname)
        self.driver.find_element(*Locator.address_input).send_keys(address)
        metro_click = self.driver.find_element(By.CLASS_NAME, 'select-search__input')
        metro_click.click()
        metro_click.send_keys(metro)
        metro_click.send_keys(Keys.ARROW_DOWN)
        metro_click.send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@placeholder='* Телефон: на него позвонит курьер']")))
        self.driver.find_element(*Locator.phone_input).send_keys(phone)

    def second_form_order(self, date, comment):
        date_send = self.driver.find_element(*Locator.date_input)
        date_send.send_keys(date)
        date_send.send_keys(Keys.ENTER)
        self.driver.find_element(By.CLASS_NAME, 'Dropdown-placeholder').click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'Dropdown-menu')]"))).click()
        self.driver.find_element(*Locator.checkbox).click()
        self.driver.find_element(*Locator.comment_input).send_keys(comment)
        self.driver.find_element(*Locator.order_button).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and contains(text(), "Да")]'))
        ).click()
        self.order_text = self.driver.find_element(By.CLASS_NAME, 'Order_ModalHeader__3FDaJ').text




    def submit_order(self):
        self.driver.find_element(*Locator.submit_button).click()


