function submitRegistrationForm(){
    let data = {
        Full_Name: $('#Name1').val(),
        // user_type: $('#user_type').val(),
        username: $('#mob1').val(),
        Phone_Number: $('#mob1').val(),
        Email_Address: $('#email').val(),
        Password: $('#password').val(),
        Age: $("#age").val(),
        Gender: $("#gender").val(),
        Blood_Group: $("#bloodGroup").val(),
        Height: $("#height").val(),
        Weight: $("#weight").val(),
        // marital_status: 'Not Specified'
    }
    console.log("data is", data);
    $.ajax({
        url: 'https://teleduce.corefactors.in/lead/apiwebhook/a224db72-cafb-4cce-93ab-3d7f950c92e2/Register/',
        method: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json',
    }).done((response)=>{
            $.cookie('Token', response.token, { expires: 1 })
            window.location.href = 'patients/dashboard'
        }).fail((error)=>{
        console.log(error)

    })


}


function submitSubscriptionForm (data) {
    console.log("Data coming so function is called.", data);
    $.ajax({
        url: 'https://teleduce.corefactors.in/lead/apiwebhook/a224db72-cafb-4cce-93ab-3d7f950c92e2/BookAnAppoinment/',
        method: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json',
    }).done((response) => {
        console.log(response);
        alert("Got it !! Request received, our medical representative will get back to you at the earliest");
        $("#appointments-main-form").find("input[type=text], textarea, input[type=tel], input[type=number]").val("")
    })
        .fail((error) => {
            console.log(error)
        })
}

function newsLetterSubscription(data) {
    $.ajax({
        url: 'https://teleduce.corefactors.in/lead/apiwebhook/a224db72-cafb-4cce-93ab-3d7f950c92e2/Newsletter/',
        method: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json',
    }).done((response) => {
        console.log(response);
        alert("You are now registered for important updates and newsletters");
        $("#newsletter-form").find("input[type=email]").val("")
    })
        .fail((error) => {
            console.log(error)
        })
}

$("#newsletter-form").submit(function(e) {
        e.preventDefault();
        e.stopImmediatePropagation();
        console.log(
            "Form submitted successfully."
        )
        let data = {
            Subsricbe_To_Newsletter: $('#SubsricbeToNewsletter').val()
        }
        newsLetterSubscription(data);
        
    })
    /////////////////////  APPOINMENT FORM SUBMITED /////////////////
    $("#appointments-main-form").submit(function (e) {
        e.preventDefault();
        e.stopImmediatePropagation();

        let data = {
            Your_Name: $('#id_name').val(),
            Your_Email: $('#id_email').val(),
            Enter_Phone: $('#id_ph_no').val(),
            gender: $('#id_gender').val(),
            Blood_Group: $("#id_blood").val(),
            Age: $("#id_age").val(),
            Speciaility: $("#select-specialist").val(),
            Your_City: $("#id_city").val(),
            Briefly_Describe_About_Your_Problem: $("#id_message").val()
        };
        submitSubscriptionForm(data)
       

    })
    
    $('#submit').click(submitRegistrationForm)
