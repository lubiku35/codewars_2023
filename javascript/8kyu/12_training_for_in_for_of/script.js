function giveMeFive(obj){
    let out = []
    for (let key in obj) {
        if (key.length === 5) out.push(key) ;
        if (obj[key].length === 5) out.push(obj[key]) ;
    }
    return out
}
giveMeFive({Our:"earth",is:"a",beautyful:"world"})