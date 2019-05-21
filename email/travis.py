from email_sender import Email

travis = Email(email="travistolman1.services@gmail.com", password="Tomsky26", 
             to="travistolman1.services@gmail.com", bcc="travis_bcc.txt", subject="New Start Enquiry",
             text="travis_content.txt", headless=False)

travis.main()
