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