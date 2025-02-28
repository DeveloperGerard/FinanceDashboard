document.addEventListener('DOMContentLoaded', function() {
    let account    = document.getElementById('account_object');
    let account_id =account.value;

    fetch("informacion_cuenta/"+account_id)
        .then(response => response.json())
        .then(data => {
            console.log('Account Data:', data);
            let name = document.getElementById('name');
            name.setAttribute('value', data.account_name);
            let card = document.getElementById('card');
            card.setAttribute('value', data.card);
        })
        .catch(error => {
            console.error('Error fetching user data:', error);
        });
});
let select = document.getElementById('account_xd');
select.addEventListener("change",function(){
    let account    = document.getElementById('account_object');
    let account_id =account.value;
    fetch("informacion_cuenta/"+account_id)
        .then(response => response.json())
        .then(data => {
            console.log('Account Data:', data);
            let name = document.getElementById('name');
            name.value = data.name
            let card = document.getElementById('card');
            card.value = data.card
        })
        .catch(error => {
            console.error('Error fetching user data:', error);
        });
})
