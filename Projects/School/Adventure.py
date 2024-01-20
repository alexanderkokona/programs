# Intro
name = input("Hang on, who are you?\n").capitalize()
print(f"Well, {name}, what are you doing out here by the trolley tracks?")
print("Nevermind, don't answer that.")
direction = input("What do you want to do? Go LEFT or RIGHT?\n").lower()

# First choice 
if direction == ('left'):
    print("Sounds good! Hey, do you see that over there?")
    print("Yeah, that random lever")
    lever = input("Do you wanna GO to the lever or TURN AROUND?\n").lower()
    
    # First to second choice (LEFT)
    if lever == 'go':
        print("Huh, strange. What's a lever doing here at a random split in the tracks in the middle of nowhere?")
        print("And is that a person tied to the tracks over there?!")
        choice = input(f"Listen {name}, Do you want to STAY or LEAVE?\n").lower()

        # Second to third choice (STAY/LEAVE)
        if choice == 'stay':
            print("Do you hear that? Is that... no way!")
            print("It's a runaway trolley full of innocent people!")
            print("It's headed right for the end of the tracks, they'll all die!")
            decide = input("Do you want to PULL the lever and kill the one person\nor LEAVE the pulley alone and let nature take it's course?\n").lower()

            # Conclusion 1
            if decide == 'pull':
                print("Well, there goes the trolley, and there goes that random guy.")
                print(f"Well {name}, good luck and safe travels.")
                print("Imma leave now, hope the knowledge that you killed someone doesn't haunt you!")

            elif decide == 'leave':
                print("Wow, that was spectacular!")
                print("The trolley derailed and then rolled.")
                print("When it finally stopped, it blew up!")
                print("At least that one random guy is still alive.")
                print(f"I guess this is the end {name}, I'll see you around.")
                print("And good luck with the trauma and the, you know, pieces of people everywhere...")

            elif decide == 'kill them all':
                print(f"Oh my... {name}, did you just flip the pulley so the trolley derails")
                print("at the right time so that the random guy is hit and the trolley explodes?")
                print("I have no words...")

            else:
                print("You are taken hostage by a crazy old man and tied to the tracks where the other guy used to be...")

        elif choice == 'leave':
            tracks = input(f"Well, {name}, do you want to go ACROSS the tracks or AWAY from them?\n").lower()

            # Conclusion 2
            if tracks == 'across':
                print("And you get hit by the trolley yourself and die...")
                print(f"That's tough {name}")
            
            elif tracks == 'away':
                print("Look out! It's a old man with a knife!")
                print(f"Sorry to say {name}, but you done did got killed.")

            else:
                print("A swarm of rabbid flying squirrels pick you up and use you to feed their children.")

        else:
            print("A black hole appears in front of you and you are spaghettified...epically.")

    elif lever == 'turn around':
        print("Whoah! Where'd that old man come from?")
        print("Hmmmm, he could be a serial killer living in the woods")
        print("Or he could just be a nice old man...")
        man = input(f"So, {name}, do we KILL him before he kills us or should we TALK to him?\n").lower()

        # Second to third choice (KILL/TALK)
        if man == 'kill':
            print("Wow, did you really have to be that gruesome?")
            murder = input("So are you gonna HIDE the body or try to find HELP?\n").lower()

            # Conclusion 3
            if murder == 'hide':
                print(f"Dang {name}, I never expected you to be this good at hiding bodies")
                print("Do you think the cops will find out?")
                print("Best if you just lie lowfor a few years...")
                print(f"Good luck {name}")
            
            elif murder == 'help':
                print("Hey look! A ranger cabin! Through the woods, see it?")
                print("Oh, they don't look happy...")
                print("They seem to be pointing something at you.")
                print("Ope, they shot you, that's tough")

            else:
                print("You turn into a tree and cut down to be made into toilet paper.")
                print("Hey, I don't make the rules here")

        elif man == 'talk':
            print("Oh, he's squareing up on you")
            boi = input("Are you gonna RUN away like a coward or are you gonna FIGHT like an idiot?\n").lower()

            # Conclusion 4
            if boi == 'run':
                print("You really should've done more cardio, 'cause that old man is rapidly approaching")
                print(f"Yeah, {name}, sorry to say, but he caught up and turned you into random-person-salad")

            elif boi == 'fight':
                print(f"Bet. {name}, You got this, just remember; don't let the knife cut your vitals-")
                print("Like that, yeah, just like that. You had one job you know...")

            else:
                print("There are now hundreds of crazy old men with knives swarming from the tree line...")
                print("You are minced like a bulb of garlic or a freash onion")
                print("before a chef makes an omlette")

        else:
            print("Are- are you just staring him down?")
            print("What is this?")
            print("Uhhhhh... Imma go now...")
            print("Bye...")

    else:
        print(f"And just like that, you {name}, went mentally insane from indecision.")

elif direction == 'right':
    print("Cool, oh hey, there's a bridge over there.")
    bridge = input("Wanna CROSS the bridge or SIT on the bridge?\n").lower()

    # First to second choice (RIGHT)
    if bridge == 'cross':
        print("Oh, a pretty meadow is over here.")
        meadow = input("Well, do you want to LAY DOWN or CROSS the meadow?\n").lower()

        # Second to third choice (LAY DOWN/CROSS)
        if meadow == 'lay down':
            print("How pretty! They sky is gorgeous today!")
            clouds = input("You gonna SLEEP or watch the CLOUDS roll by?\n").lower()

            # Conclusion 5
            if clouds == 'sleep':
                print(f"Rest well, {name}. I'll see you on the other side...")
            
            elif clouds == 'clouds':
                print("Dang, look at that one! It looks like a dragon!")
                print("That one looks like a house!")
                print("That one looks like a meteor!")
                print("...")
                print("hmmm...that is a meteor...")
                print(f"Well {name}, it was a pleasure")
                print("Good luck with this whole meteor thing")

            else:
                print("You are consumed by hundreds of ducks...")
                print("Don't ask how, it's just what happened")

        elif meadow == 'cross':
            print("Looks like theere is just woods over here")
            print("and veranda over there for picnics and the like.")
            edge = input(f"So {name}, you gonna head into the WOODS or go over to that VERANDA over there?\n").lower()

            # Conclusion 6
            if edge == 'woods':
                print("So... we've been walking for awhile now...")
                print("You planning on stopping-")
                print("did you hear that?")
                print("Oh gosh! There's an old man with a knife!")
                print("You got stabbed, multiple times, you got Caesared! Shish-kababed! Diced! You know?")

            elif edge == 'veranda':
                print("This is nice. Just being one with the world you know.")
                print("*sigh* nice")

            else:
                print("You are struck by lightning and die")
                print(f"Shoud've chosen a different option {name}. Just sayin'")

        else:
            print("You go home")
            print("No idea how")
            print("You just go home")

    elif bridge == 'sit':
        print(f"Hey look, {name}! There's a large man crossing the bridge.")
        print("What? He's huge, there's no denying it.")
        large = input("Do you want to TALK with the big man or IGNORE him? Or... and this is totally an intrusive thought, we could PUSH him off the bridge.\n").lower()

        # Second to third choice (TALK/IGNORE/PUSH)
        if large == 'talk':
            print("Large man: 'Oh hey there friend. How are you this fine day?'")
            print("Don't say anything, just shrug and sigh")
            print("Large man: 'I understand, you came out here to answer some questions...'")
            print("Don't acknowledge him")
            question = input("Large man: 'I have a question for you: Do you like DOGS or CATS?'\n").lower()

            # Conclusion 7
            if question == 'dogs':
                print("Large man: 'Yeah, those floofers are the goodest bois.")
                print("This is my goodest boi, a right poofer he is.'")
                print("You're gonna sit here the rest of the day aren't you?")
            
            elif question == 'cats':
                print("Large man: 'I do like a cat that likes to curl up on your lap and takes a nap.")
                print("Hey that ryhmes!")
                print("Well anyway, this is my kitter, she likes to take naps on laps, wanna hold her?'")
                print("Alright, Isee you're stuck here now, I guess I'll see you around")

            else:
                print("Large man: 'Oh, I didn't quite get that.")
                print("Well anyways, I have both right over on the other side of the bridge if you wanna go say hi.")
                print("If you would rather not, I'll see you around friend!'")

        elif large == 'ignore':
            print("Huh, looks like he is gonna just stand there. Probably to take in the scenery")
            print("Hang on, is that a run away trolley?!")
            trolley = input("Quick! Should we PUSH the large man or do NOTHING? You know the trolley will stop if we push the large man.").lower()

            # Conclusion 8
            if trolley == 'push':
                print("Woah, you actually pushed him off the bridge...")
                print("I wonder if the trolley will actually stop or not.")

            elif trolley == 'nothing':
                print("Huh, you chose not to push the large man, and there goes the trolley...")
                print("Oooo, nice, that was a big explosion")

            else:
                print("The large man pushes you off the bridge to try and stop the trolley.")
                print("It doesn't work by the way...")

        elif large == 'push':
            print("Dang, he really fell head first onto the tracks. I guess that's that...")
            print("Wait, do you hear that?")
            print("Oh, you've got to be kidding me! Is that a runnaway trolley full of innocent people?!")
            print("And it's headed for the end of the tracks where they'll all die?!")
            print("Do you think the big guy can stop the trolley?")
            jump = input("Should we JUMP to add more mass and possibly stop the trolley or WAIT and see?\n").lower()

            # Conclusion 9
            if jump == 'jump':
                print("Ha! You actually jumped!? Well, I'm not telling you how this ends.")
                print("What? It doesn't matter for you, you're dead.")

            elif jump == 'wait':
                print("Woah! the trolley totally got stopped by the large man's corpse! Crazy. At least the people are safe now.")

            else:
                print("An earthquake occurs, throwing both you and the large man onto the tracks")
                print("and brings the bridge down on top of you, the large man, and the trolley")
    
        else:
            print("Fine, your intrusive thoughts win and you jump after him.")
            print("And then you're both run over by a runaway trolley.")

    else:
        print(f"You, {name}, are abducted by a family of moosen who keep you as a prisoner of war.")
        print("Which war? Doesn't matter...")

elif direction == ('neither'):
    print("okay then...")
    print("I guess we'll just sit here then...")

else:
    print("Then I'll choose for you.")
    print("Do you see that over there?")
    print("Yeah, that random lever")
    lever = input("Do you wanna GO to the lever or TURN AROUND?\n").lower()