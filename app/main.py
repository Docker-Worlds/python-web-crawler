import random
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def random_sleep():
    sleep_seconds = random.uniform(1, 5)
    time.sleep(sleep_seconds)

def get_book_url_index():
    bible_columns = ['Book','chapter number','Origin url info', 'Korean url info']
    bible_info_dataFrame = pd.DataFrame(columns=bible_columns)
    
    bible_info_dataFrame.loc[0] = ["Genesis", 50, "1", 'gen']
    bible_info_dataFrame.loc[1] = ["Exodus", 40, "2", 'exo']
    bible_info_dataFrame.loc[2] = ["Leviticus", 27, "3", 'lev']
    bible_info_dataFrame.loc[3] = ["Numbers", 36, "4", 'num']
    bible_info_dataFrame.loc[4] = ["Deuteronomy", 34, "5", 'deu']
    bible_info_dataFrame.loc[5] = ["Joshua", 24, "6", 'jos']
    bible_info_dataFrame.loc[6] = ["Judges", 21, "7", 'jdg']
    bible_info_dataFrame.loc[7] = ["Ruth", 4, "8", 'rut']
    bible_info_dataFrame.loc[8] = ["Samuel1", 31, "9", '1sa']
    bible_info_dataFrame.loc[9] = ["Samuel2", 24, "10", '2sa']
    bible_info_dataFrame.loc[10] = ["Kings1", 22, "11", '1ki']
    bible_info_dataFrame.loc[11] = ["Kings2", 25, "12", '2ki']
    bible_info_dataFrame.loc[12] = ["Chronicles1", 29, "13", '1ch']
    bible_info_dataFrame.loc[13] = ["Chronicles2", 36, "14", '2ch']
    bible_info_dataFrame.loc[14] = ["Ezra", 10, "15", 'ezr']
    bible_info_dataFrame.loc[15] = ["Nehemiah", 13, "16", 'neh']
    bible_info_dataFrame.loc[16] = ["Esther", 10, "17", 'est']
    bible_info_dataFrame.loc[17] = ["Job", 42, "18", 'job']
    bible_info_dataFrame.loc[18] = ["Psalms", 150, "19", 'psa']
    bible_info_dataFrame.loc[19] = ["Proverbs", 31, "20", 'pro']
    bible_info_dataFrame.loc[20] = ["Ecclesiastes", 12, "21", 'ecc']
    bible_info_dataFrame.loc[21] = ["Song", 8, "22", 'sng']
    bible_info_dataFrame.loc[22] = ["Isaiah", 66, "23", 'isa']
    bible_info_dataFrame.loc[23] = ["Jeremiah", 52, "24", 'jer']
    bible_info_dataFrame.loc[24] = ["Lamentations", 5, "25", 'lam']
    bible_info_dataFrame.loc[25] = ["Ezekiel", 48, "26", 'ezk']
    bible_info_dataFrame.loc[26] = ["Daniel", 12, "27", 'dan']
    bible_info_dataFrame.loc[27] = ["Hosea", 14, "28", 'hos']
    bible_info_dataFrame.loc[28] = ["Joel", 3, "29", 'jol']
    bible_info_dataFrame.loc[29] = ["Amos", 9, "30", 'amo']
    bible_info_dataFrame.loc[30] = ["Obadiah", 1, "31", 'oba']
    bible_info_dataFrame.loc[31] = ["Jonah", 4, "32", 'jnh']
    bible_info_dataFrame.loc[32] = ["Micah", 7, "33", 'mic']
    bible_info_dataFrame.loc[33] = ["Nahum", 3, "34", 'nam']
    bible_info_dataFrame.loc[34] = ["Habakkuk", 3, "35", 'hab']
    bible_info_dataFrame.loc[35] = ["Zephaniah", 3, "36", 'zep']
    bible_info_dataFrame.loc[36] = ["Haggai", 2, "37", 'hag']
    bible_info_dataFrame.loc[37] = ["Zechariah", 14, "38", 'zec']
    bible_info_dataFrame.loc[38] = ["Malachi", 4, "39", 'mal']
    
    bible_info_dataFrame.loc[39] = ["Matthew", 28, "50", 'mat']
    bible_info_dataFrame.loc[40] = ["Mark", 16, "51", 'mrk']
    bible_info_dataFrame.loc[41] = ["Luke", 24, "52", 'luk']
    bible_info_dataFrame.loc[42] = ["John", 21, "53", 'jhn']
    bible_info_dataFrame.loc[43] = ["Acts", 28, "54", 'act']
    bible_info_dataFrame.loc[44] = ["Romans", 16, "55", 'rom']
    bible_info_dataFrame.loc[45] = ["Corinthians1", 16, "56", '1co']
    bible_info_dataFrame.loc[46] = ["Corinthians2", 13, "57", '2co']
    bible_info_dataFrame.loc[47] = ["Galatians", 6, "58", 'gal']
    bible_info_dataFrame.loc[48] = ["Ephesians", 6, "59", 'eph']
    bible_info_dataFrame.loc[49] = ["Philippians", 4, "60", 'php']
    bible_info_dataFrame.loc[50] = ["Colossians", 4, "61", 'col']
    bible_info_dataFrame.loc[51] = ["Thessalonians1", 5, "62", '1th']
    bible_info_dataFrame.loc[52] = ["Thessalonians2", 3, "63", '2th']
    bible_info_dataFrame.loc[53] = ["Timothy1", 6, "64", '1ti']
    bible_info_dataFrame.loc[54] = ["Timothy2", 4, "65", '2ti']
    bible_info_dataFrame.loc[55] = ["Titus", 3, "66", 'tit']
    bible_info_dataFrame.loc[56] = ["Philemon", 1, "67", 'phm']
    bible_info_dataFrame.loc[57] = ["Hebrews",  13, "68", 'heb']
    bible_info_dataFrame.loc[58] = ["James", 5, "69", 'jas']
    bible_info_dataFrame.loc[59] = ["Peter1", 5, "70", '1pe']
    bible_info_dataFrame.loc[60] = ["Peter2", 3, "71", '2pe']
    bible_info_dataFrame.loc[61] = ["John1", 5, "72", '1jn']
    bible_info_dataFrame.loc[62] = ["John2", 1, "73", '2jn']
    bible_info_dataFrame.loc[63] = ["John3", 1, "74", '3jn']
    bible_info_dataFrame.loc[64] = ["Jude", 1, "75", 'jud']
    bible_info_dataFrame.loc[65] = ["Revelation", 22, "76", 'rev']

    return bible_info_dataFrame

def crawl_bible(book, chapter):
    # Book 정보 추출
    new_testament_pandas = get_book_url_index()
    book_record = new_testament_pandas.loc[new_testament_pandas['Book'] == book]
    book_index = book_record.index.values[:][0] + 1

    # URL 생성
    korean_web_book_index = book_record['Korean url info'].values[:][0]
    korean_web_chapter = str(chapter)

    korean_complete_url = "http://bible.godpia.com/read/reading.asp?ver=gae&ver2=&vol=" + korean_web_book_index + "&chap="+ korean_web_chapter +"&sec="

    # 대기
    random_sleep()

    # chrome driver 사용
    driver = webdriver.Chrome(executable_path='app/chromedriver.exe')
    driver.get(url=korean_complete_url)
    driver.implicitly_wait(time_to_wait=0.5)

    num_of_pagedowns = 3

    # 스크롤하기 위해 소스 추출
    body = driver.find_element_by_tag_name('body')

    while num_of_pagedowns:
        time.sleep(1)
        body.send_keys(Keys.PAGE_DOWN)
        num_of_pagedowns -= 1
    time.sleep(1)

    # html 추출 완료
    korean_html = driver.page_source
    driver.close()

    # verse 저장용 string
    verse_string = "{\n"
    verse_string += "\t\"verses\":[\n"

    # html 파싱
    korean_soup = BeautifulSoup(korean_html, 'lxml')
    korean_bible = korean_soup.find(class_="wide")
    raw_verses = korean_bible.select('p > span')

    for raw_verse in raw_verses:
        full_verse = raw_verse.get_text() # 전체 verse text

        parsed_raw_verse = raw_verse.select('span')[0].get_text()
        verse_index = parsed_raw_verse # verse index text

        pure_verse = full_verse[len(verse_index):] # index 제거된 verse

        verse_string += "\t\t{\"" + verse_index + "\":\"" + pure_verse + "\"},\n"

    # end save string 
    verse_string = verse_string[:-2]
    verse_string += "\n"
    verse_string += "\t]\n"
    verse_string += "}"

    # write verses as json
    f = open(os.path.join("app", "result", "book" + str(book_index), "chapter" + str(chapter)+".json"), 'w', encoding='utf8')
    f.write(verse_string)
    f.close()



    
def main():
    # Book, Chapter, Verse Info 추출
    new_testment = get_book_url_index()
    books = new_testment['Book'].values[:]
    chapters = new_testment['chapter number'].values[:]

    # result 폴더 생성
    if os.path.exists(os.path.join("app", "result")) is False:
        os.mkdir(os.path.join("app", "result"))

    # start crawler
    for book_index, (book_name, max_chapter) in enumerate(zip(books, chapters)):
        if os.path.exists(os.path.join("app", "result", "book" + str(book_index + 1))) is False:
            os.mkdir(os.path.join("app", "result", "book" + str(book_index + 1)))
        
        for chapter in range(1, max_chapter+1):
            crawl_bible(book_name, chapter)
    

if __name__ == '__main__':
    main()
