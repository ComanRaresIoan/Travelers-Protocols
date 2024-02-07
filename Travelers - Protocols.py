# In the Travelers series on Netflix, there are few protocols that the characters must respect. Let's present them along with the explanation to you :)
print("Welcome!\nSince you are here, I think you saw the Travelers Series on Netflix. Let's get to know each other.")
print("I am the director, also known as 001. Who are you Traveler?")
traveler_number = input("Enter your number, Traveler!\n")
print("Hello, Traveler",traveler_number,"What is the name of your HOST?")
host = input("")
print("Okay",host,"or traveler",traveler_number,". Let's begin with your casher and see if you will be overwritten.")
Protocols ={'Alpha': "Top Priority",
            '1': "The mission comes first.",
            '2': "Never jeopardize your cover",
            '2H': "Updates are not to be discussed with anyone. Ever.",
            '3' : " Don't take a life;Don't save a life, unless otherwise directed.Do not interfere.",
            '4' : "Do not reproduce.",
            '5' : "In the absence of direction, maintain your host's life.",
            '6' : "No inter-team/deep web communication except in extreme emergencies or when sanctioned.",
            'Omega' : "The Director will no longer be intervening in this timeline." }
x = input("Enter the number of protocol you want to see: ")
x_input = Protocols.get(x)

print(f"The Protocol '{x_input}' means: ")
if x == 'Alpha':
    print("Protocol Alpha requires all Travelers to do whatever it takes to resolve the issue at hand.")
elif x == "1":
    print("This means putting aside all other priorities for the task at hand.\n"
          "A Traveler must be dedicated to the mission, and it must be the most important thing to them.\n"
          "Completing the mission is the only task that really matters.\n"
          "Everything you do as a Traveler should somehow further the mission's objective.\n")
elif x == "2":
    print("This has two parts:\n"
          "Do not call each other by future names “Leave the future in the past”.\n"
          "Do not use future knowledge for personal gain.\n"
          "Either of those things could mean that people will find out there is something off about you,\n"
          "that you aren't really who you say you are. Self-control is key to becoming a Traveler.\n"
          "You are no longer who you were in the future.\n"
          "You must assume the identity of your host and acknowledge your team only as their new identity.\n"
          "The future knowledge you have is for the betterment of your mission and your fellow Travelers,\n"
          "not for your own advancement.")
elif x =="2H":
    print("Periodically a Historian will need to be updated due to changes in the timeline caused by Travelers.\n"
          "Updates will include historical information relevant to a team’s role in the Grand Plan,\n"
          "including potential candidates, investments, etc. But by its very nature,\n"
          "updates may also include historical information about your team members, loved ones, about the Historian.\n"
          "This is a burden they will have to carry with them until the day they die—a date which,\n"
          "for obvious reasons, will be omitted from the update.")
elif x =="3":
    print("That's not what you're here for. Changing the past can have dire consequences to the future,\n"
          "and the mission is the only change that has been mandated.\n"
          "Refrain from putting yourself in a position where you have to take or save a life.\n"
          "The lives of others are not your concern, do not interfere.")
elif x =="4":
    print("This can massively interfere with the mission, and involves changes to the past that have not been approved.\n"
          "Refrain from creating relationships that can lead to this. Do not complicate things.\n")
elif x =="5":
    print("Keeping your host alive means keeping yourself alive to further the mission.\n"
          "Maintain good health, and avoid situations that put your host in danger.\n"
          "Your host's death means your own death.\n"
          "You were sent here for a reason, and the mission needs you.\n")
elif x =="6":
    print("Your team is the only group of Travelers you should be interacting with.\n"
          "You share a common mission, and the others have their own missions.\n"
          "You do not need to interact, and should refrain from doing so at all costs.\n"
          "Extreme emergencies may warrant an exception to this rule, but the situation must be dire indeed.\n")
elif x =="Omega":
    print("Those who are part of the Traveler program are free to live out their days, such as they are,\n"
          "as they see fit. Protocol Omega can be enacted because the Grand Plan has succeeded and we're now\n"
          "on the optimal path to a better future or because there's no possible way of saving the future.")
else:
    print("You have not introduced any Protocol code. Please run the program again to get it")
print(f"Let's create a record of on {traveler_number},{host} with all the protocols that the traveler broke.")
print("What protocol did you broke?")
broke_protocol = str(input("Enter the protocol you broke:"))
f = open(f"History of {traveler_number},{host}:\n",'a')
with open(f"History of {traveler_number},{host}", 'a') as f:
    f.write(f"History of {traveler_number},{host}\n\nThe traveler {traveler_number} having the host called {host}"
            f" broke the protocol {broke_protocol}\n")
    add_more = str(input(f"Enter the text you want to add in the record {traveler_number},{host}\n"))
    f.write(add_more)



