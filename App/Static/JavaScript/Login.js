async function LoginFormHandler(Event) {
    Event.preventDefault();

    const Email = document.querySelector('#Email-Login').value.trim();
    const Password = document.querySelector('#Password-Login').value.trim();
    
    if (Email && Password) {
        const Response = await fetch('/api/users/login', {
            method: 'POST',
            body: JSON.stringify({
                Email,
                Password
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (Response.ok) {
            document.location.replace('/dashboard/');
        } else {
            alert(Response.statusText);
        }
    }
}

async function SignupFormHandler(Event) {
    Event.preventDefault();
    
    const Username = document.querySelector('#Username-Signup').value.trim();
    const Email = document.querySelector('#Email-Signup').value.trim();
    const Password = document.querySelector('#Password-Signup').value.trim();
    
    if (Username && Email && Password) {
        const Response = await fetch('/api/users', {
            method: 'POST',
            body: JSON.stringify({
                Username,
                Email,
                Password
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        });
    
        if (Response.ok) {
            document.location.replace('/dashboard/');
        } else {
            alert(Response.statusText);
        }
    }
}

document.querySelector('.Login-Form').addEventListener('submit', LoginFormHandler);

document.querySelector('.Signup-Form').addEventListener('submit', SignupFormHandler);