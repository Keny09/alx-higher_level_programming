#!/usr/bin/node
// prints all charaters in starwar movie

const request = require('request');
const requestURL = 'https://swapi.co/api/films/' + process.argv[2];

request(requestURL, (err, response, body) => {
  if (err) throw err;
  const dict = JSON.parse(body);
  const characters = dict.characters;
  characters.forEach(character => {
    request(character, (error, response, data) => {
      if (error) throw error;
      console.log(JSON.parse(data).name);
    });
  });
});
