# Super Duper Easy

## Challenge Description

Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".

## Challenge Solutions

### Solution 01

```jsx
function problem(x) {
    if (typeof x === "string") {
      return "Error"
    } else {
      return x * 50 + 6
    }
}
```

**DESCRIPTION:**

usage of typeof