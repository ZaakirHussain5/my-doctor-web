/* eslint-disable no-unused-vars */
// Make a copy of this file and save it as config.js (in the js directory).

// Set this to the base URL of your sample server, such as 'https://your-app-name.herokuapp.com'.
// Do not include the trailing slash. See the README for more information:

var SAMPLE_SERVER_BASE_URL = 'http://localhost:8000';

// OR, if you have not set up a web server that runs the learning-opentok-php code,
// set these values to OpenTok API key, a valid session ID, and a token for the session.
// For test purposes, you can obtain these from https://tokbox.com/account.

var API_KEY = '46964534';
var SESSION_ID = '';
var TOKEN = '';
const urlParams = new URLSearchParams(window.location.search);

$.ajax({
    url: '/api/videoCall?doctor_id='+urlParams.get('doctor_id'),
    method: 'POST',
    contendType: 'application/json',
    'async': false,
    beforeSend: function (xhr) {
        xhr.setRequestHeader("Authorization", "Token " + $.cookie('Token'));
    },
}).done((response)=>{
    console.log(response)
    SESSION_ID = response.session_id
    TOKEN = response.token
})
