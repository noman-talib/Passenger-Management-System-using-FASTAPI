document.addEventListener("DOMContentLoaded", function(){

    const updatebyidbutton = document.querySelector("#updatebyid");
    updatebyidbutton.addEventListener("click", async function(){
        const id = document.querySelector("#idInput").value;
        const name = document.querySelector("#passengerName").value;
        const cnic = document.querySelector("#passengerCnic").value;
        const age = document.querySelector("#passengerAge").value;
        const destination = document.querySelector("#passengerDestination").value;
        const fare = document.querySelector("#passengerFare").value;
        const gender = document.querySelector("#passengerGender").value;
        const phone = document.querySelector("#passengerPhone").value;

        const updatedData = {};

        if(name !== "") updatedData.name = name;
        if(cnic !== "") updatedData.cnic = cnic;
        if(age !== "") updatedData.age = age;
        if(destination !== "") updatedData.destination = destination;
        if(fare !== "") updatedData.fare = fare;
        if(gender !== "") updatedData.gender = gender;
        if(phone !== "") updatedData.phone_number = phone;

        if(Object.keys(updatedData).length === 0){
            alert("Please fill at least one field to update");
            return;
        }

        const response = await fetch(`http://127.0.0.1:8000/Passengers/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(updatedData)
        });
        const data = await response.json();
    });

});