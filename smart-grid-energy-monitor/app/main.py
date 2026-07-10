from fastapi import FastAPI

app = FastAPI(
    title="Smart Grid Energy Monitoring System",
    description="Real-time Smart Grid Monitoring Backend",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "status": "running",
        "message": "Welcome to Smart Grid Energy Monitoring System"
    }