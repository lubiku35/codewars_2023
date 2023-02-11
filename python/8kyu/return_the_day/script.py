import timeit

def whatday(num):
    days = {
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
        1: "Sunday",
    }
    return days.get(num) if num in days.keys() else 'Wrong, please enter a number between 1 and 7'

def whatday2(num):
    arr = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return arr[num - 1] if num <= 7 else 'Wrong, please enter a number between 1 and 7'

def whatday3(num):
    if num == 2: return "Monday"
    elif num == 3: return "Tuesday"
    elif num == 4: return "Wednesday"
    elif num == 5: return "Thursday"
    elif num == 6: return "Friday"
    elif num == 7: return "Saturday"
    elif num == 1: return "Sunday"
    else: return 'Wrong, please enter a number between 1 and 7'

print(whatday(5))
print(whatday2(5))
print(whatday3(5))

# Effectivity Tests

x = timeit.timeit(lambda: whatday(5), number=1000)
y = timeit.timeit(lambda: whatday2(5), number=1000)
z = timeit.timeit(lambda: whatday3(5), number=1000)

print(x)
print(y)
print(z) 

print(min(x, y, z))