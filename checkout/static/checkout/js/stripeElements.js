// From Stripe documentation
let stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
let clientSecret = $("#id_client_secret").text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
let cardElement = $("#card-element");

const style = {
    base: {
        color: "#000",
        fontFamily: "'Inter', sans-serif",
        fontSmoothing: "antialiased",
        fontSize: "1.3rem",
        "::placeholder": {
            color: "#aab7c4"
        }
    },
    invalid: {
        color: "#dc3545",
        iconColor: '#dc3545',
    }
};

let card = elements.create("card", { style: style });
card.mount("#card-element");

card.on('change', function (event) {
    var displayError = document.getElementById('card-errors');
    if (event.error) {
        displayError.textContent = event.error.message;
    } else {
        displayError.textContent = '';
    }
});

// Realtime Stripe validation errors
card.addEventListener('change', (event) => {
    let errorDiv = $("#card-errors");
    if (event.error) {
        let html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>`;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = "";
    }
})

// Form submission
let form = $("#payment-form");

form.addEventListener('submit', (e) => {
    // Prevent posting so that the below code can be executed
    e.preventDefault();
    // Disable card and submit button to prevent multiple submissions
    card.update({ "disabled": true });
    $("#submit-button").attr("disabled", true);
    // Send card details to Stripe
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then((result) => {
        if (result.error) {
            // If error, show error to customer
            let errorDiv = $("#card-errors");
            let html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            // Re-enable card and submit button to allow the user to try again
            card.update({ "disabled": false });
            $("#submit-button").attr("disabled", false);
        } else {
            // If payment has gone through, submit form
            if (result.paymentIntent.status === "succeeded") {
                form.submit();
            }
        }
    })
});