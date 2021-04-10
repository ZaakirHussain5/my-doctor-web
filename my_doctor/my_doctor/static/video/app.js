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
    serializedMessage(event.data, event.from.connectionId === video_session.connection.connectionId ? 'self' : 'other')
  });
}


function serializedMessage(message, messageOf) {
  let lis = '';
  var messagesContainer = $('.messages');
  let li = `<li class="${messageOf}">${message}</li>`;
  var allMessages = $('#messagess').html();
  var UpdatedMessages = allMessages + li;
  $('#messagess').html(UpdatedMessages)
  messagesContainer.finish().animate({
    scrollTop: messagesContainer.prop("scrollHeight")
  }, 250);
  openElement();
}

function sendNewMessage() {
  sendMessageAjax($('.text-box').html());
}

function sendMessageAjax(message) {
  video_session.signal({
      type: 'msg',
      data: message
  }, function signalCallback(error) {
      if (error) {
          console.error('Error sending signal:', error.name, error.message);
      } else {
        $('.text-box').html('');
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

var element = $('.floating-chat');
var myStorage = localStorage;

setTimeout(function () {
    element.addClass('enter');
}, 100);

element.click(openElement);

function openElement() {
    var messages = element.find('.messages');
    var textInput = element.find('.text-box');
    $('.chat-btn').hide();
    element.addClass('expand');
    element.find('.chat').addClass('enter');
    var strLength = textInput.val().length * 2;
    textInput.keydown(onMetaAndEnter).prop("disabled", false).focus();
    element.off('click', openElement);
    element.find('.header button').click(closeElement);
    element.find('#sendMessage').click(sendNewMessage);
    messages.scrollTop(messages.prop("scrollHeight"));
}

function closeElement() {
    element.find('.chat').removeClass('enter').hide();
    $('.chat-btn').show();
    element.removeClass('expand');
    element.find('.header button').off('click', closeElement);
    element.find('#sendMessage').off('click', sendNewMessage);
    element.find('.text-box').off('keydown', onMetaAndEnter).prop("disabled", true).blur();
    setTimeout(function () {
        element.find('.chat').removeClass('enter').show()
        element.click(openElement);
    }, 500);
}
