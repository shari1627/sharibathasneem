function validate(){


    var message_name = document.getElementById("message_name").value;
    var message_number = document.getElementById("message_number").value;
    var message_email = document.getElementById("message_email").value;
    var message = document.getElementById("message").value;
    var error_message = document.getElementById("error_message");
    
    error_message.style.padding = "10px";
    
    var text;
    if(message_name.length < 5){
      text = "Please Enter valid Name";
      error_message.innerHTML = text;
      return false;
    }
    if(message_email.indexOf("@") == -1 || message_email.length < 6){
        text = "Please Enter valid Email";
        error_message.innerHTML = text;
        return false;
      }
    if(isNaN(message_number) || message_number.length != 10){
      text = "Please Enter valid Phone Number";
      error_message.innerHTML = text;
      return false;
    }
    
    if(message.length <= 10){
      text = "Please Enter More Than 10 Characters";
      error_message.innerHTML = text;
      return false;
    }
    
    alert("Thank you for choosing use\n Will be contacting you soon");
    return true;
  }