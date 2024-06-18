document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const documentList = document.getElementById('documentList');

    if (searchInput && documentList) {
        searchInput.addEventListener('input', function() {
            const query = this.value;
            fetch(`/search/?query=${query}`)
                .then(response => response.json())
                .then(data => {
                    documentList.innerHTML = '';
                    data.documents.forEach(document => {
                        documentList.innerHTML += `
                            <tr>
                                <td></td>
                                <td>${document.title}<br>
                                <small class="text-muted d-block">${document.description}</small></td>
                                <td class="align-middle">${document.download_count}</td>
                                <td class="align-middle">${document.email_count}</td>
                                <td>
                                    <form method="get" action="/download/${document.id}/">
                                        <button type="submit" class="btn btn-success">Download</button>
                                    </form>
                                </td>
                                <td>
                                    <a href="/send_email/${document.id}/">Send Email</a>
                                </td>
                            </tr>
                        `;
                    });
                });
        });
    }
});