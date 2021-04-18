# AFL Fixture Creation Program
# Version 0_1

# Entity class for a round fixture
class Fixture:
    
    # constructor    
    def __init__(self, inRoundNo):
        self.roundNo = inRoundNo
        self.roundMatches = [] # round matches component

    # Display round and matches for a given fixture
    def printFixture(self):
        print("Fixture for ROUND " + str(self.roundNo) + "\n")
        for i in range(0, len(self.roundMatches)):
            print("Match " + str(i+1))
            self.roundMatches[i].printMatch()

    # Provide fixture data in a form that can be
    # converted into JSON format
    def serialize(self):
        result = '{"roundNo": "' + str(self.roundNo) + '", '
        result += '"matches": [ '
        for i in range(0, len(self.roundMatches)):
            result += self.roundMatches[i].serialize()
            if i < len(self.roundMatches)-1:
                result += ','
        result += ' ] }'
        return result
        
# Entity class for an AFL match
class Match:

    # constructor
    def __init__(self):
        self.matchDate = ""
        self.matchTime = ""
        self.matchVenue = ""
        self.homeTeam = ""
        self.awayTeam = ""

    # Display a match's details
    def printMatch(self):
        print("Match date: " + str(self.matchDate))
        print("Match time: " + str(self.matchTime))
        print("Match venue: " + str(self.matchVenue))
        print("Home team: " + self.homeTeam)
        print("Away team: " + self.awayTeam + "\n")

    # Provide match data in a form that can be
    # converted directly into JSON format
    def serialize(self):
        result = ""
        result = '{"matchdate": "' + self.matchDate + '", '
        result += '"matchtime": "' + self.matchTime + '", '
        result += '"matchVenue": "' + self.matchVenue + '", '
        result += '"homeTeam": "' + self.homeTeam + '", '
        result += '"awayTeam": "' + self.awayTeam + '"}'
        return result
    
        
        
        
    
