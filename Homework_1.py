from queue import Queue
import random
import string

q = Queue()

def generate_request():

    # генеруємо номер заявки
    chars = string.ascii_letters + string.digits
    new_request = ''.join(random.choices(chars, k=10))
    q.put(new_request) # додали заявку в чергу
    return f"{new_request} заявку додано в чергу. Всього в черзі {q.qsize()} заявок."

def process_request():
    if not q.empty():
        request = q.get() # видалили заявку з черги
        print (f"{request} заявка обробляється. Всього в черзі залишилось {q.qsize()} заявок.")
        
    else:
        print ("Черга порожня")

while True:
    # автоматично створюємо від 1 до 3 заявок
    count = random.randint(1, 3)
    for i in range(count):
        print(generate_request())
    
    # автоматично обробляємо заявку
    process_request()
    
    """питаємо користувача чи продовжувати 
    (тут умову так/ні можна покращити але це просто для тестування коду 
    зробила щоб генерував заявки)"""
    
    answer = input("Продовжити? (так/ні): ")
    if answer.strip().lower() == "ні":
        break
