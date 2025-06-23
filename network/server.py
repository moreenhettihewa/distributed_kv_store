# network/server.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from kv_store import KVStore

app = FastAPI()
store = KVStore(None)  # Will be initialized per node
node_id = None

class KeyValue(BaseModel):
    value: str

@app.get("/kv/{key}")
def get_key(key: str):
    value = store.get_key(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"key": key, "value": value}

@app.put("/kv/{key}")
def set_key(key: str, payload: KeyValue):
    store.set_key(key, payload.value)
    return {"message": f"Key '{key}' set successfully."}

@app.delete("/kv/{key}")
def delete_key(key: str):
    store.delete(key)
    return {"message": f"Key '{key}' deleted successfully."}

@app.get("/health")
def health():
    return {"status": "OK", "node_id": node_id}

def start_server(db_file: str, id: str, port: int = 8000):
    global store, node_id
    store = KVStore(db_file)
    node_id = id

    import uvicorn
    uvicorn.run("network.server:app", host="0.0.0.0", port=port, reload=False)