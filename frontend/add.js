const submitButton = document.querySelector("#submitPassenger");
submitButton.addEventListener("click", async function(){
    const name = document.querySelector("#passengerName").value;
    const cnic = document.querySelector("#passengerCnic").value;
    const age = parseInt(document.querySelector("#passengerAge").value);
    const destination = document.querySelector("#passengerDestination").value;
    const fare = parseInt(document.querySelector("#passengerFare").value);
    const gender = document.querySelector("#passengerGender").value;
    const phone = document.querySelector("#passengerPhone").value;

    if(!name || !cnic || !age || !destination || !fare || !gender || !phone){
        document.querySelector("#addpassenger").innerHTML = `<p>Please fill all fields</p>`;
        return; 
    }
    try
    {
        const response = await fetch("http://127.0.0.1:8000/Passengers",{
        method : "Post",
        headers : {
            "Content-Type": "application/json"
        },
        body: JSON.stringify ({
            name : name,
            cnic: cnic,
            age: parseInt(age),
            destination: destination,
            fare : parseInt(fare),
            gender : gender,
            phone_number : phone
        })
    });
    const data = await response.json();
    console.log(data.detail);
    const displaydiv = document.querySelector("#addpassenger");
    displaydiv.innerHTML = `
    <p>Passenger added successfully</p>
    `;
    setTimeout(() =>{
        displaydiv.innerHTML = "";
    }, 3000);
    } catch (error){
        console.log("Error", error)
    }
});