from email_sender import Email

adam = Email(email="adamgavin.services@gmail.com", password="Tomsky26", 
             to="adamgavin.services@gmail.com", bcc="adam_bcc.txt", subject="Car Wash Enquiry",
             text="adam_content.txt", headless=False)

adam.main()
