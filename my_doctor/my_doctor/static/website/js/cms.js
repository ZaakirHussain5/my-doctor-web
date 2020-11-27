function submitRegistrationForm() {
    let data = {
        full_name: $('#Name1').val(),
        username: $('#mob1').val(),
        ph_no: $('#mob1').val(),
        email: $('#email').val(),
        password: $('#password').val(),
        age: $("#age").val(),
        gender: $("#gender").val(),
        blood_group: "Not Specified",
        height: $("#height").val(),
        weight: $("#weight").val(),
        marital_status: 'Not Specified',
        user_type: 'P'
    }
    let tele_data = {
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

    $('#submit').html(`
    <i class="fa fa-spinner fa-spin"></i> Your Dashboard is getting Ready...
    `)

    $('#submit').attr('disabled', 'disabled')

    if ($('#OTP').val() == '') {
        alert('Enter The OTP')
        return
    }
    $.ajax({
        url: 'https://teleduce.corefactors.in/validate-otp/a224db72-cafb-4cce-93ab-3d7f950c92e2/',
        data: {
            mobile: $('#mob1').val(),
            otp: $('#OTP').val()
        }
    }).done(function (response) {
        console.log(response)
        if (response.response_code != "8000") {
            alert('Invalid OTP Please Check the OTP and Try Again')
            $('#submit').html('Register')
            $('#submit').removeAttr('disabled')
            return
        }

        $.ajax({
            url: '/api/GeneratePatientID',
            method: 'GET',
            contentType: 'application/json',
        }).done((response) => {
            data.pat_id = response.pat_id
            $.ajax({
                url: '/api/PatientRegInApp',
                data: JSON.stringify(data),
                method: 'POST',
                contentType: 'application/json'
            }).done((response) => {
                $.cookie('Token', response.token, { expires: 1 })
                $.ajax({
                    url: 'https://teleduce.corefactors.in/lead/apiwebhook/a224db72-cafb-4cce-93ab-3d7f950c92e2/Register/',
                    method: 'POST',
                    data: JSON.stringify(tele_data),
                    contentType: 'application/json',
                }).done((response) => {
                    window.location.href = 'patients/dashboard'
                }).fail((error) => {
                    $('#submit').html('Register')
                    $('#submit').removeAttr('disabled')
                    console.log(error)
                })
            }).fail((error) => {
                $('#submit').html('Register')
                $('#submit').removeAttr('disabled')
                console.log(error);
            })
        }).fail((error) => {
            $('#submit').html('Register')
            $('#submit').removeAttr('disabled')
            console.log(error)
        })
    })



    console.log("data is", data);



}


function submitSubscriptionForm(data) {
    console.log("Data coming so function is called.", data);
    $.ajax({
        url: 'https://teleduce.corefactors.in/lead/apiwebhook/a224db72-cafb-4cce-93ab-3d7f950c92e2/BookAnAppoinment/',
        method: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json',
    }).done((response) => {
        console.log(response);
        alert("Thank you!! We have your details, Our representatives will get back to you.");
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

$("#newsletter-form").submit(function (e) {
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

$('#patientRegistration').submit(submitRegistrationForm)
