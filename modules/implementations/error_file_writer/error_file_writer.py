from datetime import datetime
from modules.interfaces.error_handler_interface import ErrorHandlerInterface, LEVEL
from settings import Settings


class ErrorFileWriter(ErrorHandlerInterface):
    def __init__(self, cfg: Settings.ErrorHandler) -> None:
        self.cfg = cfg
        # Create a new file or clear the existing file
        with open(self.cfg.path, 'w') as f:
            f.write('')

    def handle(self, lvl: LEVEL, info: str) -> None:
        # Get the current timestamp if needed
        timestamp = '[' + datetime.now().isoformat() + ']\t' if self.cfg.save_timestamp else ''
        log_entry = f"{timestamp}[{lvl}]\t{info}\n"
        # Append the log entry to the file
        with open(self.cfg.path, 'a') as f:
            f.write(log_entry)
