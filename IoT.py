# -*- Coding: utf-8 -*-

import os
import subprocess
import datetime
from time import sleep

def main():
    dt_now = datetime.datetime.now()
    print(dt_now.strftime('%Y/%m/%d %H:%M:%S') + "10秒更新中...")
    print(os.environ.get('LANG'))
    #print(os.environ.get('RemoteENV'))


if __name__ == '__main__':
    while True:
        main()
        sleep(10)
