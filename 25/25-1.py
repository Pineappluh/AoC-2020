def get_loop_number(pk):
    subject = 7
    n = 7
    i = 1
    while n != pk:
        n = (n * subject) % 20201227
        i += 1
    return i


def transform(subject, loops):
    n = 1
    for i in range(loops):
        n = (n * subject) % 20201227
    return n


card_pk = 523731
door_pk = 1717001

card_loops = get_loop_number(card_pk)
door_loops = get_loop_number(door_pk)

sk = transform(card_pk, door_loops)
print(sk)
