import logging
import os
from datetime import datetime

from from_root import from_root

# Create logs folder inside your project root
logs_dir = os.path.join(from_root(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Name of the log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
