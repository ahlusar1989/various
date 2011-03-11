function example() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheets()[0];
  var myValue = Browser.inputBox("Enter a number"); 
  sheet.getRange("A1").setValue("Number entered:");
  var b1Range = sheet.getRange("B1");
  b1Range.setValue(myValue);
  var valueToShow = b1Range.getValue() + 1;
  Browser.msgBox("The value you entered plus one is: " + valueToShow);
}