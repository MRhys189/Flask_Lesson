def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")


Students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rhys", "grades": [85, 60]},
    {"name": "James", "grades": [40, 90]}
]

friends = [

    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
]

def get_friend_or_student(friend):
    return friend["name"]

print(search())