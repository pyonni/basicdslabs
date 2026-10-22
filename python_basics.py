#только когда сделала, увидела что были заготовки.

def count_vowels(s):
    count = 0
    for letter in s:
        if any(letter.lower() == el for el in "aeiou"):
            count += 1
    return count


def has_unique_characters(s):
    d = {}
    for ch in s:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    for key in d:
        if d[key] == 1:
            return True
    return False


def count_one_bits(num):
    b = bin(num)[2:]
    count = 0
    print(b)
    for el in str(b):
        if el == '1':
            count += 1
    return count


def multiplicative_persistence(num, count=0):
    if num < 10 and count == 0:
        return 0
    multipliers = []
    while num > 0:
        multipliers.append(num % 10)
        num //= 10
    mp = 1
    for el in multipliers:
        mp *= el
    count += 1
    if mp % 10 == mp:
        return count
    else:
        return multiplicative_persistence(mp, count)


def mse(x, y):
    return sum((x[i] - y[i]) ** 2 for i in range(len(x))) / len(x)


def prime_factorization(num):
    if num < 2:
        return f"({num})"
    multipliers = []
    el = 2
    while num != 1:
        if num % el == 0:
            multipliers.append(el)
            num //= el
        else:
            el += 1
    d = {}
    for n in multipliers:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
    result = ""
    for key in d:
        if d[key] != 1:
            result += f"({key}**{d[key]})"
        else:
            result += f"({key})"
    return result


def pyramid(n):
    if n == 0:
        return "It is impossible"
    num = 1
    sum = 0
    while sum < n:
        sum += num ** 2
        num += 1
    if sum == n:
        return num - 1
    else:
        return "It is impossible"


def is_balanced_number(num):
    if num < 100:
        return False
    sNum = str(num)
    length = len(sNum)
    if length % 2 == 0:
        halfLength = length // 2 - 1
    else:
        halfLength = (length - 1) // 2
    left = sNum[:halfLength]
    right = sNum[-halfLength:]
    return (sum((int(n)) for n in left)) == (sum((int(n)) for n in right))

#тесты
#count_vowels

def test_word():
    assert count_vowels("lesson") == 2
def test_uppercase():
    assert count_vowels("AEIOU") == 5
def test_empty_str():
    assert count_vowels("") == 0

#has_u_c
def test_all_unique():
    assert has_unique_characters("pastry") == True
def test_no_unique():
    assert has_unique_characters("aaoo") == False
def test_has_un():
    assert has_unique_characters("lasso") == True


#count_b
def test_count_basic():
    assert count_one_bits(1245) == 7
def test_zero():
    assert count_one_bits(0) == 0


#m p
def test_mp():
    assert multiplicative_persistence(39) == 3
    assert multiplicative_persistence(4) == 0
    assert multiplicative_persistence(999) == 4

#mse
def test_mse():
    assert mse([0, 2], [4, 0]) == 10.0
    assert mse([-1, -2], [1, 2]) == 10.0
    assert mse([10], [20]) == 100.0

#prime_f
def test_prime_f():
    assert prime_factorization(86240) == "(2**5)(5)(7**2)(11)"
    assert prime_factorization(100) == "(2**2)(5**2)"
    assert prime_factorization(0) == "(0)"


#pyramid
def test_pyramid():
    assert pyramid(14) == 3
    assert pyramid(0) == "It is impossible"
    assert pyramid(8) == "It is impossible"

def test_balanced():
    assert is_balanced_number(23014) == True
    assert is_balanced_number(0) == False
    assert is_balanced_number(25) == False
    assert is_balanced_number(121) == True
    assert is_balanced_number(1000) == False