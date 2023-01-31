import logging
import os
from datetime import datetime

if not os.path.exists("log"):
    os.makedirs("log")

logging.basicConfig(filename='./log/' + '{:%Y-%m-%d}.log'.format(datetime.now()),
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)
