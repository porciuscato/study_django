const adder = function(x, y) {
    return x + y
}

const cal = {
    add: (x, y) => { return x + y },
    sub: (x, y) => { return x - y },
}
console.log(cal.add(1, 2))

const document = {
    title: 'New Tab',
    querySelector: function(){},
}