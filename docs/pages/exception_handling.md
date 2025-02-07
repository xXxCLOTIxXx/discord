# **Error Handling**

In UDISCORD, error handling is made easy by providing several built-in exception classes. You can handle these exceptions to improve the robustness of your bot and provide meaningful feedback when things go wrong.

---

### **1. Basic Error Handling**

To handle errors during the login process (or any other part of the code), you can use standard `try` and `except` blocks. Here's an example of how to handle login errors:

```python
from udiscord import Client, exceptions

# Create a client instance
client = Client()

try:
    # Try to log in with provided credentials
    client.login("email", "password")
except exceptions.InvalidLoginOrPassword:
    # Handle invalid login credentials
    print("Invalid authentication data")
except exceptions.UnknownError as e:
    # Handle unknown errors
    print("Unknown error: ", e)
```

In this example:
- If the login data is incorrect, the `InvalidLoginOrPassword` exception will be raised.
- If there's an unknown error, the `UnknownError` exception will be caught, and its details will be printed.

---

### **2. Common Exceptions**

UDISCORD includes several exception classes that can be used for different error scenarios. Some of the most common exceptions are:

- `exceptions.InvalidLoginOrPassword`: Raised when invalid login credentials are provided.
- `exceptions.RateLimited`: Raised when the bot is rate-limited by Discord's servers.
- `exceptions.UnknownInvitation`: Raised when an unknown invitation is used.
- `exceptions.UnknownError`: A catch-all for any unspecified errors.

For a full list of exceptions and their descriptions, you can refer to the source code at [udiscord/utils/exceptions.py](https://github.com/xXxCLOTIxXx/discord/blob/main/udiscord/utils/exceptions.py).

---

### **3. Handling Multiple Exceptions**

You can also handle multiple exceptions by chaining them or using more specific handlers for different scenarios:

```python
try:
    # Your code that might raise exceptions
    client.login("email", "password")
except (exceptions.InvalidLoginOrPassword, exceptions.RateLimited):
    print("There was an issue with login or rate-limiting.")
except exceptions.UnknownError as e:
    print("Unknown error occurred: ", e)
```

This approach allows you to handle different types of exceptions with different error messages or actions.

---

### **4. Handling error groups**

There are 2 groups of main errors in the library. server errors and library errors (server errors are those answered by discord, and library errors are caused by incorrectly specifying arguments, lack of authorization, etc.)

```python
try:
    raise exceptions.ArgumentNotSpecifiedError("Missing required argument")
except exceptions.DiscordError:
    print("Server error")
except exceptions.LibraryError:
    print("User error")
```

```python
try:
    client.login("email", "password")
except exceptions.DiscordError as e:
    print(e)
```

---

### **5. Error Class List**

For all the exception classes and detailed descriptions, you can view the source code here:  
[udiscord/utils/exceptions.py](https://github.com/xXxCLOTIxXx/discord/blob/main/udiscord/utils/exceptions.py)

Here, you will find a complete list of all exceptions you can use and more advanced handling techniques.

---

Now, you have an understanding of how to handle errors in UDISCORD and can implement it to make your bot more resilient to unexpected issues.


<div align="center">
  <a href="https://github.com/xXxCLOTIxXx/discord/blob/main/docs/index.md">🏠Main</a>
</div>

