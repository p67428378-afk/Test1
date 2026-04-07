from fastapi import FastAPI, HTTPException

app = FastAPI()

# In-memory user data (simulating a database)
users_db = {
    1: {"user_id": 1, "name": "John Doe"},
    2: {"user_id": 2, "name": "Jane Smith"},
}

@app.get("/profile/{user_id}")
async def read_profile(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]
