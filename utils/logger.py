```python
import logging
import logging.config
from config import LOGGING_CONFIG

class Logger:
    def __init__(self):
        logging.config.dictConfig(LOGGING_CONFIG)
        self.logger = logging.getLogger(__name__)

    def log(self, message, level='info'):
        if level.lower() == 'info':
            self.logger.info(message)
        elif level.lower() == 'warning':
            self.logger.warning(message)
        elif level.lower() == 'error':
            self.logger.error(message)
        elif level.lower() == 'debug':
            self.logger.debug(message)
        elif level.lower() == 'critical':
            self.logger.critical(message)
        else:
            self.logger.info(message)

# Example usage:
# logger = Logger()
# logger.log("This is an info message")
# logger.log("This is a warning message", level='warning')
```