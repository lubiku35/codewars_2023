function pickIt(arr){
    let odd=[], even=[];
    for (const key in arr) { arr[key] % 2 === 0 ? even.push(arr[key]) : odd.push(arr[key]) }
    return [odd,even];
}