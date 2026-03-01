import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.services.post_alert_management import router as post_alert_management_router
from app.services.institution_management import router as institution_management_router

logger = logging.getLogger(__name__)
app = FastAPI()

app.include_router(post_alert_management_router.router)
app.include_router(institution_management_router.router)

# Exception handlers
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=422, content={"detail": exc.errors()})

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return await http_exception_handler(request, exc)

@app.exception_handler(RequestValidationError)
async def form_validation_exception_handler(request: Request, exc: RequestValidationError):
    return await validation_exception_handler(request, exc)
