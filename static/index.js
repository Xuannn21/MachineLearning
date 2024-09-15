// Get references to form elements and buttons
var form_1 = document.querySelector(".form_1");
var form_2 = document.querySelector(".form_2");
var form_3 = document.querySelector(".form_3");

var form_1_btns = document.querySelector(".form_1_btns");
var form_2_btns = document.querySelector(".form_2_btns");
var form_3_btns = document.querySelector(".form_3_btns");

var form_1_next_btn = document.querySelector(".form_1_btns .btn_next");
var form_2_back_btn = document.querySelector(".form_2_btns .btn_back");
var form_2_next_btn = document.querySelector(".form_2_btns .btn_next");
var form_3_back_btn = document.querySelector(".form_3_btns .btn_back");

var form_2_progessbar = document.querySelector(".form_2_progessbar");
var form_3_progessbar = document.querySelector(".form_3_progessbar");

var btn_done = document.querySelector(".btn_done");
var modal_wrapper = document.querySelector(".modal_wrapper");
var shadow = document.querySelector(".shadow");

// Function to show error messages inline
function showError(input, message) {
    var errorElement = input.nextElementSibling; // Assumes the error message is the next sibling
    if (errorElement && errorElement.classList.contains('error-message')) {
        errorElement.innerText = message;
        errorElement.style.display = 'block';
    }
}

// Function to hide error messages
function hideError(input) {
    var errorElement = input.nextElementSibling; // Assumes the error message is the next sibling
    if (errorElement && errorElement.classList.contains('error-message')) {
        errorElement.style.display = 'none';
    }
}

// Function to validate the form fields
function validateForm(form) {
    var isValid = true;
    var inputs = form.querySelectorAll('input[required], select[required]');
    
    inputs.forEach(function(input) {
        if (input.tagName === 'SELECT') {
            if (input.value === '') {
                showError(input, 'Please select an option.');
                isValid = false;
            } else {
                hideError(input);
            }
        } else if (input.tagName === 'INPUT') {
            if (input.value.trim() === '') { // Check for empty or whitespace
                showError(input, 'Please enter a value.');
                isValid = false;
            } else {
                hideError(input);
            }
        }
    });

    return isValid;
}

// Event listener for form 1 'Next' button
form_1_next_btn.addEventListener("click", function() {
    if (validateForm(form_1)) {
        form_1.style.display = "none";
        form_2.style.display = "block";

        form_1_btns.style.display = "none";
        form_2_btns.style.display = "flex";

        form_2_progessbar.classList.add("active");
    } else {
        alert("Please complete all required fields in Basic Information.");
    }
});

// Event listener for form 2 'Back' button
form_2_back_btn.addEventListener("click", function() {
    form_1.style.display = "block";
    form_2.style.display = "none";

    form_1_btns.style.display = "flex";
    form_2_btns.style.display = "none";

    form_2_progessbar.classList.remove("active");
});

// Event listener for form 2 'Next' button
form_2_next_btn.addEventListener("click", function() {
    if (validateForm(form_2)) {
        form_2.style.display = "none";
        form_3.style.display = "block";

        form_3_btns.style.display = "flex";
        form_2_btns.style.display = "none";

        form_3_progessbar.classList.add("active");
    } else {
        alert("Please complete all required fields in Service Details.");
    }
});

// Event listener for form 3 'Back' button
form_3_back_btn.addEventListener("click", function() {
    form_2.style.display = "block";
    form_3.style.display = "none";

    form_3_btns.style.display = "none";
    form_2_btns.style.display = "flex";

    form_3_progessbar.classList.remove("active");
});

// Final button to validate and show modal
btn_done.addEventListener("click", function(event) {
    if (validateForm(form_3)) { // Final validation
        modal_wrapper.classList.add("active");
    } else {
        alert("Please complete all required fields in the form.");
    }ert("Please complete all required fields in the form.");
    // }
});

// To close modal on shadow click
shadow.addEventListener("click", function() {
    modal_wrapper.classList.remove("active");
    
});
