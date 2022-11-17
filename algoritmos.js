function factorial(num) {
    var numeroFactorial = 1;
    for(var i=1; i <= num; i++){
        numeroFactorial *= i;
    }
    return numeroFactorial;
}

console.log(factorial(3));