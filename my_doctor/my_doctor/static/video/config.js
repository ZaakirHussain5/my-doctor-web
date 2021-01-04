/* eslint-disable no-unused-vars */
// Make a copy of this file and save it as config.js (in the js directory).

// Set this to the base URL of your sample server, such as 'https://your-app-name.herokuapp.com'.
// Do not include the trailing slash. See the README for more information:


// OR, if you have not set up a web server that runs the learning-opentok-php code,
// set these values to OpenTok API key, a valid session ID, and a token for the session.
// For test purposes, you can obtain these from https://tokbox.com/account.
const urlParams = new URLSearchParams(window.location.search);
var API_KEY = '47034434';
var SESSION_ID = urlParams.get('session_id');
var TOKEN = urlParams.get('session_token');

