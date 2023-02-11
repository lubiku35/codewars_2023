# Return The Day

## Challenge Description

Complete the function which returns the weekday according to the input number:

- `1` returns `"Sunday"`
- `2` returns `"Monday"`
- `3` returns `"Tuesday"`
- `4` returns `"Wednesday"`
- `5` returns `"Thursday"`
- `6` returns `"Friday"`
- `7` returns `"Saturday"`
- Otherwise returns `"Wrong, please enter a number between 1 and 7"`

## Challenge Solutions

### Solution 01

```python
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
```

### Solution 02

```python
def whatday(num):
    arr = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return arr[num - 1] if num <= 7 else 'Wrong, please enter a number between 1 and 7'
```

### Solution 03

```python
def whatday(num):
    if num == 2: return "Monday"
    elif num == 3: return "Tuesday"
    elif num == 4: return "Wednesday"
    elif num == 5: return "Thursday"
    elif num == 6: return "Friday"
    elif num == 7: return "Saturday"
    elif num == 1: return "Sunday"
    else: return 'Wrong, please enter a number between 1 and 7'
```

**DESCRIPTION** 

Also testing cases included 