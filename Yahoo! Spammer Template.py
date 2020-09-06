from selenium import webdriver
import time

# This script will send as many emails as you would like using Yahoo! Mail.
# I was able to make this program simulate a human by having it puase after inputting           information.
# This makes it harder for Google Chrome and Yahoo! Mail to detect that this is a script.

NumberOfEmails = 3  # This is how many emails the program will send.

# Here are functions that are regularly used throughout the program to click and type.
# These functions may be short, however they make the main code look much more clean.


def Wait(Time):
    "This delays the program a certain amout of time to replicate a person. The arguement passed is in seconds."
    time.sleep(Time)


def ClickButton(Xpath):
    "This clicks a button on a webpage. The arguement passed is the Xpath of the button."
    btn = driver.find_element_by_xpath(Xpath)  # Applies the Xpath
    btn.click()                                # Clicks the button


def Type(Xpath, Phrase):
    "This clicks on a text box and types input. The arguements are the Xpath of the box and the desired text."
    box = driver.find_element_by_xpath(Xpath)  # Applies the Xpath
    Wait(0.80)                                 # Delays the code
    box.send_keys(Phrase)                      # Types in the box


# This is the start of the program.

# First open up the chrome browser and go to Yahoo! Mail
driver = webdriver.Chrome(
    executable_path=r"C:\Users\rober\Documents\Personal Code\Webscraping\Drivers\chromedriver.exe"
)
Wait(1)
driver.get("http://www.mail.yahoo.com")  # Go to Yahoo! Mail.

# Click "Sign In" button.
Wait(2.03)
ClickButton('//*[@id="signin-main"]/div[1]/a[2]/span')

# Click on the username input box and type in username.
Wait(1.91)
Type('//*[@id="login-username"]', "username")  # Input username as the second arguement.

# Click "Next" button.
Wait(0.73)
ClickButton('//*[@id="login-signin"]')

# Click on the password input box and type in password.
Wait(2)
Type('//*[@id="login-passwd"]', "password")    # Input password as the second arguement.

# Click "Next" button.
Wait(1.01)
ClickButton('//*[@id="login-signin"]')

# At this point we are succesfully logged into our Yahoo! Mail. We need to go to our inbox.

# To make this script more consistent, we will just reload Yahoo! Mail.
Wait(4.07)
driver.get("http://www.mail.yahoo.com")

Wait(5)

# This is the spamming loop.
for x in range(0, NumberOfEmails):

    # Click on the "Compose" button to start creating an email to send.
    ClickButton('//*[@id="app"]/div[2]/div/div[1]/nav/div/div[1]/a')

    # Click on the "To" input box and type in the recipient's email
    Wait(2)
    Type('//*[@id="message-to-field"]', "person@gmail.com")

    # Click on the "Subject" input box and type in the subject
    Wait(2.04)
    Type('//*[@id="mail-app-component"]/div[2]/div/div[1]/div[3]/div/div/input', "Spam")

    # Click on the "Subject" input box and type in the subject
    Wait(2.04)
    Type('//*[@id="editor-container"]/div[1]', "Message")

    # Click the send button
    Wait(4)
    ClickButton('//*[@id="mail-app-component"]/div[2]/div/div[2]/div[2]/div/button/span')

    # An email was successfully sent!
    Wait(3)
