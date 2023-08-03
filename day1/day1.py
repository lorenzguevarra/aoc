# /usr/bin/env python

from typing import List

INPUT_FILE = "input.txt"

if __name__ == "__main__":
    max_calories = 0
    all_calories: List[int] = []

    with open(INPUT_FILE) as f:
        calories: List[int] = []
        for line in f:
            line = line.strip()
            if len(line) == 0:
                calory_count = sum(calories)
                all_calories.append(calory_count)
                max_calories = max(max_calories, calory_count)
                calories.clear()
            else:
                calories.append(int(line))

        # Include the last collected calories
        if len(calories) > 0:
            calory_count = sum(calories)
            all_calories.append(calory_count)
            max_calories = max(max_calories, calory_count)

    print(f"max         = {max_calories}")
    top3_count = sum(sorted(all_calories, reverse=True)[:3])
    print(f"top 3 count = {top3_count}")
