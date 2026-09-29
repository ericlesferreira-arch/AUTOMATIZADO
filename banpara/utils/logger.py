import logging

def setup_logger(nome="AUTOMACAO"):
    logger = logging.getLogger(nome)
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger  # evita duplicar handler

    file_handler = logging.FileHandler("test_fluxo.log", mode="a", encoding="utf-8")
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger