attempts = 0
while attempts  <3:
    answer = input("do you agree!(yes/no):")
    if answer == "yes":
        print("glad we're on the same page")
        break
    attempts += 1
else:
    print("3 three strikes you are out")