document.getElementById("searchBtn").addEventListener("click", () => {
    const query = document.getElementById("queryInput").value;
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = "Loading...";

    fetch(`http://127.0.0.1:5000/search?q=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(data => {
            resultsDiv.innerHTML = "";

            data.results.forEach(item => {
                const post = document.createElement("div");
                post.innerHTML = `
                <strong><a href="${item.url}" target = "_blank">${item.title}</a></strong>
                <p>${item.top_comment}</p>
                <hr/>
                `;
                resultsDiv.appendChild(post);
            });
        })
        .catch(err => {
            resultsDiv.innerHTML = "Error fetching results.";
            console.error(err);
        });
});