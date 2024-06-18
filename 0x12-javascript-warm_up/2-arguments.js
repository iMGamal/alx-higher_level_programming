#!/usr/bin/node
const { argv } = require('node:process');
argv.forEach((argument) =>
	{
		if (argv === argv[0])
		{
			console.log('No arguments');
		}
		else
		{
			console.log('Arguments found');
		}
	});
