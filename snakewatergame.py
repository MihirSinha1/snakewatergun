# Snake Water Gun
print("Welcome to Snake Water Gun game \nNote - Please keep calculating your points")
d=1
while(d<=10):
    import random
    b=["Snake","Water","Gun"] 
    c= random.choice(b)
    a = input("Type 's' for snake \nType 'w' for water \nType 'g' for gun \n")
    if a=="s":
        print(c)
        if c=="Snake":
            print("It is a tie")
        if c=="Water":    
            print("You won the point")
        if c=="Gun":
            print("Computer won the point")  
    elif a=="w":
        print(c)
        if c=="Snake":
            print("Computer won the point")
        if c=="Water":
            print("It is a tie")
        if c=="Gun":
            print("You won the point") 
    elif a=="g":   
        print(c)
        if c=="Snake":
            print("you won the point")
        if c=="Water":
            print("computer won the point")
        if c=="Gun":
            print("It is a tie")
    print(10-d, "No. of chances left")
    d = d+1
if d>10 :
    print("Game Over")











