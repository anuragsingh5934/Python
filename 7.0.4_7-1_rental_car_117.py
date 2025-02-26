garage = {
    'Nano':{
        'rent fee': '700/day inr',
        'top speed': '90 KMPL',
        'color': 'gray',
        'fule': 'pitrol',
        'engine size': '600cc'
    },
    
    'Swift':{
        'rent fee': "2000/day inr",
        'top speed': '130 KMPH',
        'color': "white",
        'fule': ['cng','petrol'],
        'engine size': '1200cc'
    }
}
    
user_resp =input('Which type of car you like - ')
print(f'Let me see, if i can find you a {user_resp.upper()}')