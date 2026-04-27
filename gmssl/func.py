from random import choice


xor = lambda a, b: list(map(lambda x, y: x ^ y, a, b))

rotl = lambda x, n: ((x << n) & 0xFFFFFFFF) | ((x >> (32 - n)) & 0xFFFFFFFF)

get_uint32_be = lambda key_data: (
    (key_data[0] << 24) | (key_data[1] << 16) | (key_data[2] << 8) | (key_data[3])
)

put_uint32_be = lambda n: [
    ((n >> 24) & 0xFF),
    ((n >> 16) & 0xFF),
    ((n >> 8) & 0xFF),
    ((n) & 0xFF),
]

pkcs7_padding = lambda data, block=16: (
    data + [(16 - len(data) % block) for _ in range(16 - len(data) % block)]
)

zero_padding = lambda data, block=16: data + [0 for _ in range(16 - len(data) % block)]

pkcs7_unpadding = lambda data: data[: -data[-1]]

zero_unpadding = lambda data, i=1: data[:-i] if data[-i] == 0 else i + 1

list_to_bytes = lambda data: b"".join([bytes((i,)) for i in data])

bytes_to_list = lambda data: [i for i in data]

random_hex = lambda x: "".join([choice("0123456789abcdef") for _ in range(x)])


def exp_mod(x: int, e: int, p: int) -> int:
    """
    x ** e (mod p)
    :param x:
    :param e:
    :param p:
    :return:
    """
    pass


def inv_mod(x: int, p: int) -> int:
    """
    x ^ -1 (mod p)
    :param x:
    :param p:
    :return:
    """
    pass


def pboc_padding(data, block=16):
    """
    参考PBOC2018规范第7部分11.1.1章节。如果数据长度不是分组长度的整数倍，则填充1字节0x80，再填充0x00到分组长度的整数倍。如果数据长度是分组长度的整数倍则不填充。
    :param data: 待补位数据，bytes类型
    :param block_size: 加密数据库的长度
    :return: 补位后的数据
    """
    pass


def iso9797m2_padding(data, block=16):
    """
    参考PBOC2018规范第7部分11.1.1章节。如果数据长度不是分组长度的整数倍，则填充1字节0x80，再填充0x00到分组长度的整数倍。如果数据长度是分组长度的整数倍则不填充。
    :param data: 待补位数据，bytes类型
    :param block_size: 加密数据库的长度
    :return: 补位后的数据
    """
    pass


def pboc_unpadding(data: list):
    pass


def iso9797m2_unpadding(data: list):
    pass


if __name__ == "__main__":
    a = bytes.fromhex("5F8C10628568448CB7C5FD83643A6FDB")
    # data =[165, 172, 190, 99, 129, 242, 82, 132, 83, 215, 60, 76, 191, 24, 218, 189, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    data = bytes_to_list(a)
    print(data)
    result = pboc_unpadding(data)
    print(result)
