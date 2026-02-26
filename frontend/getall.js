const getAllButton = document.querySelector(".getall");
getAllButton.addEventListener("click", async function(){
    try {
    const response = await fetch("http://127.0.0.1:8000/Passengers");
    const data = await response.json();
    console.log("Data received", data)
    document.querySelector(".getallcontainer").style.display = "none";
    const displaydiv = document.querySelector("#passengersList");
    displaydiv.innerHTML = "";
    const table = document.createElement("table")
    table.innerHTML = `
    <thead>
            <tr>
                <th>Id</th>
                <th>Name</th>
                <th>Age</th>
                <th>Gender</th>
                <th>Fare</th>
                <th>Destination</th>
                <th>Phone Number</th>
            </tr>
    </thead>
    `;
    const tbody = document.createElement("tbody");
    data.forEach(function(passenger){
        const row = document.createElement("tr");
        row.innerHTML = `
        <td>${passenger.id}</td>
        <td>${passenger.name}</td>
        <td>${passenger.age}</td>
        <td>${passenger.gender}</td>
        <td>${passenger.fare}</td>
        <td>${passenger.destination}</td>
        <td>${passenger.phone_number}</td>
        `;
         tbody.appendChild(row);
    });
    table.appendChild(tbody);
    displaydiv.appendChild(table);

    document.body.appendChild(displaydiv);
    } catch (error){
        console.error("Error Fetching Passengers", error)
    }
});