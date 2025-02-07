# **Client Class Documentation**

The `Client` class is the main class for interacting with Discord's API. It provides methods for automating actions, managing accounts, and interacting with Discord.

---

### **Constructor Arguments:**

The `Client` class accepts the following arguments during initialization:

- **`proxies: dict = None`**  
  A dictionary for configuring proxies to use for the connection. This is useful if you need to route your traffic through a specific proxy server.

- **`sock_trace: bool = False`**  
  Enables WebSocket connection debugging if set to `True`. This provides detailed logs of the WebSocket connection and can be helpful for debugging issues with the connection or interactions with Discord’s API.

---

### **Attributes Available in the Client Class:**

The `Client` class provides several attributes that are available once the client is initialized and connected to the Discord WebSocket API.

- **`Client.token: str`**  
  A string containing the authorization token after the login process. This token is used to authenticate the bot with Discord's servers.

- **`Client.userId: int`**  
  The user ID of the account that is logged in. This is available after logging in successfully.

- **`Client.account: AccountInfo`**  
  An instance of the `AccountInfo` class that contains all the account details retrieved after the client connects to the WebSocket. This class includes information such as username, avatar, and other relevant account data.

---

### **Example Usage:**

```python
from udiscord import Client

# Create a new Client instance with no proxy and WebSocket debugging enabled
client = Client(sock_trace=True)

# Example of initializing the client with a proxy
proxies = {
    "http": "http://yourproxy.com:8080",
    "https": "https://yourproxy.com:8080"
}
client_with_proxy = Client(proxies=proxies)

# Access client data after logging in
print(client.token)  # Prints the bot's token
print(client.userId)  # Prints the bot's user ID
print(client.account)  # Prints account information
```

You can also retrieve the account ID using its token, with the built-in function:

```python
from udiscord import get_userId_from_token

uid = get_userId_from_token("DISCORD AUTH TOKEN")
```

---
### **Functions**

You can also view all the functions in the source code: [udiscord/client.py](https://github.com/xXxCLOTIxXx/discord/blob/main/udiscord/client.py)


## Login

### Login with Email and Password

```python
from udiscord import Client

# Create a client instance
client = Client()

# Log in with email and password (this also initiates the socket connection, and in a few seconds, account data will be available in client.account)
info = client.login(email="email", password="password")
print(info.token)  # Prints the token after successful login

# Log out and disconnect from the socket
client.logout()
```

### Login with a Saved Token

```python
# Log in using a previously obtained token
info = client.login_token(token="some token after login")

```

### QR Code Authentication

```python
# Authenticate using a QR code from another device
client.qrcode_auth(code="Y6f55Rf5", temporary_token=False)  # Scan the QR code and paste the code from the link to confirm login
```


# More soon... just look source code


<div align="center">
  <a href="https://github.com/xXxCLOTIxXx/discord/blob/main/docs/index.md">🏠Main</a>
</div>
