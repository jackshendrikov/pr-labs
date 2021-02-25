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
