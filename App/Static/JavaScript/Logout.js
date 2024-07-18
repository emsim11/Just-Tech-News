async function Logout(Event) {
    const Response = await fetch('/api/users/logout', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    if (Response.ok) {
        document.location.replace('/');
    } else {
        alert(Response.statusText);
    }
}

document.querySelector('#Logout').addEventListener('click', Logout);