async function NewFormHandler(Event) {
    Event.preventDefault();

    const Title = document.querySelector('input[name="Post-Title"]').value;
    const Post_URL = document.querySelector('input[name="Post-URL"]').value;

    const Response = await fetch(`/api/posts`, {
        method: 'POST',
        body: JSON.stringify({
            Title,
            Post_URL
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    });

    if (Response.ok) {
        document.location.replace('/dashboard');
    } else {
        alert(Response.statusText);
    }
}

document.querySelector('.New-Post-Form').addEventListener('submit', NewFormHandler);