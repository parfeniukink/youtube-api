import random
import string
import itertools


def get_generated_channel_id():
    channel_id = ''.join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(24))
    return channel_id


def get_generated_channel_id_2():
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    digits = list(string.digits)
    chars = lowercase + uppercase + digits
    return itertools.permutations(chars, 24)


if __name__ == '__main__':
    stop = 100
    generated_channel_ids = set()
    generated_channel_ids_2 = set()

    ids = get_generated_channel_id_2()
    while stop > 0:
        generated_channel_ids.add(get_generated_channel_id())
        generated_channel_ids_2.add(''.join(next(ids)))

        stop -= 1
    print(generated_channel_ids)
    print(generated_channel_ids_2)