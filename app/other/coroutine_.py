#!/usr/bin/python3

import asyncio
import requests

@asyncio.coroutine
def download(url):
    print("%s 下载中" % url)
    yield from asyncio.sleep(1)
    resp = requests.get(url)
    return resp.content, resp.status_code


@asyncio.coroutine
def write_file(filename, content):
    with open(filename, 'wb') as f:
        f.write(content)
    print(filename, " Write OK")


@asyncio.coroutine
def save(url, filename):
    content, code = yield from download(url)
    print(url, code)
    yield from write_file(filename, content)
    print(url, filename, '保存成功！')


if __name__ == '__main__':
    # 获取事件循环器对象
    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.wait([
        save('https://www.dushu.com', 'dushu.html'),
        save('https://www.taobao.com', 'taobao.html'),
        save('https://www.aliyun.com', 'aliyun.html'),
        save('https://www.baidu.com', 'baidu.html'),
    ]))