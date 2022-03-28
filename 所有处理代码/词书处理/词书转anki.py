import sys
sys.path.append("..")
from haici import haici
import sqlite3
import os
search = haici()
def anki(db):
    print(db)
    # 构建词书单词映射
    word_list = {}
    conn = sqlite3.connect(db)
    c = conn.cursor()
    cursor = c.execute("SELECT * FROM word;")
    for row in cursor:
        word_list[row[0]] = row[1]
    # 构建单词列表
    words = []
    c = conn.cursor()
    try:
        try:
            cursor = c.execute("SELECT * FROM vocabulary_unit_mapping;")
            for row in cursor:
                words.append(word_list[row[1]])
        except:
            cursor = c.execute("SELECT * FROM vocabulary_word_briefdef_mapping;")
            for row in cursor:
                words.append(word_list[row[2]])
    except KeyError:
        print('词书映射找不到单词')
    conn.close()

    print('找到{}个单词'.format(len(words)))
    err_word = []
    with open(db.replace('.db' , '.txt'), 'w', encoding='utf8') as file:
        for word in words:
            #if len(word.split(' ')) >= 2:
            #    continue
            try:
                p = search.search_word(word)
                file.write(word + '\t' + p + '\n')
            except ValueError:
                err_word.append(word)
            except:
                p = search.search_word(word)
                file.write(word + '\t' + p + '\n')
            continue
    print('找不到 ', err_word)
for i in [ii for ii in os.listdir(r'C:\资料库\代码片段\ankidroid词卡制作\新东方词书\词书数据库') if 'db' in ii]:
    anki(r'C:\资料库\代码片段\ankidroid词卡制作\新东方词书\词书数据库\\' + i)