#!/usr/bin/node
// computes the number of tasks completed by user_id

const request = require('request');
const requestURL = process.argv[2];

request(requestURL, (err, response, body) => {
  if (err) throw err;
  const dict = JSON.parse(body);
  const newDic = {};
  const entries = Object.entries(dict);
  entries.forEach(entry => {
    if (entry[1].userId in newDic && entry[1].completed === true) {
      newDic[entry[1].userId]++;
    } else if (entry[1].completed === true) {
      newDic[entry[1].userId] = 1;
    }
  });
  console.log(newDic);
});
