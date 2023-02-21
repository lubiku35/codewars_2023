function animal(obj){
    let x = Object.values(obj)
    return `This ${x[2]} ${x[0]} has ${x[1]} legs.`
}

function animal(obj){
    return `This ${obj.color} ${obj.name} has ${obj.legs} legs.`
}

const x = {name:"dog",legs:4,color:"white"}