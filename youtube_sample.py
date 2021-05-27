from __future__ import unicode_literals
import youtube_search
import youtube_dl
# import webbrowser

print("Do you know the url(y) or would you like to search(n)")
chk = input("y/n\t")

if chk == 'y':
    print("If url is invalid the closest result will be considered")
    url = input("Enter url\n")
    print('\n')

elif chk == 'n':
    search_keyword = str(input("Enter search keyword\t"))
    results = youtube_search.YoutubeSearch(search_keyword, max_results=10).to_dict()

    i = 0
    for x in results:
        print(str(i) + '.\t' + x['duration'] + '\t' + x['title'])
        i += 1

    print('\n')
    i = int(input("Enter result number\t"))
    print('\n')
    url_suffix = results[i]['url_suffix']
    url = 'https://www.youtube.com' + url_suffix

else:
    raise TypeError("Input was not one of y/n")

# webbrowser.open(url)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading')


ydl_opts = {
    'simulate': False,
    'format': 'best',  # bestaudio/best
    'noplaylist': True,
    'logtostderr': False,
    'default_search': 'auto',
    ''' 'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],'''
    'progress_hooks': [my_hook],
    'geo_bypass_country': 'US',
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
