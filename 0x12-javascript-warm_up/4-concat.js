#!/usr/bin/node
const argsCount = process.argv;
let length = 0;
while (argsCount[length] !== undefined) {
  length++;
}
if (length === 2) {
  console.log(`undefined is undefined`);
} else if (length === 3) {
  console.log(`${argsCount[2]} is undefined`);
} else {
  console.log(`${argsCount[2]} is ${argsCount[3]}`);
}
