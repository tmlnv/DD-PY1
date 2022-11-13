import string
from random import sample


def get_random_password(n=8) -> str:
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    rand_pass_list = sample((upper + lower + digits), n)
    return ''.join([v for v in rand_pass_list])


print(get_random_password())
