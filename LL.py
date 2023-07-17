class Song:
    def __init__(self,track,artist,duration):
        self.track=track
        self.artist=artist
        self.duration=duration
        self.next=None
        self.previous=None

    def show(self):
        print("track of the song is",self.track)
        print("artist of the song is",self.artist)
        print("duration of the song is",self.duration)

class Playlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def append(self,Song):
        self.size= self.size+1
        if  self.head==None:
            self.head=Song
            self.tail=Song

        else:
            self.tail.next=Song
            Song.previous=self.tail

            self.tail=Song

            self.head.previous=self.tail
            self.tail.next=self.head

    def iterate(self,direction=0):
        if direction==0:
            temp=self.head
            while True:
                temp.show()
                temp=temp.next

                if temp==self.head:
                    break
                        




            
        
            

        