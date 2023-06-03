#two functions that simulate gold gain in an action based game
#main function requiers input and gives the option of what to calculate
#first function will calculate how much gold the player can gain in a given time
#second calculates how much time it will take to gain an amount of gold

def gainByTime():
    goldPerAction = float(input("Enter Gold Per Action"))
    speed = float(input("Enter Action Speed in seconds"))
    goldGain = 0
    timeFrame = int(input("Enter Timeframe in seconds"))

    actions = round(timeFrame/speed)
    for x in range(0, actions):
        goldGain += goldPerAction

    print("Actions: " + str(actions))
    return goldGain

def goldTime():
    goldPerAction = float(input("Enter Gold Per Action"))
    speed = float(input("Enter Action Speed in seconds"))
    goldDesired = int(input("Enter Desired gold to gain"))

    timeFrame = round((goldDesired/goldPerAction) * speed, 2)
    actions = round(timeFrame/speed)
    print("Actions: " + str(actions))
    return timeFrame

def simulate():

    simBool = input("Type '1' to simulate gold gained in an amount of time, Type '2' to simulate how much time to gain x amount of gold. Type 'c' to close")

    if simBool == "1":
        print("Gold Gained: " + str(gainByTime()))
        simulate()

    elif simBool == "2":
        goldTimeT = goldTime()
        hours = round(goldTimeT/3600 , 2)
        print("Time till desired gold: " + str(goldTimeT))
        print("Time in hours: " + str(hours))
        simulate()
    
    elif simBool == "c":
        return False

    else:
        print("Invalid input, try again")
        simulate()

simulate()
