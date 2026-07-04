from collections import defaultdict, Counter


def get_team_passes(events, team_name):

    passes = []

    for event in events:

        if event["type"]["name"] != "Pass":
            continue

        if event["team"]["name"] != team_name:
            continue

        if "recipient" not in event["pass"]:
            continue

        passes.append(event)

    return passes


def count_pass_pairs(passes):

    counter = Counter()

    for event in passes:

        passer = event["player"]["name"]
        receiver = event["pass"]["recipient"]["name"]

        counter[(passer, receiver)] += 1

    return counter

def get_average_positions(team_passes):
    """
    Calculate each player's average pass starting location.

    Returns:
        dict:
            {
                player_name: (average_x, average_y)
            }
    """

    positions = defaultdict(list)

    for event in team_passes:

        player = event["player"]["name"]

        x, y = event["location"]

        positions[player].append((x, y))

    average_positions = {}

    for player, coords in positions.items():

        avg_x = sum(x for x, _ in coords) / len(coords)
        avg_y = sum(y for _, y in coords) / len(coords)

        average_positions[player] = (avg_x, avg_y)

    return average_positions