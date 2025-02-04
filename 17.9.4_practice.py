favorite_language = {
    'aniruddh': 'python',
    'sumit' : 'c++',
    'kundan': 'java'
}

friends = ['sumit', 'sarah']
for name in favorite_language.keys():
    print(f"hi {name.title()}.")

    if name in friends:
        fav_lan = favorite_language[name].title()
        print(f"\t{name.title()}, i see you love {fav_lan}!")