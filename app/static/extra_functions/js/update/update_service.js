document.addEventListener('DOMContentLoaded', function() {
    let service    = document.getElementById('service_object');
    let service_id =service.value;

    fetch("/informacion_servicio/"+service_id)
        .then(response => response.json())
        .then(data => {
            console.log('service Data:', data);
            let name = document.getElementById('name');
            name.setAttribute('value', data.name);

            let dateString    = data.expiration_date
            let date          = new Date(dateString)
            let formattedDate = date.toISOString().split('T')[0];  
            let expiration_date = document.getElementById('expiration_date');
            expiration_date.setAttribute('value',formattedDate);

            
            let description = document.getElementById('description');
            description.value = data.description;

            let price = document.getElementById('price');
            price.setAttribute('value',data.price);

            let category = document.querySelectorAll('#category input[type="radio"]');
            category.forEach(element => {
                if(element.value == data.category){
                    element.checked = true;
                }
                
            });
            //category.setAttribute('value',data.category);
        })
        .catch(error => {
            console.error('Error fetching user data:', error);
        });
});

let select = document.getElementById('service_object');
select.addEventListener("change",function(){
    let service    = document.getElementById('service_object');
    let service_id =service.value;

    fetch("/informacion_servicio/"+service_id)
        .then(response => response.json())
        .then(data => {
            console.log('service Data:', data);
            let name = document.getElementById('name');
            name.value = data.name

            let dateString    = data.expiration_date
            let date          = new Date(dateString)
            let formattedDate = date.toISOString().split('T')[0];  
            let expiration_date = document.getElementById('expiration_date');
            expiration_date.value = formattedDate

            
            let description = document.getElementById('description');
            description.value = data.description;

            let price = document.getElementById('price');
            price.value = data.price

            let category = document.querySelectorAll('#category input[type="radio"]');
            category.forEach(element => {
                if(element.value == data.category){
                    element.checked = true;
                }
                
            });
            //category.setAttribute('value',data.category);
        })
        .catch(error => {
            console.error('Error fetching user data:', error);
        });
})