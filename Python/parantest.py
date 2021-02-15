from collections import deque
def m(s):
    d={'(':')','{':'}','[':']'}
    st=deque()
    for i in s:
        if i=='(' or i=="[" or i=='{':
            st.append(i)
        if i==')' or i==']' or i=='}':
            if len(st)==0:
                return False
            if not d[st.pop()]==i:
                return False
    return len(st)==0
                





print(m('()'))
print(m("({a+b})"))
print(m("))((a+b}{"))
print(m("((a+b))"))
print(m("((a+g))"))
print(m("))"))
print(m("[a+b]*(x+2y)*{gg+kk}"))
