"""
Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji,
która może zawierać zagnieżdżone podsekwencje. Wskazówka: rozważyć wersję
rekurencyjną, a sprawdzanie, czy element jest sekwencją, wykonać przez
isinstance(item, (list, tuple)). """


def sum_seq(sequence):
    result = 0
    for element in sequence:
        if isinstance(element, (list, tuple)):
            result += sum_seq(element)
        else:
            result += element
    
    return result
    

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(sum_seq(seq))
