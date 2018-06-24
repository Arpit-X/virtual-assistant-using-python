import mechanicalsoup
from Stack_answer import stack_answer
import webbrowser

def search_stack(queiry):
    result=""
    try:
        link="https://www.stackoverflow.com/search?q="+queiry.replace(" ","+")
        browser=mechanicalsoup.Browser()
        page=browser.get(link)
        soup = page.soup
        req=soup.find('div',{'class':'question-summary search-result'}).a
        qlink=req.get('href')
        qlink="https://www.stackoverflow.com"+qlink
        result= stack_answer(qlink)
    except :
        result= 0
    return result    




    

