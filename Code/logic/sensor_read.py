# emotion.py

# Priority-based emotion scoring system:
#
# | Emotion   | Meaning                    | Score |
# |-----------|----------------------------|-------|
# | freeze    | Critically cold            |   3   |
# | hot       | Critically hot             |   3   |
# | thirsty   | Low soil moisture          |   2   |
# | hydrated  | Very moist soil            |   2   |
# | sleepy    | Low light conditions       |   1   |
# | happy     | Everything is fine         |   1   (default if no issues)
#
# Higher score = higher priority when multiple conditions match.
# This ensures that more critical plant states are prioritized.

def get_current_emotion(temperature, ldr_percent, moisture_percent):
    scores = {
        "freeze": 0,
        "hot": 0,
        "thirsty": 0,
        "hydrated": 0,
        "sleepy": 0,
        "happy": 0,
    }

    if temperature < Temperature_min:
        scores["freeze"] += 3
    elif temperature > Temperature_max:
        scores["hot"] += 3

    if moisture_percent < Moisture_min:
        scores["thirsty"] += 2
    elif moisture_percent > Moisture_max:
        scores["hydrated"] += 2

    if ldr_percent < LDR_Percent_min:
        scores["sleepy"] += 1

    if all(value == 0 for value in scores.values()):
        scores["happy"] = 1

    return max(scores, key=scores.get)