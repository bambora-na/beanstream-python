response_codes = {
  "0": {
    "type": "test",
    "cardholder_message": "Authorization Failed",
    "approved": False,
    "merchant_message": "Authorization Failed",
  },
  "1114": {
    "type": "Desjardins",
    "cardholder_message": "KEY CHANGE REQUIRED",
    "approved": False,
    "merchant_message": "Declined. First transaction for a terminal must be a transaction code 96"
  },
  "595": {
    "type": "Global Payments",
    "cardholder_message": "DB UNAVAIL 03",
    "approved": False,
    "merchant_message": "DB UNAVAIL 03"
  },
  "312": {
    "type": "Bambora",
    "cardholder_message": "Card type not accepted",
    "approved": False,
    "merchant_message": "Card type not accepted"
  },
  "1125": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. Requires caisse authorization"
  },
  "1025": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. Cannot authorize"
  },
  "483": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Merchant",
    "approved": False,
    "merchant_message": "Invalid Merchant"
  },
  "765": {
    "type": "EBP/ACH",
    "cardholder_message": "No pre-notification - Personal",
    "approved": False,
    "merchant_message": "No pre-notification - Personal"
  },
  "427": {
    "type": "Paymentech",
    "cardholder_message": "TKN Data Error",
    "approved": False,
    "merchant_message": "TKN Data Error"
  },
  "16": {
    "type": "Bambora",
    "cardholder_message": "Duplicate Transaction \u2013 This transaction has already been approved",
    "approved": True,
    "merchant_message": "Duplicate Transaction \u2013 This transaction has already been approved"
  },
  "893": {
    "type": "UK",
    "cardholder_message": "Invalid input data",
    "approved": False,
    "merchant_message": "Invalid input data"
  },
  "364": {
    "type": "Paymentech",
    "cardholder_message": "Request Denied",
    "approved": False,
    "merchant_message": "Request Denied"
  },
  "422": {
    "type": "Paymentech",
    "cardholder_message": "Inv Input/Use VRU",
    "approved": False,
    "merchant_message": "Inv Input/Use VRU"
  },
  "206": {
    "type": "Bambora",
    "cardholder_message": "Account missing terminal id",
    "approved": False,
    "merchant_message": "Account missing terminal id"
  },
  "342": {
    "type": "EBP/ACH",
    "cardholder_message": "Interbank reject - Invalid institution number",
    "approved": False,
    "merchant_message": "Interbank reject - Invalid institution number"
  },
  "1089": {
    "type": "Desjardins",
    "cardholder_message": "FORMAT ERROR",
    "approved": False,
    "merchant_message": "Declined. Error in the contents of a field in the transaction"
  },
  "635": {
    "type": "INTERAC Online",
    "cardholder_message": "CARD USE LIMITED REFER TO BRANCH",
    "approved": False,
    "merchant_message": "CARD USE LIMITED REFER TO BRANCH"
  },
  "801": {
    "type": "Bambora",
    "cardholder_message": "Card number missing for given customer code (token)",
    "approved": False,
    "merchant_message": "Card number missing for given customer code (token)"
  },
  "819": {
    "type": "Bambora",
    "cardholder_message": "Missing AVS and CVD data required for Discover transaction",
    "approved": False,
    "merchant_message": "Missing AVS and CVD data required for Discover transaction"
  },
  "590": {
    "type": "Global Payments",
    "cardholder_message": "AP AUTH-ONLY",
    "approved": False,
    "merchant_message": "AP AUTH-ONLY"
  },
  "1009": {
    "type": "Desjardins",
    "cardholder_message": "SYSTEM NOT AVAIL.",
    "approved": False,
    "merchant_message": "Declined. The host cannot authorize the transaction at this time"
  },
  "709": {
    "type": "First Data",
    "cardholder_message": "INV VEHICLE NBR",
    "approved": False,
    "merchant_message": "INV VEHICLE NBR"
  },
  "410": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Sys Info",
    "approved": False,
    "merchant_message": "Invalid Sys Info"
  },
  "700": {
    "type": "First Data",
    "cardholder_message": "INVALID TERM ID",
    "approved": False,
    "merchant_message": "INVALID TERM ID"
  },
  "848": {
    "type": "UK",
    "cardholder_message": "Invalid reference transaction ID",
    "approved": False,
    "merchant_message": "Invalid reference transaction ID"
  },
  "1057": {
    "type": "Desjardins",
    "cardholder_message": "CALL FOR AUTH",
    "approved": False,
    "merchant_message": "Declined. ARQC error"
  },
  "338": {
    "type": "EBP/ACH",
    "cardholder_message": "Incorrect payor/payee name",
    "approved": False,
    "merchant_message": "Incorrect payor/payee name"
  },
  "199": {
    "type": "Bambora",
    "cardholder_message": "Credit card does not match original purchase.",
    "approved": False,
    "merchant_message": "Credit card does not match original purchase."
  },
  "742": {
    "type": "First Data",
    "cardholder_message": "DECLINE",
    "approved": False,
    "merchant_message": "DECLINE"
  },
  "693": {
    "type": "First Data",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "DECLINED"
  },
  "375": {
    "type": "Paymentech",
    "cardholder_message": "Prod Restricted",
    "approved": False,
    "merchant_message": "Prod Restricted"
  },
  "420": {
    "type": "Paymentech",
    "cardholder_message": "Inv Mult Clr Seq No",
    "approved": False,
    "merchant_message": "Inv Mult Clr Seq No"
  },
  "944": {
    "type": "Bambora",
    "cardholder_message": "Card entry method not accepted",
    "approved": False,
    "merchant_message": "Card entry method not accepted"
  },
  "856": {
    "type": "UK",
    "cardholder_message": "Transaction refused: The sum of this and previously credited amounts (if any) exceeds debited amount",
    "approved": False,
    "merchant_message": "Transaction refused: The sum of this and previously credited amounts (if any) exceeds debited amount"
  },
  "453": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Function",
    "approved": False,
    "merchant_message": "Invalid Function"
  },
  "1127": {
    "type": "Desjardins",
    "cardholder_message": "CARD NOT SUPPORTED",
    "approved": False,
    "merchant_message": "Declined. Caisse (branch) does not exist"
  },
  "421": {
    "type": "Paymentech",
    "cardholder_message": "Inv Purch Card Data",
    "approved": False,
    "merchant_message": "Inv Purch Card Data"
  },
  "1041": {
    "type": "Desjardins",
    "cardholder_message": "REFUND LIMIT",
    "approved": False,
    "merchant_message": "Declined. Limit in the no. of trans. or refund amount and Interac cancellations reached for the terminal"
  },
  "1032": {
    "type": "Desjardins",
    "cardholder_message": "REFUND LIMIT",
    "approved": False,
    "merchant_message": "Declined. Max refund amount for a transaction"
  },
  "1111": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. EMV - TVR error"
  },
  "505": {
    "type": "Vital",
    "cardholder_message": "Already Reversed",
    "approved": False,
    "merchant_message": "Already Reversed"
  },
  "147": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined INVALID TRAN DATE"
  },
  "26": {
    "type": "Bambora",
    "cardholder_message": "Invalid expiry date",
    "approved": False,
    "merchant_message": "Invalid expiry date"
  },
  "387": {
    "type": "Paymentech",
    "cardholder_message": "Incorrect Act Amt",
    "approved": False,
    "merchant_message": "Incorrect Act Amt"
  },
  "569": {
    "type": "Global Payments",
    "cardholder_message": "AP WITH ID",
    "approved": False,
    "merchant_message": "AP WITH ID"
  },
  "1077": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. EMV - TVR error"
  },
  "470": {
    "type": "Paymentech",
    "cardholder_message": "JCB Not Allowed",
    "approved": False,
    "merchant_message": "JCB Not Allowed"
  },
  "207": {
    "type": "Bambora",
    "cardholder_message": "Invalid merchant id",
    "approved": False,
    "merchant_message": "Invalid merchant id"
  },
  "484": {
    "type": "Paymentech",
    "cardholder_message": "Call Voice Op",
    "approved": False,
    "merchant_message": "Call Voice Op"
  },
  "674": {
    "type": "Bambora",
    "cardholder_message": "Payment declined",
    "approved": False,
    "merchant_message": "Payment declined"
  },
  "437": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Function",
    "approved": False,
    "merchant_message": "Invalid Function"
  },
  "705": {
    "type": "First Data",
    "cardholder_message": "DOWNLOAD FAILED",
    "approved": False,
    "merchant_message": "DOWNLOAD FAILED"
  },
  "771\u2013787": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "803": {
    "type": "Global Payments",
    "cardholder_message": "ISSUER UNAVAIL",
    "approved": False,
    "merchant_message": "ISSUER UNAVAIL"
  },
  "1083": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. PPC - Activation correction impossible"
  },
  "362": {
    "type": "Paymentech",
    "cardholder_message": "Invalid PIN",
    "approved": False,
    "merchant_message": "Invalid PIN"
  },
  "139": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined SERVICE MERCHANT NOT ON FILE"
  },
  "726": {
    "type": "First Data",
    "cardholder_message": "AMT EXCEEDED LIMIT",
    "approved": False,
    "merchant_message": "AMT EXCEEDED LIMIT"
  },
  "807": {
    "type": "Bambora",
    "cardholder_message": "Batch close completed successfully",
    "approved": False,
    "merchant_message": "Batch close completed successfully"
  },
  "345": {
    "type": "EBP/ACH",
    "cardholder_message": "Interbank reject - Other",
    "approved": False,
    "merchant_message": "Interbank reject - Other"
  },
  "571": {
    "type": "Global Payments",
    "cardholder_message": "INVLD AMOUNT",
    "approved": False,
    "merchant_message": "INVLD AMOUNT"
  },
  "730": {
    "type": "First Data",
    "cardholder_message": "REV REJECTED",
    "approved": False,
    "merchant_message": "REV REJECTED"
  },
  "525": {
    "type": "Vital",
    "cardholder_message": "Failure HV",
    "approved": False,
    "merchant_message": "Failure HV"
  },
  "659": {
    "type": "INTERAC Online",
    "cardholder_message": "CANNOT PROCESS PLEASE RE-TRY",
    "approved": False,
    "merchant_message": "RE-TRY SYSTEM PROBLEM"
  },
  "447": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Function",
    "approved": False,
    "merchant_message": "Invalid Function"
  },
  "154": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined BAD FORMAT"
  },
  "696": {
    "type": "First Data",
    "cardholder_message": "HOLD - CALL CTR",
    "approved": False,
    "merchant_message": "HOLD - CALL CTR"
  },
  "891": {
    "type": "UK",
    "cardholder_message": "Communication problems",
    "approved": False,
    "merchant_message": "Communication problems"
  },
  "731": {
    "type": "First Data",
    "cardholder_message": "ENTER LESSER AMOUNT",
    "approved": False,
    "merchant_message": "ENTER LESSER AMOUNT"
  },
  "887\u2013888": {
    "type": "UK",
    "cardholder_message": "Server error",
    "approved": False,
    "merchant_message": "Server error"
  },
  "488": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Term ID",
    "approved": False,
    "merchant_message": "Invalid Term ID"
  },
  "365": {
    "type": "Paymentech",
    "cardholder_message": "Not Online to XX",
    "approved": False,
    "merchant_message": "Not Online to XX"
  },
  "1010": {
    "type": "Desjardins",
    "cardholder_message": "TRX NOT ALLOWED",
    "approved": False,
    "merchant_message": "Declined. The transaction type is invalid"
  },
  "370": {
    "type": "Paymentech",
    "cardholder_message": "Card Not Allowed",
    "approved": False,
    "merchant_message": "Card Not Allowed"
  },
  "761": {
    "type": "Bambora",
    "cardholder_message": "Payment Canceled",
    "approved": False,
    "merchant_message": "Payment Canceled"
  },
  "60": {
    "type": "Bambora",
    "cardholder_message": "Declined - Operation restricted through Master Merchant",
    "approved": False,
    "merchant_message": "Declined - Operation restricted through Master Merchant"
  },
  "669": {
    "type": "INTERAC Online",
    "cardholder_message": "CANNOT PROCESS OVER STORE LIMIT",
    "approved": False,
    "merchant_message": "OVER RETAILER LIMIT"
  },
  "1081": {
    "type": "Desjardins",
    "cardholder_message": "INC. AMOUNT/CARD",
    "approved": False,
    "merchant_message": "Declined. PPC - Amount differs from the program"
  },
  "319": {
    "type": "Bambora",
    "cardholder_message": "CALL HELP DESK",
    "approved": False,
    "merchant_message": "Transaction Declined - Restricted transaction type"
  },
  "603": {
    "type": "Global Payments",
    "cardholder_message": "INVALID FIID",
    "approved": False,
    "merchant_message": "INVALID FIID"
  },
  "812": {
    "type": "Bambora",
    "cardholder_message": "Insufficient user permission for processing refund transactions",
    "approved": False,
    "merchant_message": "Insufficient user permission for processing refund transactions"
  },
  "1071": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. EMV - ARQC invalid"
  },
  "710": {
    "type": "First Data",
    "cardholder_message": "INV EXP DATE",
    "approved": False,
    "merchant_message": "INV EXP DATE"
  },
  "749": {
    "type": "Elavon",
    "cardholder_message": "REQ. EXCEEDS BAL. (Gift Card)",
    "approved": False,
    "merchant_message": "REQ. EXCEEDS BAL. (Gift Card)"
  },
  "372": {
    "type": "Paymentech",
    "cardholder_message": "BIN Not Allowed",
    "approved": False,
    "merchant_message": "BIN Not Allowed"
  },
  "1132": {
    "type": "Desjardins",
    "cardholder_message": "Invalid Accord D Transaction",
    "approved": False,
    "merchant_message": "Invalid Accord D Transaction"
  },
  "935": {
    "type": "Bambora",
    "cardholder_message": "Adjustment failed, please wait one minute and retry",
    "approved": False,
    "merchant_message": "Adjustment failed, please wait one minute and retry"
  },
  "1068": {
    "type": "Desjardins",
    "cardholder_message": "INVALID DATE",
    "approved": False,
    "merchant_message": "Declined. The expiry date of the card is invalid"
  },
  "473": {
    "type": "Paymentech",
    "cardholder_message": "No Sponsor Inst",
    "approved": False,
    "merchant_message": "No Sponsor Inst"
  },
  "324": {
    "type": "Bambora",
    "cardholder_message": "CALL HELP DESK",
    "approved": False,
    "merchant_message": "Invalid product quantity"
  },
  "198": {
    "type": "Bambora",
    "cardholder_message": "Zero value transactions cannot be voided",
    "approved": False,
    "merchant_message": "Zero value transactions cannot be voided"
  },
  "148": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined INVALID EXP DATE"
  },
  "691": {
    "type": "First Data",
    "cardholder_message": "INV TERMINAL",
    "approved": False,
    "merchant_message": "INV TERMINAL"
  },
  "480": {
    "type": "Paymentech",
    "cardholder_message": "Bat Already Rels",
    "approved": False,
    "merchant_message": "Bat Already Rels"
  },
  "553": {
    "type": "Vital",
    "cardholder_message": "Unpaid Items",
    "approved": False,
    "merchant_message": "Unpaid Items"
  },
  "214": {
    "type": "Bambora",
    "cardholder_message": "Transaction reversed",
    "approved": False,
    "merchant_message": "Transaction reversed"
  },
  "662\u2013664": {
    "type": "INTERAC Online",
    "cardholder_message": "CANNOT PROCESS PLEASE RETRY",
    "approved": False,
    "merchant_message": "RE-TRY EDIT ERROR"
  },
  "322": {
    "type": "Bambora",
    "cardholder_message": "CALL HELP DESK",
    "approved": False,
    "merchant_message": "Transaction amount does not match inventory calculation"
  },
  "600": {
    "type": "Global Payments",
    "cardholder_message": "INVALID POS CARD",
    "approved": False,
    "merchant_message": "INVALID POS CARD"
  },
  "920": {
    "type": "UK",
    "cardholder_message": "Acquirer error. Transaction not processed",
    "approved": False,
    "merchant_message": "Acquirer error. Transaction not processed"
  },
  "429": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Term ID",
    "approved": False,
    "merchant_message": "Invalid Term ID"
  },
  "594": {
    "type": "Global Payments",
    "cardholder_message": "DB UNAVAIL 02",
    "approved": False,
    "merchant_message": "DB UNAVAIL 02"
  },
  "741": {
    "type": "First Data",
    "cardholder_message": "DBTSW PIN XL ERR",
    "approved": False,
    "merchant_message": "DBTSW PIN XL ERR"
  },
  "459": {
    "type": "Paymentech",
    "cardholder_message": "DC Not Allowed",
    "approved": False,
    "merchant_message": "DC Not Allowed"
  },
  "873": {
    "type": "UK",
    "cardholder_message": "Server error, no transaction sent to acquirer",
    "approved": False,
    "merchant_message": "Server error, no transaction sent to acquirer"
  },
  "389": {
    "type": "Paymentech",
    "cardholder_message": "Auth Busy - Retry",
    "approved": False,
    "merchant_message": "Auth Busy - Retry"
  },
  "1112": {
    "type": "Desjardins",
    "cardholder_message": "UNABLE TO PROCESS",
    "approved": False,
    "merchant_message": "Declined. Error in the tax calculation"
  },
  "1106": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. Limit exceeded"
  },
  "634": {
    "type": "INTERAC Online",
    "cardholder_message": "APPROVED THANKS",
    "approved": True,
    "merchant_message": "APPROVED"
  },
  "563": {
    "type": "Global Payments",
    "cardholder_message": "CALL",
    "approved": False,
    "merchant_message": "CALL"
  },
  "580\u2013581": {
    "type": "Global Payments",
    "cardholder_message": "INV ACCT MATCH",
    "approved": False,
    "merchant_message": "INV ACCT MATCH"
  },
  "124\u2013126": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "1092": {
    "type": "Desjardins",
    "cardholder_message": "FORMAT ERROR",
    "approved": False,
    "merchant_message": "Declined. Error in the Desjardins host acquirer system"
  },
  "335": {
    "type": "EBP/ACH",
    "cardholder_message": "Funds not cleared",
    "approved": False,
    "merchant_message": "Funds not cleared"
  },
  "72": {
    "type": "TD",
    "cardholder_message": "Declined EXPIRED CARD",
    "approved": False,
    "merchant_message": "Declined EXPIRED CARD"
  },
  "54": {
    "type": "Bambora",
    "cardholder_message": "Transaction timeout - No available device",
    "approved": False,
    "merchant_message": "Transaction timeout - No available device"
  },
  "551": {
    "type": "Vital",
    "cardholder_message": "Invalid ABA",
    "approved": False,
    "merchant_message": "Invalid ABA"
  },
  "921": {
    "type": "UK",
    "cardholder_message": "System error",
    "approved": False,
    "merchant_message": "System error"
  },
  "426": {
    "type": "Paymentech",
    "cardholder_message": "CVD Data Error",
    "approved": False,
    "merchant_message": "CVD Data Error"
  },
  "481": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Rtng Ind",
    "approved": False,
    "merchant_message": "Invalid Rtng Ind"
  },
  "560": {
    "type": "Bambora",
    "cardholder_message": "Transaction In Process",
    "approved": False,
    "merchant_message": "Transaction In Process"
  },
  "482": {
    "type": "Paymentech",
    "cardholder_message": "AX Not Allowed",
    "approved": False,
    "merchant_message": "AX Not Allowed"
  },
  "898": {
    "type": "UK",
    "cardholder_message": "Invalid Merchant ID",
    "approved": False,
    "merchant_message": "Invalid Merchant ID"
  },
  "886": {
    "type": "UK",
    "cardholder_message": "Transaction refused: Velocity check rule violation (details provided in description)",
    "approved": False,
    "merchant_message": "Transaction refused: Velocity check rule violation (details provided in description)"
  },
  "1074": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. EMV - Key cannot be found in the security module"
  },
  "461": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Key",
    "approved": False,
    "merchant_message": "Invalid Key"
  },
  "1107": {
    "type": "Desjardins",
    "cardholder_message": "HOLD CARD",
    "approved": False,
    "merchant_message": "Declined. Amount exceeds the limit"
  },
  "1051": {
    "type": "Desjardins",
    "cardholder_message": "CALL FOR AUTH",
    "approved": False,
    "merchant_message": "Declined. Maximum amount limit for the day reached"
  },
  "745": {
    "type": "Elavon",
    "cardholder_message": "INVALID CARD (Gift Card)",
    "approved": False,
    "merchant_message": "INVALID CARD (Gift Card)"
  },
  "1110": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. EMV - CVR error"
  },
  "1035": {
    "type": "Desjardins",
    "cardholder_message": "NOT AVAILABLE",
    "approved": False,
    "merchant_message": "Declined. Balance inquiry transaction not permitted"
  },
  "906": {
    "type": "UK",
    "cardholder_message": "Invalid Card Type",
    "approved": False,
    "merchant_message": "Invalid Card Type"
  },
  "1021": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. Format error in the transaction"
  },
  "1122": {
    "type": "Desjardins",
    "cardholder_message": "ADM PIN NOT IN FILE",
    "approved": False,
    "merchant_message": "Declined. Unrecognized administrative card"
  },
  "917": {
    "type": "UK",
    "cardholder_message": "Invalid Issue",
    "approved": False,
    "merchant_message": "Invalid Issue"
  },
  "514": {
    "type": "Vital",
    "cardholder_message": "Date Error",
    "approved": False,
    "merchant_message": "Date Error"
  },
  "815": {
    "type": "Bambora",
    "cardholder_message": "Invalid session source",
    "approved": False,
    "merchant_message": "Invalid session source"
  },
  "701": {
    "type": "First Data",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "PLEASE RETRY"
  },
  "885": {
    "type": "UK",
    "cardholder_message": "The Originating Account Type parameter is invalid",
    "approved": False,
    "merchant_message": "The Originating Account Type parameter is invalid"
  },
  "435": {
    "type": "Paymentech",
    "cardholder_message": "Too Many Batches",
    "approved": False,
    "merchant_message": "Too Many Batches"
  },
  "637": {
    "type": "INTERAC Online",
    "cardholder_message": "EXPIRED CARD REFER TO BRANCH",
    "approved": False,
    "merchant_message": "EXPIRED CARD REFER TO BRANCH"
  },
  "386": {
    "type": "Paymentech",
    "cardholder_message": "Block Act Not Alwd",
    "approved": False,
    "merchant_message": "Block Act Not Alwd"
  },
  "683": {
    "type": "Bambora",
    "cardholder_message": "Declined. Missing or invalid merchant data.",
    "approved": False,
    "merchant_message": "Declined. Missing or invalid merchant data."
  },
  "1115": {
    "type": "Desjardins",
    "cardholder_message": "CARD NOT SUPPORTED",
    "approved": False,
    "merchant_message": "Declined."
  },
  "87": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined ADJ NOT ALLOWED"
  },
  "900": {
    "type": "UK",
    "cardholder_message": "Server error",
    "approved": False,
    "merchant_message": "Server error"
  },
  "391": {
    "type": "Paymentech",
    "cardholder_message": "Auth Error - Retry",
    "approved": False,
    "merchant_message": "Auth Error - Retry"
  },
  "423": {
    "type": "Paymentech",
    "cardholder_message": "Invalid EC Data 329",
    "approved": False,
    "merchant_message": "Invalid EC Data 329"
  },
  "913": {
    "type": "UK",
    "cardholder_message": "Corrupt input data to server",
    "approved": False,
    "merchant_message": "Corrupt input data to server"
  },
  "748": {
    "type": "Elavon",
    "cardholder_message": "ALREADY ACTIVE (Gift Card)",
    "approved": False,
    "merchant_message": "ALREADY ACTIVE (Gift Card)"
  },
  "570": {
    "type": "Global Payments",
    "cardholder_message": "INVLD",
    "approved": False,
    "merchant_message": "INVLD"
  },
  "218": {
    "type": "Bambora",
    "cardholder_message": "DECLINE",
    "approved": False,
    "merchant_message": "Transaction Declined AC"
  },
  "931": {
    "type": "UK",
    "cardholder_message": "Operation cannot be performed at this time: [Description]",
    "approved": False,
    "merchant_message": "Operation cannot be performed at this time: [Description]"
  },
  "871": {
    "type": "UK",
    "cardholder_message": "Invalid track 2 data",
    "approved": False,
    "merchant_message": "Invalid track 2 data"
  },
  "515\u2013521": {
    "type": "Vital",
    "cardholder_message": "Decline",
    "approved": False,
    "merchant_message": "Decline"
  },
  "1031": {
    "type": "Desjardins",
    "cardholder_message": "REFUND LIMIT",
    "approved": False,
    "merchant_message": "Declined. Max offline refund amount reached for a card for the period"
  },
  "1109": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. EMV - ARQC error"
  },
  "1099": {
    "type": "Desjardins",
    "cardholder_message": "PIN TRIES EXCEEDED",
    "approved": False,
    "merchant_message": "Declined. Number of PIN attempts exceeded"
  },
  "808": {
    "type": "Bambora",
    "cardholder_message": "Batch close failed on all terminals",
    "approved": False,
    "merchant_message": "Batch close failed on all terminals"
  },
  "585": {
    "type": "Global Payments",
    "cardholder_message": "USE DUP THEN BAL",
    "approved": False,
    "merchant_message": "USE DUP THEN BAL"
  },
  "552": {
    "type": "Vital",
    "cardholder_message": "Amount Error",
    "approved": False,
    "merchant_message": "Amount Error"
  },
  "547": {
    "type": "Vital",
    "cardholder_message": "CVV2 Mismatch",
    "approved": False,
    "merchant_message": "CVV2 Mismatch"
  },
  "158": {
    "type": "TD",
    "cardholder_message": "PLEASE TRY AGAIN",
    "approved": False,
    "merchant_message": "Declined - TIMEOUT"
  },
  "719": {
    "type": "First Data",
    "cardholder_message": "INVL ARRIVAL-DT",
    "approved": False,
    "merchant_message": "INVL ARRIVAL-DT"
  },
  "149": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined INVALID TRANCODE"
  },
  "529": {
    "type": "Vital",
    "cardholder_message": "No Account",
    "approved": False,
    "merchant_message": "No Account"
  },
  "178": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined ADMIN CARD NOT ALLOWED"
  },
  "535": {
    "type": "Vital",
    "cardholder_message": "No Save Account",
    "approved": False,
    "merchant_message": "No Save Account"
  },
  "737": {
    "type": "First Data",
    "cardholder_message": "UNDEFINED CARD",
    "approved": False,
    "merchant_message": "UNDEFINED CARD"
  },
  "753": {
    "type": "Elavon",
    "cardholder_message": "SEQ ERR PLS CALL (Gift Card)",
    "approved": False,
    "merchant_message": "SEQ ERR PLS CALL (Gift Card)"
  },
  "914": {
    "type": "UK",
    "cardholder_message": "Invalid LARID",
    "approved": False,
    "merchant_message": "Invalid LARID"
  },
  "877": {
    "type": "UK",
    "cardholder_message": "Transaction refused: Reference transaction already captured",
    "approved": False,
    "merchant_message": "Transaction refused: Reference transaction already captured"
  },
  "360": {
    "type": "Paymentech",
    "cardholder_message": "Call Voice Oper",
    "approved": False,
    "merchant_message": "Call Voice Oper"
  },
  "443": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Function",
    "approved": False,
    "merchant_message": "Invalid Function"
  },
  "346": {
    "type": "Paymentech",
    "cardholder_message": "Approved",
    "approved": True,
    "merchant_message": "Approved"
  },
  "596": {
    "type": "Global Payments",
    "cardholder_message": "DB UNAVAIL 04",
    "approved": False,
    "merchant_message": "DB UNAVAIL 04"
  },
  "834": {
    "type": "UK",
    "cardholder_message": "Server configuration error",
    "approved": False,
    "merchant_message": "Server configuration error"
  },
  "88": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "407": {
    "type": "Paymentech",
    "cardholder_message": "Entry Mode Invalid",
    "approved": False,
    "merchant_message": "Entry Mode Invalid"
  },
  "1075": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. EMV - ATC error"
  },
  "476": {
    "type": "Paymentech",
    "cardholder_message": "Amount Too Large",
    "approved": False,
    "merchant_message": "Amount Too Large"
  },
  "457": {
    "type": "Paymentech",
    "cardholder_message": "Rev Not Allowed",
    "approved": False,
    "merchant_message": "Rev Not Allowed"
  },
  "1126": {
    "type": "Desjardins",
    "cardholder_message": "ACCOUNT NOT SET UP",
    "approved": False,
    "merchant_message": "Declined. Non-existent account"
  },
  "743": {
    "type": "Elavon",
    "cardholder_message": "APPROVAL",
    "approved": True,
    "merchant_message": "APPROVAL"
  },
  "1082": {
    "type": "Desjardins",
    "cardholder_message": "INVALID AMOUNT",
    "approved": False,
    "merchant_message": "Declined. PPC - The amount does not correspond with the program"
  },
  "864": {
    "type": "UK",
    "cardholder_message": "Transaction refused: Merchant ID not active.",
    "approved": False,
    "merchant_message": "Transaction refused: Merchant ID not active."
  },
  "930": {
    "type": "UK",
    "cardholder_message": "Business rule violation: [Description]",
    "approved": False,
    "merchant_message": "Business rule violation: [Description]"
  },
  "1045": {
    "type": "Desjardins",
    "cardholder_message": "SYSTEM NOT AVAIL.",
    "approved": False,
    "merchant_message": "Declined. The authorization host is not available"
  },
  "415": {
    "type": "Paymentech",
    "cardholder_message": "Inv MSDI",
    "approved": False,
    "merchant_message": "Inv MSDI"
  },
  "356": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Bank MID",
    "approved": False,
    "merchant_message": "Invalid Bank MID"
  },
  "1043": {
    "type": "Desjardins",
    "cardholder_message": "INVALID CARD",
    "approved": False,
    "merchant_message": "Declined. The check digit of the card number is invalid"
  },
  "601": {
    "type": "Global Payments",
    "cardholder_message": "ACCT TYPE INVLD",
    "approved": False,
    "merchant_message": "ACCT TYPE INVLD"
  },
  "908": {
    "type": "UK",
    "cardholder_message": "Invalid Currency Subunit",
    "approved": False,
    "merchant_message": "Invalid Currency Subunit"
  },
  "380": {
    "type": "Paymentech",
    "cardholder_message": "*Request Denied*",
    "approved": False,
    "merchant_message": "*Request Denied*"
  },
  "865": {
    "type": "UK",
    "cardholder_message": "Server error, no transaction sent to acquirer",
    "approved": False,
    "merchant_message": "Server error, no transaction sent to acquirer"
  },
  "353": {
    "type": "Paymentech",
    "cardholder_message": "Invalid ICA No",
    "approved": False,
    "merchant_message": "Invalid ICA No"
  },
  "413": {
    "type": "Paymentech",
    "cardholder_message": "Inv PIN Capability",
    "approved": False,
    "merchant_message": "Inv PIN Capability"
  },
  "1015": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. Auth. type incorrectly defined. Host problem"
  },
  "835\u2013836": {
    "type": "UK",
    "cardholder_message": "Server error, no transaction sent to acquirer",
    "approved": False,
    "merchant_message": "Server error, no transaction sent to acquirer"
  },
  "438": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Term ID",
    "approved": False,
    "merchant_message": "Invalid Term ID"
  },
  "881": {
    "type": "UK",
    "cardholder_message": "Transaction refused: Capture amount exceeds authorized amount",
    "approved": False,
    "merchant_message": "Transaction refused: Capture amount exceeds authorized amount"
  },
  "767": {
    "type": "EBP/ACH",
    "cardholder_message": "Agreement revoked - Business",
    "approved": False,
    "merchant_message": "Agreement revoked - Business"
  },
  "878": {
    "type": "UK",
    "cardholder_message": "Required data was too long",
    "approved": False,
    "merchant_message": "Required data was too long"
  },
  "810": {
    "type": "Bambora",
    "cardholder_message": "Batch close failed on store and forward",
    "approved": False,
    "merchant_message": "Batch close failed on store and forward"
  },
  "394": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Term ID",
    "approved": False,
    "merchant_message": "Invalid Term ID"
  },
  "150\u2013153": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "681": {
    "type": "Bambora",
    "cardholder_message": "Payment method not accepted on this account",
    "approved": False,
    "merchant_message": "Payment method not accepted on this account"
  },
  "1088": {
    "type": "Desjardins",
    "cardholder_message": "FORMAT ERROR",
    "approved": False,
    "merchant_message": "Declined. Error in the format of the transaction"
  },
  "866": {
    "type": "UK",
    "cardholder_message": "Transaction refused",
    "approved": False,
    "merchant_message": "Transaction refused"
  },
  "837": {
    "type": "UK",
    "cardholder_message": "Bank system error",
    "approved": False,
    "merchant_message": "Bank system error"
  },
  "1064": {
    "type": "Desjardins",
    "cardholder_message": "NEED ADMIN CARD",
    "approved": False,
    "merchant_message": "Declined. Admin card required. Currently only validated for admin PIN change transactions"
  },
  "486\u2013487": {
    "type": "Paymentech",
    "cardholder_message": "Auth Busy-Retry",
    "approved": False,
    "merchant_message": "Auth Busy-Retry"
  },
  "791": {
    "type": "Europay, Mastercard, Visa",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "703": {
    "type": "First Data",
    "cardholder_message": "SYSTEM PROBLEM",
    "approved": False,
    "merchant_message": "SYSTEM PROBLEM"
  },
  "1053": {
    "type": "Desjardins",
    "cardholder_message": "CALL SERVICE",
    "approved": False,
    "merchant_message": "Declined. System error"
  },
  "21": {
    "type": "Bambora",
    "cardholder_message": "Validation is less than the minimum amount",
    "approved": False,
    "merchant_message": "Validation is less than the minimum amount"
  },
  "193": {
    "type": "Bambora",
    "cardholder_message": "Amount does not match the transaction you are modifying.",
    "approved": False,
    "merchant_message": "Amount does not match the transaction you are modifying."
  },
  "922": {
    "type": "UK",
    "cardholder_message": "Invalid track 2 data",
    "approved": False,
    "merchant_message": "Invalid track 2 data"
  },
  "916": {
    "type": "UK",
    "cardholder_message": "Invalid Start Date",
    "approved": False,
    "merchant_message": "Invalid Start Date"
  },
  "452": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Term ID",
    "approved": False,
    "merchant_message": "Invalid Term ID"
  },
  "1007": {
    "type": "Desjardins",
    "cardholder_message": "ADM PIN TRIES EXCEE",
    "approved": False,
    "merchant_message": "Declined. Max PIN attempts with an Administrative card reached"
  },
  "381": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Driver Number",
    "approved": False,
    "merchant_message": "Invalid Driver Number"
  },
  "331": {
    "type": "EBP/ACH",
    "cardholder_message": "Payment Stopped",
    "approved": False,
    "merchant_message": "Payment Stopped"
  },
  "645": {
    "type": "INTERAC Online",
    "cardholder_message": "PIN ERROR PLEASE RE-TRY",
    "approved": False,
    "merchant_message": "RE-TRY EDIT ERROR"
  },
  "399": {
    "type": "Paymentech",
    "cardholder_message": "Amt Entry Error",
    "approved": False,
    "merchant_message": "Amt Entry Error"
  },
  "544": {
    "type": "Vital",
    "cardholder_message": "System Error",
    "approved": False,
    "merchant_message": "System Error"
  },
  "868-870": {
    "type": "UK",
    "cardholder_message": "System error",
    "approved": False,
    "merchant_message": "System error"
  },
  "297-310": {
    "type": "Bambora",
    "cardholder_message": "Service Unavailable - Please try again later",
    "approved": False,
    "merchant_message": "Service Unavailable - Please try again later"
  },
  "379": {
    "type": "Paymentech",
    "cardholder_message": "Auth Declined",
    "approved": False,
    "merchant_message": "Auth Declined"
  },
  "606": {
    "type": "Global Payments",
    "cardholder_message": "INVALID STATE CD",
    "approved": False,
    "merchant_message": "INVALID STATE CD"
  },
  "740": {
    "type": "First Data",
    "cardholder_message": "RESUB EXCDS LMT",
    "approved": False,
    "merchant_message": "RESUB EXCDS LMT"
  },
  "583": {
    "type": "Global Payments",
    "cardholder_message": "ITEM ADJ",
    "approved": False,
    "merchant_message": "ITEM ADJ"
  },
  "579": {
    "type": "Global Payments",
    "cardholder_message": "SYSTEM UNAVAILABLE",
    "approved": False,
    "merchant_message": "SYSTEM UNAVAILABLE"
  },
  "592": {
    "type": "Global Payments",
    "cardholder_message": "TRAN TYPE INVLD",
    "approved": False,
    "merchant_message": "TRAN TYPE INVLD"
  },
  "720": {
    "type": "First Data",
    "cardholder_message": "INVL CHECKOUT DT",
    "approved": False,
    "merchant_message": "INVL CHECKOUT DT"
  },
  "1005": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined"
  },
  "1011": {
    "type": "Desjardins",
    "cardholder_message": "TRX NOT ALLOWED",
    "approved": False,
    "merchant_message": "Declined. The transaction type is not supported on this terminal"
  },
  "448": {
    "type": "Paymentech",
    "cardholder_message": "Amount Too Large",
    "approved": False,
    "merchant_message": "Amount Too Large"
  },
  "1019": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. The transaction date is invalid."
  },
  "1002": {
    "type": "Desjardins",
    "cardholder_message": "APPROVED",
    "approved": True,
    "merchant_message": "Approved without the balance"
  },
  "744": {
    "type": "Elavon",
    "cardholder_message": "DECLINED-HELP 9999 (Gift Card \u2013 Host Busy)",
    "approved": False,
    "merchant_message": "DECLINED-HELP 9999 (Gift Card \u2013 Host Busy)"
  },
  "721": {
    "type": "First Data",
    "cardholder_message": "INVL ROOM RATE",
    "approved": False,
    "merchant_message": "INVL ROOM RATE"
  },
  "200": {
    "type": "Bambora",
    "cardholder_message": "Transaction cannot be adjusted",
    "approved": False,
    "merchant_message": "Transaction cannot be adjusted"
  },
  "424": {
    "type": "Paymentech",
    "cardholder_message": "INV Function or Multiple FS or Unknown TKN",
    "approved": False,
    "merchant_message": "INV Function or Multiple FS or Unknown TKN"
  },
  "128\u2013138": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "1054": {
    "type": "Desjardins",
    "cardholder_message": "CALL SERVICE",
    "approved": False,
    "merchant_message": "Declined. System error"
  },
  "692": {
    "type": "First Data",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "PLEASE RETRY"
  },
  "91": {
    "type": "TD",
    "cardholder_message": "PLEASE TRY AGAIN",
    "approved": False,
    "merchant_message": "Declined"
  },
  "417": {
    "type": "Paymentech",
    "cardholder_message": "Inv Pref Cust Ind",
    "approved": False,
    "merchant_message": "Inv Pref Cust Ind"
  },
  "937": {
    "type": "Bambora",
    "cardholder_message": "Declined please try again",
    "approved": False,
    "merchant_message": "Single use token service unavailable"
  },
  "578": {
    "type": "Global Payments",
    "cardholder_message": "AP DUPE",
    "approved": False,
    "merchant_message": "AP DUPE"
  },
  "1129": {
    "type": "Desjardins",
    "cardholder_message": "SELECT OTHER ACCT",
    "approved": False,
    "merchant_message": "Declined. Account does not exist"
  },
  "361": {
    "type": "Paymentech",
    "cardholder_message": "Lost/Stolen Card",
    "approved": False,
    "merchant_message": "Lost/Stolen Card"
  },
  "639\u2013640": {
    "type": "INTERAC Online",
    "cardholder_message": "CANNOT PROCESS PLEASE RE-TRY",
    "approved": False,
    "merchant_message": "RE-TRY INVALID TRANSACTION"
  },
  "732": {
    "type": "First Data",
    "cardholder_message": "PIN XLATE ERROR",
    "approved": False,
    "merchant_message": "PIN XLATE ERROR"
  },
  "872": {
    "type": "UK",
    "cardholder_message": "Invalid track 2 expiry date",
    "approved": False,
    "merchant_message": "Invalid track 2 expiry date"
  },
  "1006": {
    "type": "Desjardins",
    "cardholder_message": "EXPIRED CARD",
    "approved": False,
    "merchant_message": "Declined. Expired card"
  },
  "155": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined BAD DATA"
  },
  "436": {
    "type": "Paymentech",
    "cardholder_message": "Release Batch",
    "approved": False,
    "merchant_message": "Release Batch"
  },
  "1116": {
    "type": "Desjardins",
    "cardholder_message": "SELECT OTHER ACCT",
    "approved": False,
    "merchant_message": "Declined. Inactive Desjardins Interac account"
  },
  "751": {
    "type": "Elavon",
    "cardholder_message": "NON RELOADABLE (Gift Card)",
    "approved": False,
    "merchant_message": "NON RELOADABLE (Gift Card)"
  },
  "106\u2013108": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "539": {
    "type": "Vital",
    "cardholder_message": "Sec Violation",
    "approved": False,
    "merchant_message": "Sec Violation"
  },
  "682": {
    "type": "Bambora",
    "cardholder_message": "Decline",
    "approved": False,
    "merchant_message": "Decline"
  },
  "321": {
    "type": "Bambora",
    "cardholder_message": "CALL HELP DESK",
    "approved": False,
    "merchant_message": "Missing or invalid return URL"
  },
  "1037": {
    "type": "Desjardins",
    "cardholder_message": "OVER MAX NUMBER TRX",
    "approved": False,
    "merchant_message": "Declined. The number of refunds for this card type has been reached"
  },
  "1017": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. Partial cancellations are not supported"
  },
  "104": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined NUM TIMES USED"
  },
  "330": {
    "type": "EBP/ACH",
    "cardholder_message": "Invalid Account",
    "approved": False,
    "merchant_message": "Invalid Account"
  },
  "852": {
    "type": "UK",
    "cardholder_message": "No response from bank before client timeout",
    "approved": False,
    "merchant_message": "No response from bank before client timeout"
  },
  "53": {
    "type": "Bambora",
    "cardholder_message": "Application Error - Sending Request",
    "approved": False,
    "merchant_message": "Application Error - Sending Request"
  },
  "479": {
    "type": "Paymentech",
    "cardholder_message": "Tran Not Allowed",
    "approved": False,
    "merchant_message": "Tran Not Allowed"
  },
  "314": {
    "type": "Bambora",
    "cardholder_message": "Missing or invalid payment information - Please validate all required payment information.",
    "approved": False,
    "merchant_message": "Missing or invalid consumer payment information"
  },
  "643": {
    "type": "INTERAC Online",
    "cardholder_message": "USAGE EXCEEDED REFER TO BRANCH",
    "approved": False,
    "merchant_message": "USAGE EXCEEDED REFER TO BRANCH"
  },
  "894": {
    "type": "UK",
    "cardholder_message": "Transaction refused",
    "approved": False,
    "merchant_message": "Transaction refused"
  },
  "690": {
    "type": "First Data",
    "cardholder_message": "INV ACCT NUM",
    "approved": False,
    "merchant_message": "INV ACCT NUM"
  },
  "556": {
    "type": "Vital",
    "cardholder_message": "Too Many Checks",
    "approved": False,
    "merchant_message": "Too Many Checks"
  },
  "325": {
    "type": "Bambora",
    "cardholder_message": "File Transfer Approved",
    "approved": True,
    "merchant_message": "File Transfer Approved"
  },
  "598": {
    "type": "Global Payments",
    "cardholder_message": "INVALID CARD",
    "approved": False,
    "merchant_message": "INVALID CARD"
  },
  "929": {
    "type": "UK",
    "cardholder_message": "Illegal argument: [Description]",
    "approved": False,
    "merchant_message": "Illegal argument: [Description]"
  },
  "512": {
    "type": "Vital",
    "cardholder_message": "Check Digit Err",
    "approved": False,
    "merchant_message": "Check Digit Err"
  },
  "926": {
    "type": "UK",
    "cardholder_message": "Pick up card",
    "approved": False,
    "merchant_message": "Pick up card"
  },
  "51": {
    "type": "Bambora",
    "cardholder_message": "DECLINE",
    "approved": False,
    "merchant_message": "Restricted Card or IP"
  },
  "161": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined BAD RESPONSE LENGTH"
  },
  "411": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Format",
    "approved": False,
    "merchant_message": "Invalid Format"
  },
  "739": {
    "type": "First Data",
    "cardholder_message": "TRAN CT EXCD LMT",
    "approved": False,
    "merchant_message": "TRAN CT EXCD LMT"
  },
  "1027": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. Insufficient funds"
  },
  "577": {
    "type": "Global Payments",
    "cardholder_message": "MAX PIN RETRIES",
    "approved": False,
    "merchant_message": "MAX PIN RETRIES"
  },
  "763": {
    "type": "EBP/ACH",
    "cardholder_message": "Not in accordance with agreement - Personal",
    "approved": False,
    "merchant_message": "Not in accordance with agreement - Personal"
  },
  "927": {
    "type": "UK",
    "cardholder_message": "Originating account type value not supported",
    "approved": False,
    "merchant_message": "Originating account type value not supported"
  },
  "511": {
    "type": "Vital",
    "cardholder_message": "Cashback Not Avl",
    "approved": False,
    "merchant_message": "Cashback Not Avl"
  },
  "548": {
    "type": "Vital",
    "cardholder_message": "Duplicate Trans",
    "approved": False,
    "merchant_message": "Duplicate Trans"
  },
  "434": {
    "type": "Paymentech",
    "cardholder_message": "Proc Error 7",
    "approved": False,
    "merchant_message": "Proc Error 7"
  },
  "510": {
    "type": "Vital",
    "cardholder_message": "Cashback Not App",
    "approved": False,
    "merchant_message": "Cashback Not App"
  },
  "73\u201375": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "867": {
    "type": "UK",
    "cardholder_message": "Transaction refused. Card Expired",
    "approved": False,
    "merchant_message": "Transaction refused. Card Expired"
  },
  "589": {
    "type": "Global Payments",
    "cardholder_message": "AP NOT CAPTURED",
    "approved": False,
    "merchant_message": "AP NOT CAPTURED"
  },
  "766": {
    "type": "EBP/ACH",
    "cardholder_message": "Not in accordance with agreement - Business",
    "approved": False,
    "merchant_message": "Not in accordance with agreement - Business"
  },
  "445": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Function",
    "approved": False,
    "merchant_message": "Invalid Function"
  },
  "862": {
    "type": "UK",
    "cardholder_message": "Transaction refused: Server temporarily unavailable",
    "approved": False,
    "merchant_message": "Transaction refused: Server temporarily unavailable"
  },
  "472": {
    "type": "Paymentech",
    "cardholder_message": "Bank Not On File",
    "approved": False,
    "merchant_message": "Bank Not On File"
  },
  "524": {
    "type": "Vital",
    "cardholder_message": "Expired Card",
    "approved": False,
    "merchant_message": "Expired Card"
  },
  "1093": {
    "type": "Desjardins",
    "cardholder_message": "TERMINAL DEACTIVATED",
    "approved": False,
    "merchant_message": "Declined. The terminal is deactivated at the Desjardins acquirer host"
  },
  "687": {
    "type": "First Data",
    "cardholder_message": "APPRV LESSER AMT",
    "approved": False,
    "merchant_message": "APPRV LESSER AMT"
  },
  "1102": {
    "type": "Desjardins",
    "cardholder_message": "HOLD CARD",
    "approved": False,
    "merchant_message": "Declined. Stolen card"
  },
  "393": {
    "type": "Paymentech",
    "cardholder_message": "Err - Pls Retry",
    "approved": False,
    "merchant_message": "Err - Pls Retry"
  },
  "1067": {
    "type": "Desjardins",
    "cardholder_message": "CALL SERVICE",
    "approved": False,
    "merchant_message": "Declined. The transaction date is invalid"
  },
  "756": {
    "type": "Elavon",
    "cardholder_message": "PICK UP CARD",
    "approved": False,
    "merchant_message": "PICK UP CARD"
  },
  "462": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Key",
    "approved": False,
    "merchant_message": "Invalid Key"
  },
  "1024": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. Routing problem"
  },
  "215": {
    "type": "Bambora",
    "cardholder_message": "Address Validation Failed",
    "approved": False,
    "merchant_message": "Address Validation Failed"
  },
  "925": {
    "type": "UK",
    "cardholder_message": "Server configuration error",
    "approved": False,
    "merchant_message": "Server configuration error"
  },
  "1063": {
    "type": "Desjardins",
    "cardholder_message": "INVALID ADMIN PIN",
    "approved": False,
    "merchant_message": "Declined. The administrative PIN is invalid"
  },
  "597": {
    "type": "Global Payments",
    "cardholder_message": "UNAUTH USER",
    "approved": False,
    "merchant_message": "UNAUTH USER"
  },
  "804": {
    "type": "Bambora",
    "cardholder_message": "Declined - Entered Information Cannot Be Authenticated",
    "approved": False,
    "merchant_message": "Declined - Entered Information Cannot Be Authenticated"
  },
  "652": {
    "type": "INTERAC Online",
    "cardholder_message": "INVALID CARD REFER TO BRANCH",
    "approved": False,
    "merchant_message": "CARD NOT SUPPORTED REFER TO BRANCH"
  },
  "939": {
    "type": "First Data",
    "cardholder_message": "Reversal Outside Window",
    "approved": False,
    "merchant_message": "Reversal Outside Window"
  },
  "371": {
    "type": "Paymentech",
    "cardholder_message": "PL Setup Reqd",
    "approved": False,
    "merchant_message": "PL Setup Reqd"
  },
  "736": {
    "type": "First Data",
    "cardholder_message": "ISSUER UNAV",
    "approved": False,
    "merchant_message": "ISSUER UNAV"
  },
  "558": {
    "type": "Bambora",
    "cardholder_message": "Decline",
    "approved": False,
    "merchant_message": "Decline"
  },
  "604": {
    "type": "Global Payments",
    "cardholder_message": "VERIFY",
    "approved": False,
    "merchant_message": "VERIFY"
  },
  "349": {
    "type": "Paymentech",
    "cardholder_message": "Hold - Call",
    "approved": False,
    "merchant_message": "Hold - Call"
  },
  "1033": {
    "type": "Desjardins",
    "cardholder_message": "OVER MAX NUMBER TRX",
    "approved": False,
    "merchant_message": "Declined. Max number of refunds reached for a card for the period"
  },
  "789": {
    "type": "Bambora",
    "cardholder_message": "Card Number Mismatch",
    "approved": False,
    "merchant_message": "Card Number Mismatch"
  },
  "656": {
    "type": "INTERAC Online",
    "cardholder_message": "CANNOT PROCESS PLEASE RETRY",
    "approved": False,
    "merchant_message": "RE-TRY EDIT ERROR"
  },
  "101\u2013102": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "829": {
    "type": "UK",
    "cardholder_message": "Duplicate transaction found",
    "approved": False,
    "merchant_message": "Duplicate transaction found"
  },
  "315": {
    "type": "Bambora",
    "cardholder_message": "CALL HELP DESK",
    "approved": False,
    "merchant_message": "HTTPS Connection Required"
  },
  "609": {
    "type": "Global Payments",
    "cardholder_message": "SCAN UNAVAILABLE",
    "approved": False,
    "merchant_message": "SCAN UNAVAILABLE"
  },
  "1128": {
    "type": "Desjardins",
    "cardholder_message": "CARD NOT SET UP",
    "approved": False,
    "merchant_message": "Declined. Card inactive at the Desjardins Interac issuing host"
  },
  "1108": {
    "type": "Desjardins",
    "cardholder_message": "HOLD CARD",
    "approved": False,
    "merchant_message": "Declined. Retain card"
  },
  "722": {
    "type": "First Data",
    "cardholder_message": "INVL FOLIO NBR",
    "approved": False,
    "merchant_message": "INVL FOLIO NBR"
  },
  "1046": {
    "type": "Desjardins",
    "cardholder_message": "CALL FOR AUTH",
    "approved": False,
    "merchant_message": "Declined. The authorization host is not available"
  },
  "109": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined MAX REFUND NUMBER"
  },
  "725": {
    "type": "First Data",
    "cardholder_message": "INCORRECT PIN",
    "approved": False,
    "merchant_message": "INCORRECT PIN"
  },
  "858": {
    "type": "UK",
    "cardholder_message": "Transaction type not supported by server",
    "approved": False,
    "merchant_message": "Transaction type not supported by server"
  },
  "849": {
    "type": "UK",
    "cardholder_message": "Transaction refused: Card Number can only contain numbers",
    "approved": False,
    "merchant_message": "Transaction refused: Card Number can only contain numbers"
  },
  "351": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Card No",
    "approved": False,
    "merchant_message": "Invalid Card No"
  },
  "735": {
    "type": "First Data",
    "cardholder_message": "DBT SWITCH UNAVL",
    "approved": False,
    "merchant_message": "DBT SWITCH UNAVL"
  },
  "52": {
    "type": "Bambora",
    "cardholder_message": "Invalid Card Number",
    "approved": False,
    "merchant_message": "Invalid Card Number"
  },
  "168": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined EXPIRED CARD"
  },
  "574": {
    "type": "Global Payments",
    "cardholder_message": "INVLD EXP DATE",
    "approved": False,
    "merchant_message": "INVLD EXP DATE"
  },
  "608": {
    "type": "Global Payments",
    "cardholder_message": "DB UNAVAIL 01",
    "approved": False,
    "merchant_message": "DB UNAVAIL 01"
  },
  "564": {
    "type": "Global Payments",
    "cardholder_message": "INVLD MERCH ID",
    "approved": False,
    "merchant_message": "INVLD MERCH ID"
  },
  "1013": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. The status of the card is unknown"
  },
  "828": {
    "type": "UK",
    "cardholder_message": "Approved",
    "approved": True,
    "merchant_message": "Approved"
  },
  "1029": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. Duplicate transaction"
  },
  "790": {
    "type": "Europay, Mastercard, Visa",
    "cardholder_message": "Approved",
    "approved": True,
    "merchant_message": "Approved"
  },
  "802": {
    "type": "Bambora",
    "cardholder_message": "Declined HASH\u00a0EXPIRED",
    "approved": False,
    "merchant_message": "Declined HASH\u00a0EXPIRED"
  },
  "337": {
    "type": "EBP/ACH",
    "cardholder_message": "Account frozen",
    "approved": False,
    "merchant_message": "Account frozen"
  },
  "650": {
    "type": "INTERAC Online",
    "cardholder_message": "CANNOT PROCESS PLEASE RE-TRY",
    "approved": False,
    "merchant_message": "RE-TRY INVALID CARD"
  },
  "755": {
    "type": "Elavon",
    "cardholder_message": "DECLINE CVV2",
    "approved": False,
    "merchant_message": "DECLINE CVV2"
  },
  "532": {
    "type": "Vital",
    "cardholder_message": "No Action Taken",
    "approved": False,
    "merchant_message": "No Action Taken"
  },
  "205": {
    "type": "Bambora",
    "cardholder_message": "Transaction only voidable on the date processed",
    "approved": False,
    "merchant_message": "Transaction only voidable on the date processed"
  },
  "653\u2013654": {
    "type": "INTERAC Online",
    "cardholder_message": "ACCT NOT SET UP REFER TO BRANCH",
    "approved": False,
    "merchant_message": "ACCT NOT SET UP REFER TO BRANCH"
  },
  "334": {
    "type": "EBP/ACH",
    "cardholder_message": "No chequing privileges",
    "approved": False,
    "merchant_message": "No chequing privileges"
  },
  "746": {
    "type": "Elavon",
    "cardholder_message": "INVALID TERM ID (Gift Card)",
    "approved": False,
    "merchant_message": "INVALID TERM ID (Gift Card)"
  },
  "55": {
    "type": "Bambora",
    "cardholder_message": "Transaction timeout - No transaction Response",
    "approved": False,
    "merchant_message": "Transaction timeout - No transaction Response"
  },
  "824": {
    "type": "TD",
    "cardholder_message": "Approved",
    "approved": True,
    "merchant_message": "Approved"
  },
  "191": {
    "type": "Bambora",
    "cardholder_message": "Invalid Transaction Amount",
    "approved": False,
    "merchant_message": "Invalid Transaction Amount"
  },
  "388": {
    "type": "Paymentech",
    "cardholder_message": "Auth Down - Retry",
    "approved": False,
    "merchant_message": "Auth Down - Retry"
  },
  "1039": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. Status of the card inactive"
  },
  "1084": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. PPC - amount of the transaction higher than the starting amount"
  },
  "747": {
    "type": "Elavon",
    "cardholder_message": "AMOUNT ERROR (Gift Card)",
    "approved": False,
    "merchant_message": "AMOUNT ERROR (Gift Card)"
  },
  "404": {
    "type": "Paymentech",
    "cardholder_message": "Policy # Wrong Len",
    "approved": False,
    "merchant_message": "Policy # Wrong Len"
  },
  "943": {
    "type": "EFT",
    "cardholder_message": "Rejected by the bank",
    "approved": False,
    "merchant_message": "Rejected by the bank"
  },
  "658": {
    "type": "INTERAC Online",
    "cardholder_message": "CANNOT PROCESS PLEASE RE-TRY",
    "approved": False,
    "merchant_message": "RE-TRY EDIT ERROR"
  },
  "341": {
    "type": "EBP/ACH",
    "cardholder_message": "Interbank reject - Invalid due date",
    "approved": False,
    "merchant_message": "Interbank reject - Invalid due date"
  },
  "923": {
    "type": "UK",
    "cardholder_message": "Requires telephone authorization",
    "approved": False,
    "merchant_message": "Requires telephone authorization"
  },
  "454": {
    "type": "Paymentech",
    "cardholder_message": "Rev Not Allowed",
    "approved": False,
    "merchant_message": "Rev Not Allowed"
  },
  "376": {
    "type": "Paymentech",
    "cardholder_message": "Prod Not On File",
    "approved": False,
    "merchant_message": "Prod Not On File"
  },
  "632": {
    "type": "Bambora",
    "cardholder_message": "Decline",
    "approved": False,
    "merchant_message": "Max number of recurring billing accounts reached"
  },
  "942": {
    "type": "Bambora",
    "cardholder_message": "DECLINE",
    "approved": False,
    "merchant_message": "checkout_resource_url is required"
  },
  "408": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Industry Data",
    "approved": False,
    "merchant_message": "Invalid Industry Data"
  },
  "14": {
    "type": "Bambora",
    "cardholder_message": "Invalid expiration date",
    "approved": False,
    "merchant_message": "Invalid expiration date"
  },
  "857": {
    "type": "UK",
    "cardholder_message": "Server error, no transaction sent to acquirer",
    "approved": False,
    "merchant_message": "Server error, no transaction sent to acquirer"
  },
  "390": {
    "type": "Paymentech",
    "cardholder_message": "Auth Busy - Retry",
    "approved": False,
    "merchant_message": "Auth Busy - Retry"
  },
  "166": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined BAD SEQUENCE NUMBER"
  },
  "794": {
    "type": "Paymentech",
    "cardholder_message": "NO CHECKING ACCT",
    "approved": False,
    "merchant_message": "NO CHECKING ACCT"
  },
  "140\u2013146": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "513": {
    "type": "Vital",
    "cardholder_message": "CID Format Error",
    "approved": False,
    "merchant_message": "CID Format Error"
  },
  "566": {
    "type": "Global Payments",
    "cardholder_message": "DECLINE",
    "approved": False,
    "merchant_message": "DECLINE"
  },
  "1070": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. Transaction amount exceeds the allowable limit"
  },
  "1047": {
    "type": "Desjardins",
    "cardholder_message": "CALL FOR AUTH",
    "approved": False,
    "merchant_message": "Declined. The authorization host is not available"
  },
  "1096": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. Cardholder card data decrypting error."
  },
  "568": {
    "type": "Global Payments",
    "cardholder_message": "Decline-CV2 FAIL",
    "approved": False,
    "merchant_message": "Decline-CV2 FAIL"
  },
  "1012": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. The card status is lost or stolen"
  },
  "833": {
    "type": "UK",
    "cardholder_message": "Invalid input data (details provided in description)",
    "approved": False,
    "merchant_message": "Invalid input data (details provided in description)"
  },
  "1028": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. Preauthorization limit reached for the period"
  },
  "123": {
    "type": "TD",
    "cardholder_message": "Call for Auth",
    "approved": False,
    "merchant_message": "Call for Auth"
  },
  "169\u2013176": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "431": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Act Code",
    "approved": False,
    "merchant_message": "Invalid Act Code"
  },
  "792": {
    "type": "Bambora",
    "cardholder_message": "Credit card must support 3D Secure VBV or SecureCode",
    "approved": False,
    "merchant_message": "Credit card must support 3D Secure VBV or SecureCode"
  },
  "559": {
    "type": "Bambora",
    "cardholder_message": "No Transaction Found",
    "approved": False,
    "merchant_message": "No Transaction Found"
  },
  "489": {
    "type": "Paymentech",
    "cardholder_message": "Term Not Active",
    "approved": False,
    "merchant_message": "Term Not Active"
  },
  "565": {
    "type": "Global Payments",
    "cardholder_message": "PIC UP",
    "approved": False,
    "merchant_message": "PIC UP"
  },
  "162-165": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "723": {
    "type": "First Data",
    "cardholder_message": "INV TRN TYPE",
    "approved": False,
    "merchant_message": "INV TRN TYPE"
  },
  "630": {
    "type": "EBP/ACH",
    "cardholder_message": "Payment Recalled",
    "approved": False,
    "merchant_message": "Payment Recalled"
  },
  "208": {
    "type": "Bambora",
    "cardholder_message": "Completion greater than remaining reserve amount.",
    "approved": False,
    "merchant_message": "Completion greater than remaining reserve amount."
  },
  "201": {
    "type": "Bambora",
    "cardholder_message": "Invalid transaction adjustment ID",
    "approved": False,
    "merchant_message": "Invalid transaction adjustment ID"
  },
  "105": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined MAX REFUND TOTAL"
  },
  "418": {
    "type": "Paymentech",
    "cardholder_message": "Inv MO/TO Number",
    "approved": False,
    "merchant_message": "Inv MO/TO Number"
  },
  "485": {
    "type": "Paymentech",
    "cardholder_message": "Auth Down-Retry",
    "approved": False,
    "merchant_message": "Auth Down-Retry"
  },
  "369": {
    "type": "Paymentech",
    "cardholder_message": "Auth Declined",
    "approved": False,
    "merchant_message": "Auth Declined"
  },
  "50": {
    "type": "Bambora",
    "cardholder_message": "Invalid transaction type",
    "approved": False,
    "merchant_message": "Invalid transaction type"
  },
  "412": {
    "type": "Paymentech",
    "cardholder_message": "Inv Transaction Class",
    "approved": False,
    "merchant_message": "Inv Transaction Class"
  },
  "738": {
    "type": "First Data",
    "cardholder_message": "DBTSW INV MERID",
    "approved": False,
    "merchant_message": "DBTSW INV MERID"
  },
  "607": {
    "type": "Global Payments",
    "cardholder_message": "EDC UNAVAILABLE",
    "approved": False,
    "merchant_message": "EDC UNAVAILABLE"
  },
  "533": {
    "type": "Vital",
    "cardholder_message": "No Check Account",
    "approved": False,
    "merchant_message": "No Check Account"
  },
  "490": {
    "type": "Paymentech",
    "cardholder_message": "No Transactions",
    "approved": False,
    "merchant_message": "No Transactions"
  },
  "355": {
    "type": "Paymentech",
    "cardholder_message": "Invalid PIN No",
    "approved": False,
    "merchant_message": "Invalid PIN No"
  },
  "549": {
    "type": "Vital",
    "cardholder_message": "Approval",
    "approved": True,
    "merchant_message": "Approval"
  },
  "400": {
    "type": "Paymentech",
    "cardholder_message": "Invalid PIN",
    "approved": False,
    "merchant_message": "Invalid PIN"
  },
  "358": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Amount",
    "approved": False,
    "merchant_message": "Invalid Amount"
  },
  "409": {
    "type": "Paymentech",
    "cardholder_message": "Inv Fleet Data",
    "approved": False,
    "merchant_message": "Inv Fleet Data"
  },
  "1097": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. MAC error"
  },
  "1065": {
    "type": "Desjardins",
    "cardholder_message": "CALL SERVICE",
    "approved": False,
    "merchant_message": "Declined. The amount of the transaction is too high"
  },
  "899": {
    "type": "UK",
    "cardholder_message": "Invalid Transaction Channel",
    "approved": False,
    "merchant_message": "Invalid Transaction Channel"
  },
  "1003": {
    "type": "Desjardins",
    "cardholder_message": "APPROVED",
    "approved": True,
    "merchant_message": "Approved VIP"
  },
  "392": {
    "type": "Paymentech",
    "cardholder_message": "Err - Pls Retry",
    "approved": False,
    "merchant_message": "Err - Pls Retry"
  },
  "573": {
    "type": "Global Payments",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "PLEASE RETRY"
  },
  "530": {
    "type": "Vital",
    "cardholder_message": "No Action Taken",
    "approved": False,
    "merchant_message": "No Action Taken"
  },
  "537": {
    "type": "Vital",
    "cardholder_message": "PIN Exceeded",
    "approved": False,
    "merchant_message": "PIN Exceeded"
  },
  "1055": {
    "type": "Desjardins",
    "cardholder_message": "CALL SERVICE",
    "approved": False,
    "merchant_message": "Declined. System error (admin card)"
  },
  "1058": {
    "type": "Desjardins",
    "cardholder_message": "CALL FOR AUTH",
    "approved": False,
    "merchant_message": "Declined. CVR error"
  },
  "492": {
    "type": "Paymentech",
    "cardholder_message": "Batch Not Found",
    "approved": False,
    "merchant_message": "Batch Not Found"
  },
  "1105": {
    "type": "Desjardins",
    "cardholder_message": "HOLD CARD",
    "approved": False,
    "merchant_message": "Declined. Card probably fraudulent."
  },
  "1036": {
    "type": "Desjardins",
    "cardholder_message": "OVER MAX NUMBER TRX",
    "approved": False,
    "merchant_message": "Declined. Usage limit has been reached"
  },
  "915": {
    "type": "UK",
    "cardholder_message": "Invalid Sub Merchant ID",
    "approved": False,
    "merchant_message": "Invalid Sub Merchant ID"
  },
  "419": {
    "type": "Paymentech",
    "cardholder_message": "Inv Sale/Chg Des/Folio",
    "approved": False,
    "merchant_message": "Inv Sale/Chg Des/Folio"
  },
  "859": {
    "type": "UK",
    "cardholder_message": "Transaction refused: The status of the reference transaction does not allow this transaction",
    "approved": False,
    "merchant_message": "Transaction refused: The status of the reference transaction does not allow this transaction"
  },
  "528": {
    "type": "Vital",
    "cardholder_message": "Invalid Trans",
    "approved": False,
    "merchant_message": "Invalid Trans"
  },
  "196": {
    "type": "Bambora",
    "cardholder_message": "Original purchase transaction has been voided",
    "approved": False,
    "merchant_message": "Original purchase transaction has been voided"
  },
  "328": {
    "type": "EBP/ACH",
    "cardholder_message": "Non sufficient Funds",
    "approved": False,
    "merchant_message": "Non sufficient Funds"
  },
  "820": {
    "type": "Bambora",
    "cardholder_message": "Invalid use of trnAmount field, must pass ordItemPrice with taxes enabled.",
    "approved": False,
    "merchant_message": "Invalid use of trnAmount field, must pass ordItemPrice with taxes enabled."
  },
  "378": {
    "type": "Paymentech",
    "cardholder_message": "Auth Declined",
    "approved": False,
    "merchant_message": "Auth Declined"
  },
  "500\u2013503": {
    "type": "Vital",
    "cardholder_message": "Hold-call or Pick Up Card",
    "approved": False,
    "merchant_message": "Hold-call or Pick Up Card"
  },
  "727": {
    "type": "First Data",
    "cardholder_message": "HOST KEY ERROR",
    "approved": False,
    "merchant_message": "HOST KEY ERROR"
  },
  "892": {
    "type": "UK",
    "cardholder_message": "Server unavailable",
    "approved": False,
    "merchant_message": "Server unavailable"
  },
  "842": {
    "type": "UK",
    "cardholder_message": "Invalid order ID",
    "approved": False,
    "merchant_message": "Invalid order ID"
  },
  "160": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined TERMINAL DEACTIVATED"
  },
  "905": {
    "type": "UK",
    "cardholder_message": "Invalid Expire Date",
    "approved": False,
    "merchant_message": "Invalid Expire Date"
  },
  "197": {
    "type": "Bambora",
    "cardholder_message": "Transactions cannot be adjusted to a zero or negative value",
    "approved": False,
    "merchant_message": "Transactions cannot be adjusted to a zero or negative value"
  },
  "506": {
    "type": "Vital",
    "cardholder_message": "Amount Error",
    "approved": False,
    "merchant_message": "Amount Error"
  },
  "496\u2013497": {
    "type": "Vital",
    "cardholder_message": "Call",
    "approved": False,
    "merchant_message": "Call"
  },
  "602": {
    "type": "Global Payments",
    "cardholder_message": "INVALID PREFIX",
    "approved": False,
    "merchant_message": "INVALID PREFIX"
  },
  "1020": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. Transaction declined by the issuer"
  },
  "442": {
    "type": "Paymentech",
    "cardholder_message": "Proc Error 15",
    "approved": False,
    "merchant_message": "Proc Error 15"
  },
  "347": {
    "type": "Paymentech",
    "cardholder_message": "Auth Declined",
    "approved": False,
    "merchant_message": "Auth Declined"
  },
  "809": {
    "type": "Bambora",
    "cardholder_message": "Batch close on one or more terminals",
    "approved": False,
    "merchant_message": "Batch close on one or more terminals"
  },
  "672": {
    "type": "INTERAC Online",
    "cardholder_message": "CANNOT PROCESS OVER CORR LIMIT",
    "approved": False,
    "merchant_message": "EXCEEDS CORRECTION LIMIT"
  },
  "1131": {
    "type": "Desjardins",
    "cardholder_message": "CARD NOT SET UP",
    "approved": False,
    "merchant_message": "Declined. Account does not exist"
  },
  "932": {
    "type": "UK",
    "cardholder_message": "System error",
    "approved": False,
    "merchant_message": "System error"
  },
  "816": {
    "type": "Bambora",
    "cardholder_message": "Card track data cannot be decrypted",
    "approved": False,
    "merchant_message": "Card track data cannot be decrypted"
  },
  "938": {
    "type": "Bambora",
    "cardholder_message": "Authentication is required to process this transaction",
    "approved": False,
    "merchant_message": "Authentication is required to process this transaction"
  },
  "670": {
    "type": "INTERAC Online",
    "cardholder_message": "CANNOT PROCESS PLEASE RE-TRY",
    "approved": False,
    "merchant_message": "RE-TRY INVALID TRANSACTION"
  },
  "550": {
    "type": "Vital",
    "cardholder_message": "Cannot Convert",
    "approved": False,
    "merchant_message": "Cannot Convert"
  },
  "1104": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. Invalid card"
  },
  "734": {
    "type": "First Data",
    "cardholder_message": "CRYPTO BOX UNAV",
    "approved": False,
    "merchant_message": "CRYPTO BOX UNAV"
  },
  "567": {
    "type": "Global Payments",
    "cardholder_message": "REVERSED",
    "approved": False,
    "merchant_message": "REVERSED"
  },
  "708": {
    "type": "First Data",
    "cardholder_message": "INV DRIVER NBR",
    "approved": False,
    "merchant_message": "INV DRIVER NBR"
  },
  "460": {
    "type": "Paymentech",
    "cardholder_message": "CB Not Allowed",
    "approved": False,
    "merchant_message": "CB Not Allowed"
  },
  "830": {
    "type": "UK",
    "cardholder_message": "No charge model found",
    "approved": False,
    "merchant_message": "No charge model found"
  },
  "831": {
    "type": "UK",
    "cardholder_message": "Invalid currency",
    "approved": False,
    "merchant_message": "Invalid currency"
  },
  "527": {
    "type": "Vital",
    "cardholder_message": "Invalid Routing",
    "approved": False,
    "merchant_message": "Invalid Routing"
  },
  "541": {
    "type": "Vital",
    "cardholder_message": "Serv NOt Allowed",
    "approved": False,
    "merchant_message": "Serv NOt Allowed"
  },
  "1130": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. Amount exceeds the allowable limit"
  },
  "760": {
    "type": "Bambora",
    "cardholder_message": "Multiple Transaction Matches Found",
    "approved": False,
    "merchant_message": "Multiple Transaction Matches Found"
  },
  "883": {
    "type": "UK",
    "cardholder_message": "Telephone auth code not requested",
    "approved": False,
    "merchant_message": "Telephone auth code not requested"
  },
  "636": {
    "type": "INTERAC Online",
    "cardholder_message": "FUNDS NOT AVAIL REFER TO BRANCH",
    "approved": False,
    "merchant_message": "INSUFFICIENT FUNDS REFER TO BRANCH"
  },
  "724": {
    "type": "First Data",
    "cardholder_message": "MAX TIP $999",
    "approved": False,
    "merchant_message": "MAX TIP $999"
  },
  "350": {
    "type": "Paymentech",
    "cardholder_message": "Call Voice Oper",
    "approved": False,
    "merchant_message": "Call Voice Oper"
  },
  "561": {
    "type": "Global Payments",
    "cardholder_message": "APPROVED",
    "approved": True,
    "merchant_message": "APPROVED"
  },
  "757": {
    "type": "Elavon",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "DECLINED"
  },
  "195": {
    "type": "Bambora",
    "cardholder_message": "Invalid adjustment amount.",
    "approved": False,
    "merchant_message": "Invalid adjustment amount."
  },
  "911": {
    "type": "UK",
    "cardholder_message": "Invalid Reference Transaction ID",
    "approved": False,
    "merchant_message": "Invalid Reference Transaction ID"
  },
  "657": {
    "type": "INTERAC Online",
    "cardholder_message": "CANNOT PROCESS PLEASE RETRY",
    "approved": False,
    "merchant_message": "RETRY SYSTEM TIMEOUT"
  },
  "699": {
    "type": "First Data",
    "cardholder_message": "AVS ACCEPTED",
    "approved": False,
    "merchant_message": "AVS ACCEPTED"
  },
  "1090": {
    "type": "Desjardins",
    "cardholder_message": "FORMAT ERROR",
    "approved": False,
    "merchant_message": "Declined. Error in Batch Close"
  },
  "449": {
    "type": "Paymentech",
    "cardholder_message": "Amount Too Large",
    "approved": False,
    "merchant_message": "Amount Too Large"
  },
  "642": {
    "type": "INTERAC Online",
    "cardholder_message": "CARD USE LIMITED REFER TO BRANCH",
    "approved": False,
    "merchant_message": "CARD USE LIMITED REFER TO BRANCH"
  },
  "194": {
    "type": "Bambora",
    "cardholder_message": "Transaction exceeds return limit.",
    "approved": False,
    "merchant_message": "Transaction exceeds return limit."
  },
  "477": {
    "type": "Paymentech",
    "cardholder_message": "Reenter Odometer",
    "approved": False,
    "merchant_message": "Reenter Odometer"
  },
  "217": {
    "type": "Bambora",
    "cardholder_message": "DECLINE",
    "approved": False,
    "merchant_message": "Transaction Declined TR"
  },
  "706": {
    "type": "First Data",
    "cardholder_message": "INVLID MAC",
    "approved": False,
    "merchant_message": "INVLID MAC"
  },
  "936": {
    "type": "Bambora",
    "cardholder_message": "Declined please try again",
    "approved": False,
    "merchant_message": "Invalid or expired single use token"
  },
  "1018": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. Invalid amount"
  },
  "209": {
    "type": "Bambora",
    "cardholder_message": "Merchant Account Disabled",
    "approved": False,
    "merchant_message": "Merchant Account Disabled"
  },
  "203": {
    "type": "Bambora",
    "cardholder_message": "Pre-Authorization already completed",
    "approved": False,
    "merchant_message": "Pre-Authorization already completed"
  },
  "599": {
    "type": "Global Payments",
    "cardholder_message": "DB ISSUER UNAVAIL",
    "approved": False,
    "merchant_message": "DB ISSUER UNAVAIL"
  },
  "805": {
    "type": "Paymentech",
    "cardholder_message": "Signature Debit Not Allowed",
    "approved": False,
    "merchant_message": "Signature Debit Not Allowed"
  },
  "1085": {
    "type": "Desjardins",
    "cardholder_message": "ALREADY ACTIVE",
    "approved": False,
    "merchant_message": "Declined. PPC - card already activated"
  },
  "59": {
    "type": "Bambora",
    "cardholder_message": "Declined - Operation must be performed by Master Merchant",
    "approved": False,
    "merchant_message": "Declined - Operation must be performed by Master Merchant"
  },
  "818": {
    "type": "Bambora",
    "cardholder_message": "Invalid track format indicator",
    "approved": False,
    "merchant_message": "Invalid track format indicator"
  },
  "838": {
    "type": "UK",
    "cardholder_message": "Bank system temporary unreachable",
    "approved": False,
    "merchant_message": "Bank system temporary unreachable"
  },
  "762": {
    "type": "Bambora",
    "cardholder_message": "Expired session. Transaction not completed in allocated time.",
    "approved": False,
    "merchant_message": "Expired session. Transaction not completed in allocated time."
  },
  "1103": {
    "type": "Desjardins",
    "cardholder_message": "INVALID AMOUNT",
    "approved": False,
    "merchant_message": "Declined. Invalid amount"
  },
  "498\u2013499": {
    "type": "Vital",
    "cardholder_message": "No Reply",
    "approved": False,
    "merchant_message": "No Reply"
  },
  "882": {
    "type": "UK",
    "cardholder_message": "This capture requires a telephone auth code",
    "approved": False,
    "merchant_message": "This capture requires a telephone auth code"
  },
  "697": {
    "type": "First Data",
    "cardholder_message": "SERV NOT ALLOWED",
    "approved": False,
    "merchant_message": "SERV NOT ALLOWED"
  },
  "841": {
    "type": "UK",
    "cardholder_message": "Invalid card type",
    "approved": False,
    "merchant_message": "Invalid card type"
  },
  "1062": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. Account type invalid."
  },
  "545": {
    "type": "Vital",
    "cardholder_message": "Term Id Error",
    "approved": False,
    "merchant_message": "Term Id Error"
  },
  "1030": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. Max online refund amount reached for a card for the period"
  },
  "890": {
    "type": "UK",
    "cardholder_message": "Invalid transaction type",
    "approved": False,
    "merchant_message": "Invalid transaction type"
  },
  "933": {
    "type": "UK",
    "cardholder_message": "Authentication Problem",
    "approved": False,
    "merchant_message": "Authentication Problem"
  },
  "336": {
    "type": "EBP/ACH",
    "cardholder_message": "Payor/Payee Deceased",
    "approved": False,
    "merchant_message": "Payor/Payee Deceased"
  },
  "316": {
    "type": "Bambora",
    "cardholder_message": "CALL HELP DESK",
    "approved": False,
    "merchant_message": "Invalid transaction validation type"
  },
  "1117": {
    "type": "Desjardins",
    "cardholder_message": "CARD NOT SET UP",
    "approved": False,
    "merchant_message": "Declined. Inactive Desjardins Interac card"
  },
  "204": {
    "type": "Bambora",
    "cardholder_message": "Declined: Use Pre-Auth Completion",
    "approved": False,
    "merchant_message": "Declined: Use Pre-Auth Completion"
  },
  "904": {
    "type": "UK",
    "cardholder_message": "Invalid Card Number",
    "approved": False,
    "merchant_message": "Invalid Card Number"
  },
  "1078": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. EMV - Transaction in fallback"
  },
  "210": {
    "type": "Bambora",
    "cardholder_message": "Merchant Account Closed",
    "approved": False,
    "merchant_message": "Merchant Account Closed"
  },
  "471": {
    "type": "Paymentech",
    "cardholder_message": "JCB Not Allowed",
    "approved": False,
    "merchant_message": "JCB Not Allowed"
  },
  "586": {
    "type": "Global Payments",
    "cardholder_message": "NO DUP FOUND",
    "approved": False,
    "merchant_message": "NO DUP FOUND"
  },
  "343": {
    "type": "EBP/ACH",
    "cardholder_message": "Interbank reject - Invalid account number",
    "approved": False,
    "merchant_message": "Interbank reject - Invalid account number"
  },
  "685": {
    "type": "First Data",
    "cardholder_message": "REFERRAL",
    "approved": False,
    "merchant_message": "REFERRAL"
  },
  "728": {
    "type": "First Data",
    "cardholder_message": "PIN RETRY EXCEEDED",
    "approved": False,
    "merchant_message": "PIN RETRY EXCEEDED"
  },
  "56": {
    "type": "Bambora",
    "cardholder_message": "Application Error - Retrieving Response",
    "approved": False,
    "merchant_message": "Application Error - Retrieving Response"
  },
  "919": {
    "type": "UK",
    "cardholder_message": "Invalid CVD Code",
    "approved": False,
    "merchant_message": "Invalid CVD Code"
  },
  "202": {
    "type": "Bambora",
    "cardholder_message": "Invalid order number",
    "approved": False,
    "merchant_message": "Invalid order number"
  },
  "103": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined MAX PER REFUND"
  },
  "1060": {
    "type": "Desjardins",
    "cardholder_message": "CALL FOR AUTH",
    "approved": False,
    "merchant_message": "Declined. This message is an EMV referral - \"fallback\""
  },
  "698": {
    "type": "First Data",
    "cardholder_message": "APPROVAL",
    "approved": True,
    "merchant_message": "APPROVAL"
  },
  "329": {
    "type": "EBP/ACH",
    "cardholder_message": "Account Closed",
    "approved": False,
    "merchant_message": "Account Closed"
  },
  "814": {
    "type": "Bambora",
    "cardholder_message": "User session validation failed",
    "approved": False,
    "merchant_message": "User session validation failed"
  },
  "1069": {
    "type": "Desjardins",
    "cardholder_message": "CALL SERVICE",
    "approved": False,
    "merchant_message": "Declined. Transaction code invalid"
  },
  "1100": {
    "type": "Desjardins",
    "cardholder_message": "EXPIRED CARD",
    "approved": False,
    "merchant_message": "Declined. Expired card"
  },
  "1091": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. Desjardins acquirer system timeout"
  },
  "1124": {
    "type": "Desjardins",
    "cardholder_message": "SYSTEM NOT AVAIL.",
    "approved": False,
    "merchant_message": "Declined. Desjardins Interac issuing host unavailable"
  },
  "546": {
    "type": "Vital",
    "cardholder_message": "Wrong Pin",
    "approved": False,
    "merchant_message": "Wrong Pin"
  },
  "1022": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. Invalid acquirer institution"
  },
  "212": {
    "type": "Bambora",
    "cardholder_message": "Service Unavailable - Please try again later",
    "approved": False,
    "merchant_message": "Service Unavailable - Please try again later"
  },
  "311": {
    "type": "Bambora",
    "cardholder_message": "3D Secure Failed",
    "approved": False,
    "merchant_message": "3D Secure Failed"
  },
  "405": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Ind Code",
    "approved": False,
    "merchant_message": "Invalid Ind Code"
  },
  "800": {
    "type": "Bambora",
    "cardholder_message": "Invalid customer code (token)",
    "approved": False,
    "merchant_message": "Invalid customer code (token)"
  },
  "395": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Function",
    "approved": False,
    "merchant_message": "Invalid Function"
  },
  "591": {
    "type": "Global Payments",
    "cardholder_message": "INV BANK",
    "approved": False,
    "merchant_message": "INV BANK"
  },
  "159": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "793": {
    "type": "Bambora",
    "cardholder_message": "Address validation failed. Transaction reversed.",
    "approved": False,
    "merchant_message": "Address validation failed. Transaction reversed."
  },
  "1094": {
    "type": "Desjardins",
    "cardholder_message": "FORMAT ERROR",
    "approved": False,
    "merchant_message": "Declined. The transaction is invalid. The response sent by the host only contains a header."
  },
  "504": {
    "type": "Vital",
    "cardholder_message": "Acct Length Err",
    "approved": False,
    "merchant_message": "Acct Length Err"
  },
  "523": {
    "type": "Vital",
    "cardholder_message": "Error",
    "approved": False,
    "merchant_message": "Error"
  },
  "326": {
    "type": "Bambora",
    "cardholder_message": "Declined - Invalid bank account",
    "approved": False,
    "merchant_message": "Declined - Invalid bank account"
  },
  "758": {
    "type": "Elavon",
    "cardholder_message": "CALL AUTH. CENTER",
    "approved": False,
    "merchant_message": "CALL AUTH. CENTER"
  },
  "446": {
    "type": "Paymentech",
    "cardholder_message": "Please Try Again",
    "approved": False,
    "merchant_message": "Please Try Again"
  },
  "49": {
    "type": "Bambora",
    "cardholder_message": "Invalid transaction request string",
    "approved": False,
    "merchant_message": "Invalid transaction request string"
  },
  "769": {
    "type": "EBP/ACH",
    "cardholder_message": "Customer Initiated Return Credit Only",
    "approved": False,
    "merchant_message": "Customer Initiated Return Credit Only"
  },
  "190": {
    "type": "Bambora",
    "cardholder_message": "Unknown transaction response",
    "approved": False,
    "merchant_message": "Unknown transaction response"
  },
  "717": {
    "type": "First Data",
    "cardholder_message": "COMM ERR RESEND",
    "approved": False,
    "merchant_message": "COMM ERR RESEND"
  },
  "638": {
    "type": "INTERAC Online",
    "cardholder_message": "PIN ERROR PLEASE RE-TRY",
    "approved": False,
    "merchant_message": "RE-TRY PIN ERROR"
  },
  "507\u2013508": {
    "type": "Vital",
    "cardholder_message": "Cant Verify PIN",
    "approved": False,
    "merchant_message": "Cant Verify PIN"
  },
  "363": {
    "type": "Paymentech",
    "cardholder_message": "Over Credit Flr",
    "approved": False,
    "merchant_message": "Over Credit Flr"
  },
  "750": {
    "type": "Elavon",
    "cardholder_message": "MAX REACHED (Gift Card)",
    "approved": False,
    "merchant_message": "MAX REACHED (Gift Card)"
  },
  "478": {
    "type": "Paymentech",
    "cardholder_message": "<Duplicate Tran>",
    "approved": False,
    "merchant_message": "<Duplicate Tran>"
  },
  "1133": {
    "type": "Desjardins",
    "cardholder_message": "Accord D transaction cannot be processed as recurring.",
    "approved": False,
    "merchant_message": "Accord D transaction cannot be processed as recurring."
  },
  "1076": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. EMV - CVR error"
  },
  "1049": {
    "type": "Desjardins",
    "cardholder_message": "TRX NOT ALLOWED",
    "approved": False,
    "merchant_message": "Declined. Unsupported transaction"
  },
  "924": {
    "type": "UK",
    "cardholder_message": "The bank reported time out. Please retry",
    "approved": False,
    "merchant_message": "The bank reported time out. Please retry"
  },
  "1040": {
    "type": "Desjardins",
    "cardholder_message": "HOLD CARD",
    "approved": False,
    "merchant_message": "Declined. Stolen card"
  },
  "402": {
    "type": "Paymentech",
    "cardholder_message": "Auth # Not Entered",
    "approved": False,
    "merchant_message": "Auth # Not Entered"
  },
  "403": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Down Pay Ind",
    "approved": False,
    "merchant_message": "Invalid Down Pay Ind"
  },
  "474": {
    "type": "Paymentech",
    "cardholder_message": "Failed Plz Call",
    "approved": False,
    "merchant_message": "Failed Plz Call"
  },
  "880": {
    "type": "UK",
    "cardholder_message": "Transaction refused: The currency code does not match with the reference transaction",
    "approved": False,
    "merchant_message": "Transaction refused: The currency code does not match with the reference transaction"
  },
  "86": {
    "type": "TD",
    "cardholder_message": "PLEASE TRY AGAIN",
    "approved": False,
    "merchant_message": "Declined"
  },
  "827": {
    "type": "Bambora",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "876": {
    "type": "UK",
    "cardholder_message": "Transaction refused: Reference transaction cancelled",
    "approved": False,
    "merchant_message": "Transaction refused: Reference transaction cancelled"
  },
  "1023": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. Routing problem"
  },
  "702": {
    "type": "First Data",
    "cardholder_message": "RESEND BATCH",
    "approved": False,
    "merchant_message": "RESEND BATCH"
  },
  "644": {
    "type": "INTERAC Online",
    "cardholder_message": "EXCESS PIN RETRY REFER TO BRANCH",
    "approved": False,
    "merchant_message": "EXCESS PIN RETRY REFER TO BRANCH"
  },
  "788": {
    "type": "Bambora",
    "cardholder_message": "Duplicate Order Number - This order number has already been processed",
    "approved": False,
    "merchant_message": "Duplicate Order Number - This order number has already been processed"
  },
  "540": {
    "type": "Vital",
    "cardholder_message": "Serv Not Allowed",
    "approved": False,
    "merchant_message": "Serv Not Allowed"
  },
  "348": {
    "type": "Paymentech",
    "cardholder_message": "Call Voice Oper",
    "approved": False,
    "merchant_message": "Call Voice Oper"
  },
  "430": {
    "type": "Paymentech",
    "cardholder_message": "Term Not Active",
    "approved": False,
    "merchant_message": "Term Not Active"
  },
  "352": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Exp. Date",
    "approved": False,
    "merchant_message": "Invalid Exp. Date"
  },
  "673": {
    "type": "INTERAC Online",
    "cardholder_message": "CANNOT PROCESS",
    "approved": False,
    "merchant_message": "CANNOT PROCESS"
  },
  "1121": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. PIN Required. The card must be inserted into the chip reader."
  },
  "92\u201399": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "61\u201370": {
    "type": "TD",
    "cardholder_message": "Approved",
    "approved": True,
    "merchant_message": "Approved"
  },
  "127": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined CARD NOT SUPPORTED"
  },
  "817": {
    "type": "Bambora",
    "cardholder_message": "Card track data cannot be parsed for card number and expiry",
    "approved": False,
    "merchant_message": "Card track data cannot be parsed for card number and expiry"
  },
  "853": {
    "type": "UK",
    "cardholder_message": "Communication problems",
    "approved": False,
    "merchant_message": "Communication problems"
  },
  "384": {
    "type": "Paymentech",
    "cardholder_message": "CVC2/CID ERROR",
    "approved": False,
    "merchant_message": "CVC2/CID ERROR"
  },
  "401": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Card",
    "approved": False,
    "merchant_message": "Invalid Card"
  },
  "884": {
    "type": "UK",
    "cardholder_message": "Server error, no transaction sent to acquirer",
    "approved": False,
    "merchant_message": "Server error, no transaction sent to acquirer"
  },
  "1120": {
    "type": "Desjardins",
    "cardholder_message": "INVALID PIN",
    "approved": False,
    "merchant_message": "Declined. Incorrect PIN"
  },
  "832": {
    "type": "UK",
    "cardholder_message": "Invalid Transaction Channel",
    "approved": False,
    "merchant_message": "Invalid Transaction Channel"
  },
  "554": {
    "type": "Vital",
    "cardholder_message": "Duplicate Number",
    "approved": False,
    "merchant_message": "Duplicate Number"
  },
  "806": {
    "type": "Global Payments",
    "cardholder_message": "TRAN NOT ALLOWED",
    "approved": False,
    "merchant_message": "TRAN NOT ALLOWED"
  },
  "382": {
    "type": "Paymentech",
    "cardholder_message": "PIN Not Selected",
    "approved": False,
    "merchant_message": "PIN Not Selected"
  },
  "320": {
    "type": "Bambora",
    "cardholder_message": "CALL HELP DESK",
    "approved": False,
    "merchant_message": "Missing errorPage URL"
  },
  "367": {
    "type": "Paymentech",
    "cardholder_message": "Auth Declined",
    "approved": False,
    "merchant_message": "Auth Declined"
  },
  "1014": {
    "type": "Desjardins",
    "cardholder_message": "ACCOUNT NOT SET UP",
    "approved": False,
    "merchant_message": "Declined. The account used in the transaction is not defined"
  },
  "713": {
    "type": "First Data",
    "cardholder_message": "INV EXP DATE",
    "approved": False,
    "merchant_message": "INV EXP DATE"
  },
  "538": {
    "type": "Vital",
    "cardholder_message": "RE Enter",
    "approved": False,
    "merchant_message": "RE Enter"
  },
  "1101": {
    "type": "Desjardins",
    "cardholder_message": "HOLD CARD",
    "approved": False,
    "merchant_message": "Declined. Card probably fraudulent."
  },
  "317": {
    "type": "Bambora",
    "cardholder_message": "CALL HELP DESK",
    "approved": False,
    "merchant_message": "Authentication Failed"
  },
  "444": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Function",
    "approved": False,
    "merchant_message": "Invalid Function"
  },
  "313": {
    "type": "Bambora",
    "cardholder_message": "DECLINE",
    "approved": False,
    "merchant_message": "Over sales limit"
  },
  "167": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "651": {
    "type": "INTERAC Online",
    "cardholder_message": "CANNOT PROCESS PLEASE RE-TRY",
    "approved": False,
    "merchant_message": "RE-TRY SYSTEM PROBLEM"
  },
  "1113": {
    "type": "Desjardins",
    "cardholder_message": "CANCELLATION LIMIT\u00c2\u00a0",
    "approved": False,
    "merchant_message": "Declined. Daily Interac cancellation limit reached"
  },
  "534": {
    "type": "Vital",
    "cardholder_message": "No Credit Acct",
    "approved": False,
    "merchant_message": "No Credit Acct"
  },
  "821": {
    "type": "Bambora",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "CVD mismatch. Transaction reversed"
  },
  "357": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Term No",
    "approved": False,
    "merchant_message": "Invalid Term No"
  },
  "1061": {
    "type": "Desjardins",
    "cardholder_message": "RETAILER NOT FOUND",
    "approved": False,
    "merchant_message": "Declined. The merchant number is invalid"
  },
  "825": {
    "type": "Bambora",
    "cardholder_message": "Missing or invalid term URL",
    "approved": False,
    "merchant_message": "CALL HELP DESK"
  },
  "587": {
    "type": "Global Payments",
    "cardholder_message": "INVALID DATA",
    "approved": False,
    "merchant_message": "INVALID DATA"
  },
  "450": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Term ID",
    "approved": False,
    "merchant_message": "Invalid Term ID"
  },
  "1034": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. Max refund amount reached for a card for the period"
  },
  "414": {
    "type": "Paymentech",
    "cardholder_message": "Inv/Missing Retr Ref",
    "approved": False,
    "merchant_message": "Inv/Missing Retr Ref"
  },
  "1052": {
    "type": "Desjardins",
    "cardholder_message": "CALL SERVICE",
    "approved": False,
    "merchant_message": "Declined. Issuing host did not respond (timeout)"
  },
  "861": {
    "type": "UK",
    "cardholder_message": "Transaction refused: The currency code does not match the reference transaction",
    "approved": False,
    "merchant_message": "Transaction refused: The currency code does not match the reference transaction"
  },
  "76": {
    "type": "TD",
    "cardholder_message": "PLEASE TRY AGAIN",
    "approved": False,
    "merchant_message": "PLEASE TRY AGAIN"
  },
  "179\u2013189": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "456": {
    "type": "Paymentech",
    "cardholder_message": "Dscv Not Allowed",
    "approved": False,
    "merchant_message": "Dscv Not Allowed"
  },
  "928": {
    "type": "UK",
    "cardholder_message": "System error",
    "approved": False,
    "merchant_message": "System error"
  },
  "339": {
    "type": "EBP/ACH",
    "cardholder_message": "Refused by payor/payee",
    "approved": False,
    "merchant_message": "Refused by payor/payee"
  },
  "332": {
    "type": "EBP/ACH",
    "cardholder_message": "Cannot trace account",
    "approved": False,
    "merchant_message": "Cannot trace account"
  },
  "718": {
    "type": "First Data",
    "cardholder_message": "INVL TERMINAL ID",
    "approved": False,
    "merchant_message": "INVL TERMINAL ID"
  },
  "89": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined INVALID TRAN DATE"
  },
  "660": {
    "type": "INTERAC Online",
    "cardholder_message": "Bad sequence number: resend transaction",
    "approved": False,
    "merchant_message": "Bad sequence number: resend transaction"
  },
  "712": {
    "type": "First Data",
    "cardholder_message": "INVLD ACCT 2",
    "approved": False,
    "merchant_message": "INVLD ACCT 2"
  },
  "1073": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. EMV - Error with the security box"
  },
  "366": {
    "type": "Paymentech",
    "cardholder_message": "Auth Down-Retry",
    "approved": False,
    "merchant_message": "Auth Down-Retry"
  },
  "536": {
    "type": "Vital",
    "cardholder_message": "No Such Issuer",
    "approved": False,
    "merchant_message": "No Such Issuer"
  },
  "428": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Term ID",
    "approved": False,
    "merchant_message": "Invalid Term ID"
  },
  "850\u2013851": {
    "type": "UK",
    "cardholder_message": "Communication problems",
    "approved": False,
    "merchant_message": "Communication problems"
  },
  "1026": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. Invalid card number length"
  },
  "432": {
    "type": "Paymentech",
    "cardholder_message": "Void Not Allowed",
    "approved": False,
    "merchant_message": "Void Not Allowed"
  },
  "839": {
    "type": "UK",
    "cardholder_message": "Operation not supported by bank",
    "approved": False,
    "merchant_message": "Operation not supported by bank"
  },
  "455": {
    "type": "Paymentech",
    "cardholder_message": "Rev Not Allowed",
    "approved": False,
    "merchant_message": "Rev Not Allowed"
  },
  "398": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Action Code",
    "approved": False,
    "merchant_message": "Invalid Action Code"
  },
  "344": {
    "type": "EBP/ACH",
    "cardholder_message": "Interbank reject - Invalid institution and account number",
    "approved": False,
    "merchant_message": "Interbank reject - Invalid institution and account number"
  },
  "733": {
    "type": "First Data",
    "cardholder_message": "INV CASHBACK AMT",
    "approved": False,
    "merchant_message": "INV CASHBACK AMT"
  },
  "1095": {
    "type": "Desjardins",
    "cardholder_message": "INVALID PIN LENGTH",
    "approved": False,
    "merchant_message": "Declined. PIN length invalid"
  },
  "192": {
    "type": "Bambora",
    "cardholder_message": "Transaction cannot be voided after being returned",
    "approved": False,
    "merchant_message": "Transaction cannot be voided after being returned"
  },
  "764": {
    "type": "EBP/ACH",
    "cardholder_message": "Agreement revoked - Personal",
    "approved": False,
    "merchant_message": "Agreement revoked - Personal"
  },
  "707": {
    "type": "First Data",
    "cardholder_message": "INVALID ID NBR",
    "approved": False,
    "merchant_message": "INVALID ID NBR"
  },
  "907": {
    "type": "UK",
    "cardholder_message": "Invalid Currency Code",
    "approved": False,
    "merchant_message": "Invalid Currency Code"
  },
  "910": {
    "type": "UK",
    "cardholder_message": "Invalid VAT Numerator",
    "approved": False,
    "merchant_message": "Invalid VAT Numerator"
  },
  "759": {
    "type": "Elavon",
    "cardholder_message": "ELAVON PROCESSING ERROR",
    "approved": False,
    "merchant_message": "ELAVON PROCESSING ERROR"
  },
  "584": {
    "type": "Global Payments",
    "cardholder_message": "MUST BALANCE NOW",
    "approved": False,
    "merchant_message": "MUST BALANCE NOW"
  },
  "374": {
    "type": "Paymentech",
    "cardholder_message": "Inv Merc Rstrct Code",
    "approved": False,
    "merchant_message": "Inv Merc Rstrct Code"
  },
  "611": {
    "type": "Global Payments",
    "cardholder_message": "EXCEEDS MAX USES",
    "approved": False,
    "merchant_message": "EXCEEDS MAX USES"
  },
  "895": {
    "type": "UK",
    "cardholder_message": "Server error",
    "approved": False,
    "merchant_message": "Server error"
  },
  "368": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Pin No",
    "approved": False,
    "merchant_message": "Invalid Pin No"
  },
  "1066": {
    "type": "Desjardins",
    "cardholder_message": "CARD NOT SET UP",
    "approved": False,
    "merchant_message": "Declined. The card is not set up in the acquirer's host (POS)"
  },
  "90": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "526": {
    "type": "Vital",
    "cardholder_message": "Failure CV",
    "approved": False,
    "merchant_message": "Failure CV"
  },
  "704": {
    "type": "First Data",
    "cardholder_message": "CVV2 DECLINED",
    "approved": False,
    "merchant_message": "CVV2 DECLINED"
  },
  "1118": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. Desjardins Interac card, insufficient funds"
  },
  "1123": {
    "type": "Desjardins",
    "cardholder_message": "PIN CHG NOT ALLOWED",
    "approved": False,
    "merchant_message": "Declined. This Admin card cannot be used to change the PIN"
  },
  "1086": {
    "type": "Desjardins",
    "cardholder_message": "INSUFF. FUNDS",
    "approved": False,
    "merchant_message": "Declined. PPC - Insufficient funds"
  },
  "729": {
    "type": "First Data",
    "cardholder_message": "DUPLICATE TRAN",
    "approved": False,
    "merchant_message": "DUPLICATE TRAN"
  },
  "385": {
    "type": "Paymentech",
    "cardholder_message": "Tran Not Defined",
    "approved": False,
    "merchant_message": "Tran Not Defined"
  },
  "879": {
    "type": "UK",
    "cardholder_message": "Transaction refused: Merchant ID inactive",
    "approved": False,
    "merchant_message": "Transaction refused: Merchant ID inactive"
  },
  "752": {
    "type": "Elavon",
    "cardholder_message": "CARD NOT ACTIVE (Gift Card)",
    "approved": False,
    "merchant_message": "CARD NOT ACTIVE (Gift Card)"
  },
  "177": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined ADMIN CARD NOT FOUND"
  },
  "71": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "439": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Term ID",
    "approved": False,
    "merchant_message": "Invalid Term ID"
  },
  "684": {
    "type": "First Data",
    "cardholder_message": "APPROVAL",
    "approved": True,
    "merchant_message": "APPROVAL"
  },
  "582": {
    "type": "Global Payments",
    "cardholder_message": "INV ITEM NUM",
    "approved": False,
    "merchant_message": "INV ITEM NUM"
  },
  "22": {
    "type": "Bambora",
    "cardholder_message": "Validation greater than maximum amount",
    "approved": False,
    "merchant_message": "Validation greater than maximum amount"
  },
  "770": {
    "type": "Global Payments",
    "cardholder_message": "INVALID CID",
    "approved": False,
    "merchant_message": "INVALID CID"
  },
  "605": {
    "type": "Global Payments",
    "cardholder_message": "INVALID LIC",
    "approved": False,
    "merchant_message": "INVALID LIC"
  },
  "397": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Exp. Date",
    "approved": False,
    "merchant_message": "Invalid Exp. Date"
  },
  "1119": {
    "type": "Desjardins",
    "cardholder_message": "NOT ALLOWED",
    "approved": False,
    "merchant_message": "Declined. Transaction not allowed"
  },
  "688": {
    "type": "First Data",
    "cardholder_message": "BAD PROCESSING CODE",
    "approved": False,
    "merchant_message": "BAD PROCESSING CODE"
  },
  "843\u2013847": {
    "type": "UK",
    "cardholder_message": "Transaction refused",
    "approved": False,
    "merchant_message": "Transaction refused"
  },
  "1059": {
    "type": "Desjardins",
    "cardholder_message": "CALL FOR AUTH",
    "approved": False,
    "merchant_message": "Declined. TVR error"
  },
  "661": {
    "type": "INTERAC Online",
    "cardholder_message": "CANNOT PROCESS PLEASE RE-TRY",
    "approved": False,
    "merchant_message": "RE-TRY SYSTEM PROBLEM"
  },
  "495": {
    "type": "Vital",
    "cardholder_message": "Card OK",
    "approved": False,
    "merchant_message": "Card OK"
  },
  "641": {
    "type": "INTERAC Online",
    "cardholder_message": "$ LIMIT EXCEEDED REFER TO BRANCH",
    "approved": False,
    "merchant_message": "$ LIMIT EXCEEDED REFER TO BRANCH"
  },
  "754": {
    "type": "Elavon",
    "cardholder_message": "DECLINED-HELP 9999 (Gift Card \u2013 System Error)",
    "approved": False,
    "merchant_message": "DECLINED-HELP 9999 (Gift Card \u2013 System Error)"
  },
  "897": {
    "type": "UK",
    "cardholder_message": "No transaction matching the referenced transaction",
    "approved": False,
    "merchant_message": "No transaction matching the referenced transaction"
  },
  "840": {
    "type": "UK",
    "cardholder_message": "Invalid expiry date",
    "approved": False,
    "merchant_message": "Invalid expiry date"
  },
  "823": {
    "type": "First Data",
    "cardholder_message": "ISS UNAV/DATE ER",
    "approved": False,
    "merchant_message": "ISS UNAV/DATE ER"
  },
  "715": {
    "type": "First Data",
    "cardholder_message": "INVLD ACCT 1",
    "approved": False,
    "merchant_message": "INVLD ACCT 1"
  },
  "863": {
    "type": "UK",
    "cardholder_message": "Transaction refused: Active configuration differs from the one used in the reference transaction",
    "approved": False,
    "merchant_message": "Transaction refused: Active configuration differs from the one used in the reference transaction"
  },
  "896": {
    "type": "UK",
    "cardholder_message": "Card type is not allowed",
    "approved": False,
    "merchant_message": "Card type is not allowed"
  },
  "416": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Duration",
    "approved": False,
    "merchant_message": "Invalid Duration"
  },
  "522": {
    "type": "Vital",
    "cardholder_message": "Encryption Error",
    "approved": False,
    "merchant_message": "Encryption Error"
  },
  "491": {
    "type": "Paymentech",
    "cardholder_message": "Bat Already Rels",
    "approved": False,
    "merchant_message": "Bat Already Rels"
  },
  "377": {
    "type": "Paymentech",
    "cardholder_message": "Auth Declined",
    "approved": False,
    "merchant_message": "Auth Declined"
  },
  "323": {
    "type": "Bambora",
    "cardholder_message": "CALL HELP DESK",
    "approved": False,
    "merchant_message": "One or more products not found in inventory"
  },
  "542\u2013543": {
    "type": "Vital",
    "cardholder_message": "Stop Recurring",
    "approved": False,
    "merchant_message": "Stop Recurring"
  },
  "100": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined DUPLICATE TRAN"
  },
  "494": {
    "type": "Vital",
    "cardholder_message": "Approval",
    "approved": True,
    "merchant_message": "Approval"
  },
  "912": {
    "type": "UK",
    "cardholder_message": "Transaction type not supported by legacy system",
    "approved": False,
    "merchant_message": "Transaction type not supported by legacy system"
  },
  "575": {
    "type": "Global Payments",
    "cardholder_message": "PIN INVALID",
    "approved": False,
    "merchant_message": "PIN INVALID"
  },
  "711": {
    "type": "First Data",
    "cardholder_message": "INVLD AMT 3",
    "approved": False,
    "merchant_message": "INVLD AMT 3"
  },
  "433": {
    "type": "Paymentech",
    "cardholder_message": "Ref Num Not Found",
    "approved": False,
    "merchant_message": "Ref Num Not Found"
  },
  "811": {
    "type": "Bambora",
    "cardholder_message": "Insufficient user permission for processing payment transactions",
    "approved": False,
    "merchant_message": "Insufficient user permission for processing payment transactions"
  },
  "425": {
    "type": "Paymentech",
    "cardholder_message": "INV TKN Value",
    "approved": False,
    "merchant_message": "INV TKN Value"
  },
  "1050": {
    "type": "Desjardins",
    "cardholder_message": "CALL FOR AUTH",
    "approved": False,
    "merchant_message": "Declined. Maximum amount limit"
  },
  "396": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Card",
    "approved": False,
    "merchant_message": "Invalid Card"
  },
  "562": {
    "type": "Global Payments",
    "cardholder_message": "CALL CARD ISSUER",
    "approved": False,
    "merchant_message": "CALL CARD ISSUER"
  },
  "695": {
    "type": "First Data",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "DECLINED"
  },
  "1098": {
    "type": "Desjardins",
    "cardholder_message": "CALL SERVICE",
    "approved": False,
    "merchant_message": "Declined. Sequence number (see header) is invalid"
  },
  "1044": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. A forced transaction ended in error due to a system problem"
  },
  "901": {
    "type": "UK",
    "cardholder_message": "Invalid Order ID",
    "approved": False,
    "merchant_message": "Invalid Order ID"
  },
  "1087": {
    "type": "Desjardins",
    "cardholder_message": "INVALID CARD",
    "approved": False,
    "merchant_message": "Declined. PPC - Invalid card"
  },
  "588": {
    "type": "Global Payments",
    "cardholder_message": "NO TRANS FOUND",
    "approved": False,
    "merchant_message": "NO TRANS FOUND"
  },
  "1056": {
    "type": "Desjardins",
    "cardholder_message": "CALL FOR AUTH",
    "approved": False,
    "merchant_message": "Declined. System error with security boxes"
  },
  "822": {
    "type": "Bambora",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "AVS mismatch. Transaction reversed"
  },
  "156\u2013157": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "555": {
    "type": "Vital",
    "cardholder_message": "MICR Error",
    "approved": False,
    "merchant_message": "MICR Error"
  },
  "813": {
    "type": "Bambora",
    "cardholder_message": "User session has expired",
    "approved": False,
    "merchant_message": "User session has expired"
  },
  "903": {
    "type": "UK",
    "cardholder_message": "Invalid Order Info",
    "approved": False,
    "merchant_message": "Invalid Order Info"
  },
  "647\u2013649": {
    "type": "INTERAC Online",
    "cardholder_message": "CANNOT PROCESS PLEASE RE-TRY",
    "approved": False,
    "merchant_message": "RE-TRY EDIT ERROR"
  },
  "689": {
    "type": "First Data",
    "cardholder_message": "INV AMT",
    "approved": False,
    "merchant_message": "INV AMT"
  },
  "716": {
    "type": "First Data",
    "cardholder_message": "CAPT. NOT ALLOWED",
    "approved": False,
    "merchant_message": "CAPT. NOT ALLOWED"
  },
  "874\u2013875": {
    "type": "UK",
    "cardholder_message": "Transaction refused: Card is blacklisted",
    "approved": False,
    "merchant_message": "Transaction refused: Card is blacklisted"
  },
  "77\u201385": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "655": {
    "type": "INTERAC Online",
    "cardholder_message": "CARD IS NOT SETUP REFER TO BRANCH",
    "approved": False,
    "merchant_message": "CARD IS NOT SETUP REFER TO BRANCH"
  },
  "340": {
    "type": "EBP/ACH",
    "cardholder_message": "Payment recalled",
    "approved": False,
    "merchant_message": "Payment recalled"
  },
  "475": {
    "type": "Paymentech",
    "cardholder_message": "WX Not Allowed",
    "approved": False,
    "merchant_message": "WX Not Allowed"
  },
  "110\u2013122": {
    "type": "TD",
    "cardholder_message": "Declined",
    "approved": False,
    "merchant_message": "Declined"
  },
  "1079": {
    "type": "Desjardins",
    "cardholder_message": "INVALID PROGRAM",
    "approved": False,
    "merchant_message": "Declined. PPC - The selected program is inactive"
  },
  "665\u2013668": {
    "type": "INTERAC Online",
    "cardholder_message": "CANNOT PROCESS PLEASE RE-TRY",
    "approved": False,
    "merchant_message": "RETRY SYSTEM PROBLEM"
  },
  "627": {
    "type": "EBP/ACH",
    "cardholder_message": "Edit Reject",
    "approved": False,
    "merchant_message": "Edit Reject"
  },
  "934": {
    "type": "UK",
    "cardholder_message": "Blocked in fraud screening",
    "approved": False,
    "merchant_message": "Blocked in fraud screening"
  },
  "889": {
    "type": "UK",
    "cardholder_message": "Server received corrupt input data format",
    "approved": False,
    "merchant_message": "Server received corrupt input data format"
  },
  "509": {
    "type": "Vital",
    "cardholder_message": "Card No. Error",
    "approved": False,
    "merchant_message": "Card No. Error"
  },
  "686": {
    "type": "First Data",
    "cardholder_message": "INVLD MER ID",
    "approved": False,
    "merchant_message": "INVLD MER ID"
  },
  "576": {
    "type": "Global Payments",
    "cardholder_message": "UNAUTH TRANS",
    "approved": False,
    "merchant_message": "UNAUTH TRANS"
  },
  "1016": {
    "type": "Desjardins",
    "cardholder_message": "INVALID CARD",
    "approved": False,
    "merchant_message": "Declined. Track2 invalid"
  },
  "354": {
    "type": "Paymentech",
    "cardholder_message": "Invalid ABA No",
    "approved": False,
    "merchant_message": "Invalid ABA No"
  },
  "1038": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. Declined by the issuer"
  },
  "768": {
    "type": "EBP/ACH",
    "cardholder_message": "No pre-notification - Business",
    "approved": False,
    "merchant_message": "No pre-notification - Business"
  },
  "359": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Tran Fmt",
    "approved": False,
    "merchant_message": "Invalid Tran Fmt"
  },
  "909": {
    "type": "UK",
    "cardholder_message": "Invalid Amount",
    "approved": False,
    "merchant_message": "Invalid Amount"
  },
  "1008": {
    "type": "Desjardins",
    "cardholder_message": "INVALID CARD",
    "approved": False,
    "merchant_message": "Declined. The Admin card must be from the same institution as the POS"
  },
  "610": {
    "type": "Global Payments",
    "cardholder_message": "EXCEEDS MAX AMT",
    "approved": False,
    "merchant_message": "EXCEEDS MAX AMT"
  },
  "854\u2013855": {
    "type": "UK",
    "cardholder_message": "Transaction refused",
    "approved": False,
    "merchant_message": "Transaction refused"
  },
  "714": {
    "type": "First Data",
    "cardholder_message": "INV ACCT",
    "approved": False,
    "merchant_message": "INV ACCT"
  },
  "1072": {
    "type": "Desjardins",
    "cardholder_message": "DECLINED",
    "approved": False,
    "merchant_message": "Declined. EMV - Error with the security box"
  },
  "383": {
    "type": "Paymentech",
    "cardholder_message": "Auth Declined",
    "approved": False,
    "merchant_message": "CVD Error 248"
  },
  "531": {
    "type": "Vital",
    "cardholder_message": "Unsolic Reversal",
    "approved": False,
    "merchant_message": "Unsolic Reversal"
  },
  "1048": {
    "type": "Desjardins",
    "cardholder_message": "PLEASE RETRY",
    "approved": False,
    "merchant_message": "Declined. System error"
  },
  "646": {
    "type": "INTERAC Online",
    "cardholder_message": "INVALID CARD REFER TO BRANCH",
    "approved": False,
    "merchant_message": "INVALID CARD REFER TO BRANCH"
  },
  "940": {
    "type": "Bambora",
    "cardholder_message": "DECLINE",
    "approved": False,
    "merchant_message": "Masterpass account is not enabled"
  },
  "918": {
    "type": "UK",
    "cardholder_message": "Invalid CVD Code State",
    "approved": False,
    "merchant_message": "Invalid CVD Code State"
  },
  "593": {
    "type": "Global Payments",
    "cardholder_message": "APPROVED",
    "approved": True,
    "merchant_message": "APPROVED"
  },
  "1001": {
    "type": "Desjardins",
    "cardholder_message": "APPROVED",
    "approved": True,
    "merchant_message": "Approved with balance"
  },
  "1042": {
    "type": "Desjardins",
    "cardholder_message": "PIN REQUIRED",
    "approved": False,
    "merchant_message": "Declined. The card PIN is required for this card (can be admin card)"
  },
  "318": {
    "type": "Bambora",
    "cardholder_message": "CALL HELP DESK",
    "approved": False,
    "merchant_message": "No transaction request data received"
  },
  "441": {
    "type": "Paymentech",
    "cardholder_message": "Proc Error 14",
    "approved": False,
    "merchant_message": "Proc Error 14"
  },
  "373": {
    "type": "Paymentech",
    "cardholder_message": "Card Not Allowed",
    "approved": False,
    "merchant_message": "Card Not Allowed"
  },
  "572": {
    "type": "Global Payments",
    "cardholder_message": "INVLD ACCT",
    "approved": False,
    "merchant_message": "INVLD ACCT"
  },
  "451": {
    "type": "Paymentech",
    "cardholder_message": "Proc Error 24",
    "approved": False,
    "merchant_message": "Proc Error 24"
  },
  "211": {
    "type": "Bambora",
    "cardholder_message": "Service Unavailable - Please try again later",
    "approved": False,
    "merchant_message": "Service Unavailable - Please try again later"
  },
  "941": {
    "type": "Bambora",
    "cardholder_message": "DECLINE",
    "approved": False,
    "merchant_message": "oauth_verifier is required"
  },
  "458": {
    "type": "Paymentech",
    "cardholder_message": "Dscv Not Allowed",
    "approved": False,
    "merchant_message": "Dscv Not Allowed"
  },
  "671": {
    "type": "INTERAC Online",
    "cardholder_message": "CANNOT PROCESS",
    "approved": False,
    "merchant_message": "CANNOT PROCESS"
  },
  "1080": {
    "type": "Desjardins",
    "cardholder_message": "TRX NOT ALLOWED",
    "approved": False,
    "merchant_message": "Declined. PPC - The merchant does not have access to the transaction program"
  },
  "463\u2013469": {
    "type": "Paymentech",
    "cardholder_message": "Failed-Plz Call",
    "approved": False,
    "merchant_message": "Failed-Plz Call"
  },
  "406": {
    "type": "Paymentech",
    "cardholder_message": "Invalid Function",
    "approved": False,
    "merchant_message": "Invalid Function"
  },
  "694": {
    "type": "First Data",
    "cardholder_message": "EXPIRED CARD",
    "approved": False,
    "merchant_message": "EXPIRED CARD"
  },
  "860": {
    "type": "UK",
    "cardholder_message": "Transaction refused: The type of the reference transaction does not allow this transaction",
    "approved": False,
    "merchant_message": "Transaction refused: The type of the reference transaction does not allow this transaction"
  },
  "629": {
    "type": "EBP/ACH",
    "cardholder_message": "Currency/Account Mismatch",
    "approved": False,
    "merchant_message": "Currency/Account Mismatch"
  },
  "1004": {
    "type": "Desjardins",
    "cardholder_message": "APPROVED",
    "approved": True,
    "merchant_message": "Approved. Administrative Transaction"
  },
  "440": {
    "type": "Paymentech",
    "cardholder_message": "Proc Error 13",
    "approved": False,
    "merchant_message": "Proc Error 13"
  },
  "902": {
    "type": "UK",
    "cardholder_message": "Invalid Order Description",
    "approved": False,
    "merchant_message": "Invalid Order Description"
  }
}

avs_response_codes = {
  '0': {'result': '0', 'processed': '0', 'address': '0', 'postal': '0', 'message': 'Address Verification not performed for this transaction.'},
  '5': {'result': '0', 'processed': '0', 'address': '0', 'postal': '0', 'message': 'Invalid AVS Response.'},
  '9': {'result': '0', 'processed': '0', 'address': '0', 'postal': '0', 'message': 'Address Verification Data contains edit error.'},
  'A': {'result': '0', 'processed': '1', 'address': '1', 'postal': '0', 'message': 'Street address matches, Postal/ZIP does not match.'},
  'B': {'result': '0', 'processed': '1', 'address': '1', 'postal': '0', 'message': 'Street address matches, Postal/ZIP not verified.'},
  'C': {'result': '0', 'processed': '1', 'address': '0', 'postal': '0', 'message': 'Street address and Postal/ZIP not verified.'},
  'D': {'result': '1', 'processed': '1', 'address': '1', 'postal': '1', 'message': 'Street address and Postal/ZIP match.'},
  'E': {'result': '0', 'processed': '0', 'address': '0', 'postal': '0', 'message': 'Transaction ineligible.'},
  'G': {'result': '0', 'processed': '0', 'address': '0', 'postal': '0', 'message': 'Non AVS participant. Information not verified.'},
  'I': {'result': '0', 'processed': '0', 'address': '0', 'postal': '0', 'message': 'Address information not verified for international transaction.'},
  'M': {'result': '1', 'processed': '1', 'address': '1', 'postal': '1', 'message': 'Street address and Postal/ZIP match.'},
  'N': {'result': '0', 'processed': '1', 'address': '0', 'postal': '0', 'message': 'Street address and Postal/ZIP do not match.'},
  'P': {'result': '0', 'processed': '1', 'address': '0', 'postal': '1', 'message': 'Postal/ZIP matches. Street address not verified.'},
  'R': {'result': '0', 'processed': '0', 'address': '0', 'postal': '0', 'message': 'System unavailable or timeout.'},
  'S': {'result': '0', 'processed': '0', 'address': '0', 'postal': '0', 'message': 'AVS not supported at this time.'},
  'U': {'result': '0', 'processed': '0', 'address': '0', 'postal': '0', 'message': 'Address information is unavailable.'},
  'W': {'result': '0', 'processed': '1', 'address': '0', 'postal': '1', 'message': 'Postal/ZIP matches, street address does not match.'},
  'X': {'result': '1', 'processed': '1', 'address': '1', 'postal': '1', 'message': 'Street address and Postal/ZIP match.'},
  'Y': {'result': '1', 'processed': '1', 'address': '1', 'postal': '1', 'message': 'Street address and Postal/ZIP match.'},
  'Z': {'result': '0', 'processed': '1', 'address': '0', 'postal': '1', 'message': 'Postal/ZIP matches, street address does not match.'},
}
