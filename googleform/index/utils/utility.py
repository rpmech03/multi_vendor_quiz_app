import random
import string


#generate token by this 
def generate_random_string(N=10)->str:
    token = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(N))
    return token