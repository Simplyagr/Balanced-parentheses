openingparenthesis = '[{('
closingparenthesis = ')}]'

openingList = []

exp = '[{(){}}]' #user can input any expression of choice

pairs = {')':'(', '}':'{',']':'['}

def checkParenthesis(exp):
    for i in exp:
        if i in openingparenthesis:
            openingList.append(i)
        elif i in closingparenthesis:
            if openingList==[]:
                return False
            elif pairs[i] == openingList[-1]:
                    openingList.pop()
            else:
                 return False
    if openingList==[]:
         return True
    else:
         return False

print(checkParenthesis(exp))


