

class Emotion:
    """
    Emotion class to determine the current emotion of the plant based on environmental conditions.
    The class uses a scoring system to prioritize emotions based on temperature, light intensity, and moisture levels.
    The emotions are:
    - freeze: Critically cold
    - hot: Critically hot
    - thirsty: Low soil moisture
    - hydrated: Very moist soil
    - sleepy: Low light conditions
    - happy: Everything is fine (default if no issues)
    """

    def __init__(self, cfg):
        """ Initialize the Emotion class with configuration parameters.
        Args:
            cfg (dict): Configuration parameters for the emotion class.
        """
        # min max values
        self.LDR_Percent_min = int(cfg['Light Intensity min'])#20
        self.LDR_Percent_max = int(cfg['Light Intensity max'])#20
        self.Temperature_min = int(cfg['Temperature min'])#22
        self.Temperature_max = int(cfg['Temperature max'])#30
        self.Moisture_min = int(cfg['Moisture min'])#10
        self.Moisture_max = int(cfg['Moisture max'])#90
        return
    
    def get_current_emotion(self, temperature, ldr_percent, moisture_percent):
        """Determine the current emotion based on temperature, light intensity, and moisture level.
        Args:
            temperature (float): The current temperature.
            ldr_percent (float): The current light intensity as a percentage.
            moisture_percent (float): The current moisture level as a percentage.
        Returns:
            str: The current emotion of the plant.
        """
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
        scores = {
            "freeze": 0,
            "hot": 0,
            "thirsty": 0,
            "hydrated": 0,
            "sleepy": 0,
            "happy": 0,
        }
        # Check conditions and assign scores
        if temperature < self.Temperature_min:
            scores["freeze"] += 3
        elif temperature > self.Temperature_max:
            scores["hot"] += 3

        if moisture_percent < self.Moisture_min:
            scores["thirsty"] += 2
        elif moisture_percent > self.Moisture_max:
            scores["hydrated"] += 2

        if ldr_percent < self.LDR_Percent_min:
            scores["sleepy"] += 1

        if all(value == 0 for value in scores.values()):
            scores["happy"] = 1  # Standard

        # Determine the emotion with the highest score
        emotion = max(scores, key=scores.get)
        return emotion