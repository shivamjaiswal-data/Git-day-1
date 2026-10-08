while True :
    str = input("Enter a string: ")
    print(str)


    # To check passward 
correct_password = "some_pass"
not_found = True

while not_found:
    passw =input("Enter the password: ")
    if passw == correct_password:
        not_found = False
print("Password is correct!")