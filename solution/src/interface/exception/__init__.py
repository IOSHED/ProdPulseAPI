from fastapi.exceptions import RequestValidationError
from src.interface.exception.json_handlers import (
    base_exception_handler,
    db_unique_exception_handler,
    doesnot_exists_handler,
    profile_access_denied_exception_handler,
    validation_exception_handler,
)
from src.infra.database.exception import DBUniqueException
from src.domain.exception.service_exception import (
    BaseRouterException,
    DoesNotExistsException,
    ProfileAccessDenied,
)


exception_handlers = [
    (DoesNotExistsException, doesnot_exists_handler),
    (BaseRouterException, base_exception_handler),
    (RequestValidationError, validation_exception_handler),
    (DBUniqueException, db_unique_exception_handler),
    (ProfileAccessDenied, profile_access_denied_exception_handler),
]
