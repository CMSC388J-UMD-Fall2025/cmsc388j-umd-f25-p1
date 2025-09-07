from src.practice import *

import pytest

import random
import collections
import operator

def test_hello_world():
    assert 'Hello, World!' == hello_world()


def test_empty_sum_unique():
    l = []
    assert 0 == sum_unique(l)


def test_sum_unique():
    copies = random.randint(2, 10)

    assert 9 == sum_unique(([5] * copies) + [4])

    copies = random.randint(2, 10)
    l1 = [1, 2, 4, 5] * copies
    random.shuffle(l1)

    assert 12 == sum_unique(l1)

    copies = random.randint(2, 10)

    assert 4 == sum_unique([4] * copies)


def test_single_element_palindrome():
    assert palindrome('')
    assert palindrome('f')
    assert palindrome('7')


def test_longer_palindromes():
    assert palindrome('aa')
    assert palindrome(33)
    assert not palindrome('ab')
    assert not palindrome(48)


def test_even_longer_palindromes():
    assert palindrome('racecar')
    assert palindrome(1337331)
    assert not palindrome('python')
    assert not palindrome(1234567)


def test_small_sum_multiples():
    assert 0 == sum_multiples(2)
    assert 2 == sum_multiples(3)

    assert 6 == sum_multiples(5)
    assert 6 == sum_multiples(6)
    assert 12 == sum_multiples(7)


def test_large_sum_multiples():
    assert 63 == sum_multiples(16)
    assert 184 == sum_multiples(25)
    assert 434280 == sum_multiples(1234)

def test_valid_twosum():
    assert [0, 1] == two_sum([2, 7, 11, 15], 9)
    assert [1, 2] == two_sum([3, 2, 4], 6)
    assert [0, 1] == two_sum([3, 3], 6)

def test_invalid_twosum():
    assert -1 == two_sum([1, 2, 3], 7)

def test_empty_lists_num_func_mapper():
    nums = []
    funs = [sum_unique, sum]
    assert [0, 0] == num_func_mapper(nums, funs)

    nums = [2, 2, 2, 4, 5]
    funs = []
    assert [] == num_func_mapper(nums, funs)


def test_num_func_mapper_1():
    nums = [2, 2, 2, 4, 5]
    funs = [sum_unique, sum]
    assert [11, 15] == num_func_mapper(nums, funs)


def test_num_func_mapper_2():
    def most_occurring(nums):
        c = collections.Counter(nums)
        # Returns key in dict with highest value
        return max(c.items(), key=operator.itemgetter(1))[0]

    nums = [2, 2, 2, 4, 5, 8, 9]
    funs = [sum, max, most_occurring]
    assert [32, 9, 2] == num_func_mapper(nums, funs)

def test_height_sort():
    names3 = ["David", "Eva", "Frank"]
    heights3 = [175, 160, 185]
    result3 = height_sort(names3, heights3)
    assert result3 == ["Frank", "David", "Eva"], f"Expected ['Frank', 'David', 'Eva'], but got {result3}"

    names4 = ["Sophia", "Liam", "Olivia", "Noah"]
    heights4 = [160, 175, 168, 182]
    result4 = height_sort(names4, heights4)
    assert result4 == ["Noah", "Liam", "Olivia", "Sophia"], f"Expected ['Noah', 'Liam', 'Olivia', 'Sophia'], but got {result4}"
    
def test_custom_sort():
    assert [1, 3, 5, 2, 4] == custom_sort([1, 2, 3, 4, 5])
    assert [5, 5, 5, 4, 4, 4] == custom_sort([4, 5, 4, 5, 5, 4])
    
