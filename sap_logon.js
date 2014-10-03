var retcd      = 0;
var exceptions = 0;
var fns        = null;

function SAPlogon() {
  fns       = new ActiveXObject("SAP.Functions");
  var trans = fns.Transactions;
  var conn  = fns.connection;

  conn.ApplicationServer = "server"
  conn.System            = "DEV"
  conn.SystemNumber      = "00"
  conn.UseSAPLogonIni    = "false"
  conn.user              = "user";
  conn.password          = "passwd";
  conn.client            = "200";
  conn.language          = "E";
  conn.tracelevel        = 6;
  conn.RFCWithDialog     = true;

//  conn.RFCWithDialog = 0;

  conn.logon(0,0);
  exceptions = 0;
}

function SAPlogoff() {
  conn.logoff(0, 0);    
  exceptions = 0;
}

function SAPcallTransaction(tcode) {
  exceptions = 0;
  callta = fns.add("RFC_CALL_TRANSACTION_USING");
  callta.exports("TCODE") = tcode;
  callta.exports("MODE") = "E";
  
  retcd = callta.call;
  conn.logoff();    
  SAPcallTransaction = retcd;
}
