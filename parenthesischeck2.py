openingparenthesis = '[{('

closingparenthesis = ')}]'
openingList = []



exp = '(){'

pairs = {')':'(', '}':'{',']':'['}

def checkParenthesis(exp):
    for i in exp:
        if i in openingparenthesis:
            openingList.append(i)
        elif i in closingparenthesis:
            if openingList==[]:
                return False
            if pairs[i] == openingList[-1]:
                    openingList.pop()
    return True 

print(checkParenthesis(exp))



