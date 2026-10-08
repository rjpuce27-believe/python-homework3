def distribute_tickets(total_tickets, players, volunteers):
    if len(players) == 0:
        return "Tickets cannot be distributed."

    number_of_players = len(players)

    base = total_tickets // number_of_players
    remainder = total_tickets % number_of_players

    tickets={}

    for player in players:
        tickets[player]= base

    extra_players = []

    # Give extra tickets to volunteers first
    for player in volunteers:
        if len(extra_players) < remainder:
            extra_players.append(player)

    # Give any remaining extra tickets in batting order
    for player in players:
        if len(extra_players) < remainder:
            if player not in extra_players:
                extra_players.append(player)

    # Add one extra ticket to the selected players
    for player in extra_players:
        tickets[player] += 1

    return tickets

print(distribute_tickets(
    64,
    ["Alex", "Ben", "Chris", "Dylan", "Evan", "Frank"],
    ["Dylan", "Ben"]))

print(distribute_tickets(
    60,
    ["Sam", "Tyler", "Will"],
    []))

print(distribute_tickets(
    52,
    ["Aiden", "Brady", "Connor", "Jack", "Luke"],
    ["Connor", "Aiden", "Luke"]))