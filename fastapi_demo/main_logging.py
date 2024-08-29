import logging
import time

from fastapi import FastAPI

app = FastAPI()

logging.basicConfig(
    filename="app.log",
    level=logging.WARN,
    datefmt="%Y-%m-%d %H:%M:%S",
)

# 로거 생성
# logger = logging.getLogger(__name__)
logger = logging.getLogger("base")
logger.setLevel(logging.ERROR)

logger = logging.getLogger("base.app")
logger.setLevel(logging.NOTSET)

# 파일 핸들러 설정
file_handler = logging.FileHandler(__name__)
file_handler.setLevel(logging.NOTSET)

# 콘솔 핸들러 설정
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 포맷 설정
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 핸들러 추가
logger.addHandler(file_handler)
logger.addHandler(console_handler)


@app.get("/")
def home():
    logger.debug("debug log")
    logger.info("info log")
    logger.warn("warn log")
    logger.error("error log")
    return "home"


@app.get("/sleep")
def sleep_api():
    time.sleep(0.2)
    return "ok"
