from fastapi import APIRouter

app = APIRouter()


@app.post('/login')
async def login():
    return {'message': 'Login router'}
