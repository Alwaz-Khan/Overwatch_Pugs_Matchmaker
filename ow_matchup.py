import random

def open_file():
    """
    takes input the from a text filled called "match.txt" the syntax of input should be: on each line name of player
    followed by space followed by sr
    :return:    Dictionary containing name of players as key and their sr as values.
                List containing only the sr of all the players; all sr having int data type
    """
    dict1 = {}
    sr = []
    with open("matchup.txt", "r") as txt_file:
        for line in txt_file:
            x = line.split()
            dict1[x[0]] = int(x[1])
            sr.append(int(x[1]))
    return dict1, sr


def matchmake_teams(sr):
    """
    takes a list  of sr, selects the 12 highest sr and matches them into equally into a team of 2 having 6 sr each.
    if more than 12 sr are present, it benches the lowest sr guys so they can spectate and get better game sense of
    high sr gameplay. Need to drastically improve the match make algorithm."
    :param sr: list of sr of all players
    :return: 2 list containing list of 6 sr each, basically mathcup of the two teams
    """

    sr.sort(reverse=True)
    qualified_players = [sr[i] for i in range(12)]
    spectators = sr[-(len(sr) - 12):]
    team_1 = [sr[i] for i in (0, 3, 4, 7, 8, 11)]
    team_2 = [sr[i] for i in (1, 2, 5, 6, 9, 10)]
    return team_1, team_2, spectators


def matchmake_teams_2(sr):
    """

    :param sr:
    :return:
    """
    team_a = random.sample(sr,6)
    team_a_sr = sum(team_a)
    sr_1 = [value for value in sr if value not in team_a]
    team_b = random.sample(sr_1,6)
    team_b_sr = sum(team_b)
    spectators = [value for value in sr_1 if value not in team_b]
    teams_sr_difference = abs(team_a_sr - team_b_sr)
    if  teams_sr_difference >= 100:
        team_a, team_b, spectators, teams_sr_difference = matchmake_teams_2(sr)
    else:
        print(abs(team_a_sr - team_b_sr))
    return team_a, team_b, spectators, teams_sr_difference


def display_teams(team_1, team_2, spectators, teams_sr_difference):
    """

    :param dict1: Dictionary containing name of players as key and their sr as values.
    :param team_1: list containing sr of individual players of team 1
    :param team_2: list containing sr of individual players of team 2
    :return: writes a txt file containing the names of 12 individuals; who belongs to group 1 and who belongs to group 2
    """
    with open("teams.txt", "w") as teams:

        teams.write("Teams SR Difference = " + str(teams_sr_difference) + "\n\n")
        teams.write("Team 1\n")
        for given_sr in team_1:
            teams.write(find_player_with_sr(given_sr) + "\n")
        teams.write("\n")

        teams.write("Team 2\n")
        for given_sr in team_2:
            teams.write(find_player_with_sr(given_sr) + "\n")
        teams.write("\n")

        teams.write("Spectators\n")
        for given_sr in spectators:
            teams.write(find_player_with_sr(given_sr) + "\n")


def find_player_with_sr(sr):
    """
    Finds the name of the player based on his sr
    :param sr:integer value, used to find the player whose sr is that
    :return: string,name of the player
    """
    key_list = list(dict1.keys())
    val_list = list(dict1.values())
    player = key_list[val_list.index(sr)]
    return player


if __name__ == '__main__':
    dict1, sr = open_file()
    #team_1, team_2, spectators = matchmake_teams(sr)
    team_1, team_2, spectators, teams_sr_difference = matchmake_teams_2(sr)
    display_teams(team_1, team_2, spectators, teams_sr_difference)

# Next 3
# 1 - improve code to show list of spectators
# 2 - for same 12 members, advice the top 3 combinations with least team diff sr
# 3 - improve algorithm, open and role something

# Improvements
# instead of ommiting the lowest sr guy, cycle players so the extra person can spectate in turns
# team making algo is rudimentary
# instead of making teams based on sr, track output of each match and then suggest best combination for close matches
# also consider the role they would prefer to play
# convert this into online app where people can just join a group based on code and the app does teh rest
# get stats directly from ow page. use some verification and make available unique login id.
# upscale this so that no. of teams can be varied and this can be used for tournaments totally.
