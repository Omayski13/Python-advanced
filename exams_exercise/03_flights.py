def flights(*args):
    flights_dict = {}
    result = []
    for flight_index in range(0,len(args),2):
        flight = args[flight_index]
        if flight == "Finish":
            break
        passangers = int(args[flight_index + 1])
        if flight not in flights_dict:
            flights_dict[flight] = passangers
        else:
            flights_dict[flight] += passangers

    return flights_dict

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))

