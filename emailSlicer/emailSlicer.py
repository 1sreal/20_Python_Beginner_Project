print("Welcome to the mail slicer.\n")

base_mail = input("Supply your email address: \n")
(username, domain) = base_mail.split("@")
(domain,extension) = domain.split(".")

print("\n username:  " + username + "\n domain:  " + domain + "\n extension:  " + extension )