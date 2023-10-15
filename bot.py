# Import for the Web Bot
from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd
from botcity.web.util import element_as_select


# url = 'https://aai-devportal-media.s3.us-west-2.amazonaws.com/challenges/customer-onboarding-challenge.csv'
# r = requests.get(url, allow_redirects=True)
# open('customer-onboarding-challenge.csv', 'wb').write(r.content)
#
pd.set_option('display.max_columns', None)
dados =pd.read_csv('customer-onboarding-challenge.csv', sep= ',')
print(dados)

bot = WebBot()
bot.headless = False
bot.browser= Browser.CHROME
bot.driver_path = ChromeDriverManager().install()

bot.browse("https://developer.automationanywhere.com/challenges/automationanywherelabs-customeronboarding.html")
bot.maximize_window()
bot.wait(1000)

for linha in dados.index:

    customer_name = dados.loc[linha, 'Company Name']
    customer_id = dados.loc[linha, 'Customer ID']
    primary_contact = dados.loc[linha, 'Primary Contact']
    street_adress = dados.loc[linha, 'Street Address']
    city = dados.loc[linha, 'City']
    email = dados.loc[linha, 'Email Address']
    zip = dados.loc[linha, 'Zip']
    state = dados.loc[linha, 'State']

    customername_input  = bot.find_element('customerName', By.ID).send_keys(customer_name)
    customerid_input = bot.find_element( 'customerID', By.ID,).send_keys(customer_id)
    primarycontact_input = bot.find_element( 'primaryContact', By.ID,).send_keys(primary_contact)
    street_adress = bot.find_element( 'primaryContact', By.ID,).send_keys(street_adress)
    city = bot.find_element('city', By.ID,).send_keys(city)
    email = bot.find_element( 'email', By.ID,).send_keys(email)
    zip = bot.find_element( 'zip', By.ID,).send_keys(str(zip))
    state_checkbox = bot.find_element(selector = 'state' , by = By.ID)
    state_checkbox = element_as_select(state_checkbox)
    state_checkbox.select_by_value(value=state)

    if dados.loc[linha, 'Offers Discounts'] == 'YES':
        bot.find_element('activeDiscountYes', By.ID).click()
    else:
        bot.find_element('activeDiscountNo', By.ID).click()

    if dados.loc[linha, 'Non-Disclosure On File'] == 'NO':
        bot.find_element('NDA', By.ID).click()

    bot.find_element('submit_button', By.ID).click()

bot.wait(100)
print = bot.screenshot('Accuracy.png')
bot.stop_browser()


def not_found(label):
    print(f"Element not found: {label}")


#if __name__ == '__main__':
    #main()

