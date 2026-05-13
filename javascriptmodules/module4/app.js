// 1. Haetaan lomake-elementti
const searchForm = document.querySelector('#search-form');

// 2. Lisätään tapahtumankuuntelija 'submit'-tapahtumalle
searchForm.addEventListener('submit', async function(event) {
    // Estetään lomakkeen oletusarvoinen lähetys (sivun uudelleenlataus)
    event.preventDefault();

    // 3. Haetaan käyttäjän syöttämä arvo
    const value_from_input = document.querySelector('#query').value;

    // 4. Tehdään haku TVMaze API:in
    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${value_from_input}`);

        // Muutetaan vastaus JSON-muotoon
        const data = await response.json();

       // Tulostetaan jokaisen löydetyn sarjan nimi konsoliin
data.forEach(result => {
    console.log(result.show.name);
});

    } catch (error) {
        console.error("Haku epäonnistui:", error);
    }
});