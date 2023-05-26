import logging


logger = logging.getLogger(__name__)
FORMAT = "[%(asctime)s %(filename)s:%(lineno)s %(funcName)s() %(levelname)s] %(message)s"
logging.basicConfig(format=FORMAT,
                    level=logging.INFO)
#filename="logfile.txt")

logging.info("this is a info")
logging.debug("this is a info")
logging.warning("this is a warning", extra={"a": "b"})
logging.error("this is a error")

try:
    res = 1 / 0
except ZeroDivisionError:
    logging.exception("Attempted division by zero")
