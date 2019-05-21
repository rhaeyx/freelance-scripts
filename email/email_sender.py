from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class Email:
    def __init__(self,
                 email="",
                 password="",
                 to="asd",
                 bcc="asd",
                 subject="Test",
                 text="This is a content test.",
                 headless=True):
        """
            params:
            email - string
            password - string
            to - string
            bcc - .txt file
            subject - string
            text - .txt file        
        """

        if not email or not password or not bcc or not to:
            print("Please pass all paremeters...")
            exit()

        self.email = email
        self.password = password
        self.to = to 
        with open(bcc, "r") as f:
            self.bcc = f.read().split("\n")
        self.subject = subject
        with open(text, "r") as f:
            self.text = f.read()

        self.headless = headless

    def open_gmail(self):
        try:
            print("Opening gmail...")
            options = Options()
            options.headless = self.headless
            options.add_argument("--log-level=3")
            options.add_argument("--silent")

            self.chrome = webdriver.Chrome("../../chromedriver.exe", options=options)
            self.chrome.get("https://mail.google.com")
        except:
            print("Something went wrong with opening gmail...")

    def login(self):
        print("Logging in as", self.email + "...")
        email_inp = self.chrome.find_element_by_css_selector("#identifierId")
        email_inp.send_keys(self.email)

        next_btn = self.chrome.find_element_by_css_selector("#identifierNext > content > span")
        next_btn.click()
        
        sleep(3)

        password_inp = self.chrome.find_element_by_css_selector("#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
        password_inp.send_keys(self.password)

        next_btn = self.chrome.find_element_by_css_selector("#passwordNext > content > span")
        next_btn.click()
        print("Logged in...")

    def send_email(self, bcc):
        compose = self.chrome.find_element_by_css_selector(".z0 > div")
        compose.click()

        sleep(3)

        to_inp = self.chrome.find_element_by_name('to')
        to_inp.send_keys(self.to)
        sleep(1)
        to_inp.send_keys('\n')


        sleep(3)

        bcc_btn = self.chrome.find_element_by_css_selector(".aA6 > span > span > span:nth-child(2)")
        bcc_btn.click()

        sleep(3)

        bcc_inp = self.chrome.find_element_by_name("bcc")
        bccs = ' '.join(bcc)
        print(bccs)
        bcc_inp.send_keys(bccs)
        
        subject_inp = self.chrome.find_element_by_name("subjectbox")
        subject_inp.send_keys(self.subject)

        sleep(3)

        text_inp = self.chrome.find_element_by_css_selector('.Ar.Au > div')
        text_inp.send_keys(self.text)

        sleep(3)

        send_btn = self.chrome.find_element_by_css_selector(".dC > div")
        send_btn.click()
        print("Email sent.")

    def main(self):
        input("Enter to start...")
        print("Email:", self.email)
        print("BCCs:", self.bcc)
        print("Email Subject:", self.subject)
        print("Email Content:", self.text, end='\n')

        print("Starting the bot now...")
        
        self.open_gmail()

        sleep(5)

        self.login()

        sleep(10)

        counter = 0
        input('Start now...')
        while counter < len(self.bcc):
            if counter != 0 and counter % 60 == 0:
                sleep(300)
                print("5 minutes break...")
            bcc_recipients = self.bcc[counter: counter + 3 if counter + 3 < len(self.bcc) - 1 else None]
            counter += 3
            print("BCCs:", bcc_recipients)
            self.send_email(bcc_recipients)
            for i in range(5):
                sleep(1)
