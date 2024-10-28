from fastapi import FastAPI, Request  
from fastapi.responses import JSONResponse  
import uvicorn  

app = FastAPI()  

@app.get("/oauth/callback")  
async def oauth_callback(  
    code: str | None = None,  
    state: str | None = None,  
    referer: str | None = None,  
    client_id: str | None = None,error: str | None = None  
):  
    if error:  
        return JSONResponse({  
            "status": "error",  
            "error": error  
        })  
    
    return JSONResponse({  
        "status": "success",  
        "code": code,  
        "state": state,  
        "referer": referer,  
        "client_id": client_id  
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
