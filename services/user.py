from database import users
from schemas.user import User, UserBase, UserUpdate

class UserService:

  @staticmethod
  def get_user_by_id(user_id: int):
    for user in users:
      if user.id == user_id:
        return user
    return None
  
  @staticmethod
  def create_user(user_in: UserBase):
    user_id = len(users) + 1
    new_user = User(id=user_id, **user_in.model_dump())
    users.append(new_user)
    return new_user
  
  @staticmethod
  def update_user(user_id: int, user_in: UserUpdate):
    for user in users:
      if user.id == user_id:
        user.name = user_in.name
        user.email = user_in.email
        return user
    return None
  
  @staticmethod
  def delete_user(user_id: int):
    for user in users:
      if user.id == user_id:
        users.remove(user)
        return True
    return False
  
user_service = UserService()

