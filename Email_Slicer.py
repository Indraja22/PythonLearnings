class Email_Slicer:

    def get_domain(self, email_address):
        email_domain = email_address.split("@")[-1]
        username = email_address.split("@")[0]
        return email_domain, username

email_slicer = Email_Slicer()

print(email_slicer.get_domain("indraja9@gmail.com"))
print(email_slicer.get_domain("indraja42@accenture.in"))
print(email_slicer.get_domain("indraja23@yahoo.in"))