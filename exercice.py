import csv
import string
from hash_tables import HashTable as ht

def main():
    tempfile = first_EX()
    hash_file = second_EX()
    poem = third_EX()
    print(f"EXO 1: The max temperature in january was {tempfile[0]}, and \nthe average temperature in the first week was {tempfile[1]}\n")
    print(f"EXO 2: The temperature in 4 january was {hash_file['Jan 4']} \nthen in january 9 it was {hash_file['Jan 9']} \n")
    print("EXO 3:")
    for key,value in poem.items():
        print(f"{key}: {value}")

def first_EX():
    average = 0
    max_temp = 0
    counter = 0
    with open('weather.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            temp = float(row[1])
            counter += 1
            if counter <= 7:
                average += temp
            if temp > max_temp:
                max_temp = temp
    return max_temp, round(average / 7, 2)

def second_EX():
    weather_table = ht()
    with open('weather.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            weather_table[row[0]] = float(row[1])
    return weather_table

def third_EX():
    poem = {}
    with open('poem.txt', 'r') as f:
        text = f.read()
        words = text.split()
        for word in words:
            word = word.strip(string.punctuation).lower()
            if word in poem:
                poem[word] += 1
            else:
                poem[word] = 1
    return poem


if __name__ == '__main__':
    main()

### hash table 1, general tree 1, queue 2
