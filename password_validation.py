# Validate the quality and correctness of Password
#Must not be empty
#Must be atleast 8 characters
#Must include at least one upper case
#Must include at least one lower case
#Must not be same as email
#Must not contain any spaces 
#Must start or end with a letter or a digi

password = "Bachakhanbaba54"
email = "Kousaralam111@gmail.com"
# clean the string
password = password.strip()
#password mustn't be empty
if password == " ":
    print("password can't be empyt")
#Password Must be at least eight Character's long
elif  len(password) <8:
    print("password must be at least 8 characters long")
#Password must contain at least 1 upper case letter
elif not any(character.isupper() for character in password):
    print("password must contain at least one uppper case letter")
#password Must contain at least one lower case letter
elif not any(character.lower() for character in password):
    print("Password Must contain at least one lower case letter")
#The password must not be the same as email
elif password == email:
    print("the password must not be the same as email")
#The password must be start and end with a letter and a digit
elif not(password[0].isalnum() and password[-1].isalnum()):
    print("The password must start and end with a letter or  a digit")
else:
    print("The password is valid")
