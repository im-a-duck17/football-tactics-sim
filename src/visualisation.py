from mplsoccer import Pitch
import matplotlib.pyplot as plt
from utils import short_name


def draw_passing_network(pass_pairs, average_positions, min_passes=3):

    pitch = Pitch(
        pitch_type="statsbomb",
        pitch_color="#2E8B57",      # Green pitch
        line_color="white",
        linewidth=2
    )

    fig, ax = pitch.draw(figsize=(14, 10))

    ############################################
    # Draw Passes
    ############################################

    for (passer, receiver), count in pass_pairs.items():

        if count < min_passes:
            continue

        if passer not in average_positions:
            continue

        if receiver not in average_positions:
            continue

        x1, y1 = average_positions[passer]
        x2, y2 = average_positions[receiver]

        pitch.arrows(
            x1,
            y1,
            x2,
            y2,
            ax=ax,
            width=1.2,
            headwidth=4,
            headlength=5,
            color="white",
            alpha=min(0.25 + count / 20, 0.9)
        )

    ############################################
    # Draw Players
    ############################################

    for player, (x, y) in average_positions.items():

        pitch.scatter(
            x,
            y,
            s=900,
            color="#6CABDD",          # Manchester City blue
            edgecolors="white",
            linewidth=2,
            ax=ax,
            zorder=5
        )

        surname = short_name(player)

        ax.text(
            x,
            y,
            surname,
            color="white",
            fontsize=9,
            ha="center",
            va="center",
            fontweight="bold",
            zorder=6
        )

    plt.title(
        "Manchester City Passing Network vs Arsenal (2015/16)",
        fontsize=18,
        color="white",
        pad=20
    )

    plt.show()