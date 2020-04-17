import sys
movies_watched = {"The Matrix", "Avatar", "Her"}
movie_a_watched = "The Matrix"

if movie_a_watched in movies_watched:
    print(f"{movie_a_watched} is a great classic")
else:
    print(f"{movie_a_watched} is not on the list")

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = []
start_s = []
start_s = starts_s  # makes the 2 lists equal

for friend in friends:
    if friend.startswith("S"):
        start_s.append(friend)
print(start_s)

starts_s = [friend for friend in friends if friend.startswith("S")]
print(starts_s)

my_string = 'hello world'
e = []
for i in my_string:
    print(i)
    e.append(i)
print(e)

print([[i+j for i in 'abc'] for j in 'def'])

for j in 'def':
    for i in "abc":
        print(i+j)

l = [1, 2, 3, 4, 5]
g = [1, 2, 3, 4, 6]
print([x & 1 for x in l])
print(2 & 1)
for i in zip(l, g):
    print(i)

student_attendance = {"Rolf": 25, "James": 95, "Rhys": 100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}% ")

print(student_attendance["Rolf"])
student_attendance.items()
print(student_attendance.items())

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")  # better than line 44-45

for t in student_attendance.items():
    print(t)  # better than line 44-45
y = 2, 3, 4
x = tuple(y)
print(x)

person = ("Bob,", 42, "Mechanic")
name, _, profession = person

print(name, person)

# collecting
head, *tail = [1, 2, 3, 4, 5]
print(tail)


def hello():
    print("Hello")


hello()


# def user_age_in_seconds():
#     user_age = int(input("Enter your age: "))
#     age_seconds = user_age * 365 * 24 * 60 * 60
#     print(f"Your age in seconds is {age_seconds}")


# user_age_in_seconds()


def add(x, y): return x + y


print(add(5, 7))


def double(x):
    return x*2


sequence = [1, 2, 3, 4, 5]
doubled = [double(x) for x in sequence]
doubled_map = map(double, sequence)
print(doubled_map)
doubled_map2 = []
for dd in doubled_map:
    doubled_map2.append(dd)

print(doubled_map2)
doubled3 = [lambda x: map(double(x), sequence)]
print(doubled3)

double_t = []
for ddd in doubled3:
    double_t.append(ddd)
print(double_t)


users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234"),
]

username_mapping = {user[1]: user for user in users}
print(username_mapping["Bob"])
# # username_input = input("Enter your username: ")
# # password_input = input("Enter your password: ")
# _, username, password = username_mapping[username_input]

# if password_input == password:
#     print("Your details are correct")
# else:
#     print("Your details are incorrect")
# enumerate(username_mapping, 1)

names = [
    (0, "Rhys", "wakawaka"),
    (1, "James", "coolkid234"),
    (2, "Chirau", "12345")
]
print(names)

obj1 = enumerate(names)
print(sys.path)


