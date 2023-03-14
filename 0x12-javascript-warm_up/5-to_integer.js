const arg = process.argv[2];

if (/^-?\d+\.?\d*$/.test(arg)) {
  console.log(`My number: ${parseInt(Number(arg))}`);
} else {
  console.log('Not a number');
}
