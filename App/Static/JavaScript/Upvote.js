async function UpvoteClickHandler(Event) {
    Event.preventDefault();

    const Id = window.location.toString().split('/')[
        window.location.toString().split('/').length - 1
    ];
    
    const Response = await fetch('/api/posts/upvote', {
        method: 'PUT',
        body: JSON.stringify({
            Post_Id: Id
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    });

    if (Response.ok) {
        document.location.reload();
    } else {
        alert(Response.statusText);
    }
}

document.querySelector('.Upvote-Btn').addEventListener('click', UpvoteClickHandler);