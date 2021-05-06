from src.models.user_model import UserModel

def is_active(user: UserModel) -> bool:
    if user.status == 'active':
        return True
    
    return False