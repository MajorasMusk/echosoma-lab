from fastapi import FastAPI
from pydantic import BaseModel
from scar_loop import run_scar_loop
from sigil_engine import run_sigil
from archive import get_archive, update_archive
from viz import render_sigil

app = FastAPI(title="ECHOSOMA Action Lab")

class SigilRequest(BaseModel):
    text: str
    temp: float = 25.0
    humidity: float = 0.5
    radiation: float = 0.0

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/scar_loop")
def scar_loop_endpoint(seed: str = "default"):
    return run_scar_loop(seed)

@app.post("/sigil")
def sigil_endpoint(req: SigilRequest):
    return run_sigil(req.text, {
        "temp": req.temp,
        "humidity": req.humidity,
        "radiation": req.radiation
    })

@app.get("/archive")
def archive_get():
    return get_archive()

@app.post("/archive")
def archive_post(entry: dict):
    return update_archive(entry)

@app.get("/viz")
def viz_endpoint():
    return render_sigil()
