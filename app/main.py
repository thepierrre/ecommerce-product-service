from fastapi import FastAPI, HTTPException
from dependencies.api_key import API_KEY
import httpx
app = FastAPI()

url = f"https://api.nasa.gov/neo/rest/v1/feed?api_key={API_KEY}"

@app.get("/asteroids")
async def get_asteroids():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return response.json()
    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code, detail=exc.response.text)
    except httpx.HTTPError as exc:
        raise HTTPException(detail="Error while connecting to the external service.")
