import random
import string
from typing import List


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_from_lines_list() -> List[str]:
    lines_list = [
        "bakerloo",
        "central",
        "circle",
        "district",
        "hammersmith-city",
        "jubilee",
        "metropolitan",
        "northern",
        "piccadilly",
        "victoria",
        "waterloo-city",
    ]
    return random.sample(lines_list, random.randint(1, 3))
