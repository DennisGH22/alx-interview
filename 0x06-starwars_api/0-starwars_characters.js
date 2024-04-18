#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const filmID = process.argv[2];

async function starwarsCharacters (filmId) {
  try {
    const filmResponse = await request(`https://swapi-api.alx-tools.com/api/films/${filmId}`);
    const { characters } = JSON.parse(filmResponse.body);

    for (const characterUrl of characters) {
      const characterResponse = await request(characterUrl);
      const { name } = JSON.parse(characterResponse.body);
      console.log(name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

starwarsCharacters(filmID);
