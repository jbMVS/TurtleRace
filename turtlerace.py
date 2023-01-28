## -- This is where python starts.  Your code should always start with any imports you may have.
import turtle
import random
import time

## -- Classes, and then functions, should come after imports.  We haven't gotten to classes, so the next thing in our code is functions.
def graphics(): # Creates a start and finish line
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()
    pen.goto(-386,196)
    pen.write("Start", align="center", font=("Arial", 9, "bold"))
    pen.goto(-365, 190)
    pen.pendown()
    pen.right(90)
    pen.fd(380)
    pen.penup()
    pen.goto(386,196)
    pen.write("Finish", align="center", font=("Arial", 9, "bold"))
    pen.goto(365, 190)
    pen.pendown()
    pen.fd(380)
    pen.penup()


def starttimer(): # Displays "3, 2, 1, GO!" and delays start at beginning of race
    start = turtle.Turtle()
    start.hideturtle()
    start.write(3, font=("Arial", 40, "bold"))
    time.sleep(1)
    start.clear()
    start.write(2, font=("Arial", 40, "bold"))
    time.sleep(1)
    start.clear()
    start.write(1, font=("Arial", 40, "bold"))
    time.sleep(1)
    start.clear()
    start.write("GO!", font=("Arial", 40, "bold"))
    time.sleep(1)
    start.clear()


def endgame(winner, total): # endgame loop - asks if player wants to continue, and clears the previous racers if they do
    ending = True
    winningracer = turtle.Turtle()
    winningracer.hideturtle()
    winningracer.penup()
    winningracer.goto(-80, 0)
    winningracer.write("Turtle " + str(winner + 1) + " wins!", font=("Arial", 20, "bold"))
    print("Turtle " + str(winner + 1) + " wins!")
    while ending == True:
        again = input("Do you want to race again? y/n\n> ") # this is where we give hte player the option to quit the game.
        if again == "n": # "n" goes through the standard closing message we've done before
            print("Goodbye! Closing in 5 seconds...")
            time.sleep(5)
            quit()
        elif again == "y": # "y" goes the list of racers and clears them from the board, along with the winning racer graphic.
            winningracer.clear()
            for val in range(0, len(total)) :
                total[val].clear()
                total[val].hideturtle()
                ending = False
        elif again != "y" or "n": # error message if anything but y/n are entered.
            print("You must enter y or n")

## -- Here is where python actually starts executing code.  Before this point, our imports and functions are only being loaded into memory.
turtle.bgcolor("green") #sets the background color of the race track
turtle.title("Turtle Race") #names the racetrack screen
turtle.setup(824, 424)  #defines width and height, respectively

graphics() # draws the start and finish line on the racetrack.


## -- This is our main game loop.  After everything is loaded, our program will loop from line 76 up to 115, depending on what happens during play.
while True:
    colors = ["blue", "red", "white", "purple", "pink", "orange", "yellow", "brown"] # available color choices for racers, defined within the loop so it can reset each game.
    race = True
    tAmount = input("How many racers? (Max 8)\n> ")
    if tAmount.isnumeric() and int(tAmount) <= 8:
        if int(tAmount) > 1:    
            firstplace = -175 # first place's y value
            racers = [] # an empty list of racers that is added to based on amount chosen by player
            racernum = 1 # Python defaults to starting at 0, this is a placeholder variable so that racer #1 is named correctly, and not racer #0, and so on
            for n in range(int(tAmount)): # uses a for loop to create amount of racers entered in tAmount
                n = turtle.Turtle()
                n.hideturtle() # hides the turtle while changes are made
                n.speed(0)
                n.shape("turtle")
                racers.append(n)
                n.penup()
                n.goto(-380, firstplace) # player (x,y) position
                n.back(20)
                n.write(racernum, font=("Arial", 12, "bold"))
                racernum = racernum + 1
                n.fd(20)
                colorchoice = random.randint(0, (len(colors) - 1)) # picks a random color from the "colors" variable
                n.color(colors[colorchoice]) # makes the turtle the picked color
                colors.pop(colorchoice) # removes the color choice from "colors" so each turtle is unique
                n.showturtle() # shows turtle after changes are made
                firstplace = int(firstplace) + 50 # "firstplace" increments by this amount for every successive player added
            starttimer()
            while race == True:
                for n in range(int(tAmount)): # another for loop, this one to move turtles forward a random amount between 2 and 20
                    if racers[n].pos() < (350, 0): # 1st value is finish line 
                        racers[n].fd(random.randint(2, 20))
                        if racers[n].pos() >= (350, 0):
                            race = False
                            winner = n
                            break # Break can be tricky.  It's important to note which loop it is breaking, see below:
            # ** this is where the break loop exits to.  Note that we are still within the greater "while True:" loop.
            endgame(winner, racers) # This will display the winner, and takes the total number of racers so that it knows how many to erase from the track.
        else:
            print("You must enter a number between 2-8") # error message if anything but 2-8 is entered.
    else:
        print("You must enter a number between 2-8") # error message if anything but 2-8 is entered.