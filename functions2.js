var host = 'http://3.65.226.102:5000';
var datasetID = sessionStorage.getItem('datasetID');
console.log(datasetID);


// URL, an die die JSON-Daten gesendet werden sollen
var url = host + '/api/dataset/' + encodeURIComponent(datasetID) + '/heatmap';

console.log(url);

// AJAX-Anfrage senden
var xhr = new XMLHttpRequest();
xhr.open('GET', url);

xhr.onreadystatechange = function() {
if (xhr.readyState === 4 && xhr.status === 200) {
    // Erfolgreiche Antwort verarbeiten
    var response = JSON.parse(xhr.responseText);
    console.log(response);
    var imgSrc = '../' + response.heatmap
    const image = document.createElement('img');

    // 👇️ Remote image
    image.setAttribute('id', 'imageElement')
    image.setAttribute('src', imgSrc);
    image.setAttribute('alt', 'heatmap');
    document.getElementById('imageBox').appendChild(image);

} else {
    // Fehler oder andere Statuscodes behandeln
    console.error(xhr.statusText);
}
};

xhr.send();
