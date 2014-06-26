import urllib2
import urllib

# Specify the url
url = 'https://webservice.paymentxp.com/wh/GetToken.aspx?CardNumber=4111111111111111ExpirationDateMMYY=1218&MerchantID=10012'
# This packages the request (it doesn't make it) 
request = urllib2.Request(url)

# Sends the request and catches the response
response = urllib2.urlopen(request)

# Extracts the response
html = response.read()

# Print it out
print html 
