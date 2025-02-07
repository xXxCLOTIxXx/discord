## Extending Functionality

If the built-in functions of the library aren't enough for your needs, you can add your own custom functions. We also encourage you to suggest changes to improve the library.

### HTTP Requests

To make HTTP requests, you can directly use the `req` object available in the client.

```python
from udiscord import Client

client = Client()

# Make an HTTP request
client.req.make_request(method="GET", endpoint="/some/endpoint", body=None, allowed_code=200, proxies=None)

# Or use a session for various HTTP methods
client.req.session.get("http://example.com")
client.req.session.post("http://example.com", data={"key": "value"})
client.req.session.delete("http://example.com")
```

## WebSocket Communication

To send data through the WebSocket connection, use the built-in send method or directly interact with the socket object.


```python
# Send data using the built-in send method
client.send(data="Hello, Discord!")

# Or use the socket object for more control
client.socket.send(data="Hello, WebSocket!", opcode=1)
```

By utilizing these features, you can customize your client to handle both HTTP requests and WebSocket communication, tailoring the functionality to your specific needs.


<div align="center">
  <a href="https://github.com/xXxCLOTIxXx/discord/blob/main/docs/index.md">🏠Main</a>
</div>
