// Datei auswählen
document.getElementById('uploadButton').addEventListener('click', function() {
    document.getElementById('fileInput').click();
  });
  
  document.getElementById('fileInput').addEventListener('change', function() {
    var file = this.files[0];
    if (file) {
      console.log('Ausgewählte Datei:', file);
      // Hier zum Verarbeiten der hochgeladenen Datei implementieren
    }
  });
  
  // Kaggle-Link senden
  document.getElementById('submitButton').addEventListener('click', function() {
    var link = document.getElementById('linkInput').value;
    if (link) {
      console.log('Eingegebener Link:', link);
      // Hier Code Öffnen des Kaggle-Links implementieren
    }
  });
  