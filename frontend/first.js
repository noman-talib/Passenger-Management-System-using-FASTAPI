const button = document.querySelector('.primary');
button.addEventListener("click", async function(){
    try{
        const response = await fetch("http://127.0.0.1:8000/");
        const data = await response.json();

        const resultofbase = document.querySelector('#BaseMessageResult');
        resultofbase.innerHTML = data.message;
    } catch (error){
        console.log("Error", error);
    }
});

const addButton = document.querySelector(".Add");
addButton.addEventListener("click", function(){
    const form = document.querySelector("#Addform");
    form.style.display = "block";
});


