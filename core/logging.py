import logging

def get_logger(name: str = "HermesCore", level: str = "INFO"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(level)
        handler = logging.StreamHandler()
        formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(name)s: %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
