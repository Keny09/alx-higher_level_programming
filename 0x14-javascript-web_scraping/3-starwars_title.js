#!/usr/bin/node
// prints the starwar movie title by id

const request = require('request');
const requestURL = 'http://swapi.co/api/films/' + process.argv[2];

request(requestURL, (err, response, body) => {
  if (err) throw err;
  const dict = JSON.parse(body);
  console.log(dict.title);
});
