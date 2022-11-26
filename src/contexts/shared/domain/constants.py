from dataclasses import dataclass


@dataclass
class LoggerLevels:
    DEBUG = "debug"
    ERROR = "error"
    INFO = "info"


DomainConstants = {
    "uuid_version": 4,
    "logger_filename": "log/logs.txt",
    "logger_name": "DomainLogger",
    "logger_level": LoggerLevels.INFO,
    "logger_format": "%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    "logger_date_format": "%d-%b-%y %H:%M:%S",
}
