# Python Labs
## My very first Python code (1 course)

<h3 align="center">Lab 1</h3> 
<b>Task 1:</b> Write an expression calculation program. Provide data from the computer keyboard and print calculation results. 

`F = sin(x+0.4)^2 / (y^2 + 7.325x) `

<details>
  <summary>Solution</summary><p align="left">
  ```python
 from math import sin, pow

while True:
    try:
        x = float(input("Enter x: "))
        y = float(input("Enter y: "))
    except ValueError:
        print("Enter number!")
    else:
        part1 = pow(sin(x + 0.4), 2)
        part2 = pow(y, 2) + 7.325 * x
        try:
            result = part1 / part2
        except ZeroDivisionError:
            print("You cannot divide by zero!")
        else:
            print("F ≈ ", round(result, 6))
            break

  ```
</details>

<b>Task 2:</b> Enter the current time from the keyboard and determine the time of day (am - from 0 to 12:00, pm - from 12:00 to 24:00) in Kyiv, London and New York.

<details>
  <summary>Solution</summary><p align="left">
  ```python
from datetime import timedelta, datetime

while True:
    try:
        Kyiv_time = datetime.strptime(input("Enter current time in Kyiv: "), '%H:%M:%S')
    except ValueError:
        print("Enter time value!")
    else:
        London = Kyiv_time - timedelta(hours=3)
        Paris = Kyiv_time - timedelta(hours=1)
        NewYork = Kyiv_time - timedelta(hours=7)

        London_time = London.strftime('%H:%M:%S')
        Paris_time = Paris.strftime('%H:%M:%S')
        NewYork_time = NewYork.strftime('%H:%M:%S')

        am, pm = "(am)", "(pm)"

        if London.hour < 12: London_time = London_time + am
        else: London_time = London_time + pm

        if Paris.hour < 12: Paris_time = Paris_time + am
        else: Paris_time = Paris_time + pm

        if NewYork.hour < 12: NewYork_time = NewYork_time + am
        else: NewYork_time = NewYork_time + pm

        print("Time in London:", London_time)
        print("Time in Paris:", Paris_time)
        print("Time in New York:", NewYork_time)

        print("\nDifference between Paris and London -", Paris.hour - London.hour, "hours")
        print("Difference between Paris New York -",  Paris.hour - NewYork.hour, "hours")
        print("Difference between London and New York -", London.hour - NewYork.hour, "hours")

        break


  ```
</details>


<b>Task 3:</b> Enter a natural number N > 100 from the keyboard and form a sequence of natural numbers `i = 11,12,...N`
Calculate the sequence `s{i} = s{i-1} + i^2`, provided that `s{10} = 10`.
Print sequence elements.

<details>
  <summary>Solution</summary><p align="left">
  ```python
while True:
    try:
        n = int(input("Enter N: "))
    except ValueError:
        print("Enter correct number!")
    else:
        if n <= 100:
            print("Error: N must be greater than 100!")
        else:
            for i in range(11, n + 1):
                s = i
                i = (i-1) + i*i
                if i < 11:
                    i = 10
                print(i)
            break
  ```
</details>

<h3 align="center">Lab 2</h3> 
<b>Task 1:</b> Enter a line. Get the penultimate word of this line. Word separators are considered to be one or more spaces. 

<details>
  <summary>Solution</summary><p align="left">
  ```python
 new_line = input(str("Enter sequence of symbols: "))
print(new_line.split()[-2])
  ```
</details>

<b>Task 2:</b> Enter a sequence of characters. Print all words containing the sequence as separate character lists (without spaces). 

<details>
  <summary>Solution</summary><p align="left">
  ```python
line = bytes(input('Enter sequence of symbols : '), 'utf-8')

for i in line.split():
    print(list("%s" % ''.join(i.decode("utf-8"))))

  ```
</details>

<h3 align="center">Lab 3</h3> 
<b>Task 1:</b> An integer list is randomly specified. Determine the number of sections of the list in which the elements grow monotonically (each subsequent number is greater than the previous one). After each of the sections, insert the number of elements of this section as a list item and find the sum of the items in the resulting list.

<details>
  <summary>Solution</summary><p align="left">
  ```python
 from random import randrange
try:
    size = int(input("Enter array size: "))
except ValueError:
    print("Enter correct size!")
else:
    a = [randrange(10, 100) for i in range(size)]
    print("Generated List: ", a)
    a.append(0)
    b, count = [], 1

    for i in range(size):
        b.append(a[i])
        if a[i + 1] > a[i]: count += 1
        elif count > 1:
            b.append(count)
            count = 1

    print("New List: ", list(map(lambda x: x, b)), '\n' + '-'*50)
    print('Sum of elements in list - ', sum(b))
  ```
</details>

<b>Task 2:</b> Generate a matrix A of dimension m × m from random elements that are two-digit integers. Find the maximum element on the main diagonal and divide by this element all the elements of the matrix, except himself.

<details>
  <summary>Solution</summary><p align="left">
  ```python
from random import randrange
from numpy import array, diagonal

try: size = int(input("Enter matrix size: "))
except ValueError: print("Enter correct matrix size")
else:
    print("Generated matrix:")
    matrix = [[randrange(10, 100) for j in range(size)] for i in range(size)]
    print(array(matrix), "\n")

    max_elem = max(diagonal(matrix))
    print("The maximum number of the main diagonal -", max_elem, "\n")

    new_array = array([[max_elem if i == j and matrix[i][j] == max_elem else matrix[i][j] / max_elem for i in range(size)] for j in range(size)])
    print("New matrix:\n", array([['%.2f' % elem for elem in a] for a in new_array]))

  ```
</details>

<h3 align="center">Lab 4</h3> 
Create a dictionary with keys - the names of the continents of our planet. The values of this dictionary will be dictionaries with the keys-names of the countries which are located on the given continent, and values-tuples. The elements of such tuples should be the names of the capitals of the countries, their area and population. The program should display a list of countries when entering the name of the continent and display the continent, population and area when entering the name of the country.

<details>
  <summary>Solution</summary><p align="left">
  ```python
 continents = {
    "Asia":
        {'Japan': ("Tokyo", 377975, 125620000)},
    "Europe":
        {'Austria': ("Vienna", 83800, 8404000),
         'Germany': ("Berlin", 357000, 81751000),
         'Great Britain': ("London", 244800, 62700000),
         'Iceland': ("Reykjavík", 103000, 317630),
         'Italy': ("Rome", 301400, 60605000),
         'Spain': ("Madrid", 506000, 46162000),
         'Ukraine': ("Kyiv", 603700, 45562000)}
}

name = input("Enter the name of the continent or country: ").title()
continents_list = continents.keys()

if name in continents_list:
    for country, info in continents.get(name).items():
        print("Country: " + country,
              "\n\tCapital: ", info[0],
              "\n\tArea: ", info[1], "km²"
              "\n\tPopulation: ", info[2])
else:
    for i in continents.keys():
        info = continents.get(i).get(name)
        if info is None: continue
        print("Continent: ", i,
              "Area: ", info[1], "km²",
              "Population: ", info[2])
  ```
</details>

<h3 align="center">Lab 5</h3> 
Create a class that describes the continent. The class must contain the name of the continent, a dictionary with keys - the names of the countries that are located on the continent, and tuple values. The elements of such tuples should be the names of the capitals of the respective countries, their area and population. Methods of the class must determine the country's affiliation to the continent, determine the parameters of the country when entering its name. Create objects of this class for multiple continents using Wikipedia data. The program should display a list of countries when entering the name of the continent and display the continent, population and area when entering the name of the country.

<details>
  <summary>Solution</summary><p align="left">
  ```python
earth = {
    "Asia":
        {'Japan': ("Tokyo", 377975, 125620000)},
    "Europe":
        {'Austria': ("Vienna", 83800, 8404000),
         'Germany': ("Berlin", 357000, 81751000),
         'Great Britain': ("London", 244800, 62700000),
         'Iceland': ("Reykjavík", 103000, 317630),
         'Italy': ("Rome", 301400, 60605000),
         'Spain': ("Madrid", 506000, 46162000),
         'Ukraine': ("Kyiv", 603700, 45562000)}
}


class Earth:
    def __init__(self, continent):
        self.dictionary = earth
        self.continent = continent

    def continent_out(self, a):
        print(
            "  Country  " + " " * 20 + "  Capital  " + " " * 15 + "     Area (km²)    " + " " * 7 + "  Population  " + "\n" +
            "-----------" + " " * 20 + "-----------" + " " * 15 + "-------------------" + " " * 7 + "--------------")
        for x in self.dictionary.get(a.title()):
            print("{:30}".format(x),
                  "{:<30}{:<25}{:<25}".format(self.dictionary.get(a.title())[x][0],
                                              str(self.dictionary.get(a.title())[x][1]) + " km²",
                                              str(self.dictionary.get(a.title())[x][2])))

    def country_out(self, a):
        a.insert(0, ('Continent', ('Capital', 'Area (km²)', 'Population')))
        b = []
        for i in a:
            b.extend((i[0], i[1][0], str(i[1][1]), str(i[1][2])))
        return ("{:<20}{:<20}{:<25}{:<25}\n" * len(a)).format(*b)

    def print_continent(self):
        return self.continent_out(self.continent)

    def print_country(self, a):
        for i in self.dictionary.keys():
            continent = i
            country_describe = self.dictionary.get(continent).get(a.title())
            if country_describe is None: continue
            return self.country_out([(continent, country_describe)])


input_str = input("Enter the name of the continent or country: ")

if input_str.title() in earth.keys():
    Earth(input_str).print_continent()
else:
    print(Earth(continent=None).print_country(input_str))

  ```
</details>

<h3 align="center">Lab 6</h3> 
Read the file "27.txt" and divide it into 2 files "271.txt", "272.txt", which contain odd and even numbered characters of the original file. Perform an "&" operation on the character sets of these files. Save the resulting file "273.txt" in the encoding "cp1251". Create a file from characters that are present in the file "27.txt" but not in "273.txt". Save this file in UTF-8 encoding. ([Open txt file](Pr-Lab6/27.txt))

<details>
  <summary>Solution</summary><p align="left">
  ```python
try:
    text, add_text = open("27.txt", "r"), open("27.txt", "r")
    text_symbols = list(text.read())
    odd_symbols = "".join(text_symbols[1::2])
    pair_symbols = "".join(text_symbols[::2])
    intersection_symbol = set(pair_symbols.lower()) & set(odd_symbols.lower())
    with open("271.txt", "w", encoding='utf-8') as output: output.write(odd_symbols)
    with open("272.txt", "w", encoding='utf-8') as output: output.write(pair_symbols)
    with open("273.txt", "w", encoding='cp1251') as output: output.write(" ".join(intersection_symbol))
    with open("274.txt", "w", encoding='utf-8') as output: output.write(" ".join(set(add_text.read().lower()) - intersection_symbol))
except IOError: print("Error: File does not exist.")
  ```
</details>

