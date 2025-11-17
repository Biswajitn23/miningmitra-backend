from typing import Union


Number = Union[int, float]


def calculate_safety_score(temperature: Number, vibration: Number) -> float:
    """
    Calculate the safety score based on temperature and vibration readings.

    Formula: 100 - (temperature * 0.3 + vibration * 1.5)
    """
    deduction = float(temperature) * 0.3 + float(vibration) * 1.5
    return 100 - deduction
