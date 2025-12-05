import time

def is_data_good(s: str) -> bool:
    if not(all([lambda x: x.is_digit() for x in s])):
        return False
    try:
        time.strptime(s, '%Y%d%m')
    except ValueError:
        return False
    return True


def is_codepoint_good(s: str) -> bool:
    if not(all([lambda x: x.is_digit() or x in "ABCDEF" for x in s])):
        return False
    if len(s) != 5: 
        return False
    return True


def is_isbn10_good(s: str) -> bool:
    if not(all([lambda x: x.is_digit() for x in s])):
        return False
    if len(s) != 10: 
        return False
    return True
