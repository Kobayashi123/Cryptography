
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Rsaプログラム：公開鍵暗号アルゴリズムであるRSAを実装するプログラムです。
"""

__author__ = 'Kobayashi Shun'
__version__ = '0.0.0'
__date__ = '2022/11/14 (Created: 2022/11/14)'

from math import gcd

class Rsa:
    """
    Rsaクラス：RSAを実装するクラスです。
    """
    def __init__(self, p, q):
        """
        コンストラクタ
        """
        self.p = p
        self.q = q
        self.n = p * q
        self.l = self.lcm(self.p - 1, self.q - 1)
        self.enc_key = 0
        self.dep_key = 0

    def generate_key(self):
        """
        RSAの鍵ペアを生成する関数です。
        """
        self.generate_enc_key()
        self.generate_dec_key()

    def lcm(self, a, b):
        """
        最小公倍数を求める関数です。
        """
        return a * b // gcd(a, b)

    def generate_enc_key(self):
        """
        公開鍵を生成する関数です。
        """
        self.enc_key = 2
        for i in range(2, self.l):
            if gcd(i, self.l) == 1:
                self.enc_key = i
                break

    def generate_dec_key(self):
        """
        秘密鍵を生成する関数です。
        """
        self.dec_key = 1
        for i in range(1, self.l):
            if (self.enc_key * i) % self.l == 1:
                self.dec_key = i
                break

    def encrypt(self, message):
        """
        暗号化を行う関数です。
        """
        encode_integer = [ord(char) for char in message]
        # print("encode: ", encode_integer)
        encrypted_integer = [pow(i, self.enc_key, self.n) for i in encode_integer]
        # print("encrypted: ", encrypted_integer)
        return encrypted_integer

    def decrypt(self, encrypted_integer):
        """
        復号を行う関数です。
        """
        decrypted_integer = [pow(i, self.dec_key, self.n) for i in encrypted_integer]
        # print("decrypted: ", decrypted_integer)
        decode_message = [chr(i) for i in decrypted_integer]
        # print("decode: ", decode_message)
        return decode_message

    def get_key(self):
        """
        鍵ペアを取得する関数です。
        """
        return self.enc_key, self.dec_key, self.n

def main():
    """
    Pythonファイルを生成するメイン（main）プログラムです。
    常に0を応答します。それが結果（リターンコード：終了ステータス）になることを想定しています。
    """
    aRsa = Rsa(17, 19)
    aRsa.generate_key()
    e, d, n = aRsa.get_key()
    print("公開鍵：", e, ",  秘密鍵：", d, ",  N：", n)
    plain = "Hello World"
    print("Plain: ", plain)
    cypher = aRsa.encrypt(plain)
    print("Encode: ", ''.join(map(str, cypher)))
    plain = aRsa.decrypt(cypher)
    print("Recode: ", ''.join(plain))


if __name__ == '__main__':  # このスクリプトファイルが直接実行されたときだけ、以下の部分を実行する。
    import sys
    sys.exit(main())
