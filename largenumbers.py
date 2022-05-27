from secrets import randbits
import time

size = [8, 16, 32, 64, 128, 256, 512, 1024] 
keysizeforbruteforce = int(input('Введите размер ключа для атаки типа "грубая сила": ')) 
randomkeys = dict.fromkeys(size) 

for i in size:
    print(f'Пространство ключей {i} - битовой последовательности: {pow(2,i)}')
    randomkeys[i] = hex(randbits(i))
    print(f'Случайное значение ключа для {i} - битовой последовательности: {randomkeys.get(i)}')

def bruteforce(a,b):
    while hex(a) != b:
        a += 1
    return a

time1 = time.time()
bruteforce(0,randomkeys.get(keysizeforbruteforce))
time2 = time.time()

print(f'Время для нахождения ключа  {keysizeforbruteforce} - битовой последовательности: {(time2-time1)*1000}')