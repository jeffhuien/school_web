# -*- coding: utf-8 -*-
# Author: GAO GAO
# Date: 2023-11-21 23:19:26

import requests as r

ip = "https://gdzyjsxy.hist.edu.cn/"

ls = [
    "20230601153903.jpg",
    "20230601153539.jpg",
    "20230508114718.jpg",
    "20230508110655.jpg",
    "20230508114551.jpg",
    "20230506091308.jpg",
    "20230506091342.jpg",
    "20230506091312.jpg",
    "20230505164512.jpg",
    "IMG_20230505_123425.jpg",
    "20230413091552.jpg",
    "images20230411104221.jpg",
    "20230411104448.jpg",
    "20230411104204.jpg",
    "IMG_20230330_110834.jpg",
    "images20230329090845.jpg",
    "images20230329091322.jpg",
    "images20230329090757.jpg",
    "20220503170212.jpg",
    "IMG_20220506_074327.jpg",
    "IMG_20211109_082018.jpg",
    "IMG_20210930_144958.jpg",
    "2021051901.jpg",
    "2021051203.jpg",
    "2021051201.jpg",
    "20210510.jpg",
    "20220406150157.jpg",
    "1.2.jpg",
    "1.1.jpg",
]


header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62",
}


def download(filepath, filename):
    # print("下载中:" + filename)
    req = r.get(filepath, stream=True, headers=header)
    with open(filename, "wb") as f:
        f.write(req.content)
        f.flush()
    # print(filename + "->done", prox)
    print("done")


for i in ls:
    download(ip + i, i)
