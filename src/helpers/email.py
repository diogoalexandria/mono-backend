import re

def is_email(payload) -> bool:
    email_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    if(re.search(email_regex, payload)):
        return True
    
    return False
    