/* global OT API_KEY TOKEN SESSION_ID SAMPLE_SERVER_BASE_URL */
//const urlParams = new URLSearchParams(window.location.search);
var apiKey = "46964534";
var sessionId;
var token;
var publisher = null

function handleError(error) {
  if (error) {
    console.error(error);
  }
}
var video_session;

function initializeSession() {
  video_session = OT.initSession(apiKey, sessionId);

  // Subscribe to a newly created stream
  video_session.on('streamCreated', function streamCreated(event) {
    var subscriberOptions = {
      insertMode: 'append',
      width: '100%',
      height: '100%'
    };
    video_session.subscribe(event.stream, 'subscriber', subscriberOptions, handleError);
  });

  video_session.on('sessionDisconnected', function sessionDisconnected(event) {
    console.log('You were disconnected from the session.', event.reason);
  });

  // initialize the publisher
  var publisherOptions = {
    insertMode: 'append',
    width: '100%',
    height: '100%'
  };
  publisher = OT.initPublisher('publisher', publisherOptions, handleError);

  // Connect to the session
  video_session.connect(token, function callback(error) {
    if (error) {
      handleError(error);
    } else {
      // If the connection is successful, publish the publisher to the session
      video_session.publish(publisher, handleError);
    }
  });
  
  video_session.on('signal:msg', function signalCallback(event) {
    serializedMessage(event.data, event.from.connectionId === session.connection.connectionId ? 'self' : 'other')
  });
}


function serializedMessage(message, messageOf) {
  let lis = '';
  var messagesContainer = $('.messages');
  let li = `<li class="${messageOf}">${message}</li>`;
  $('#messagess').append(lis);
  messagesContainer.finish().animate({
      scrollTop: messagesContainer.prop("scrollHeight")
  }, 250);
}

function sendNewMessage() {
  sendMessageAjax(newMessage);
}

function sendMessageAjax(message) {
  video_session.signal({
      type: 'msg',
      data: message
  }, function signalCallback(error) {
      if (error) {
          console.error('Error sending signal:', error.name, error.message);
      } else {
          msgTxt.value = '';
      }
  });
}

function onMetaAndEnter(event) {
  if ((event.metaKey || event.ctrlKey) && event.keyCode == 13) {
      sendNewMessage();
  }
}

$('#micBtn').click(function(){
  var isConnected = $(this).attr('data-connected')
  if(isConnected == 'true'){
    $(this).attr('data-connected','false')
    $(this).removeClass('btn-outline-danger')
    $(this).addClass('btn-danger')
    publisher.publishAudio(false)
  }
  else{
    $(this).attr('data-connected','true')
    $(this).removeClass('btn-danger')
    $(this).addClass('btn-outline-danger')
    publisher.publishAudio(true)
  }
})

$('#videoBtn').click(function(){
  var isConnected = $(this).attr('data-connected')
  if(isConnected == 'true'){
    $(this).attr('data-connected','false')
    $(this).removeClass('btn-outline-danger')
    $(this).addClass('btn-danger')
    publisher.publishVideo(false)
  }
  else{
    $(this).attr('data-connected','true')
    $(this).removeClass('btn-danger')
    $(this).addClass('btn-outline-danger')
    publisher.publishVideo(true)
  }
})

$('#endCall').click(function(){
  if(window.location.href.search('DoctorVideoUI') !=-1) {
    $.ajax({
      'url': '/api/vedioChatOparetion/' + urlParams.get('conf_id')+'/',
      'method': 'DELETE',
      beforeSend: function (xhr) {
          xhr.setRequestHeader("Authorization", "Token " + localStorage.getItem('DoctorToken'));
      },
  }).done((response) => {
      console.log(response)
  }).fail((response) => {
      console.log(response)
  })
  }
  video_session.disconnect()

})

// See the config.js file.
if (API_KEY && TOKEN && SESSION_ID) {
  apiKey = API_KEY;
  sessionId = SESSION_ID;
  token = TOKEN;
  initializeSession();
} else if (SAMPLE_SERVER_BASE_URL) {
  // Make an Ajax request to get the OpenTok API key, session ID, and token from the server
  fetch(SAMPLE_SERVER_BASE_URL + '/session').then(function fetch(res) {
    return res.json();
  }).then(function fetchJson(json) {
    apiKey = json.apiKey;
    sessionId = json.sessionId;
    token = json.token;

    initializeSession();
  }).catch(function catchErr(error) {
    handleError(error);
    alert('Failed to get opentok sessionId and token. Make sure you have updated the config.js file.');
  });
}
