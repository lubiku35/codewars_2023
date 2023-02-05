# Printing Array elements with Comma delimiters

## Challenge Description

Input: Array of elements

["h","o","l","a"]

Output: String with comma delimited elements of the array in th same order.

"h,o,l,a"

Note: if this seems too simple for you try [the next level](https://www.codewars.com/kata/5711d95f159cde99e0000249)

## Challenge Solutions

### Solution 01

```jsx
function printArray(array){
  return array.join(",")
}
```

**DESCRIPTION:**

usage of join