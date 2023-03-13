# Greeting users! Hurray!
print(f"Hello and Welcome! It is story time, so please gather around! This one is about Mordecai the cat's adventure! ")
print(f"To begin, I would like to ask you, wonderful person a few questions to get started. :)")
print(f"Please press the enter key after answering the questions or we won't able to start the story time!")

startOver = "yes"
while startOver.lower() == "yes":


    
#questions for you :)

#Question 1
    catPersonality = input(f"\nWhat is the cat's personality?:  ")
    while len(catPersonality) == 0:
         catPersonality = input(f"Oops! Please enter personality, it is important for the story!:  ")

#Question 2
    homeRoom = input(f"\nWhich room is the cat located?:  ")
    while len(homeRoom) == 0:
        homeRoom = input(f"Oops! Please enter room, it is important for the story!:  ")

#Question 3
    catCoatcolor = input(f"\nWhat is the cat's coat color?:  ")
    while len(catCoatcolor) == 0:
        catBreed = input(f"Oops! Please enter cat's coat color, it is important for the story!:  ")

#Question 4
    catAge = input(f"\nIs Mordecai old or young:  ")
    while len(catAge) == 0:
        catAge = input(f"Oops! Please enter cat's age, it is important for the story!:   ")

#Question 5
    catSize = input(f"\nIs Mordecai chonky or smol?:  ")
    while len(catSize) == 0:
        catSize = input(f"Oops! Please enter cat's size, it is important for the story!:   ")



#Story begins!
    print(f"\nAlright! Let's start the story!")
    print(f"\nOne day a very {catPersonality}, {catAge}, and {catSize} {catCoatcolor} cat named Mordecai was waking up from his nap in {homeRoom}")
    print("When he opened his eyes, they were the most piercing blue color you'd ever seen!")
    print("He realizes that he is so hungry and hadn't eaten in hours! So, he heads to the kitchen hoping to eat something delicious.")
    print("Oh no his bowl is empty!!")

#Decision 1 Mordecai must cause chaos!
    smackBowlacrossFloor = input(f"\nShould Mordecai smack his bowl across the floor to grab his humans' attention? Please type yes or no:   ")
    while smackBowlacrossFloor.lower() != "yes" and smackBowlacrossFloor.lower() != "no":
        smackBowlacrossFloor = input(f"uh oh! type yes or no in lowercase please:  ")

    if smackBowlacrossFloor == "yes":
        print(f"\nMordecai smacks his bowl half way across the floor, making a lot of noise.")
        print(f"\nHe hopes that his human will notice that it is completely empty. He looks up and to see if his human notices all the noise in the kitchen. His human doesn't even hear the noise from the kitchen! Oh no! They are too busy on some weird light box!")
    else:
        print(f"\nMordecai decides that smacking his bowl might not work at all because the last time his human didn't even acknowledge his trick! His plan is to walk over to where his delicious food is located and meow to grab his owners' attention. If he doesn't notice him then doesn't he see that he is whittling away from hunger?")

# Decision 2 Mordecai wants to cause all the chaos?
    catMordecaiwalks = input(f"\nDoes Mordecai walk over to his human after being ignored? Please type yes or no:  ")   
    while catMordecaiwalks.lower() != "yes" and catMordecaiwalks.lower() != "no":
        catMordecaiwalks = input(f"uh oh! type yes or no in lowercase please:  ")

    if catMordecaiwalks == "yes":  
        print(f"\nAfter trying to get his human's attention Mordecai decided to take a small break and flop on the floor.")
        print(f"\nAll of this work made him a bit tired, but he needed to get up soon. A few minutes later, Mordecai got up and walked slowly with his tail flicking around towards his human.")
        print(f"\nHe walked up to his human and started giving cute head butts to his owner to get his attention. Great! he got his human's attention!")
    else:
        print(f"\nMordecai decides to stay in the kitchen, he starts reaching up toward his delicious food but that did not get him his food! Since that didn't work he starts yowling loudly so his human can come feed him!")

# Alternate endings!
    if smackBowlacrossFloor == "yes" and catMordecaiwalks == "yes":
        print(f"\nHurray Mordecai got his human's attention. His human walks to his delicious food and grabs his food, and pours the food into Mordecai's bowl. He is so happy and content. After he is done eating he walks back to his human, jumps in his lap and starts making muffins and purrs.")
    elif smackBowlacrossFloor == "no" and catMordecaiwalks == "no":
        print(f"\nMordecai is very sad no one heard his cries for food. Everyone was ignoring him or didn't hear him at all. So he decideds to lay down next to his bowl. He stays by his bowl forever, hopefully someone will come to the kitchen soon so he can show them that his bowl is empty.")
    else: 
        print(f"\nOh wow! Mordecai's human comes to the rescue to provide him with delicious food! He eats his food and then goes to his human's bedroom to sleep off his reward.")
    print(f"\nHurray our story is now complete! Thank you for your help!")
        
    startOver = input(f"\nWould you like to play again? Type in yes or no, please :):    ")
    while startOver.lower() != "yes" and startOver.lower() != "no": 
        startOver = input(f"\nOops! Please type in yes or no:    ")
           
