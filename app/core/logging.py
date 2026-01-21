import logging

# Set up structured logging
logger = logging.getLogger("telemetry-api")
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()

console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def get_logger():
    return logger
