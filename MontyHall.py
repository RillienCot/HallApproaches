import random

def play_games(number_of_games, switch_percantage):
    score = 0 # Number of rounds won
    game = 1 # Current came count
    level = number_of_games * (switch_percantage / 100)

    def switch_door():        
        Doors = [1, 2, 3]
        prize = random.choice(Doors)
        firstSelection = random.choice(Doors)

        # Decide which door to remove
        DoorsInPlay = [firstSelection, prize]
        DoorsInPlay = list(set(DoorsInPlay)) # Deduplicate list

        removableDoors = Doors.copy() # List of doors Monty could choose to reveal
        for door in DoorsInPlay:  # Remove doors in play from Monty's options to reveal
            removableDoors.remove(door)

        ghostDoor = random.choice(removableDoors) # Select a random door from removable doors to reveal

        # Remove Ghost Door
        newDoors = Doors.copy()
        newDoors.remove(ghostDoor) # Options after Monty has revealed a door

        # Choose other door
        finalSelection = newDoors.copy()
        finalSelection.remove(firstSelection)
        finalSelection = finalSelection[0]

        if finalSelection == prize:
            return 1
        else:
            return 0

    def keep_door():
        Doors = [1, 2, 3]
        prize = random.choice(Doors)
        firstSelection = random.choice(Doors)

        if firstSelection == prize:
            return 1
        else:
            return 0        

    while game <= number_of_games:
        if game <= level:
            score += switch_door()
        else:
            score += keep_door()
        
        game += 1

    winRatio = 100 * (score/number_of_games)
    lossRatio = 100 * ((number_of_games - score)/number_of_games)
    
    return winRatio, lossRatio