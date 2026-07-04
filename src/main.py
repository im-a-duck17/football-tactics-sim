from loader import load_match
from analytics import get_team_passes
from analytics import get_average_positions
from analytics import count_pass_pairs
from visualisation import draw_passing_network

MATCH_ID = 3754314

events = load_match(MATCH_ID)

city_passes = get_team_passes(
    events,
    "Manchester City"
)

pass_pairs = count_pass_pairs(city_passes)
average_positions = get_average_positions(city_passes)

print(average_positions)

draw_passing_network(pass_pairs, average_positions)