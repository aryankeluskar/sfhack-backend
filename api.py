import uvicorn
from fastapi import FastAPI

if __name__ == "__main__":
    uvicorn.run("scrape:fast", reload=True)