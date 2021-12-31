from fastapi import APIRouter, Response, Request, Depends, HTTPException
from fastapi.security import  APIKeyHeader
from num2roman.num2roman import Int2RomanConverter
import app.security.security as _security

router = APIRouter(prefix='/api/v0', tags=["Decimal to Roman"])
security = APIKeyHeader(name="api_key")


@router.get('/num2roman/{number}')
async def forecast_icing_classification(number: int, api_key: APIKeyHeader = Depends(security)):
    ''' Gets a integer and returns the roman numeral '''
    # ckeck authentication
    if not _security.validate_api_key(api_key, method = 'hmac'):
        raise HTTPException(status_code=401, detail='Access denied. Invalid "Api-Key" value in the request headers.')
    
    try:
        converter = Int2RomanConverter()
        roman = converter.convert_int_to_roman(number)
    except Exception as e:
        return Response("Bad input for {0}: {1}".format(number, e), status_code=400)

    return roman