/* eslint-disable no-unused-vars */
// Make a copy of this file and save it as config.js (in the js directory).

// Set this to the base URL of your sample server, such as 'https://your-app-name.herokuapp.com'.
// Do not include the trailing slash. See the README for more information:

const urlParams = new URLSearchParams(window.location.search);


var SAMPLE_SERVER_BASE_URL = 'http://localhost:8000';

// OR, if you have not set up a web server that runs the learning-opentok-php code,
// set these values to OpenTok API key, a valid session ID, and a token for the session.
// For test purposes, you can obtain these from https://tokbox.com/account.

var API_KEY = '46964534';
var TOKEN = '';

var SESSION_ID = urlParams.get('session_id');


$.ajax({
    url: '/api/getDoctorToken?session_id='+SESSION_ID,
    method: 'GET',
    contendType: 'application/json',
    'async': false,
    beforeSend: function (xhr) {
        xhr.setRequestHeader("Authorization", "Token " + $.cookie('Token'));
    },
}).done((response)=>{
    console.log(response)
    TOKEN = response.token
})

