import time
import logging
from fastapi import FastAPI, Request
from src.core.logging_config import CustomLogger
from  src.schemas.response_schema import ResponseModel

app = FastAPI()

info_logger = CustomLogger("INFO")
warning_logger = CustomLogger("WARNING")
error_logger = CustomLogger("ERROR")
critical_logger = CustomLogger("CRITICAL")

class LoggingMiddleware:
    async def __call__(self, request: Request, call_next):
        # Log the incoming request
        start_time = time.time()
        info_logger.log(f"Request: {request.method} {request.url}")
        # Process the request
        response = await call_next(request)
    
        # Log the response
        process_time = (time.time() - start_time) * 1000
        info_logger.log(f"Response: {response.status_code} | Time: {process_time:.2f} ms")
        warning_logger.log(f"Response: {response.status_code} | Time: {process_time:.2f} ms")
        critical_logger.log(f"Response: {response.status_code} | Time: {process_time:.2f} ms")
        error_logger.log(f"Response: {response.status_code} | Time: {process_time:.2f} ms")
        print(response)
        return response