import wolframalpha
import wikipedia
from Search_stack import search_stack
def JARVIS(question):
    result=""
    try:
        try:
            app_id="885R8W-R9UEURWJUY"
            client=wolframalpha.Client(app_id)

            res=client.query(question)
            answer =next(res.results).text

            result= answer
        except:
            try:
                result=search_stack(question)
                if(result==0):
                    print('stack failed')
                    raise Exception('not found')
            except :
                result= wikipedia.summary(question)
                
        return result
    except Exception as e:
         return "Appoligies! I am afraid i can't provide answer to this at this momment"
