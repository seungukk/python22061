
#가변인자 함수 
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

#호출
print(union("HAM","SPAM"))
print(union("HAM","SPAM","EGG"))
