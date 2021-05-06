import uvicorn
from config import PORT
import src.server.main as main

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=int(PORT), reload=True, debug=True, workers=1)