async function DeleteFormHandler(Event) {
    Event.preventDefault();

    const Id = window.location.toString().split('/')[
        window.location.toString().split('/').length - 1
    ];
    
    const Response = await fetch(`/api/posts/${Id}`, {
        method: 'DELETE'
    });

    if (Response.ok) {
        document.location.replace('/dashboard/');
    } else {
        alert(Response.statusText);
    }
}

document.querySelector('.Delete-Post-Btn').addEventListener('click', DeleteFormHandler);