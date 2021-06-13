from hillClimbing import hillClimbing  # 引入解答類別
from solution import Solution
import random


class SolutionVirginia(Solution):
    def neighbor(self):  # 單變數解答的鄰居函數。
        key1 = self.v.copy()
        len = key1.length
        i = random.randrange(0, len)
        key1[i] = random.randint(0, 255)
        return SolutionVirginia(key1)  # 建立新解答並傳回。

    def height(self):               # 能量函數
        key1 = self.v
        # 比對文章，看看出現多少次常用字，這就是分數
        score = fit(key, text)
        return score

    def str(self):  # 將解答轉為字串，以供印出觀察。
        return "key={} score={}".format(self.v, self.height())

    def fit(key, text):
        text = text.lower()
        score = 0
        for i in range(len(text)):
            if text[i].isalpha():
                score += 0.05
            if i > 0 and text[i-1].isalpha():
                continue
            head = text[i:i+5]
            for word in commons:
                if head.startswith(word) and not head[len(word)].isalpha():
                    score += 1
                    break
        return score

    def encrypt(text, key):
        list = []
        klen = len(key)
        for i in range(len(text)):
            ki = i % klen
            n1 = (ord(text[i])+key[ki]) % 128
            list.append(chr(n1))
        return ''.join(list)

    def neg(key):
        nkey = [0]*len(key)
        for i in range(len(key)):
            nkey[i] = -key[i]
        return nkey

    def decrypt(text, key):
        return encrypt(text, neg(key))
