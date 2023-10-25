#!/usr/bin/node
// scrape a page and store in a file

const request = require('request');
const fs = require('fs');
const requestURL = process.argv[2];
const filename = process.argv[3];

request(requestURL, (err, response, body) => {
  if (err) throw err;
  fs.writeFile(filename, body, (err) => {
    if (err) throw err;
  });
});
