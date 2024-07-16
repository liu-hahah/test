# -*-coding:utf-8 -*-
# @Time     :2024/7/16 14:29
# @Author   :LIU
# @File     :test_add.py
# @Software :PyCharm

import logging
import allure

logger = logging.getLogger('test')
logger.setLevel('INFO')

handler = logging.StreamHandler()
handler.setLevel("INFO")

logger.addHandler(handler)
fmt = logging.Formatter("%(asctime)s  %(message)s")
handler.setFormatter(fmt)


def test_add():
    a = 10
    b = 20
    print('a + b = {}'.format(a+b))
    logger.info('a + b = {}'.format(a+b))
    allure.step('加法')


def test_plus():
    a = 10
    b = 20
    print('a == b = {}'.format(a==b))
    logger.info('a == b = {}'.format(a==b))
    allure.step('plus法2222')
    assert a == b


