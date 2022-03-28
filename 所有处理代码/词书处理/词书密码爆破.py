from distutils.util import execute
import os
import subprocess
import time
for i in os.listdir(r'C:\资料库\代码片段\ankidroid词卡制作\新东方词书\词书压缩包'):
    if 'zip' in i:
        print(i)
        exec = r'"C:\Program Files (x86)\Advanced Archive Password Recovery\archpr.exe"'
        para = '"/c:d /min:5 /smartexit:1.txt ' + 'C:\资料库\代码片段\\ankidroid词卡制作\新东方词书\词书压缩包\\' + i + '"'
        print('[System.Diagnostics.Process]::Start(' + exec + ',' + para + ')')
        subprocess.call([
            "powershell.exe",
            '[System.Diagnostics.Process]::Start(' + exec + ',' + para + ')'
        ])
        time.sleep(0.5)
