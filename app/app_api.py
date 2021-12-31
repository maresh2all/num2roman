from fastapi import FastAPI, Request, Response
from app.controllers import main_controller
from mangum import Mangum
description = """
This API helps you do awesome stuff. 🚀

## Convert integers to roman numerals

"""

app = FastAPI(
    title="num2romanAPI",
    description=description,
    version="v0",
    contact={
        "name": "Mares Radomir",
        "email": "maresh2all@gmail.com",
    }
)

# All errors are reported as 500
@app.exception_handler(Exception)      
async def basic_error(request: Request, exc: Exception):         
    return Response("An error occured: " + str(exc), status_code=500)

app.include_router(main_controller.router)

@app.get("/", tags=["Root"])
async def root():
    return {"message": "This is the root of num2roman API!"}

handler = Mangum(app)