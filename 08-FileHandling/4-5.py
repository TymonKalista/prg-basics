import re
def email_sender(file_name, pattern):
    sender = re.search(pattern, file_name)
    if sender:
        return sender.group(1)
    else:
        return ""
    
with open("email.txt", "r") as f:
    content = f.read()
print(email_sender(content, r"From:.*<([^>]+)>"))

def email_recepient(file_name, pattern):
    recepient = re.search(pattern, file_name)
    if recepient:
        return recepient.group(1)
    else:
        return ""

with open("email.txt", "r") as f:
    content = f.read()
print(email_recepient(content, r"To:.*<([^>]+)>"))

def email_subject(file_name, pattern):
    subjet = re.search(pattern, file_name)
    if subjet:
        return subjet.group(1)
    else:
        return ""
with open("email.txt", "r") as f:
    content = f.read()
print(email_subject(content, r"Subject:\s*(.*)"))  

#def emial_body()
