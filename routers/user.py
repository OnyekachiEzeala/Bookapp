from fastapi import APIRouter, HTTPException

from database import users
from schemas.user import UserBase, UserUpdate
from services.user import user_service

user_router = APIRouter()

@user_router.get("")
def get_users():
  return users

@user_router.get("/{user_id}")
def get_user(user_id: int):
  user = user_service.get_user_by_id(user_id)
  if not user:
    raise HTTPException(status_code=404, detail="User not found.")
  return user

@user_router.post("")
def add_user(user_in: UserBase):
  user = user_service.create_user(user_in)
  return {"message": "User added successfully", "user": user}

@user_router.put("/{user_id}")
def update_user(user_id: int, user_update: UserUpdate):
  user = user_service.update_user(user_id, user_update)
  if not user:
    raise HTTPException(status_code=404, detail="User not found")
  return {"message": "User updated successfully", "user": user}

@user_router.delete("/{user_id}")
def delete_user(user_id: int):
  is_deleted = user_service.delete_user(user_id)
  if not is_deleted:
    raise HTTPException(
      status_code=404, 
      detail=f"User with id: {user_id} not found"
    )
  return {"message": "User deleted successfully"}