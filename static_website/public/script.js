function createAccount() {
    let firstname = document.getElementById('firstNameInput').value;
    let lastname = document.getElementById('lastNameInput').value;

    const account = {
        firstName: firstname,
        lastName: lastname
    };

    accJSON = JSON.stringify(account)
    console.log(accJSON);

    let req  = new XMLHttpRequest();
    req.onload = function() {
        console.log("account created")
        console.log(req.responseText)
    }

    req.open('POST', 'http://51.145.32.187:8084/addAccount');
    req.send(accJSON);
}
