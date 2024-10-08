// Benzersiz EventID kontrol ve ekleme fonksiyonu
function addUniqueEvent(eventData) {
  try {
    var cnf = new Config(); // Config sınıfının bir örneğini oluşturun
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    var lastRow = sheet.getLastRow();

    // EventID sütununun indeksini belirleyin (örneğin: A sütunu = 1, B sütunu = 2, vb.)
    var eventIdColumnIndex = 2; // Bu örnekte B sütunu, 2. sütun

    // Eğer lastRow 1 ise, yani sadece başlık satırı varsa, direkt olarak yeni satırı ekleyebiliriz
    if (lastRow === 1) {
      sheet.appendRow(Object.values(eventData));
      return;
    }

    // EventID değerlerini al
    var eventIdValues = sheet.getRange(2, eventIdColumnIndex, lastRow - 1, 1).getValues();

    // Yeni etkinlik ID'si
    var newEventId = eventData[cnf.getEventIdFieldName()];

    // EventID değerlerini kontrol et
    for (var i = 0; i < eventIdValues.length; i++) {
      if (eventIdValues[i][0] == newEventId) {
        Logger.log("Duplicate Event ID found: " + newEventId);
        return; // Aynı ID bulunursa, fonksiyondan çık
      }
    }

    // Yeni satırı ekle
    sheet.appendRow(Object.values(eventData));
  } catch(e) {
    console.error('Error occurred in addUniqueEvent function: ' + e.stack);
  }
}
