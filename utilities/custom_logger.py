import logging


class LogGen:
    @staticmethod
    def logging_setup():
        logging.basicConfig(filename=".\\logs\\log_report.log",
                            format='%(asctime)s - %(levelname)s - %(name)s : %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
