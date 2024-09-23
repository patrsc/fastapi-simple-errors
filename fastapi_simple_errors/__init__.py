"""Simple error handling for fastapi using custom error classes."""

from typing import Any, Type

from fastapi import HTTPException, status
from pydantic import BaseModel, Field


class ErrorDetail(BaseModel):
    """Represents error details."""

    error: str = Field(description="error identifier")
    message: str = Field(description="error message")


class ErrorResponse(BaseModel):
    """Represents an error response."""

    detail: ErrorDetail = Field(description="details about the error")


ResponseModelDict = dict[int | str, dict[str, Any]]


class AppError(HTTPException):
    """An error occurred."""

    # Light wrapper around HTTPException that allows specifying status code via class property
    # and default message via docstring.
    # The Python class name is used as error identifier.

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    headers = None
    model = ErrorResponse

    def __init__(self, message: str | None = None, headers: dict[str, str] | None = None) -> None:
        """Initialize."""
        message = message if message is not None else self.__doc__
        detail = ErrorDetail(message=message, error=self.__class__.__name__).model_dump()
        headers = headers if headers is not None else self.headers
        super().__init__(status_code=self.status_code, detail=detail, headers=headers)

    @classmethod
    def response_model(cls) -> ResponseModelDict:
        """Generate response model."""
        return {cls.status_code: {"model": cls.model}}


class BadRequestError(AppError):
    """Bad request."""

    status_code = status.HTTP_400_BAD_REQUEST


class UnauthorizedError(AppError):
    """Unauthorized."""

    status_code = status.HTTP_401_UNAUTHORIZED


class NotFoundError(AppError):
    """Not found."""

    status_code = status.HTTP_404_NOT_FOUND


def error_responses(*args: Type[AppError]) -> ResponseModelDict:
    """Generate dict of responses for errors."""
    responses = {}
    for cls in args:
        responses.update(cls.response_model())
    return responses


def error_responses_from_status_codes(
    *args: int, table: dict[int, Type[AppError]] | None = None
) -> ResponseModelDict:
    """Generate dict of responses for errors (from status codes)."""
    if table is None:
        table = default_errors_table()
    return error_responses(*(table[code] for code in args))


def default_errors_table() -> dict[int, Type[AppError]]:
    """Get mapping from status codes to exception classes."""
    return {
        400: BadRequestError,
        401: UnauthorizedError,
        404: NotFoundError,
    }
