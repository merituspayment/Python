import urllib2
import urllib

# Specify the url
url = 'https://webservice.paymentxp.com/wh/webhost.aspx?MerchantID=10012&MerchantKey=c22a63ee-2e7a-4ace-96ac-0958dc8d953f&CardNumber=4111111111111111&DayOfMonthOption=15&MonthlyOption=1&OccurenceOption=2&WeekOption=0&WeekdayOption=0&StartDate=08152014&MonthOfYearOption=1&ExpirationDateMMYY=1218&TransactionAmount=1.00&TransactionType=CreditCardRecurringCharge'
# This packages the request (it doesn't make it) 
request = urllib2.Request(url)

# Sends the request and catches the response
response = urllib2.urlopen(request)

# Extracts the response
html = response.read()

# Print it out
print html 
