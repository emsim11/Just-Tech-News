async function EditFormHandler(Event) {
    Event.preventDefault();

    const Title = document.querySelector('input[name="Post-Title"]').value.trim();
    const Id = window.location.toString().split('/')[
        window.location.toString().split('/').length - 1
    ];
    
    const Response = await fetch(`/api/posts/${Id}`, {
        method: 'PUT',
        body: JSON.stringify({
            Title
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

document.querySelector('.Edit-Post-Form').addEventListener('submit', EditFormHandler);