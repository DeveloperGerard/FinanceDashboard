document.addEventListener("DOMContentLoaded",function(){
    let loan = document.getElementById("loan_object");
    let loan_id = loan.value;

    fetch("/informacion_prestamo/"+loan_id)
        .then(response => response.json())
        .then(data =>{
            let name = document.getElementById("name");
            name.setAttribute('value',data.name);

            let holder = document.getElementById("holder");
            holder.setAttribute('value',data.holder);

            let price  = document.getElementById("price");
            price.setAttribute('value',data.price);

            let quota  = document.getElementById("quota");
            quota.setAttribute('value',data.quota);

            let tea    = document.getElementById("tea");
            tea.setAttribute('value',data.tea);

            let dateString    = data.expiration_date;
            let date          = new Date(dateString);
            let formattedDate = date.toISOString().split('T')[0];  
            let expiration_date = document.getElementById("expiration_date");
            expiration_date.setAttribute('value',formattedDate);



        })
})
let select = document.getElementById('loan_object');
select.addEventListener("change",function(){
    let loan = document.getElementById("loan_object");
    let loan_id = loan.value;

    fetch("/informacion_prestamo/"+loan_id)
        .then(response => response.json())
        .then(data =>{
            let name = document.getElementById("name");
            name.value = data.name;

            let holder = document.getElementById("holder");
            holder.value = data.holder;

            let price  = document.getElementById("price");
            price.value = data.price;

            let quota  = document.getElementById("quota");
            quota.value = data.quota;

            let tea    = document.getElementById("tea");
            tea.value = data.tea

            let dateString    = data.expiration_date;
            let date          = new Date(dateString);
            let formattedDate = date.toISOString().split('T')[0];  
            let expiration_date = document.getElementById("expiration_date");
            expiration_date.value =formattedDate;



        })
})