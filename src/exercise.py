import csv

def main():
    #write your code below this line
    filename = input("File:")
    games = []

    with open(filename) as f:
        data = csv.reader(f)
    
        for row in data:
            games.append([row[0], row[1], row[2], row[3]])

    team = input("Team:")
    count = 0
    wins = 0
    losses = 0

    for game in games:
        if game[0] == team or game[1] == team:
            count += 1
            if winner(game) == team:
                wins += 1
            else:
                losses += 1
        

    print("Games: " + str(count))
    print("Wins: " + str(wins))
    print("Losses: " + str(losses))

def winner(game):
    if int(game[2]) > int(game[3]):
        return game[0]
    else:
        return game[1]

if __name__ == '__main__':
    main()
