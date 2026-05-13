const searchForm = document.querySelector('#search-form');
const resultsArea = document.querySelector('#results');

searchForm.addEventListener('submit', async function(event) {
    event.preventDefault();

    // 1. Tyhjennetään vanhat tulokset ennen uutta hakua
    resultsArea.innerHTML = '';

    const value_from_input = document.querySelector('#query').value;

    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${value_from_input}`);
        const data = await response.json();

        // 2. Käydään läpi hakutulokset
        data.forEach(tvShow => {
            // Luodaan <article> kontti
            const article = document.createElement('article');

            // Nimi <h2>
            const title = document.createElement('h2');
            title.textContent = tvShow.show.name;
            article.appendChild(title);

            // Kuva <img> (optional chaining ?. ja oletuskuva jos image puuttuu)
            const img = document.createElement('img');
            img.src = tvShow.show.image?.medium || 'https://via.placeholder.com/210x295?text=No+Image';
            img.alt = tvShow.show.name;
            article.appendChild(img);

            // Linkki <a>
            const link = document.createElement('a');
            link.href = tvShow.show.url;
            link.textContent = 'View Details';
            link.target = '_blank';
            article.appendChild(document.createElement('br')); // Rivinvaihto ennen linkkiä
            article.appendChild(link);

            // Kuvaus <div>
            const summaryDiv = document.createElement('div');
            summaryDiv.innerHTML = tvShow.show.summary;
            article.appendChild(summaryDiv);

            // 3. Lisätään koko artikkeli tulosalueelle
            resultsArea.appendChild(article);
        });

    } catch (error) {
        console.error("Haku epäonnistui:", error);
    }
});