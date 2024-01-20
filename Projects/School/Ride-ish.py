status = False

rider1_age = int(input("What is your age?\n"))
rider1_height = int(input("What is your height?\n"))
second_rider = input("Is there a second rider? Just answer 'yes' or 'no'\n").lower()

if second_rider == 'yes':
    rider2_age = int(input("What is your age?\n"))
    rider2_height = int(input("What is your height?\n"))

    # check ish
    if rider1_height < 36 or rider2_height < 36:
        status = False

    else:
        if rider1_age >= 18 or rider2_age >= 18:
            status = True
        else:
            status = False

# one rider
else: 
    if rider1_age >= 18 and rider1_height >= 62:
        status = True

    else:
        status = False

if status == True:
    print("Come on in! Have fun, good luck, don't die!")
    
else:
    print("Sorry to say, you cannot ride.")