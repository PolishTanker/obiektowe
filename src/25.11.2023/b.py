from collections.abc import Iterable

a = [1, 2, 3]
b = (1, 2, 3)
c = {1, 2, 3}
d = {"a": 1, "b": 2}


def select_best_user(users: Iterable[str]):
    for key in d:
        if key in users:
            return key
    return None


if __name__ == '__main__':
    # susers = {'abra', 'kadabra', 'żerdź'}
    susers = ('abra', 'kadabra', 'żerdź')
    print(select_best_user(susers))
    

d = {"a": 1, "b": 2}
users = ("abra", "kadabra", "żerdź")

print(select_best_user(users))
