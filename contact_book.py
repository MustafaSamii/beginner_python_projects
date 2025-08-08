from pathlib import Path

file_path = Path('contact_list.txt')

if not file_path.exists():
    with open(file_path, 'w') as file:
        file.write('')

class contact_book:
    def __init__(self):
        self.contacts = []
    def add_contact(self,name,phone,email):
        new_contact = contact(name,phone,email)
        self.contacts.append(new_contact)
        with open('contact_list.txt','a') as file:
            file.write(f"Name: {name}, Phone: {phone}, Email: {email}\n")
            file.close()
    def display_contacts(self):
        with open('contact_list.txt', 'r') as file:
            contacts = file.readlines()
            print("Contact List:")
            for contact in contacts:
                print(contact.strip())

class contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

book = contact_book()


user = input("To add a contact, type 'add'. To view contacts, type 'view':").strip().lower()
if user == 'add':
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    book.add_contact(name,phone,email)
    book.display_contacts()
elif user == 'view':
    book.display_contacts()


