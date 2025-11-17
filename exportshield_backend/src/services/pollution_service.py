from typing import Union


Number = Union[int, float]


def calculate_pollution_index(depth: Number, explosives: Number) -> float:
    """
    Calculate the pollution index based on drilling depth and explosives used.

    Formula: depth * 0.5 + explosives * 2
    """
    return float(depth) * 0.5 + float(explosives) * 2
