import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.exception_handlers import http_exception_handler, validation_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI

'''
 import relatif à la cache
'''

logger = logging.getLogger(__name__)

app = FastAPI()

# Gestionnaires d'exceptions personnalisés
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return await http_exception_handler(request, exc)

@app.exception_handler(RequestValidationError)
async def form_validation_exception_handler(request: Request, exc: RequestValidationError):
    return await validation_exception_handler(request, exc)

