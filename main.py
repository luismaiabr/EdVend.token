from fastapi import FastAPI  
from fastapi.responses import JSONResponse  
import uvicorn  

app = FastAPI()  

@app.get("/oauth/callback")  
async def oauth_callback(  
    client_id: str,  
    client_secret: str,  
    grant_type: str = 'authorization_code',  
    code: str | None = None,  
    redirect_uri: str | None = None  
):  
    if not all([client_id, client_secret, code, redirect_uri]):  
        return JSONResponse({  
            "status": "error",  
            "error": "Missing required parameters"  
        })  
    print(f'code: {code}')
    return JSONResponse({  
        "status": "success",  
        "client_id": client_id,  
        "grant_type": grant_type,  
        "code": code,  
        "redirect_uri": redirect_uri  
    })  

if __name__ == "__main__":  
    uvicorn.run(  
        "main:app",  
        host="0.0.0.0",  
        port=443,  
        ssl_keyfile="key.pem",  
        ssl_certfile="cert.pem",  
        reload=True  
    )