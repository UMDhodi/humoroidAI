from faker import Faker
import shutil
import os

faker = Faker()
print(f'name: {faker.name()}')
print(f'address: {faker.address()}')
print(f'email: {faker.email()}')
print(f'country: {faker.country()}')
print(f'url: {faker.url()}')
print(f'text: {faker.text()}')
cm = input("Enter :")
if"yes":
    print("Enter name")
    name = input("")
    id = open(f'{name}.txt','w')
    id.write(f"Name: {faker.name()}\n")
    id.write(f"Address: {faker.address()}\n")
    id.write(f"Email: {faker.email()}\n")
    id.write(f"Country: {faker.country()}\n")
    id.write(f"URL: {faker.url()}\n")
    id.write(f"Bio: {faker.text()}\n")
    id.close()

    path_1 = f"C:\\Users\\mayan\\Desktop\\AI\\" +str(name) 
    path_2 = "C:\\Users\\mayan\\Desktop\\AI\\Database\\fake id"
    new_path = shutil.move(path_1,path_2)
    print("done")

else:
    pass