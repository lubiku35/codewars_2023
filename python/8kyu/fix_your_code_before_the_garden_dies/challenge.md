# Fix your code before the garden dies!

## Challenge Description

You have an award-winning garden and every day the plants need exactly 40mm of water. You created a great piece of JavaScript to calculate the amount of water your plants will need when you have taken into consideration the amount of rain water that is forecast for the day. Your jealous neighbour hacked your computer and filled your code with bugs.

Your task is to debug the code before your plants die!

## Challenge Solutions

### Solution 01

```python
def rain_amount(mm):
    return "Your plant has had more than enough water for today!" if mm >= 40 else f"You need to give your plant {40 - mm}mm of water"
```

asd