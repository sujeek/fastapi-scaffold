# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/24 15:18
@Auth ： yongjie.su
@File ：redis_module.py
@IDE ：PyCharm
@Motto：Design Review Coding Test

"""
import sys
import time

import redis
from redis.client import PubSub
from redisbloom.client import Client

from app.utils.singleton_helper import Singleton
from app.config import config


@Singleton
class RedisModule:
    def __init__(self, **kwargs):
        self._db_args = {
            'host': kwargs.get('host', '127.0.0.1'),
            'username': kwargs.get('username'),
            'password': kwargs.get('password'),
            'db': kwargs.get('db', 0),
            'port': kwargs.get('port', 6379),
            'max_connections': kwargs.get('max_connections', 20)
        }
        self.pool = redis.ConnectionPool(**self._db_args)
        # self.pool = redis.ConnectionPool(host='127.0.0.1', port=6379, max_connections=10)
        self.redis_client = redis.Redis(connection_pool=self.pool)
        # pub-sub
        self.pub_sub = PubSub(self.pool)
        # BloomFilter
        self.bf = Client()

    def get_pipe(self):
        # pipe.execute()
        return self.redis_client.pipeline(transaction=True)

    #################### string
    def set_key(self, k, v):
        return self.redis_client.set(k, v)

    def set_ex_key(self, k, time, v):
        self.redis_client.setex(k, time, v)

    def set_nx_key(self, k, v):
        self.redis_client.setnx(k, v)

    def mset_key(self, mapping):
        self.redis_client.mset(mapping)

    def mset_nx_key(self, mapping):
        self.redis_client.msetnx(mapping)

    def get_key(self, k):
        return self.redis_client.get(k)

    def mget_key(self, keys, *args):
        return self.redis_client.mget(keys, *args)

    def delete(self, k):
        return self.redis_client.delete(k)

    def incr(self, k):
        return self.redis_client.incr(k)

    def incr_by(self, k, amount):
        return self.redis_client.incrby(k, amount)

    def decr(self, k):
        return self.redis_client.decr(k)

    def decr_by(self, k, amount):
        return self.redis_client.decrby(k, amount)

    #################### List
    def lset(self, name, index, value):
        return self.redis_client.lset(name, index, value)

    def lpush(self, name, values):
        return self.redis_client.lpush(name, values)

    def lpop(self, name):
        return self.redis_client.lpop(name)

    def rpush(self, name, values):
        return self.redis_client.rpush(name, values)

    def rpop(self, name):
        return self.redis_client.rpop(name)

    #################### hash
    def hset(self, name, k, v):
        return self.redis_client.hset(name, k, v)

    def hmset(self, name, mapping):
        return self.redis_client.hmget(name, mapping)

    def hkeys(self, name):
        return self.redis_client.hkeys(name)

    def hvals(self, name):
        return self.redis_client.hvals(name)

    def hget(self, name, k):
        return self.redis_client.hget(name, k)

    def hmget(self, name, keys, *args):
        return self.redis_client.hmget(name, keys, *args)

    ####################### set
    def sadd(self, name, values):
        return self.redis_client.sadd(name, values)

    def spop(self, name, count):
        return self.redis_client.spop(name, count)

    ####################### Sorted Set
    def zadd(self, name, mapping, nx=False, xx=False, ch=False, incr=False):
        return self.redis_client.zadd(name, mapping, nx=nx, xx=xx, ch=ch, incr=incr)

    def zscore(self, name, value):
        return self.redis_client.zscore(name, value)

    def zincrby(self, name, amount, value):
        return self.redis_client.zincrby(name, amount, value)

    def zcard(self, name):
        return self.redis_client.zcard(name)

    def zcount(self, name, min, max):
        return self.redis_client.zcount(name, min, max)

    def zrange(self, name, start, end, desc=False, withscores=False, score_cast_func=float):
        return self.redis_client.zrange(name, start, end, desc, withscores, score_cast_func)

    def zrevrange(self, name, start, end, withscores=False, score_cast_func=float):
        return self.redis_client.zrevrange(name, start, end, withscores, score_cast_func)

    def zrank(self, name, value):
        return self.redis_client.zrank(name, value)

    def zrem(self, name, value):
        return self.redis_client.zrem(name, value)

    def zlexcount(self, name, min, max):
        return self.redis_client.zlexcount(name, min, max)

    def zscan(self, name, cursor=0, match=None, count=None, score_cast_func=float):
        return self.redis_client.zscan(name, cursor, match, count, score_cast_func)

    #################### 自动过期, 使用事务, Redis 2.6 版本中，延迟被降低到 1 毫秒之内。

    #################### 自动过期, 使用事务, Redis 2.6 版本中，延迟被降低到 1 毫秒之内。
    def expire(self, name, time):
        """
        set ex time 使用事务
        :param name:
        :param time: 单位：秒
        :return:
        """
        return self.redis_client.expire(name, time)

    def expireat(self, name, when):
        """
        设置 key 的过期 unix 时间戳
        :param name:
        :param when:
        :return:
        """
        return self.redis_client.expireat(name, when)

    def ttl(self, name):
        """
        以秒为单位，返回给定 key 的剩余生存时间
        当 key 不存在时，返回 -2 。 当 key 存在但没有设置剩余生存时间时，返回 -1 。 否则，以秒为单位，返回 key 的剩余生存时间。
        :param name:
        :return:
        """
        return self.redis_client.ttl(name)

    def pttl(self, name):
        return self.redis_client.pttl(name)

    def persist(self, name):
        """
        移除给定 key 的生存时间.
        当生存时间移除成功时，返回 1 . 如果 key 不存在或 key 没有设置生存时间，返回 0 。
        :param name:
        :return:
        """
        return self.redis_client.persist(name)

    def pexpire(self, name, time):
        """
        以毫秒为单位设置 key 的生存时间
        :param name:
        :param time:
        :return:
        """
        return self.redis_client.pexpire(name, time)

    def pexpireat(self, name, when):
        return self.redis_client.pexpireat(name, when)

    #################### 事务
    # mulit exec  标记一个事务块的开始。
    # 事务块内的多条命令会按照先后顺序被放进一个队列当中，最后由 EXEC 命令原子性(atomic)地执行。

    # 持久化

    # 发布与订阅
    def publish(self, channel, msg):
        return self.redis_client.publish(channel, msg)

    # 订阅
    def subscribe(self, channel):
        return self.pub_sub.subscribe(channel)

    # Bitmap
    # Bitmap和布隆过滤器存储的都是二进制（0和1），目的都是为了节省内存、提高插入和查询效率。但是不同的是，Bitmap存储的数据只能是状态值0和1，
    # 所以适合于二值状态的业务场景。而布隆过滤器可以存储任何数据，只不过这些数据是经过hash转换成位数组的下标，然后把对应下标的元素置为1。
    # 除了存储存储真实数据的不同，Bitmap和布隆过滤器还有如下区别。
    # 在一般情况下，处理海量数据时，布隆过滤器比Bitmap用到的内存更少，插入、查询效率更高。
    def set_bit(self, name, offset, value):
        return self.redis_client.setbit(name, offset, value)

    def get_bit(self, name, offset):
        return self.redis_client.getbit(name, offset)

    def bit_count(self, key, start, end):
        return self.redis_client.bitcount(key, start, end)

    # Bloom Filter
    def bf_create(self, key, errorRate, capacity):
        return self.bf.bfCreate(key, errorRate, capacity)

    def bf_add(self, key, item):
        return self.bf.bfAdd(key, item)

    def bf_madd(self, key, items):
        return self.bf.bfMAdd(key, items)

    def bf_exists(self, key, item):
        return self.bf.bfExists(key, item)

    def bf_mexists(self, key, items):
        return self.bf.bfMExists(key, items)


redis_client = RedisModule(**config['redis'])

if __name__ == '__main__':
    # value = "abcdefgabcdefg".join([str(x) for x in range(10000000)])
    # print(sys.getsizeof(value))
    # mapping = {"k": 1, "k1": 2}
    # redis_client.mset_key(mapping)
    # time.sleep(10)
    # redis_client.delete('k1')
    key = 'test'
    try:
        redis_client.bf_create(key, 0.001, 1000)
    except:
        print(f'{key} is exist.')
    for i in range(10):
        redis_client.bf_add(key, i)
    print(redis_client.bf_exists(key, 3))
