# **Logging Configuration**

Logging is an essential part of any bot as it helps in debugging and tracking the bot's behavior. UDISCORD provides a flexible logging system that allows you to set different log levels and enable socket tracing for a better understanding of the interaction between your bot and Discord servers.

By default, the logging level is set to `INFO`, meaning that only general informational messages, warnings, and critical errors will be logged.

---

### **1. Setting the Logging Level**

UDISCORD allows you to set the logging level for your bot to control the amount and severity of the logged messages. This is useful when you need to track different aspects of the bot's operation or debug specific issues.

You can set the logging level using the `set_log_level` function. The available logging levels are:

- `logging.DEBUG`: Detailed logs, including information for debugging. This is the most detailed logging level.
- `logging.INFO`: General informational messages showing the bot's actions.
- `logging.WARNING`: Warnings about potential problems or events that require attention but do not necessarily indicate a failure.
- `logging.CRITICAL`: Only the most serious errors or critical problems that require immediate attention are logged.

Example of setting the logging level:

```python
from udiscord import set_log_level, logging

# Set the logging level to DEBUG (the most detailed)
set_log_level(logging.DEBUG)

# Set the logging level to CRITICAL (only critical errors will be logged)
set_log_level(logging.CRITICAL)

# Other logging levels can also be set as needed
set_log_level(logging.WARNING)
set_log_level(logging.INFO)
```

By setting an appropriate logging level, you can control how much information is logged, which is useful during development and on a production server.

---

### **2. Built-in Logger**

Additionally, you can use the built-in logger from the UDISCORD library. To do so, you need to import the log instance and use its methods to log messages at different log levels.

Example of using the built-in logger:

```python
from udiscord import log

# Logging at the DEBUG level
log.debug("DEBUG MSG")

# Logging at the CRITICAL level
log.critical("CRITICAL ERROR")

# Logging at the INFO level
log.info("Informational message")
```
Logging methods:

- `debug(message)`: Logs a message at the DEBUG level.
- `info(message)`: Logs an informational message.
- `warning(message)`: Logs a warning.
- `error(message)`: Logs an error.
- `critical(message)`: Logs a critical error.

---

### **3. Socket Tracing**

Socket tracing is a powerful debugging tool that allows you to see the raw data of interactions between your bot and Discord servers. This can be helpful when troubleshooting API requests or when you want to see what data is being sent and received.

To enable socket tracing, pass the parameter sock_trace=True when creating the Client instance:

```python
from udiscord import Client

# Enable socket tracing for detailed logs about interactions between the bot and Discord
client = Client(sock_trace=True)
```

When socket tracing is enabled, the bot will log raw socket data, including HTTP requests and responses, as well as any WebSocket messages. This is useful for debugging issues with API requests or identifying communication problems.

### **4. Conclusion**

UDISCORD provides a simple and flexible logging system that you can use to configure the amount of information logged. By setting the appropriate logging level and enabling socket tracing, you can easily track your bot's behavior and troubleshoot any issues that arise.


<div align="center">
  <a href="https://github.com/xXxCLOTIxXx/discord/blob/main/docs/index.md">🏠Main</a>
</div>
