# AFL Fixture Creation Program
# Version 0_1

# Use Fixture and Match entity classes
from FixtureClass import Fixture
from FixtureClass import Match

# Import Python libraries
import json
import ast

# Singelton class that provides functionality for fixture creation program
class Program:

    # List of teams to build round fixture
    toFixtureTeams = ["Adelaide", "Brisbane", "Carlton", "Collingwood",
                      "Essendon", "Freemantle", "Geelong", "Gold Coast",
                      "Greater Western Sydney", "Hawthorn", "Melbourne",
                      "North Melbourne", "Port Adelaide", "Richmond",
                     "St. Kilda", "Sydney", "West Coast", "Western Bulldogs" ]
    # Fixture instance variable
    roundFixture = ""

    # Flag to diplsy certain menu items only after a fixture has been created
    fixtureSet = False

    # Program initiating method
    # Contains main program loop
    @staticmethod
    def run():
        done = False # flag to end program execution
        while not done:
            print("")
            Program.__printMainMenu()
            done = Program.__processInput()

    # Display main menu
    @staticmethod
    def __printMainMenu():
        print("AFL Fixture Program")
        print("Main Menu")
        print("---- ----")
        print("(1) Create new fixture")
        if Program.fixtureSet:
            print("(2) View fixture")
            print("(3) Output fixture to JSON file")
        print("---- ----")
        print("e(X)it")

    # Handle user's selected main menu option
    @staticmethod
    def __processInput():
        # Flag to signal whether to continue program execution
        result = False
    
        choice = input("Enter option: ")
        if choice == '1': # Create new fixture
            Program.__defineFixture()
        elif choice =='2' and Program.fixtureSet: # Display fixture if one has been created
            Program.__printFixture()
        elif choice =='3' and Program.fixtureSet: # Write fixture to JSON file, if one has been created
            Program.__writeFixture()
        elif choice == 'x' or choice == 'X': # User selects to exit program
            result = True
        else: # ALl other input invalid
            print("Invalid option. Please re-enter")
        return result

    # Dsiplay list of teams to add to a fixture
    @staticmethod
    def __printToFixtureTeams():
        print("\nTeams to fixture")
        for i in range(0, len(Program.toFixtureTeams)):
            print("(" + str(i+1) + ") " + Program.toFixtureTeams[i])

    # Convert fixture data into a format that allows
    # Python to write the fixture in JSON format to a file
    @staticmethod
    def __writeFixture():
        pythonFixture = Program.roundFixture.serialize() # serialize fixture
        dictFixture = json.loads(pythonFixture) # Convert to python dictionary
        jsonFixture = json.dumps(dictFixture) # convert dictionary to JSON object
        filename = "round" + str(Program.roundFixture.roundNo) + ".txt"
        f = open(filename, "w")
        f.write(jsonFixture) # write JSON fixture object to file
        f.close()
        print("Fixture written to file: " + filename)

    # Display fixture to screen
    @staticmethod
    def __printFixture():
        Program.roundFixture.printFixture()    

    # Add round and match data to Fixture object
    @staticmethod
    def __defineFixture():
        Program.__initFixture()
        print("\nROUND - " + str(Program.roundFixture.roundNo))
        Program.__defineMatches()
        Program.fixtureSet = True

    # Obtain fixture match information
    @staticmethod
    def __defineMatches():
        numMatches = input("Enter number of matches for round " + str(Program.roundFixture.roundNo) + ": ")
        for i in range(0, int(numMatches)):
            print("\nDetails for Match " + str(i+1))
            Program.roundFixture.roundMatches.append(Program.__getMatch())

    # Obtain actual match data from user   
    @staticmethod
    def __getMatch():
        okay = False
        match = Match()
        matchDate = input("Enter date for match (ie. Sat May 12): ")
        match.matchDate = matchDate
        matchTime = input("Enter time for match (hh:mm): ")
        match.matchTime = matchTime + "pm"
        matchVenue = input("Enter venue for match: ")
        match.matchVenue = matchVenue
        Program.__printToFixtureTeams()
        while not okay:
            homeTeamNo = input("Enter home team number for match: ")
            homeTeamNo = int(homeTeamNo)
            if homeTeamNo <= len(Program.toFixtureTeams):
                okay = True
        # Remove selected home team from displayed team list
        homeTeam = Program.toFixtureTeams[homeTeamNo-1]
        Program.toFixtureTeams.pop(homeTeamNo-1)
        match.homeTeam = homeTeam
        Program.__printToFixtureTeams()
        okay = False
        while not okay:
            awayTeamNo = input("Enter away team number for match: ")
            awayTeamNo = int(awayTeamNo)
            if awayTeamNo <= len(Program.toFixtureTeams):
                okay = True
        # Remove selected away team from displayed team list
        awayTeam = Program.toFixtureTeams[awayTeamNo-1]
        Program.toFixtureTeams.pop(awayTeamNo-1)
        match.awayTeam = awayTeam
        return match

    # Initiate Fixture object
    @staticmethod
    def __initFixture():
        Program.roundFixture = Fixture(Program.__getRoundNo())

    # Obtain round number for user
    @staticmethod
    def __getRoundNo():
        okay = False # flag to signal valid user input
        while not okay:
            round = input("Please enter round of fixture (1 to 22): ")
            try:
                round = int(round)
            except:
                print("Invalid input entered. Please provide a number between 1 and 22 (inclusive).")
                continue
            if round >= 1 and round <= 22: # valid input
                okay = True
            else:
                print("Invalid round number entered. Please provide a value from 1 to 22.")    
        return round
    
                

















        
        
        
        
