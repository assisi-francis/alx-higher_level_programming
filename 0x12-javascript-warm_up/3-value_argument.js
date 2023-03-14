#!/usr/bin/node
const argsCount = process.argv;
let length = 0;
while (argsCount[length] !== undefined) {
  length++;
}
if (length === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
