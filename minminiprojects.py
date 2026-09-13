print("You are in an abondened spooky house.\n The main front door suddenly slams.")
print("You have two options")
print("Window\nOR\nDoor")

choice_1 = input("Enter your choice  ").lower()
if choice_1 == "window":
    print(
        "SURPRISE SURPRISE SMARTY\n You are now in a room with complete darkness\n You thought you escaped"
    )
    print(
        "You wanna hop back out or keep moving thro darkness that could potentially swallow YOU\nOptions;\n1.hop back 2.keep moving"
    )
    choice_2 = input("enter your choice  ").lower()
    if choice_2 == "hop back":
        print("Not a smart move.You slipped thro the glasses shreds and died")
    else:
        print(
            "you found a key by stumbling upon it.CONGRATULATIONS!!!\n Be careful on your way out some people might die\nby slipping while jumping over the broken window."
        )

elif choice_1 == "door":

    print(
        "you enter a dark space. One man starts by\n I can make a man believe he is king, or trap him in a nightmare of his own making.\nI can be weaponized to destroy a life,or carefully woven to save one. The closer you look, the harder i am to see.\nI am born in the mind,spoken by the tongue,and lived as truth untillll i am exposed.\n    What am i ???"
    )
    ans = input("whats the ans  ").lower()
    if ans == "lie":
        print("good you are safe        for now")

    else:
        print("you fool\n A giant hand flattens you out and you DIE")


else:
    print("You wanna DIE ?\nRemember we are the choices we make.")
