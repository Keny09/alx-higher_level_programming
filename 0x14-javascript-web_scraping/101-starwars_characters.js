#!/usr/bin/node
// prints all charaters in starwar movie

const request = require('request');
const requestURL = 'https://swapi.co/api/films/' + process.argv[2];

const req = (list, i) => {
  if (i === list.length) return;
  request(list[i], (error, response, data) => {
    if (error) throw error;
    console.log(JSON.parse(data).name);
    req(list, i + 1);
  });
};

request(requestURL, (err, response, body) => {
  if (err) throw err;
  const dict = JSON.parse(body);
  req(dict.characters, 0);
});
