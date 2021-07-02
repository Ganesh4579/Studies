var s = new Set([1, 2, 3, 4, 1]);
console.log(s);
s.add(2);
s.add(8);
console.log(s.has(8));
console.log(s.values());
console.log(s.entries());
