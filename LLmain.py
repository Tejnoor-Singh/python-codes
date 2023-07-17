from LL import Song,Playlist
def main():
    play_list=Playlist()
    print(play_list,vars(play_list))

    song1=Song(track="1. Udd Jaa Kaale Kaava", artist="Udit Narayan, Alka Yagnik", duration=4.48)
    play_list.append(Song=song1)

    song2 = Song(track="2. Gustakhiyan", artist="Gurnam Bhullar", duration=3.5)
    play_list.append(Song=song2)

    song3=Song(track="3. Desperado", artist="Raghav, Tesher", duration=5.6)
    play_list.append(Song=song3)

    song4=Song(track="4. Chorni", artist="DIVINE, Sidhu Moose Wala", duration=4.12)
    play_list.append(Song=song4)

    play_list.iterate()

if __name__=="__main__":
    main() 
