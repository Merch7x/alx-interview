#!/usr/bin/node
const request = require('request');

// Get the Movie ID from the first positional argument
const movieId = process.argv[2];

// Check if movieId is provided
if (!movieId) {
  console.log('Please provide a Movie ID.');
  process.exit(1); // Exit the script
}

// Star Wars API endpoint for films
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a request to the Star Wars API to get the movie details
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the response body to JSON
  const movieData = JSON.parse(body);

  // Check if movie data is valid
  if (!movieData || !movieData.characters) {
    console.log('Invalid Movie ID or no characters found.');
    return;
  }

  // Get the list of character URLs
  const characters = movieData.characters;

  // For each character URL, make a request to get the character details
  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }

      // Parse the character data
      const characterData = JSON.parse(charBody);
      console.log(characterData.name); // Print the character's name
    });
  });
});
