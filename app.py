import constants

class Player:
    # Cleans the information of the player and assign it 
    def __init__(self, plyr):
        self.name = plyr["name"]
        self.guardians = plyr["guardians"].split(" and ")
        self.experience = True if plyr["experience"] == "YES" else False
        self.height = int(plyr["height"][: 2])

    def __str__(self):
        return self.name


class Team:
    experienced = 0
    inexperienced = 0
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.height_average = sum([plyr.height for plyr in self.players]) / len(self.players)
        self.experienced += sum([1 for plyr in self.players if plyr.experience])
        self.inexperienced += sum([1 for plyr in self.players if not plyr.experience])
        self.guardians = ", ".join([guard for plyr in self.players for guard in plyr.guardians])

    # Here is defined how the stats will be displayed
    def __str__(self):
        return """
        
Team {} stats
-------------------

Total Players: {}
Experienced Players: {}
Inexperienced Players: {}
Average height: {}

List of players:
{}

List of guardians:
{}
-------------------
        """.format(
            self.name,
            len(self.players),
            self.experienced,
            self.inexperienced,
            self.height_average,
            ", ".join([str(plyr) for plyr in self.players]),
            self.guardians)


def balance_teams(teams, players):
    #Creates the Player object and adds it to a list
    list_of_players = [Player(plyr) for plyr in players]
    experienced_players = []
    inexperienced_players = []
    team_players = []

    #Divides the players by experience
    for player in list_of_players:
        if player.experience:
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)
    
    #Distributes evenly the inexperienced and experienced players
    for i in range(0, len(experienced_players) - 1, len(teams)):
        team_players.append(Team(teams[int(i / len(teams))],
        experienced_players[i: i + int(len(experienced_players) / len(teams))] +
        inexperienced_players[i: i + int(len(inexperienced_players) / len(teams))]))
        
    return team_players


if __name__ == "__main__":
    app_running = True
    teams = balance_teams(constants.TEAMS, constants.PLAYERS)
    while app_running:
        print("""
**** MENU ****

Here are your choises:
1) Display Team Stats
2) Quit

        """)
        command = input("Please choose an option: ")
        if command == "1":
            print("""
Show The Stats
--------------------

1) Panthers
2) Bandits
3) Warriors

            """)
            team_name = input("Please choose an option (1, 2 or 3): ")
            try:
                print(teams[int(team_name) - 1])
                input("Press enter to continue...")
            except (ValueError, IndexError) as err:
                print("{}. Please choose again.".format(err))
                input("Press Enter to continue... ")

        elif command == "2":
            app_running = False
        else:
            print("You choosed {}, please choosed an availible option. ".format(command))
            input("Press Enter to continue... ")