def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
        print(f"the total is {total}")
    return total


print(multiply(1, 3, 5))
nums = [33, 44, 55]
print(multiply(*nums))


def add(x, y):
    return x+y


numss = {"x": 15, "y": 25}
print(add(numss["x"], numss["y"]))


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"

# we add * to line 25 and remove it from line 1so as to unpack each argument that will then be passed to the multiply functon
# alternatively we could remove from line 25 and add it to line 1


print(apply(1, 3, 6, 7, operator="*"))


def named(**kwargs):
    print(kwargs)


details = {"name": "Bob", "age": 25}
named(**details)
names = ["James", "Rhys", "Rose"]

it = [f"{name} is the students name" for name in names]
print(it)
