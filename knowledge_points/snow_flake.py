# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/23 16:52
@Auth ： yongjie.su
@File ：snow_flake.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

&：按位与：两位都为1,结果为1,否则为0
|：按位或：只要有一位为1，结果就为1
^：按位异或：两对应的二进位相异时，结果为1
~： 按位取反,即把1变为0,把0变为1，相当于（-x-1）
<<：左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。
>>：右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数

"""
import time

# 注 机器ID占位5 这也就意味者十进制下编号不能超过31  将机器ID与机房ID合并，最大三个机房即00 10 20 每个机房的数值 + 1 即是机器ID  备用 30 31
WORKER_ID_BITS = 5
SEQUENCE_BITS = 12

# 最大取值计算
# 异或     -1 << WORKER_ID_BITS   -31
MAX_WORKER_ID = -1 ^ (-1 << WORKER_ID_BITS)

# 移位偏移计算
WORKER_ID_SHIFT = SEQUENCE_BITS
TIMESTAMP_LEFT_SHIFT = SEQUENCE_BITS + WORKER_ID_BITS
# print(WORKER_ID_SHIFT, TIMESTAMP_LEFT_SHIFT)

# 序号循环掩码
SEQUENCE_MASK = -1 ^ (-1 << SEQUENCE_BITS)
# print(SEQUENCE_MASK)

# 起始时间
TWEPOCH = 1655978255933


class SnowFlake:
    """
    64bit 1 41 5-5 12
    """

    def __init__(self, worker_id, sequence=0):
        if worker_id > MAX_WORKER_ID or worker_id < 0:
            raise ValueError("worker_id value 值越界.")
        self.worker_id = worker_id
        self.sequence = sequence
        self.last_timestamp = -1

    def get_timestamp(self):
        return int(time.time() * 1000)

    def wait_next_millis(self, last_timestamp):
        timestamp = self.get_timestamp()
        while timestamp <= last_timestamp:
            timestamp = self.get_timestamp()
        return timestamp

    def get_id(self):
        timestamp = self.get_timestamp()
        if timestamp < self.last_timestamp:
            pass
        if timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & SEQUENCE_MASK
            if self.sequence == 0:
                timestamp = self.wait_next_millis(self.last_timestamp)
        else:
            self.sequence = 0
        self.last_timestamp = timestamp
        new_id = ((timestamp - TWEPOCH) << TIMESTAMP_LEFT_SHIFT) | (self.worker_id << WORKER_ID_SHIFT) | self.sequence
        return new_id


if __name__ == '__main__':
    # 测试效率
    import datetime
    worker = SnowFlake(worker_id=1, sequence=0)
    ids = []
    start = datetime.datetime.now()
    for i in range(100):
        new_id = worker.get_id()
        ids.append(new_id)
    end = datetime.datetime.now()
    spend_time = end - start
    print(spend_time, len(ids), len(set(ids)))
    print(ids)
