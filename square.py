class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""
        
    def choose(self):
        valid_choices = ["rock", "paper", "scissor"]
        while True:
            self.choice = input(f"{self.name}, select rock, paper, or scissor: ").lower()
            if self.choice in valid_choices:
                break
            print("Invalid choice, please try again.")
        print(f"{self.name} selects {self.choice}")

    def toNumericalChoice(self):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissor": 2
        }
        return switcher[self.choice]

    def incrementPoint(self):
        self.points += 1


class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1],  # rock vs. rock, paper, scissor
            [1, 0, -1],  # paper vs. rock, paper, scissor
            [-1, 1, 0]   # scissor vs. rock, paper, scissor
        ]
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)
        print(f"Round resulted in a {self.getResultAsString(result)}.")
        if result > 0:
            p1.incrementPoint()
            print(f"{p1.name} earns a point!")
        elif result < 0:
            p2.incrementPoint()
            print(f"{p2.name} earns a point!")
        else:
            print("No points for anybody.")

    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]

    def getResultAsString(self, result):
        res = {
            0: "draw",
            1: "win",
            -1: "loss"
        }
        return res[result]


class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant("Spock")
        self.secondParticipant = Participant("Kirk")

    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()

    def checkEndCondition(self):
        answer = input("Continue game y/n: ")
        if answer.lower() == 'y':
            return
        else:
            print(f"Game ended, {self.participant.name} has {self.participant.points}, "
                  f"and {self.secondParticipant.name} has {self.secondParticipant.points}.")
            self.determineWinner()
            self.endGame = True

    def determineWinner(self):
        if self.participant.points > self.secondParticipant.points:
            resultString = f"Winner is {self.participant.name}"
        elif self.participant.points < self.secondParticipant.points:
            resultString = f"Winner is {self.secondParticipant.name}"
        else:
            resultString = "It's a Draw"
        print(resultString)


# Start the game
game = Game()
game.start()
