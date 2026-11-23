from fastapi import FastAPI

app = FastAPI(title="Beni Ne Kurtarır?")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
