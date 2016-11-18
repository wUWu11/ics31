# ICS 31, 5-10-16

from collections import namedtuple

Album = namedtuple('Album', 'id artist title year songs')
Song = namedtuple('Song', 'track title length play_count')

MUSIC = [
    Album(1, "Peter Gabriel", "Up", 2002,
          [Song(1, "Darkness", 411, 5),
          Song(2, "Growing Up", 453, 5),
          Song(3, "Sky Blue", 397, 2),
          Song(4, "No Way Out", 473, 2),
          Song(5, "I Grieve", 444, 2),
          Song(6, "The Barry Williams Show", 735, 1),
          Song(7, "My Head Sounds Like That", 389, 1),
          Song(8, "More Than This", 362, 1),
          Song(9, "Signal to Noise", 456, 2),
          Song(10, "The Drop", 179, 1)]),
    Album(2, "Simple Minds", "Once Upon a Time", 1985,
          [Song(1, "Once Upon a Time", 345, 9),
          Song(2, "All the Things She Said", 256, 10),
          Song(3, "Ghost Dancing", 285, 7),
          Song(4, "Alive and Kicking", 326, 26),
          Song(5, "Oh Jungleland", 314, 13),
          Song(6, "I Wish You Were Here", 282, 12),
          Song(7, "Sanctify Yourself", 297, 7),
          Song(8, "Come a Long Way", 307, 5)]),
    Album(3, "The Postal Service", "Give Up", 2003,
          [Song(1, "The District Sleeps Alone", 284, 13),
          Song(2, "Such Great Heights", 266, 13),
          Song(3, "Sleeping In", 261, 12),
          Song(4, "Nothing Better", 226, 18),
          Song(5, "Recycled Air", 269, 13),
          Song(6, "Clark Gable", 294, 12),
          Song(7, "We Will Become Silhouettes", 300, 11),
          Song(8, "This Place is a Prison", 234, 9),
          Song(9, "Brand New Colony", 252, 9),
          Song(10, "Natural Anthem", 307, 7)]),
    Album(4, "Midnight Oil", "Blue Sky Mining", 1989,
          [Song(1, "Blue Sky Mine", 258, 12),
          Song(2, "Stars of Warburton", 294, 11),
          Song(3, "Bedlam Bridge", 266, 11),
          Song(4, "Forgotten Years", 266, 8),
          Song(5, "Mountains of Burma", 296, 9),
          Song(6, "King of the Mountain", 231, 8),
          Song(7, "River Runs Red", 322, 9),
          Song(8, "Shakers and Movers", 268, 9),
          Song(9, "One Country", 353, 7),
          Song(10, "Antarctica", 258, 6)]),
    Album(5, "The Rolling Stones", "Let It Bleed", 1969,
          [Song(1, "Gimme Shelter", 272, 3),
          Song(2, "Love In Vain", 259, 2),
          Song(3, "Country Honk", 187, 0),
          Song(4, "Live With Me", 213, 2),
          Song(5, "Let It Bleed", 327, 2),
          Song(6, "Midnight Rambler", 412, 1),
          Song(7, "You Got the Silver", 170, 0),
          Song(8, "Monkey Man", 251, 13),
          Song(9, "You Can't Always Get What You Want", 448, 10)])
]

#print(MUSIC)

def Song_print(s: Song) -> None:
    ''' Print a song in a readable format
    '''
    print("\t", s.track, s.title, s.length, s.play_count, sep="---")
    return

#Song_print(Song(3, "Tribute", 248, 0))

def Album_print(a: Album) -> None:
    ''' Print an Album in a readble format
    '''
    print(a.id, a.artist, a.title, a.year, sep=" / ")
    for s in a.songs:
        Song_print(s)
    return

#Album_print(MUSIC[0])

def Collection_print(C: 'list of Albums') -> None:
    ''' Print a music Collection in a readable format
    '''
    for a in C:
        Album_print(a)
        print()
    return

#Collection_print(MUSIC)

def Album_year(A: Album) -> int:
    ''' Return the year the album was released
    '''
    return A.year

'''
print("\nAlbums in order by year:\n")
MUSIC.sort(key=Album_year)
Collection_print(MUSIC)
'''

def Album_title(A: Album) -> str:
    ''' Return the title of the album
    '''
    return A.title

'''
print("\nAlbums in order by title:\n")
MUSIC.sort(key=Album_title)
Collection_print(MUSIC)
'''

# So far, this is the way we've learned how to sort Collections.
# But there is a repetitive pattern (calling .sort(key=FUNCTION)).
# We can generalize this...

def Collection_sort(C: 'list of Albums', key_function: 'function') -> None:
    ''' Reorder the collection by comparing the values that the
        key_function parameter returns
    '''
    C.sort(key=key_function)
    return

'''
print("\n\nORIGINAL:\n")
Collection_print(MUSIC)

Collection_sort(MUSIC, Album_year)
print("\n\nORDERED BY RELEASE YEAR:\n")
Collection_print(MUSIC)

Collection_sort(MUSIC, Album_title)
print("\n\nORDERED BY TITLE:\n")
Collection_print(MUSIC)
'''

def Album_length(a: Album) -> int:
    ''' Return the total number of seconds of all tracks on
        the album
    '''
    total = 0
    for s in a.songs:
        total += s.length
    return total

'''
Collection_sort(MUSIC, Album_length)
print("\n ORDERED BY LENGTH")
Collection_print(MUSIC)

for a in MUSIC:
    print(a.title, Album_length(a)) # Checks the album lengths
'''

# Now let's think about writing functionality for obtaining popular
# songs (i.e. songs played more than n+ times).

def popular_songs(C: 'list of Albums', n: int) -> 'list of Songs':
    ''' Return a list of all songs played n or more times.
    '''
    result = []
    for a in C:
        for s in a.songs:
            if s.play_count >= n:
                result.append(s)
    return result

'''
popular = popular_songs(MUSIC, 10)
for s in popular:
    Song_print(s)
    
# Write a function that displays popular songs AND album info.

- Can store album info with each song.
    - Kinda messy and changes will need to take place in various places.

- Create another namedtuple called Songdisplay
    - Contains song-title, song-length, song-play_count
    - AND album-artist, album-title, album-year.
'''
Songdisplay = namedtuple('Songdisplay', 'songtitle length play_count artist albumtitle albumyear')

def Songdisplay_print(sd: Songdisplay) -> None:
    ''' Print a songdisplay in a readable manner
    '''
    print(sd.songtitle, sd.length, sd.play_count, sd.artist, sd.albumtitle, sd.albumyear, sep=" ** ")
    return

def popular_songs2(C: 'list of Albums', n: int) -> 'list of Songdsplays':
    ''' Return a list of all songs played n or more times (as songdisplays)
    '''
    result = []
    for a in C:
        for s in a.songs:
            if s.play_count >= n:
                result.append(Songdisplay(s.title, s.length, s.play_count,
                                          a.artist, a.title, a.year))
    return result

popular = popular_songs2(MUSIC, 10)
for sd in popular:
    Songdisplay_print(sd) # Have song and album info# ICS 31, 5-10-16
