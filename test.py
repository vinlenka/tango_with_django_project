cats = {'Python': {'pages': [], 'views': 128, 'likes': 64},
        'Django': {'pages': [], 'views': 64, 'likes': 32},
        'Other Frameworks': {'pages': [], 'views': 32, 'likes': 16}}

for cat, cat_data in cats.items():

    views = cat_data['views'] if 'views' in cat_data else 0,
    likes = cat_data['likes'] if 'likes' in cat_data else 0

    print (cat)
