""" This file send a play command to a Sonos device """

import requests

IP = '192.168.0.112'
ACTION = '"urn:schemas-upnp-org:service:AVTransport:1#Play"'
ENDPOINT = '/MediaRenderer/AVTransport/Control'
BODY = '''
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"
 s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
  <s:Body>
    <u:Play xmlns:u="urn:schemas-upnp-org:service:AVTransport:1">
      <InstanceID>0</InstanceID>
      <Speed>1</Speed>
    </u:Play>
  </s:Body>
</s:Envelope>
'''

HEADERS = {
    'Content-Type': 'text/xml',
    'SOAPACTION': ACTION
}

URL = 'http://{ip}:1400{endpoint}'.format(ip=IP, endpoint=ENDPOINT)

REQ = requests.post(URL, data=BODY, headers=HEADERS)

print 'Response:'
print REQ.content
