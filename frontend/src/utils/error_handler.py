class ErrorHandler:
    def handle_exception(self, error):
        log_error(error)
        notify_admin(error)
