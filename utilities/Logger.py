import logging


# 1st define log file
# 2nd define log format
# 3rd logfile ye format ko set kr
# 4th we need to add log handler
# set log level-->debug,info,warning,critical,error

class logger_class:
    @staticmethod
    def log_gen_method():

        log_file = logging.FileHandler(".\\Logs\\orangehrm.log")
        log_format = logging.Formatter("%(asctime)s : %(levelname)s : %(funcName)s : %(message)s")
        log_file.setFormatter(log_format)
        logger = logging.getLogger()
        logger.addHandler(log_file)
        logger.setLevel(logging.INFO)
        return logger

