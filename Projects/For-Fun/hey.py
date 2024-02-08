answer = input("Hey, did you watch me code this? (y/n)\n").lower

if answer == 'y':
    print("Well I never. But I still need you to answer")
    next = input("Then do you love me? (y/n)\n").lower
    
elif answer == 'n':
    print("Then I have one question for you")
    answ = input("Do you love me? (y/n)\n").lower

else:
    print("I need a valid answer, silly goose")
    answer = input("So, did you watch me code this? (y/n)\n").lower

if next == 'y':
    print("I love you to :)))")

elif next == 'n':
    print("I still love you :)))")

else:
    print("I need a valid answer, silly goose")
    next = input("Then do you love me? (y/n)\n").lower

if answ == 'y':
    print("I love you to :)))")

elif answ == 'n':
    print("I still love you :)))")

else:
    print("I need a valid answer, silly goose")
    answ = input("Do you love me? (y/n)\n").lower
