async function CommentFormHandler(Event) {
    Event.preventDefault();

    const Comment_Text = document.querySelector('textarea[name="Comment-Body"]').value.trim();
    const Post_Id = window.location.toString().split('/')[
        window.location.toString().split('/').length - 1
    ];

    if (Comment_Text) {
        const Response = await fetch('/api/comments', {
            method: 'POST',
            body: JSON.stringify({
                Post_Id,
                Comment_Text
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
}

document.querySelector('.Comment-Form').addEventListener('submit', CommentFormHandler);