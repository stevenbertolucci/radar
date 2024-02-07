def uv_index(uv):
    if uv == 0:
        return '\033[0m'
    elif 1 <= uv <= 3:
        return '\033[96m'
    elif 4 <= uv <= 6:
        return '\033[93m'
    elif 7 <= uv <= 9:
        return '\033[94m'
    elif 10 <= uv <= 12:
        return '\033[91m'
    else:
        return '\033[95m'
