function padIt(str,n){
    let counter = 0;
    let pad = "*";
    while (counter !== n) {
        counter % 2 == 0 ? str = pad + str : str = str + pad;
        counter += 1;
    };
    return str;
}