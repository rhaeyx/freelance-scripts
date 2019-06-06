from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from random import randint

"""
from email_sender import Email
x = Email(to="adamgavin.services@gmail.com", bcc="bcc.txt", subject="Auto Body Repair Enquiry", text="content.txt", headless=False)
x.main()

"""


class Email:
    def __init__(self,
                 to="asd",
                 bcc="asd",
                 subject="Test",
                 text="This is a content test.",
                 headless=False):
        """
            params:
            email - string
            password - string
            to - string
            bcc - .txt file
            subject - string
            text - .txt file        
        """

        if not bcc or not to:
            print("Please pass all paremeters...")
            exit()

        self.to = to 
        with open(bcc, "r") as f:
            self.bcc = f.read().split("\n")

        for line in self.bcc:
            line = line.strip()

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

    def send_email(self, bcc):
        self.chrome.get("https://mail.google.com/mail/u/0/h/1modi9lfr1wvl/?&cs=b&pv=tl&v=b")

        sleep(randint(1, 3))

        to_inp = self.chrome.find_element_by_name('to')
        to_inp.send_keys(self.to)
        sleep(1)
        to_inp.send_keys('\n')

        sleep(randint(1,3))

        bcc_inp = self.chrome.find_element_by_name("bcc")
        bccs = ';'.join(bcc)
        print(bccs)
        bcc_inp.send_keys(bccs)
        
        subject_inp = self.chrome.find_element_by_name("subject")
        subject_inp.send_keys(self.subject)

        sleep(randint(1,3))

        text_inp = self.chrome.find_element_by_name('body')
        text_inp.send_keys(self.text)

        sleep(randint(1,3))

        send_btn = self.chrome.find_element_by_name("nvp_bu_send")
        send_btn.click()
        print("Email sent.")

    def start(self):
        counter = 0
        while counter < len(self.bcc):
            if counter != 0 and counter % 60 == 0:
                print("Taking break...")
                for _ in range(randint(250, 300)):
                    sleep(1)
            bcc_recipients = self.bcc[counter: counter + 3 if counter + 3 < len(self.bcc) - 1 else None]
            counter += 3
            self.send_email(bcc_recipients)
            for _ in range(randint(3, 5)):
                sleep(1)


    def main(self):
        input("Enter to start...")
        print("BCCs:", self.bcc)
        print("Email Subject:", self.subject)
        print("Email Content:", self.text, end='\n')

        print("Starting the bot now...")
        
        self.open_gmail()

        sleep(5)

        input("Log in please. Enter to continue.")

        sleep(10)

        input('Press Enter to start now...')
        self.start()
