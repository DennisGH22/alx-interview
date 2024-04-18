#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];

function fetchCharacters (filmId) {
  return new Promise((resolve) => {
    request(`https://swapi-api.alx-tools.com/api/films/${filmId}`, (body) => {
      const film = JSON.parse(body);
      resolve(film.characters);
    });
  });
}

function fetchCharacterName (characterUrl) {
  return new Promise((resolve) => {
    request(characterUrl, (body) => {
      const character = JSON.parse(body);
      resolve(character.name);
    });
  });
}

async function starwarsCharacters (filmId) {
  const characters = await fetchCharacters(filmId);
  for (const characterUrl of characters) {
    const name = await fetchCharacterName(characterUrl);
    console.log(name);
  }
}

starwarsCharacters(filmId);
