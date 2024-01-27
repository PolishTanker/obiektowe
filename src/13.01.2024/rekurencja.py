# rekurencja / depth-first-search / przeszukiwanie w głąb
def read_dir(pre: str, depth: int) -> list[str]:
    print(f'starting at depth={depth}, pre={pre}')
    if depth == 0:
        return [pre]

    left = read_dir(pre + 'L', depth - 1)
    rght = read_dir(pre + 'R', depth - 1)

    print(f'finishing at depth={depth}, pre={pre}')

    return left + rght


if __name__ == '__main__':
    z = read_dir(pre='.', depth=3)
    print(z)