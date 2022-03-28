
import os
zip = []
pwd = []
with open(r'C:\资料库\代码片段\ankidroid词卡制作\新东方词书\词书压缩包\爆破结果.txt', 'r', encoding='utf16') as result:
    for row in result:
        if 'zip' in row:
            zip.append(row.split('\\')[-1].replace('\n', ''))
        if '此文件的密码: ' in row:
            pwd.append(row[-6:-1])
for i in range(len(zip)):
   
    
    zipFile = r'"C:\资料库\代码片段\ankidroid词卡制作\新东方词书\词书压缩包\\'+zip[i]+'"'
    path = r'C:\资料库\代码片段\ankidroid词卡制作\新东方词书\词书压缩包\temp\\'
    path2 = r'C:\资料库\代码片段\ankidroid词卡制作\新东方词书\词书数据库\\'
    os.system('bz x -o:' + path + ' -p:' + pwd[i] + ' '+ zipFile)
    os.rename(path + os.listdir(path)[0], path2 + zip[i].replace('.zip', '.db'))