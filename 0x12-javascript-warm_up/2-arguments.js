#!/usr/bin/node
const { argv } = require('node:process');
process.argv
{
	if (argv.length <= 2)
	{
		console.log('No argument');
	}
	if (argv.length > 2)
	{
		console.log('Arguments found');
	}
};
