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

console.log(solve("zodiac"));