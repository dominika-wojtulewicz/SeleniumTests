import unittest
import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# DANE TESTOWE
email = "jashdh@wp.pl"
sex = "male"
firstname = "Anna"
lastname = "Nowak"
invalid_password = "hi"
birthdate = "1991-03-09"
address = "rgenkr fererfoerf eru"
city = "Chicago"
state = "Illinois"
postcode = "99000"
phone = "695367889"
alias = "cbeueg@pp.pl"

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        # Warunki wstępne
        # Otwarcie przeglądarki
        self.driver = webdriver.Firefox()
        # Pobranie strony automationpractice.com
        self.driver.get("http://automationpractice.com/")
        # Maksymalizacja okna
        self.driver.maximize_window()
        # Włączenie mechanizmu oczekiwania bezwarunkowego na elementy
        self.driver.implicitly_wait(10)

    def tearDown(self):
        print("Zakończenie testu")
        self.driver.quit()

    def testPasswordTooShort(self):
        driver = self.driver
        # 1. Kliknij „Sign in”
        # Odszukaj element
        sign_in = driver.find_element_by_partial_link_text("Sign in")
        sign_in = driver.find_element(selenium.webdriver.common.by.By.PARTIAL_LINK_TEXT, "Sign in")
        sign_in.click()
        # 2. Wpisz e-mail
        email_input = driver.find_element(selenium.webdriver.common.by.By.ID, "email_create")
        email_input.send_keys(email)
        # 3. Kliknij przycisk „Create account”
        create_account_btn = driver.find_element(selenium.webdriver.common.by.By.ID, "SubmitCreate")
        create_account_btn.click()
        # 4. Wybierz płeć
        if sex == "female":
            # Wybierz Mrs
            driver.find_element(selenium.webdriver.common.by.By.ID, "id_gender2").click()
        else:
            # Wybierz Mr
            driver.find_element(selenium.webdriver.common.by.By.ID, "id_gender1").click()

        # 5. Wpisz imię
        # Odszukaj element
        # Wpisz imie
        firstname_input = driver.find_element(selenium.webdriver.common.by.By.ID, "customer_firstname")
        firstname_input.send_keys(firstname)

        # 6. Wpisz nazwisko
        # odszukaj i wpisz
        lastname_input = driver.find_element(selenium.webdriver.common.by.By.ID, "customer_lastname")
        lastname_input.send_keys(lastname)

        # 7. Sprawdź czy mail w polu email jest zgodny z wprowadzonym wczeniej
        email_fact = driver.find_element(selenium.webdriver.common.by.By.ID, "email").get_attribute("value")
        self.assertEqual(email, email_fact)

        # 8. Wpisz zbyt krótkie hasło
        password_input = driver.find_element(selenium.webdriver.common.by.By.ID, "passwd")
        password_input.send_keys(invalid_password)

        # 9. Wybierz datę urodzenia
        birthdate_l = birthdate.split("-")
        day = str(int(birthdate_l[2]))
        month = str(int(birthdate_l[1]))
        year = birthdate_l[0]
        day_select = Select(driver.find_element(selenium.webdriver.common.by.By.ID, "days"))
        day_select.select_by_value(day)
        month_select = Select(driver.find_element(selenium.webdriver.common.by.By.ID, "months"))
        month_select.select_by_value(month)
        year_select = Select(driver.find_element(selenium.webdriver.common.by.By.ID, "years"))
        year_select.select_by_value(year)

        # 10. Sprawdź pole „First name”
        address_first_name = driver.find_element(selenium.webdriver.common.by.By.ID, "firstname")
        address_first_name.location_once_scrolled_into_view
        address_first_name_s = address_first_name.get_attribute("value")
        self.assertEqual(firstname, address_first_name_s)

        # 11. Sprawdź pole „Last name”
        address_last_name = driver.find_element(selenium.webdriver.common.by.By.ID, "lastname")
        address_last_name.location_once_scrolled_into_view
        address_last_name_s = address_last_name.get_attribute("value")
        self.assertEqual(lastname, address_last_name_s)

        # 12. Wpisz adres
        address_input = driver.find_element(selenium.webdriver.common.by.By.ID, "address1")
        address_input.send_keys(address)

        # 13. Wpisz miasto
        city_input = driver.find_element(selenium.webdriver.common.by.By.ID, "city")
        city_input.send_keys(city)

        # 14. Wpisz kod pocztowy
        postcode_input = driver.find_element(selenium.webdriver.common.by.By.ID, "postcode")
        postcode_input.send_keys(postcode)

        # 15. Wybierz stan
        state_select = Select(driver.find_element(selenium.webdriver.common.by.By.ID, "id_state"))
        state_select.select_by_visible_text(state)

        # 16. Wpisz nr telefonu komórkowego
        phone_input = driver.find_element(selenium.webdriver.common.by.By.ID, "phone_mobile")
        phone_input.send_keys(phone)

        # 17. Wpisz alias adresu
        alias_input = driver.find_element(selenium.webdriver.common.by.By.ID, "alias")
        alias_input.send_keys(alias)

        # 18. Kliknij Register
        register_btn = driver.find_element(selenium.webdriver.common.by.By.ID, "submitAccount")
        register_btn.click()

        sleep(5)