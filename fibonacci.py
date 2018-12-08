class Sqrt5Integer:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Sqrt5Integer(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Sqrt5Integer(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Sqrt5Integer(self.a * other.a + 5 * self.b * other.b,
                            self.a * other.b + self.b * other.a)

    def __iadd__(self, other):
        self.a += other.a
        self.b += other.b
        return self

    def __isub__(self, other):
        self.a -= other.a
        self.b -= other.b
        return self

    def __imul__(self, other):
        (self.a, self.b) = (self.a * other.a + self.b * other.b,
                            self.a * other.b + self.b * other.a)
        return self


def pow_fast(val: Sqrt5Integer, n: int):
    result = Sqrt5Integer(1, 0)
    bin_exp = val
    while n > 0:
        if n & 1 != 0:
            result = result * bin_exp
        bin_exp = bin_exp * bin_exp
        n >>= 1
    return result


def fibonacci(n: int):
    return (pow_fast(Sqrt5Integer(1, 1), n) - pow_fast(Sqrt5Integer(1, -1), n)).b // 2**n


def rabbit_num(n: int):
    return (fibonacci(n) + fibonacci(n + 1)) * 2


def bin_search(target_num: int):
    ng = 0
    ok = 100000
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if rabbit_num(mid) >= target_num:
            ok = mid
        else:
            ng = mid
    return ok


def output_result(target_num: int):
    term = bin_search(target_num)
    num = rabbit_num(term)
    print("{}ヶ月必要で、{}羽のうさぎに囲まれます！\n".format(term, num))
    print("== 周辺での結果 ===")
    for i in range(max(0, term - 3), term + 4):
        num = rabbit_num(i)
        print("{}ヶ月で{}羽".format(i, num))


if __name__ == '__main__':
    num = int(input('何羽のうさぎに囲まれたいですか: '))
    output_result(num)
