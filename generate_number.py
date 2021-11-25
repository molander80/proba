def generate_number (N:int, M:int, prefix=None):
    """Генерирует все гисла (с лидирующим незначащими нулями)
    в N-ричной системе счисления (N <=10)
    длины М
    """
    prefix= prefix or []
    if M == 0:
        print (prefix)
        return
    for digit in range (N):
        prefix.append(digit)
        generate_number(N, M-1, prefix)
        prefix.pop()


def find (number, A):
    """ ищет number в А и возвращает True, если такой есть
        False, если такого нет
    """
    for x in A:
        if number == x:
            return True
    return False

def generate_permutations (N:int, M:int=-1, prefix=None):
    """ Генерация всех перестановок N  чисел в M позциях,
    с префексом prefix
    """
    M = N if M == -1 else  M # По умолчанию  N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for number in range (1, N+1):
        if find (number, prefix):
            continue
        prefix.append(number)
        generate_number(N, M-1, prefix)
        prefix.pop()
generate_permutations(3)
#generate_number(4,3)