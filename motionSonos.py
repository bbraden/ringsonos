from soco import SoCo

livingroomSonos = SoCo('192.168.1.16')
gameroomSonos = SoCo('192.168.1.35')
masterbedroomSonos = SoCo('192.168.1.15')
patioSonos = SoCo('192.168.1.14')

def playSound():
    livingroomSonos.volume = 50
    gameroomSonos.volume = 50
    masterbedroomSonos.volume = 50
    patioSonos.volume = 50

    boom = 'https://www.myinstants.com/media/sounds/vine-boom.mp3'
    someonesHere = 'https://www.myinstants.com/media/sounds/someones-here.mp3'
    atDoor = 'https://www.myinstants.com/media/sounds/atthedoor.mp3'
    evermore1 = r'https://www.mboxdrive.com/yt1s.com%20-%20Taylor%20Swift%20%20evermore%20Official%20Lyric%20Video%20ft%20Bon%20Iver.mp3'
    
    
    uri = evermore1

    
    livingroomSonos.play_uri(uri)
    gameroomSonos.play_uri(uri)
    masterbedroomSonos.play_uri(uri)
    patioSonos.play_uri(uri)

    print('Sound Played Across 4 Sonos Devices!')