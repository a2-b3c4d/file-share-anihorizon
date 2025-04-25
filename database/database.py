import motor.motor_asyncio
from config import DB_URI, DB_NAME

# Create an async MongoClient
dbclient = motor.motor_asyncio.AsyncIOMotorClient(DB_URI)
database = dbclient[DB_NAME]

# Collection for users
user_data = database['users']

# Function to check if a user is present in the database
async def present_user(user_id: int):
    found = await user_data.find_one({'_id': user_id})  # Use await for async operation
    return bool(found)

# Function to add a new user to the database
async def add_user(user_id: int):
    await user_data.insert_one({'_id': user_id})  # Use await for async operation
    return

# Function to fetch all user IDs from the database
async def full_userbase():
    user_docs = user_data.find()  # Returns an async cursor
    user_ids = []
    async for doc in user_docs:  # Use async for to iterate over async cursor
        user_ids.append(doc['_id'])
    return user_ids

# Function to delete a user from the database
async def del_user(user_id: int):
    await user_data.delete_one({'_id': user_id})  # Use await for async operation
    return
