#!/usr/bin/node
// a script that display the status code of a GET request

const request = require('request');

request.get(process.argv[2], (error, response) => {
  if (error) {
    throw error;
  } else {
    console.log('code:', response.statusCode);
  }
});
