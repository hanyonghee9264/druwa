"""
problem01에서 작성한 함수에 docstring을 작성하여 함수에 대한 설명을 달아보고, help(함수명)으로 해당설명을 출력해본다.
"""
def fruits(colors):
    '''함수와 if문을 통한 문제 풀이 ㅠㅠ 그치만 여진형 도움을 받은문제'''
    if colors == 'red':
        result = 'apple'
    elif colors == 'yellow':
        result = 'banana'
    elif colors == 'green':
        result = 'melone'
    else:
        return ''' I don't know '''
    return result

# help(fruits) 를 통해 docstring 작성 내용 확인!
