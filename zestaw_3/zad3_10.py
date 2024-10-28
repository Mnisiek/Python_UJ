"""
Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim
(z literami I, V, X, L, C, D, M) na liczby arabskie
(podać kilka sposobów tworzenia takiego słownika).
Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()]. """


D1 = {'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000}

print(D1['L'])

D2 = {}
D2['I'] = 1
D2['V'] = 5
D2['X'] = 10
D2['L'] = 50
D2['C'] = 100
D2['D'] = 500
D2['M'] = 1000

print(D2['C'])



def roman2int(roman_num: str) -> int:
    D = {'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1}
    extra_dict = {'DCCCC': 'CM', 'CCCC': 'CD', 'LXXXX': 'XC',
                    'XXXX': 'XL', 'VIIII': 'IX','IIII': 'IV'}
    
    for key, value in extra_dict.items():
        roman_num = roman_num.replace(value, key)

    result = 0
    counter = 0
    i = 0
    for num in D.keys():
        while i < len(roman_num) and roman_num[i] == num:
            counter += 1
            i += 1
        if counter != 0:
            result += counter * D[num]
            counter = 0
    return result


print(roman2int("MCLXXIX"))
