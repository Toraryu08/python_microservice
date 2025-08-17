#!/usr/bin/env python3
"""Weather Application that uses Weather API"""

from fastapi import FastAPI
import uvicorn
import httpx

app = FastAPI()


@app.get("/")
async def read_root():
    """Root endpoint for the Weather API"""
    return {
        "message": "Welcome to the Weather API! Use /weather/{location} to get weather information."
    }


@app.get("/weather/{location}")
async def get_weather(location: str):
    """Get weather information for a specific location."""
    url = f"https://wttr.in/{location}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            return {"location": location, "weather": response.text}
        return {
            "error": "Could not retrieve weather data",
            "status_code": response.status_code,
        }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
