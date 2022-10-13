#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
#Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc


readT=r"homework\\DZ_seminar5\\111.txt"
zipWrite="homework\\DZ_seminar5\\222.txt"
recWrite="homework\\DZ_seminar5\\333.txt"

#чтение строки с файла
try:
    with open(readT) as data:
        file=data.read()      
except:
    print("Файл не найден")

#Сжатие файла
def Sjatie(text): 
    sjat = ''
    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
        sjat += str(count) + text[i]
        i += 1   
    return sjat
zip=Sjatie(file)

#Запись сжатых данных в файл
try:
    with open(zipWrite,'w') as data:
        data.write(zip)      
except:
    print("Файл не найден")

#Чтение сжатых данных из файла
try:
    with open(zipWrite,'r') as data:
        file2=data.read()      
except:
    print("Файл не найден")

#Восстановление данных из сжатого файла
def Recovery(text): 
    datarecovery = ''
    i = 0
    while i < len(text):
        datarecovery += str(text[i+1]) * int(text[i])
        i+=2
    return datarecovery
rec=Recovery(file2)

#Запись востановленных данных в файл
try:
    with open(recWrite,'w') as data:
        data.write(rec)      
except:
    print("Файл не найден")
