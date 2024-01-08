#!/usr/bin/node

const argsCount = process.argv.length - 2;

console.log(argsCount === 0 ? 'No argument' : argsCount === 1 ? 'Argument found' : 'Arguments found');
