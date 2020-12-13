var element = $('.floating-chat');
var myStorage = localStorage;

if (!myStorage.getItem('chatID')) {
    myStorage.setItem('chatID', createUUID());
}

setTimeout(function() {
    element.addClass('enter');
}, 1000);

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
    setTimeout(function() {
        element.find('.chat').removeClass('enter').show()
        element.click(openElement);
    }, 500);
}

function createUUID() {
    // http://www.ietf.org/rfc/rfc4122.txt
    var s = [];
    var hexDigits = "0123456789abcdef";
    for (var i = 0; i < 36; i++) {
        s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
    }
    s[14] = "4"; // bits 12-15 of the time_hi_and_version field to 0010
    s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1); // bits 6-7 of the clock_seq_hi_and_reserved to 01
    s[8] = s[13] = s[18] = s[23] = "-";

    var uuid = s.join("");
    return uuid;
}

function sendNewMessage() {

    var userInput = $('.text-box');
    var newMessage = userInput.html();

    if (!newMessage) return;

    var messagesContainer = $('.messages');

    // messagesContainer.append([
    //     '<li class="self">',
    //     newMessage,
    //     '</li>'
    // ].join(''));

    // clean out old message
    userInput.html('');
    // focus on input
    userInput.focus();

    messagesContainer.finish().animate({
        scrollTop: messagesContainer.prop("scrollHeight")
    }, 250);
    sendMessageAjax(newMessage);
}

function sendMessageAjax(message){
    
    let data = {
        'user': user,
        'message': message,
        'session_id': session
    }
    $.ajax({
        url: '/api/consultant_chats/',
        method: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json'
    }).done((response)=>{
        console.log(response)
    }).fail((err)=>{
        console.log(err);
    })
}
let total_messages = 0;
function getMyMessage(){
    $.ajax({
        url: '/api/consultant_chats?session='+ session,
        method: 'GET',
        contentType: 'application/json'
    }).done((response)=>{
        console.log('response,', response)
        if( total_messages < response.length)
        {openElement(); total_messages = response.length }
        serializedMessage(response)
    }).fail((err)=>{
        console.log(err);
    })
}
getMyMessage()
let messageInterval = setInterval(function(){
    getMyMessage();
}, 1000)

let totalMessage = 0
function serializedMessage(arrOfMessage){
    let lis = '';
    console.log(totalMessage, arrOfMessage.length)
    let subarry = arrOfMessage.slice(totalMessage, arrOfMessage.length);
    console.log(subarry)
    totalMessage = arrOfMessage.length;
    for(var i =0; i < subarry.length; i++){
        let message = subarry[i];
        if(user == message.user){
            let li = `<li class="self">${message.message}</li>`;
            lis += li
        }
        else{
            let li = `<li class="other">${message.message}</li>`;
            lis += li
        }
    }
    $('#messagess').append(lis);
    messagesContainer.finish().animate({
        scrollTop: messagesContainer.prop("scrollHeight")
    }, 250);
}

function onMetaAndEnter(event) {
    if ((event.metaKey || event.ctrlKey) && event.keyCode == 13) {
        sendNewMessage();
    }
}