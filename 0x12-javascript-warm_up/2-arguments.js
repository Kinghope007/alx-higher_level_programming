#!/usr/bin/node
const argc = process.argv.length;

if (argc > 2) {
	console.log('Argument' + (argv > 3 ? 's' : '') + ' found');
} else {
	console.log('No argument');
}
