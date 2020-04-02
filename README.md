# ezsockets
Make Python TCP easy with this library!
## Server Sample Code
```
from ezsockets import server
action = '''
print(data)
'''
server(443, action)

```
## Client Sample Code
```
from ezsockets import client
host = 'localhost'
port = 443
message = 'test'
client('localhost', 443, "Test")
```
