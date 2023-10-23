import json


def task() -> float:
    file_name = "input.json"
    with open(file_name) as f:
        data = json.load(f)

    sums = sum([item["score"] * item["weight"] for item in data])
    return round(sums, 3)


print(task())
