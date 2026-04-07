const getbyidbutton = document.querySelector(".getbyid");
getbyidbutton.addEventListener("click", async function(){
    const idInput  = document.querySelector("#idInput");
    const id = idInput.value;
    if (!idInput.value.trim()){
            idInput.setCustomValidity("Please enter an Id first");
            idInput.reportValidity();
            return
        }
    try{
    const response = await fetch(`http://127.0.0.1:8000/Passengers/${id}`);
    const data = await response.json();
    document.querySelector(".getbyidcontainer").style.display = "none";
    const displaydiv = document.querySelector("#passengerbyid");
    const table = document.createElement("table");
    table.innerHTML = `
        <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Age</th>
                    <th>Gender</th>
                    <th>Fare</th>
                    <th>Destination</th>
                    <th>Phone Number</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>${data.id}</td>
                    <td>${data.name}</td>
                    <td>${data.age}</td>
                    <td>${data.gender}</td>
                    <td>${data.fare}</td>
                    <td>${data.destination}</td>
                    <td>${data.phone_number}</td>
                </tr>
            </tbody>
    `;
    displaydiv.appendChild(table);
    } catch (error){
        console.error("Error", error);
    }
});