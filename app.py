from fastapi import FastAPI, Request
from bson import ObjectId
import motor.motor_asyncio
import pydantic 

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://Martianally13:<lifegoeson13>@cluster0.cz1u8gu.mongodb.net/?retryWrites=true&w=majority")
db = client.profile


pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str


@app.post("/profile")
async def create_new_profile(request: Request):
    profile_object = await request.json()

    new_profile = await db["profile"].insert_one(profile_object)
    created_profile = await db["profile"].find_one({"_id": new_profile.inserted_id})

    return created_profile



