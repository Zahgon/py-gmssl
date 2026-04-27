import binascii
from random import choice
from . import sm3, func
from Cryptodome.Util.asn1 import DerSequence, DerInteger
from binascii import unhexlify
# 选择素域，设置椭圆曲线参数

default_ecc_table = {
    'n': 'FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123',
    'p': 'FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFF',
    'g': '32c4ae2c1f1981195f9904466a39c9948fe30bbff2660be1715a4589334c74c7'
         'bc3736a2f4f6779c59bdcee36b692153d0a9877cc62a474002df32e52139f0a0',
    'a': 'FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFC',
    'b': '28E9FA9E9D9F5E344D5A9E4BCF6509A7F39789F515AB8F92DDBCBD414D940E93',
}


class CryptSM2(object):

    def __init__(self, private_key, public_key, ecc_table=default_ecc_table, mode=0, asn1=False):
        """
        mode: 0-C1C2C3, 1-C1C3C2 (default is 1)
        """
        self.private_key = private_key
        self.public_key = public_key[2:] if (public_key.startswith("04") and len(public_key)==130) else public_key
        self.para_len = len(ecc_table['n'])
        self.ecc_a3 = (
            int(ecc_table['a'], base=16) + 3) % int(ecc_table['p'], base=16)
        self.ecc_table = ecc_table
        assert mode in (0, 1), 'mode must be one of (0, 1)'
        self.mode = mode
        self.asn1 = asn1

    def _point_on_curve(self, point):
        pass

    def _kg(self, k, Point):  # kP运算
        pass

    def _double_point(self, Point):  # 倍点
        pass

    def _add_point(self, P1, P2):  # 点加函数，P2点为仿射坐标即z=1，P1为Jacobian加重射影坐标
        pass

    def _convert_jacb_to_nor(self, Point):  # Jacobian加重射影坐标转换成仿射坐标
        pass

    def verify(self, Sign, data):
        # 验签函数，sign签名r||s，E消息hash，public_key公钥
        pass

    def sign(self, data, K):
        """
        签名函数, data消息的hash，private_key私钥，K随机数，均为16进制字符串
        :param self: 
        :param data: data消息的hash
        :param K: K随机数
        :return: 
        """
        pass

    def encrypt(self, data):
        # 加密函数，data消息(bytes)
        pass

    def decrypt(self, data):
        # 解密函数，data密文（bytes）
        pass

    def _sm3_z(self, data):
        """
        SM3WITHSM2 签名规则:  SM2.sign(SM3(Z+MSG)，PrivateKey)
        其中: z = Hash256(Len(ID) + ID + a + b + xG + yG + xA + yA)
        """
        pass

    def sign_with_sm3(self, data, random_hex_str=None):
        pass

    def verify_with_sm3(self, sign, data):
        pass

    def recover_public_keys(self, sign: str, data: bytes, v: int = None):
        """
        根据签名和被签数据的hash，还原签名者的公钥
        Thanks to https://github.com/kypomon/public-key-recovery-of-sm2/blob/4a934d055e15f58925e862dee352c93c1684e16a/sm2.py#L198
        :param sign: 签名结果
        :param data: 被签数据(的hash)
        :param v: V in (R, S, V)
        :return: Set[签名者公钥]，长度为2(或4?)
        """
        pass
