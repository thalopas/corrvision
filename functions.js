var host = '3.65.226.102:5000';

document.getElementById('submitButton').addEventListener('click', function() {
  // Inhalte der hochgeladenen Datei und des Links abrufen
  //var file = document.getElementById('fileInput').files[0];
  var link = document.getElementById('linkInput').value;

  // JSON-Objekt erstellen
  var data = {
    "datasetName": link
  };
  

  // JSON in einen String konvertieren
  var jsonData = JSON.stringify(data);

  console.log(jsonData);

  // URL, an die die JSON-Daten gesendet werden sollen
  var url = 'http://3.65.226.102:5000/api/dataset';

  console.log(url);

  // AJAX-Anfrage senden
  var xhr = new XMLHttpRequest();
  xhr.open('POST', url);
  xhr.setRequestHeader('Content-Type', 'application/json');

  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      // Erfolgreiche Antwort verarbeiten
      var response = JSON.parse(xhr.responseText);
      console.log(response);
      
      // Datenset-ID aus der JSON-Datei auslesen
      var datasetID = response.datasetId;
      console.log("Datenset-ID: " + datasetID);

      // URL für die neue Anfrage zusammenstellen
      var apiUrl = host + '/api/' + encodeURIComponent(datasetID) + '/heatmap';

      // Neue Anfrage mit der Datenset-ID in der URL senden
      var xhr2 = new XMLHttpRequest();
      xhr2.open('GET', apiUrl, true);
      xhr2.responseType = 'blob'; // Die Antwort als Blob erhalten

      xhr2.onreadystatechange = function() {
        if (xhr2.readyState === 4 && xhr2.status === 200) {
          // Erfolgreiche Antwort verarbeiten
          var blobData = xhr2.response;
          
          // Das Blob-Objekt in eine URL konvertieren
          var imageUrl = URL.createObjectURL(blobData);

          // Das Bild darstellen oder weiterverarbeiten
          // Bild in einem <img> -Element darstellen
          var imgElement = document.getElementById('imageElement');
          imgElement.src = imageUrl;
        } else {
          // Fehler oder andere Statuscodes behandeln
          console.error(xhr2.statusText);
        }
      };

      xhr2.send();
    } else {
      // Fehler oder andere Statuscodes behandeln
      console.error(xhr.statusText);
    }
  };

  xhr.send(jsonData);
});


//document.getElementById('submitButton').addEventListener('click', function() {
//  setTimeout(function() {
//    window.location.href = 'pages/page3.html';
//  }, 2000);
//});




