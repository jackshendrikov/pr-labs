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
