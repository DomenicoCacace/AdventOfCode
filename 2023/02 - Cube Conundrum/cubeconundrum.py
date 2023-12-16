def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    print(f"Solution (part 1): {part1(lines)}")
    print(f"Solution (part 2): {part2(lines)}")
    

def part1(lines):
    games = parseLines(lines)
    retval = 0
    for game in games:
        retval += isGameValid(game)

    return retval

def part2(lines):
    games = parseLines(lines)
    retval = 0

    for game in games:
        r = 0
        g = 0
        b = 0
        
        for rnd in game.gameRounds:
            r = max(r, rnd.red)
            g = max(g, rnd.green)
            b = max(b, rnd.blue)
        
        retval += r*g*b
    
    return retval


def parseLines(lines):
    games = []
    for line in lines:
        gameId, rounds = line.strip().split(': ')
        gameId = int(gameId[len("Game "):])
        game = Game(gameId)
        rounds = rounds.split('; ')

        for rnd in rounds:
            r, g, b = parseRound(rnd)
            game.addRound(GameRound(r, g, b))
        games.append(game)

    return games

def parseRound(roundLine):
    cubes = {"red":0, "green":0, "blue":0}
    
    extraction = roundLine.split(', ')
    for x in extraction:
        amount, color = x.split(' ')
        cubes[color] = int(amount) 

    return cubes["red"], cubes["green"], cubes["blue"]

def isGameValid(game):
    for round in game.gameRounds:
        if not round.isValid():
            return 0

    return game.id

class Game:
    def __init__(self, id):
        self.id = id
        self.gameRounds = []
    
    def addRound(self, round):
        self.gameRounds.append(round)

class GameRound:
    MAXRED = 12
    MAXGREEN = 13
    MAXBLUE = 14

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def isValid(self):
        return self.red <= GameRound.MAXRED and self.green <= GameRound.MAXGREEN and self.blue <= GameRound.MAXBLUE

if __name__ == "__main__":
    main()