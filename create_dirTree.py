#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys

# #shell input dir path
# print ("脚本名：", argv[0])
# print ("input project path.")
# for i in range(1, len(sys.argv)):
#     print ("参数", i, sys.argv[i])

print ("create dir tree!")

# 将当前目录改为"工程目录"
root_dir = r"E:\Git@OSC\HAC-NT-D31A"
os.chdir(root_dir)

# 创建目录树
os.makedirs(r"source\apps\inc")
os.makedirs(r"source\apps\user")

os.makedirs(r"source\arch\cortex_m3")

os.makedirs(r"source\board\efm32lib\inc")
os.makedirs(r"source\board\efm32lib\src")
os.makedirs(r"source\board\display\led")

os.makedirs(r"source\drivers\iic")
os.makedirs(r"source\drivers\spi")
os.makedirs(r"source\drivers\serial")
os.makedirs(r"source\drivers\dma")
os.makedirs(r"source\drivers\watchdog")
os.makedirs(r"source\drivers\timer")
os.makedirs(r"source\drivers\clock")
os.makedirs(r"source\drivers\flash")
os.makedirs(r"source\drivers\gpio")

os.makedirs(r"source\misc")
os.makedirs(r"source\subsys")
os.makedirs(r"source\shield")
os.makedirs(r"source\tests")



