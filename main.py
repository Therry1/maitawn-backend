import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.exception_handlers import http_exception_handler, validation_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI


from app.services.post_alert_management import router as post_alert_management_router
from app.services.institution_management import router as institution_management_router

'''
 import relatif à la cache
'''

logger = logging.getLogger(__name__)

app = FastAPI()

# inclusion des routes

app.include_router(post_alert_management_router.router)
app.include_router(institution_management_router.router)


# Gestionnaires d'exceptions personnalisés
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return await http_exception_handler(request, exc)

@app.exception_handler(RequestValidationError)
async def form_validation_exception_handler(request: Request, exc: RequestValidationError):
    return await validation_exception_handler(request, exc)


from mangum import Mangum
handler = Mangum(app)