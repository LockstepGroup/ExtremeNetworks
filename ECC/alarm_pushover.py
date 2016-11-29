import httplib, urllib,sys

sys.argv.remove(sys.argv[0])

conn = httplib.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "APP_TOKEN",
    "user": "USER_KEY",
    "message": " ".join(sys.argv),
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()

