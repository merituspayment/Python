import urllib2
import urllib

# Specify the url
url = 'https://webservice.paymentxp.com/wh/webhost.aspx?MerchantID=10012&MerchantKey=c22a63ee-2e7a-4ace-96ac-0958dc8d953f&AccountNumber=1234567890&RoutingNumber=111000025&TransactionType=AddCustomer&CustomerName=John+Doe&CustomerID=JohnDoe1234'

# This packages the request (it doesn't make it) 
request = urllib2.Request(url)

# Sends the request and catches the response
response = urllib2.urlopen(request)

# Extracts the response
html = response.read()

# Print it out
print html 
