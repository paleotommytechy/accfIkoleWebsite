const loginCard = document.getElementById('login-card');
const registerCard = document.getElementById('register-card');
const showRegisterFormLink = document.getElementById('show-register-form');
const showLoginFormLink = document.getElementById('show-login-form');

showRegisterFormLink.addEventListener('click', (event) => {
    event.preventDefault();
    loginCard.classList.add('d-none');
    registerCard.classList.remove('d-none');
});

showLoginFormLink.addEventListener('click', (event) => {
    event.preventDefault();
    registerCard.classList.add('d-none');
    loginCard.classList.remove('d-none');
});