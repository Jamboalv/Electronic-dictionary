#!/usr/bin/python
# -*- coding: UTF-8 -*-


import urllib2
import hashlib
import json
import random


# 调用百度翻译API进行翻译
class Translation:
    def __init__(self):
        self._from = 'auto'                         # 翻译源语言
        self._to = 'zh'                             # 译文语言
        self._appid = 20170311000042076             # 开发账号APP ID
        self._key = 'eokFItPTsMta5AcVZtdw'          # 密钥
        self._salt = random.randint(10001, 99999)   # 随机数
        self._sign = ''                             # 签名
        self._dst = ''                              # 原文
        self._enable = True                         # 译文

    # 调用API接口
    # 拼接字符串，计算签名sign(md5加密)
    # 形成URL
    # 访问请求
    # 返回结果
    def StartTrans(self, text):
        text.encode('utf8')
        m = str(self._appid) + text + str(self._salt) + self._key
        m_MD5 = hashlib.md5(m)
        self._sign = m_MD5.hexdigest()

        Url_1 = 'http://api.fanyi.baidu.com/api/trans/vip/translate?'
        Url_2 = 'q=' + text + '&from=' + self._from + '&to=' + self._to + '&appid=' + str(
            self._appid) + '&salt=' + str(self._salt) + '&sign=' + self._sign
        Url = Url_1 + Url_2
        PostUrl = Url.decode()

        TransRequest = urllib2.Request(PostUrl)
        TransResponse = urllib2.urlopen(TransRequest)
        TransResult = TransResponse.read()
        data = json.loads(TransResult)
        if 'error_code' in data:
            print 'Crash'
            print 'error:', data['error_code']
            return data['error_msg']
        else:
            self._dst = data['trans_result'][0]['dst']
            return self._dst

