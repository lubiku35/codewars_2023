function grabDoll(dolls){
    let skip;
    var bag=[];
    for (const key in dolls) {
        if (dolls[key] === "Hello Kitty" || dolls[key] === "Barbie doll") {
            bag.push(dolls[key])
        } else {
            continue
        }
        if (bag.length === 3) { break }
    } 
    return bag;
}