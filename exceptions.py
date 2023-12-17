class RateLimitExceeded(Exception):
    pass

class QuotaExceeded(Exception):
    pass

class NotAllowed(Exception):
    pass

class IncorrectApikey(Exception):
    pass

class NotFound(Exception):
    pass

class ValidationError(Exception):
    pass

class OtherError(Exception):
    pass