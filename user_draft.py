from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel


app = FastAPI()

class UserBase(BaseModel):
  name: str
  email: str
  password: str

class User(UserBase):
  id: int

class UserUpdate(BaseModel):
  name: str
  email: str


users: list[User] = [] 


@app.get("/users", response_model=list[User])
def get_users():
  return users

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
  for user in users:
    if user.id == user_id:
      return user
  raise HTTPException(status_code= 404, detail="User not found")

@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserBase):
  user_id = len(users) + 1
  new_user = User(id=user_id, **user.model_dump())
  users.append(new_user)
  return new_user

@app.put("/users/{user_id}")
def update_user(user_id: int, user_update: UserUpdate):
  for user in users:
    if user.id == user_id:
      user.name = user_update.name
      user.email = user_update.email
      return {"message": "User updated successfully", "user": user}
  raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
def delete_user(user_id:int):
  for user in users:
    if user.id == user_id:
      users.remove(user)
      return {"message": "User deleted successfully"}
  raise HTTPException(status_code=404, detail="User not found")