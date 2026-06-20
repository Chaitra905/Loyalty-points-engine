import json
import os


# Get backend folder path
BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)


# Location of rules.json
RULE_FILE = os.path.join(
    BASE_DIR,
    "rules.json"
)



def load_rules():

    with open(RULE_FILE) as file:

        return json.load(file)




def calculate_points(event_type, amount):

    rules = load_rules()


    rule = rules.get(event_type)


    # Unknown event type
    if not rule:

        return 0



    # Base points
    points = rule["base_points"]



    # Apply multiplier / bonus
    points = points * rule.get(
        "multiplier",
        1
    )



    # Apply maximum cap
    points = min(
        points,
        rule["cap"]
    )


    return points