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
    # Constant list of all AFL teams
    teamsList = ["Adelaide", "Brisbane", "Carlton", "Collingwood",
                      "Essendon", "Freemantle", "Geelong", "Gold Coast",
                      "Greater Western Sydney", "Hawthorn", "Melbourne",
                      "North Melbourne", "Port Adelaide", "Richmond",
                     "St. Kilda", "Sydney", "West Coast", "Western Bulldogs" ]
    toFixtureTeams = teamsList # Assign teams list to utility variable
    
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
        prompt = "Enter number of matches for round " + str(Program.roundFixture.roundNo) + ": "
        start = 1
        end = 9
        numMatches = Program.__getNumericRangedInput(prompt, start, end)
        for i in range(0, numMatches):
            print("\nDetails for Match " + str(i+1))
            Program.roundFixture.roundMatches.append(Program.__getMatch())

    # Obtain actual match data from user   
    @staticmethod
    def __getMatch():
        match = Match()
        match.matchDate = input("Enter date for match (ie. Sat May 12): ")
        match.matchTime = input("Enter time for match (hh:mm): ") + "pm"
        match.matchVenue = input("Enter venue for match: ")
        match.homeTeam = Program.__getTeam("home")
        match.awayTeam = Program.__getTeam("away")
        return match

    # Obtain home/away team for a match from user
    @staticmethod
    def __getTeam(teamType):
        okay = False
        Program.__printToFixtureTeams()
        while not okay:
            teamNo = input("Enter " + teamType + " team number for match: ")
            if teamNo == "" or not teamNo.isnumeric():
                continue
            teamNo = int(teamNo)
            if teamNo <= len(Program.toFixtureTeams):
                okay = True
        # Remove selected team from displayed team list
        team = Program.toFixtureTeams[teamNo-1]
        Program.toFixtureTeams.pop(teamNo-1)
        return team        

    # Initiate Fixture object
    @staticmethod
    def __initFixture():
        Program.roundFixture = Fixture(Program.__getRoundNo())

    # Obtain round number from user
    @staticmethod
    def __getRoundNo():
        prompt = "Please enter round of fixture (1 to 22): "
        start = 1
        end = 22
        result = Program.__getNumericRangedInput(prompt, start, end)
        return result

    # Utility method to obtain a numeric value from the user within a given range
    @staticmethod
    def __getNumericRangedInput(inPrompt, inStart, inEnd):
        okay = False # flag to signal valid user input
        while not okay:
            result = input(inPrompt)
            try:
                result = int(result)
            except:
                print("Invalid input entered. Please provide a number between " + str(inStart) + " and " + str(inEnd) + " (inclusive).")
                continue
            if result >= inStart and result <= inEnd: # valid input
                okay = True
            else:
                print("Invalid number entered. Please provide a value from " + str(inStart) + " to " + str(inEnd) + ".")    
        return result  
    
    
                

















        
        
        
        
