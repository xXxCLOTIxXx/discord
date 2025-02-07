# **Event Handling and Command Creation**

UDISCORD allows you to easily handle events and create commands. Let's take a look at how to do this using the `Client` class.

---

### **1. Client Initialization and Login**

Before handling events, you need to initialize the client and log in.

```python
from udiscord import Client, EventType, Message

# Create a client instance
client = Client()

# Log in using email and password
client.login("email", "password")
```

---

### **2. Handling Events**

#### 2.1. Using a Decorator to Handle an Event

You can handle events by using the `@client.event()` decorator. For example, to handle the `MESSAGE_CREATE` event, you can use the following code:

```python
@client.event(EventType.MESSAGE_CREATE)
def on_message(event: Message):
    # Function that is triggered when a new message is created
    print("Message: ", event.content)
```

When a new message is created, this function will be called, and the content will be printed in the console.

#### 2.2. Using the `add_handler` Method for Handling Events

Another way to add an event handler is by using the `add_handler()` method. Here's an example:

```python
def on_message_handler(event: Message):
    # Event handler that prints the message content
    print("Message (via handler): ", event.content)

# Add the handler for the MESSAGE_CREATE event
client.add_handler(EventType.MESSAGE_CREATE, on_message_handler)
```

Now, when a new message is created, the `on_message_handler` function will be triggered.

#### 2.3. Event Types

UDISCORD supports a variety of event types. For example:

- `EventType.MESSAGE_CREATE` — Handles new message creation events.
- `EventType.ANY` — Handles any event (use with caution).

For a complete list of event types, refer to the Objects documentation.

---

### **3. Handling Commands**

UDISCORD allows you to create commands that users can trigger through messages.

#### 3.1. Using a Decorator to Create a Command

You can create a command using the `@client.command()` decorator. For example, to respond to the `!commands` or `/commands` command, use the following code:

```python
@client.command(["!commands", "/commands"])
def get_commands(message: Message):
    # The bot will reply saying it doesn't have commands
    client.send_message(message.channelId, "Sorry, I don't have commands :_(")
```

#### 3.2. Using the `add_command` Method to Create a Command

Alternatively, you can use the `add_command()` method:

```python
def get_commands_handler(message: Message):
    # Send a response to the command
    client.send_message(message.channelId, "Sorry, I don't have commands :_(")

# Register the command using add_command
client.add_command(["!commands", "/commands"], get_commands_handler)
```

---

### **4. Event Object Classes**

Each event type can return its own specific object class. These classes contain details and data relevant to the event. For example, the `MESSAGE_CREATE` event will return a `Message` object, which holds information about the message that was created.

For more information about the specific event object classes, refer to the Objects documentation.

---

Now you know how to handle events and create commands for your bot using UDISCORD. These tools will help you create dynamic and interactive Discord bots!


<div align="center">
  <a href="https://github.com/xXxCLOTIxXx/discord/blob/main/docs/index.md">🏠Main</a>
</div>
