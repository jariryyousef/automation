import re

with open ('./potential-contacts.txt','r') as f:
    file_content = f.read()


def phone_numbers():
    numbers = re.findall(r'(\d{3}[-\.]?\d{3}[-\.]?\d{4}|\(\d{3}\)\d{3}[-\.]?\d{4})' , file_content)
    # (\d{3}-\d{2}-\d{4})|\(\d{3}\)\d{3}-\d{4}
    numbers_list = []

    for i in numbers:
        if i[3] == '-':
            numbers_list.append(i)

        if i[0] == '(':
            numbers_list.append(i[1:4] + '-' + i[5:])

        if len(i) == 10:
            numbers_list.append(i[0:3] + '-' + i[3:6] + '-' + i[6:])

    number = sorted(numbers_list)
    number = list(dict.fromkeys(numbers_list))

    with open("phone_number.txt","+w") as file:
        for i in number:
            file.write(f'{i}\n') 

phone_numbers()

# (\d{3}-\d{2}-\d{4})
# \(\d{3}\)\d{3}-\d{4}


def emails():
    emails = re.findall(r'[A-z0-9._%+-]+@[A-z0-9.-]+\.[A-z]{2,}' , file_content)
    # [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
    email = sorted(emails)

    with open("emails.txt","+w") as file:
        for i in email:
            file.write(f'{i}\n') 
emails()