from aifc import Error
from pymysql import NULL
import requests
from bs4 import BeautifulSoup
import mysql.connector
import html


class haici:
    '''单词接口，先从数据库查询，不存在则访问海词api'''
    def __init__(self):
        print('Initialze database')
        self.cnx = mysql.connector.connect(user='',
                                           password='',
                                           host='',
                                           database='')

    def select_word(self, word):
        cursor = self.cnx.cursor()
        query = ('SELECT paraphase From haici WHERE word="{}"'.format(word))
        cursor.execute(query)
        d = cursor.fetchall()
        cursor.close()
        return d

    def insert_word(self, word, paraphase):
        cursor = self.cnx.cursor()
        query = (
            'INSERT INTO haici (word, paraphase) VALUES ("{}", "{}")'.format(
                word, html.escape(paraphase)))
        cursor.execute(query)
        self.cnx.commit()
        cursor.close()

    def __del__(self):
        print('Database disconnected.')
        self.cnx.close()

    def search_word(self, word):
        db_reply = self.select_word(word)
        if len(db_reply) == 0:
            print('"' + word + '"', 'From haici API')
            h = requests.get('http://apii.dict.cn/mini.php?q=' + word)
            soup = BeautifulSoup(h.text, 'html.parser')
            content = soup.body
            #print(content.text)
            if ']' not in content.text:
                raise ValueError(
                    'Word "{}" can\'t not be found. Are you mean "{}"?'.format(
                        word,
                        ', '.join([i.text
                                   for i in content.find_all('a')[:10]])))
            else:
                paraphase = '<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta name="viewport" content="width=320,initial-scale=1.3,maximum-scale=3.0,user-scalable=1"></head>' + content.__str__(
                ).replace('Define ', '').replace(
                    '<br/><div align="center"><a href="http://dict.cn/' +
                    word +
                    '" target="_blank"><font color="gray">查看详细解释</font></a></div>',
                    '') + '</html>'
                self.insert_word(word, paraphase.replace('\n', ''))
                return paraphase.replace('\n', '')
        else:
            print('"' + word + '"', 'From Database')
            return html.unescape(db_reply[0][0])


if __name__ == "__main__":
    search = haici()
    search.search_word("one's")
    search.search_word('ban')
    search.search_word('apple')
