var host = 'http://3.65.226.102:5000';

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
  var url = host + '/api/dataset';

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
      sessionStorage.setItem(datasetId,datasetID);
      console.log("Datenset-ID: " + sessionStorage.getItem(datasetId));

    } else {
      // Fehler oder andere Statuscodes behandeln
      console.error(xhr.statusText);
    }
  };

  xhr.send(jsonData);
});


//document.getElementById('submitButton').addEventListener('click', function() {
//  setTimeout(function() {
//    window.location.href = 'page3.html';
//  }, 2000);
//});




