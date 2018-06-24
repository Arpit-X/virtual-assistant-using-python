import mechanicalsoup
import re

def stack_answer(link):
    try:
        browser=mechanicalsoup.Browser()
        page=browser.get(link)
        soup=page.soup
        tag=soup.find("div",{"class":"answer accepted-answer"}).find("div",{"class":"post-text"})#.stripped_string
        results=""
        for i in tag.contents:
            results+=str(i)+'\n'    


        regex= re.compile('<.*?>')
        results=regex.sub('',results)
        return results

    except :
        return 0
