hf_token = None

def set_token(token):
    global hf_token
    hf_token = token

def get_token():
    global hf_token
    return hf_token
