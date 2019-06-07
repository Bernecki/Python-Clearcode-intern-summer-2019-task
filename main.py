__author__ = "Paweł Bernecki"

import unittest


def calculate(usb_size, memes):
    names, sizes, prices = list(zip(*memes))
    quantity = len(sizes)
    usb_size_mib = usb_size * 1024
    price_table = fill_price_table(usb_size_mib, sizes, prices, quantity)
    selected_memes = find_items_in_best_solution(usb_size_mib, names, sizes, prices, quantity, price_table)
    return price_table[-1][-1], selected_memes


def fill_price_table(usb_size_mib, sizes, prices, quantity):
    price_table = [[0 for _ in range(usb_size_mib + 1)] for _ in range(quantity + 1)]
    for i in range(1, quantity + 1):
        for j in range(1, usb_size_mib + 1):
            if j < sizes[i - 1]:
                price_table[i][j] = price_table[i - 1][j]
            else:
                price_table[i][j] = max(price_table[i - 1][j], prices[i - 1] + price_table[i - 1][j - sizes[i - 1]])
    return price_table


def find_items_in_best_solution(usb_size_mib, names, sizes, prices, quantity, price_table):
    selected_memes = set()
    price = price_table[-1][-1]
    while price > 0:
        quantity -= 1
        if price_table[quantity + 1][usb_size_mib] != price_table[quantity][usb_size_mib]:
            selected_memes.add(names[quantity])
            price -= prices[quantity]
            usb_size_mib -= sizes[quantity]
    return selected_memes


class TestStringMethods(unittest.TestCase):

    def test_basic_testcase(self):
        usb_size = 1
        memes = [('rollsafe.jpg', 205, 6), ('sad_pepe_compilation.gif', 410, 10), ('yodeling_kid.avi', 605, 12)]
        self.assertEqual(calculate(usb_size, memes), (22, {'yodeling_kid.avi', 'sad_pepe_compilation.gif'}))

    def test_increased_usb_size(self):
        usb_size = 10
        memes = [('rollsafe.jpg', 205, 6), ('sad_pepe_compilation.gif', 410, 10), ('yodeling_kid.avi', 605, 12)]
        self.assertEqual(calculate(usb_size, memes),
                         (28, {'yodeling_kid.avi', 'sad_pepe_compilation.gif', 'rollsafe.jpg'}))

    def test_increased_meme_sizes(self):
        usb_size = 1
        memes = [('rollsafe.jpg', 410, 6), ('sad_pepe_compilation.gif', 820, 10), ('yodeling_kid.avi', 1210, 12)]
        self.assertEqual(calculate(usb_size, memes), (10, {'sad_pepe_compilation.gif'}))

    def test_same_price_size_ratio_memes(self):
        usb_size = 1
        memes = [('lol.jpg', 205, 1), ('lel.jpg', 205, 1), ('lul.jpg', 205, 1), ('lyl.jpg', 205, 1), ('xd.jpg', 205, 1)]
        self.assertEqual(calculate(usb_size, memes), (4, {'lyl.jpg', 'lul.jpg', 'lel.jpg', 'lol.jpg'}))

    def test_max_size_meme(self):
        usb_size = 1
        memes = [('lol.jpg', 1024, 1)]
        self.assertEqual(calculate(usb_size, memes), (1, {'lol.jpg'}))


if __name__ == '__main__':
    unittest.main()
