def city_country(city, country):
    '''City and country formatting into list'''
    places =[]
    listed = f"{city.upper()}, {country.upper()}"
    listed.append(places)
    return places

while True:
    print("\n'q' for exit")
    city_name = input("City name - ")
    if city_name =='q':
        break

    country_name = input("Country name - ")
    if country_name =='q':
        break

formateing = city_country(city_name, country_name)
print(formateing)