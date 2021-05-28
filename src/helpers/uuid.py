import re

def is_UUID(payload) -> bool:
    uuid_regex = '[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}'

    if(re.search(uuid_regex, payload)):
        return True
    
    return False