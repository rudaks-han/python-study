import json
import logging

import yaml

from fastapi import FastAPI
from talk.talk import print_talk

app = FastAPI()

# json으로 로딩
# config = json.load(open('./logger.json'))
# logging.config.dictConfig(config)

# yml로 로딩
with open("./logger.yml", 'rt') as f:
    loggingConfig = yaml.safe_load(f.read())
    logging.config.dictConfig(loggingConfig)

# 로거 생성
logger = logging.getLogger(__name__)


@app.get("/")
def home():
    logger.debug("debug log")
    logger.info("info log")
    logger.warn("warn log")
    logger.error("error log")

    print_talk()

    return "home"
