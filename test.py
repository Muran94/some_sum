import unittest
import main

class SomeSumMethodsTests(unittest.TestCase):
    def test_sum_1(self):
        self.assertEqual(main.sum_1(10), 55)
        self.assertEqual(main.sum_1(15), 120)

    def test_sum_2(self):
        self.assertEqual(main.sum_2(10), 55)
        self.assertEqual(main.sum_2(15), 120)

    def test_sum_3(self):
        # 正常系
        ### 引数をひとつ指定
        self.assertEqual(main.sum_3(10), 55)
        self.assertEqual(main.sum_3(15), 120)

        ### 引数をふたつ指定
        self.assertEqual(main.sum_3(10, 3), 52) # 3 ~ 10 までの総和
        self.assertEqual(main.sum_3(15, 3), 117) # 3 ~ 15 までの総和

        # 異常系
        ### 引数の取るべき値がおかしい場合
        self.assertEqual(main.sum_3(1, 10), "引数の値がおかしい")
        self.assertEqual(main.sum_3(10, 10), "引数の値がおかしい")

    def test_sum_4(self):
        self.assertEqual(main.sum_4(10), 55)
        self.assertEqual(main.sum_4(15), 120)

if __name__ == "__main__":
    unittest.main()
