document.addEventListener('DOMContentLoaded', function() {
    let income    = document.getElementById('income_object');
    let income_id =income.value;

    fetch("/informacion_ingreso/"+income_id)
        .then(response => response.json())
        .then(data => {
            console.log('Income Data:', data);
            let name = document.getElementById('name');
            name.setAttribute('value', data.income_name);

            let dateString    = data.income_date
            let date          = new Date(dateString)
            let formattedDate = date.toISOString().split('T')[0];  
            let payment_date = document.getElementById('payment_date');
            payment_date.setAttribute('value',formattedDate);

            console.log(toString(data.payment_date))
            
            let description = document.getElementById('description');
            description.setAttribute('value',data.description);

            let amount = document.getElementById('amount');
            amount.setAttribute('value',data.amount);

            let category = document.querySelectorAll('#category input[type="radio"]');
            console.log(category)
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
let select = document.getElementById('income_object');
select.addEventListener("change",function(){
    let income    = document.getElementById('income_object');
    let income_id =income.value;

    fetch("/informacion_ingreso/"+income_id)
        .then(response => response.json())
        .then(data => {
            console.log('Income Data:', data);
            let name = document.getElementById('name');
            name.value = data.income_name

            let dateString    = data.income_date
            let date          = new Date(dateString)
            let formattedDate = date.toISOString().split('T')[0];  
            let payment_date = document.getElementById('payment_date');
            payment_date.value=formattedDate

            
            let description = document.getElementById('description');
            description.value = data.description;

            let amount = document.getElementById('amount');
            amount.value =data.amount;

            let category = document.querySelectorAll('#category input[type="radio"]');
            console.log(category)
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

