import logging

logging.basicConfig(level=logging.INFO, filename="log.log", filemode='w',
                    format="%(asctime)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)

logger.info("Test the custom logger")
handler = logging.FileHandler('test.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("Test the custom logger")


logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

try:
    1/0
except ZeroDivisionError as e:
    logging.exception("Test Error")    