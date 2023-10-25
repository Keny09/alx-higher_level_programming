#!/usr/bin/node
// a script writes a string to file

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], function (error) {
  if (error) {
    console.error(error);
  }
});
