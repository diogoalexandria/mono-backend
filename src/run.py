from src.config import PORT
import uvicorn
import src.server.main

def app(): 
    uvicorn.run("src.server.main:app", host='0.0.0.0', port=int(PORT), reload=True, debug=True, workers=1)