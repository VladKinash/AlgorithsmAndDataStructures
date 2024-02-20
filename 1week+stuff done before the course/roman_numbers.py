

roman = "MCMXCIV"
num = ''


def toInt(s):
    all_numerals = { 'I': 1,
                'IV': 4,
                'V': 5,
                'IX': 9,
                'X': 10,
                'XL': 40,
                'L': 50,
                'XC': 90,
                'C': 100,
                'CD': 400,
                'D': 500,
                'CM': 900,
                'M': 1000}
    temp = ""
    list_roman = []
    translated_num = 0
    for i in s:
        temp += i
        if len(temp) >= 2 and temp not in all_numerals.keys():
            list_roman.append(temp[0])
            temp = temp[1]
            
        elif len(temp) >= 2 and temp in all_numerals.keys():
            list_roman.append(temp)
            temp = ""

    if temp != "":
        list_roman.append(temp)

    for i in list_roman:
        translated_num += all_numerals[i]

    return translated_num


print(toInt(roman))