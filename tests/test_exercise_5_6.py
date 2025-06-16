try:
    from adt_examples.deque import Deque
except:
    pass
import pytest
import sys
import numpy as np


class StaticList(list):
    """A list object whose length cannot be changed once it is created."""

    def append(self, object, /):
        raise TypeError(
            "The list underpinning your Deque should be fixed length. "
            "Calling the append method is not allowed."
        )

    def insert(self, index, object, /):
        raise TypeError(
            "The list underpinning your Deque should be fixed length. "
            "Calling the insert method is not allowed."
        )

    def pop(self):
        raise TypeError(
            "The list underpinning your Deque should be fixed length. "
            "Calling the pop method is not allowed."
        )

    def extend(self, iterable, /):
        raise TypeError(
            "The list underpinning your Deque should be fixed length. "
            "Calling the extend method is not allowed."
        )

    def remove(self, value, /):
        raise TypeError(
            "The list underpinning your Deque should be fixed length. "
            "Calling the remove method is not allowed."
        )


def monkey_patch(deque):
    """Patch a Deque so that its underling list is of fixed length."""

    buffer = [a for a in dir(deque) if type(getattr(deque, a)) is list]
    if not buffer:
        raise ValueError("Deque has no attribute of type list.")

    for a in buffer:
        setattr(deque, a, StaticList(getattr(deque, a)))


def test_import_deque():
    from adt_examples.deque import Deque


@pytest.mark.parametrize("method", [
    ('append'),
    ('appendleft'),
    ('pop'),
    ('popleft')
])
def test_push_pop_available(method):
    assert hasattr(Deque(5), method), \
        f"Deque has no {method} method"


def test_append_and_pop():
    Q = Deque(1)
    monkey_patch(Q)
    Q.append(1)
    assert Q.pop() == 1, \
        "popped element in deque"


def test_peek():
    Q = Deque(2)
    monkey_patch(Q)
    Q.append(1)
    Q.append(2)
    assert Q.peek() == 2, \
        "expected value of 2"


def test_peekleft():
    Q = Deque(2)
    monkey_patch(Q)
    Q.append(1)
    Q.append(2)
    assert Q.peekleft() == 1, \
        "expected value of 1"


def test_appendleft():
    Q = Deque(3)
    monkey_patch(Q)
    Q.append(2)
    Q.append(4)
    Q.appendleft(0)
    assert Q.peekleft() == 0, \
        "expected value of 0"


def test_popleft():
    Q = Deque(3)
    monkey_patch(Q)
    Q.append(2)
    Q.append(4)
    Q.append(6)
    assert Q.popleft() == 2, \
        "expected value of 2"


@pytest.mark.parametrize("items, length", [
    ([1, 2, 'a', 'abc'], 4),
    ([2], 1),
    ([[1, 2, 3], 1, 2], 3)
])
def test_len(items, length):
    Q = Deque(10)
    monkey_patch(Q)
    for item in items:
        Q.append(item)
    assert len(Q) == length, \
        f"expected a length of {length}"


def test_len_empty():
    Q = Deque(5)
    monkey_patch(Q)
    assert not Q


@pytest.fixture
def base_data():
    Q = Deque(5)
    monkey_patch(Q)
    Q.append(5)
    Q.append(10)
    Q.append(15)
    Q.append(20)
    Q.append(25)
    Q.popleft()
    Q.popleft()
    Q.append(35)
    Q.append(40)

    T = Deque(4)
    monkey_patch(T)
    T.append('n')
    T.append('n+1')
    T.appendleft('n+2')
    T.appendleft('n+3')
    T.pop()
    T.append('n+4')
    return Q, T


def test_len_full(base_data):
    Q, _ = base_data
    assert len(Q) == 5


@pytest.mark.parametrize("idx, iterated", [
    (0, [15, 20, 25, 35, 40]),
    (1, ['n+3', 'n+2', 'n', 'n+4'])
])
def test_pointers(idx, iterated, base_data):
    Q = base_data[idx]
    assert np.array_equal([q for q in Q], iterated)


@pytest.mark.parametrize("idx, iterated", [
    (0, [15, 20, 25, 35, 40]),
    (1, ['n+3', 'n+2', 'n', 'n+4'])
])
def test_double_iterate(idx, iterated, base_data):
    Q = base_data[idx]
    assert np.array_equal([(q, r) for q in Q for r in Q],
                          [(q, r) for q in iterated for r in iterated])


def test_mem_leakage():
    Q = Deque(2)
    monkey_patch(Q)
    Q.append(1)
    A = object()
    ref = []
    ref.append(sys.getrefcount(A))
    Q.append(A)
    ref.append(sys.getrefcount(A))
    Q.pop()
    ref.append(sys.getrefcount(A))
    assert np.array_equal(ref, [2, 3, 2]), \
        "expected pop to overwrite place in memory"
