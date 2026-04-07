document.addEventListener("DOMContentLoaded", function(){

    const deletebyidbutton = document.querySelector(".deletebyid");
    deletebyidbutton.addEventListener("click", async function(){
        const idInput = document.querySelector("#idInput");
        const id = idInput.value;
        const displaydiv = document.querySelector("#deletepassengerbyid");
        if (!idInput.value.trim()){
            idInput.setCustomValidity("Please enter an Id first");
            idInput.reportValidity();
            return
        }
        idInput.setCustomValidity("");
        try{
            const response = await fetch(`http://127.0.0.1:8000/Passengers/${id}`,{
            method:"DELETE"
        });
        
        if(!response.ok){
            const error = await response.json();
            confirm(error.detail);
            return;
        }
        const data = await response.json();
        displaydiv.innerHTML = `<p>${data.message}</p>`;
        setTimeout(() =>{
                displaydiv.innerHTML = "";
            }, 3000);
        } catch(error){
            displaydiv.innerHTML = `
            <p>${error.message}</p>
            `;
        }
    });
});