document.addEventListener("DOMContentLoaded", function(){

    const deletebyidbutton = document.querySelector(".deletebyid");
    deletebyidbutton.addEventListener("click", async function(){
        const id = document.querySelector("#idInput").value;
        const response = await fetch(`http://127.0.0.1:8000/Passengers/${id}`,{
            method:"DELETE"
        });
        const data = await response.json();
        const displaydiv = document.querySelector("#deletepassengerbyid");

        displaydiv.innerHTML = `
        <p>Passenger Deleted Successfully</p>
        `;
    });

});