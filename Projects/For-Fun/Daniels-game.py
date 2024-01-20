print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?")

choice1 = input("choice(match, flashlight): ")

#flashlight

if choice1.lower() == "flashlight":
   
    print("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?")
   
    x = input("follow,look: ")
   
#follow

    if x.lower() == "follow":
     
        print("you follow the Path and find a underground bunker. Do you open bunker or keep walking?")

        woods = input("keep walking, open bunker : ")
        if woods.lower() == "keep walking":
            print("You keep walking and die of frost bite")

        if woods.lower() == "open bunker":
            print("You open the bunker and find a lifetime supply of gummie worms. The end")
       
   
  #look
    if x.lower() == "look":
 
        print("You look and find it is just an owl... no its an owl with a pitch fork! the owl starts cchasing you, what do you do run or fight ")

        owl = input("run, fight: ")
        if owl.lower() == "run":
            print("you get chased by the owl and get hit by the pitchfork, and die")

        if owl.lower() == "fight":
            print("you fight the owl but it overcomes you by hiting you with the pitchfork")


#match
       
if choice1.lower() == "match":
 
    print("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?")
   
    y = input("run, hide: ")

#run
 
    if y.lower() == "run":
   
        print("you run and the bear starts chaseing you. do you keep running, jump off the upcoming clif, or fight")

        run = input("run, jump, fight: ")

        if run.lower() == "run":
            print("you keep running and the bear catches up and mauls you")

        if run.lower() == "jump":
            print("you jump off the cliff and fall to your death")

        if run.lower() == "fight":
            print("you fight the bear and it mauls you to death")


#hideg
   
    if y.lower() == "hide":
   
        print("you are running and see 2 places to hide, dou you run up a tree or hide behind a large rock.")

        hide = input("tree, rock:")
        if hide.lower() == "tree":
            print("you run up the tree but the bear pushes the tree over and eats you")

        if hide.lower() == "rock":
            print("you hide behind the rock and the bear pushes the rock and the rock crushes you")
#else
    else:
        print("you died")
else:
    print("you died")