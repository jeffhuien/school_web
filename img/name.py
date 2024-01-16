# -*- coding: utf-8 -*-
# Author: GAO GAO
# Date: 2023-11-21 23:43:02
import os

ls = os.listdir()
for i in ls:
    if i.endswith((".py", ".js")):
        ls.remove(i)

with open("index.js", "w") as f:
    f.write(f"export default {ls}")
