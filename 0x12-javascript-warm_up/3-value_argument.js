#!/usr/bin/node
const argsCount = process.argv.length - 2;

if (argsCount === 0) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
