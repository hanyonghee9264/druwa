"""
매개변수로 문자열을 받고, 해당 문자열이 red면 apple을, yellow면 banana를, green이면 melon을, 어떤 경우도 아닐 경우 I don't know를 리턴하는 함수를 정의하고, 사용하여 result변수에 결과를 할당하고 print해본다.
"""

def fruits(colors):
    if colors == 'red':
        result = 'apple'
    elif colors == 'yellow':
        result = 'banana'
    elif colors == 'green':
        result = 'melone'
    else:
        return '''I don't know'''
    return result

# fruits('red')  ====> apple
