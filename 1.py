print('Введите h:')
h = int(input())
print('Введите a:')
a = int(input())
print('Введите r:')
r = int(input())
print('Введите v:')
v = int(input())
p = 3.14
if h>0:
    if a>0:
        if r>0:
            if v>0:
                v1 = a**3
                v2 = h*p*r**2
                if v1 == v:
                    print('Да, куб заполнится.')
                else:
                    if v1 > v:
                        print('Нет, куб не заполнится.')
                    else:
                        print('Куб переполнится.')
                
                if v2 == v:
                    print('Да, цилиндр заполнится.')
                else:
                    if v2 > v:
                        print('Нет, цилиндр не заполнится.')
                    else:
                        print('Циллиндр переполнится.')
                        
                if v1+v2 == v:
                    print('Обе емкости заполнятся.')
                else:
                    if v1+v2 > v:
                        print('Сразу 2 емкости не заполнятся.')
                    else: 
                        print('Емкости переполнятся')
            else:
                print('Ошибка!')
        else:
            print('Ошибка!')
    else:
        print('Ошибка!')
else:
    print('Ошибка!')
    
        