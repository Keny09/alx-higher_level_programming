#!/usr/bin/node
// a script reads and prints the content of a file

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (error, data) {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
