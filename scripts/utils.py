import re
import numpy as np


def roll_dice(roll_string: str, return_steps: bool = False):
    # replaces rolls with random numbers
    parsed_roll_string = roll_string
    roll_string = " ".join(roll_string.split()).strip()
    raw_rolls = re.findall(pattern="[0-9]* *d *[0-9]+", string=roll_string, flags=re.IGNORECASE)
    for roll in raw_rolls:
        multiplier, dice = [int(n) for n in roll.split("d")]
        if not multiplier:
            multiplier = 1
        rolls = np.random.randint(low=1, high=dice+1, size=multiplier)
        parsed_roll = f"({'+'.join([str(n) for n in rolls])})"
        parsed_roll_string = re.sub(pattern=roll, repl=parsed_roll, string=parsed_roll_string, count=1)
    # rolls the dices
    steps = [roll_string, parsed_roll_string, str(eval(parsed_roll_string, {}))]
    if return_steps:
        return steps
    return int(steps[-1])
