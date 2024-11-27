from random import randint, random
from time import time

from stack import Stack


# It might have made more sense to have only one
# stack as a parameter and to create the empty stack
# locally, but this is according to the instructions.
def sort(a: Stack, b: Stack) -> Stack:
    assert b.is_empty()

    while not a.is_empty():
        tmp = a.pop()

        while (top := b.pop()) is not None:
            if top < tmp:
                a.push(top)
            else:
                b.push(top)
                break

        # If our stack supported a `peek` operation, we
        # could simplify the loop above to the following:
        # while (top := b.peek()) is not None and top < tmp:
        #     a.push(b.pop())

        b.push(tmp)

    return b


def gen_random(size: int, min: int, max: int) -> Stack[int]:
    s = Stack()

    for _ in range(size):
        s.push(randint(min, max))

    return s


def gen_sorted_asc(size: int) -> Stack[int]:
    s = Stack()

    for i in reversed(range(size)):
        s.push(i)

    return s


def gen_sorted_desc(size: int) -> Stack[int]:
    s = Stack()

    for i in range(size):
        s.push(i)

    return s


def gen_almost_asc(size: int, error_chance: float) -> Stack[int]:
    assert 0 < error_chance < 1

    s = Stack()

    for i in reversed(range(size)):
        if random() < error_chance:
            s.push(i - 2)
        else:
            s.push(i)

    return s


def gen_almost_desc(size: int, error_chance: float) -> Stack[int]:
    assert 0 < error_chance < 1

    s = Stack()

    for i in range(size):
        if random() < error_chance:
            s.push(i + 2)
        else:
            s.push(i)

    return s


def is_sorted(stack: Stack) -> bool:
    a = stack.pop()

    while (b := stack.pop()) is not None:
        if a > b:
            return False
        else:
            a = b

    return True


def main():
    print("size\tsorted (asc.)\talmost asc.\tsorted (desc.)\talmost desc.\trandom")

    for size in (1, 10, 100, 1000, 10000, 50000):
        print(f"{size}\t", end="")

        inputs = (
            gen_sorted_asc(size),
            gen_almost_asc(size, 0.05),
            gen_sorted_desc(size),
            gen_almost_desc(size, 0.05),
            gen_random(size, 1, size),
        )
        for s in inputs:
            start = time()
            s = sort(s, Stack())
            end = time()

            assert is_sorted(s)

            elapsed = end - start
            print(f"{elapsed:<14.6g}\t", end="")

        print()


if __name__ == "__main__":
    main()
