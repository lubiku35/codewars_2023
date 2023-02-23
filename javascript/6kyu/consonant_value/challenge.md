# Consonant value

## Challenge Description

Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are
any letters of the alphabet except `"aeiou"`. We shall assign the following values: `a = 1, b = 2, c = 3, .... z = 26`.

For example, for the word "zodiacs", let's cross out the vowels. We get: "z **~~o~~** d **~~ia~~** cs"

```
-- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.
solve("zodiacs") = 26

For the word "strength", solve("strength") = 57
-- The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.

```

For C: do not mutate input.

More examples in test cases. Good luck

## Challenge Solutions

### Solution 01

```jsx
function solve(s) {
    s += "o"
    let cons = [];
    let counts = [];
    let str = ""
    for (let i in s.split('')) {
        if (!["a", "e", "i", "o", "u"].includes(s.split('')[i])) {
            str += s.split('')[i]
        } else {
            cons.push(str)
            str = ""    
            continue
        }
    }
    for (let i in cons) {
        x = cons[i].split('')
        let count = 0
        for (let j in x) { 
            count +=  x[j].charCodeAt(0) - 96 
        }
        counts.push(count)
    }
    return Math.max(...counts) 
    // let count = 0;
    // for (let i in s.split('')) { if (["a", "e", "i", "o", "u"].includes(s.split('')[i])) count +=  s.split('')[i].charCodeAt(0) - 96}
    // return count
};
```

**DESCRIPTION:**