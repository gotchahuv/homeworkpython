print('Номер 8')
import time
def cache(max_size=None):
    if max_size is not None and max_size<0:
        raise ValueError('max_size<0')
    def decorator(func):
        save={}
        def wrapper(*args, **kwargs):
            key=(args,str(sorted(kwargs.items())))
            if key in save:
                return save[key]
            res=func(*args, **kwargs)
            wrapper.count+=1
            if max_size is None or max_size>0:
                if max_size is not None and len(save)>=max_size:
                    i=iter(save)#итератор по ключам
                    first_key=next(i)#двигает итератор на следующий клююч
                    del save[first_key]
                save[key]=res
            return res
        wrapper.count=0
        return wrapper
    return decorator
@cache(10)
def add(a,b):
    time.sleep(2)
    return a+b
#f1=cache(10)#вовзвращем декоратор
#f2=f1(add)#возвращаем wrapper
#add=f2#функция add выполняет wrapper
print(add(1,b=2))
print('реальных вычислений',add.count)
print(add(1,b=2))
print(add(2,b=3))
print(add(2,b=3))
print('реальных вычислений',add.count)