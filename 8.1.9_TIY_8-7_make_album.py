# def make_album(artist_name, album_title):
#     """dict"""
#     dict={}
#     dict[artist_name] = album_title
#     return dict

def making_album(artist, album_title):
    album = {'artist': artist, "album tilte": album_title}
    return album

while True:
    ar_name = input("Artist name - ")
    if ar_name == 'q':
        break

    alb_name = input("album name - ")
    if alb_name == 'q':
        break
    break
aaa = making_album(ar_name,alb_name)
print(aaa)