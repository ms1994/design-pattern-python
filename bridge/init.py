"""
    Como se puede apreciar se utilizo la interface en service para crear un bridge entre dos clases abstractas
    la de camara y service para interactuar entre ellas. En service que es un parent abstract class se definieron
    funciones para manejar con los devices que son una clase para las camaras.
"""


from youtube_service import YoutubeStream
from twitch_service import TwitchStream
from dsl_camara import CamaraDSL
from otra_camara import OtraCamara
if __name__ == '__main__':
    
    # Camara 1
    camara_dsl = CamaraDSL()

    # camara 2
    camara_2 = OtraCamara()
 
    # Iniciamos el servicico de youtube y le pasamos la camara con la cual estamos trabajando
    youtube = YoutubeStream()
    youtube.add_devices(camara_2.get_buffer())
    youtube.add_devices(camara_dsl.get_buffer())

    reference = youtube.start_stream()

    youtube.fill_buffer(reference)

    youtube.stop_stream(reference)

    # Abriendo stream en twitch
    twitch = TwitchStream()
    twitch.add_devices(camara_dsl.get_buffer())
    twitch.add_devices(camara_2.get_buffer())

    reference_id = twitch.start_stream()

    twitch.fill_buffer(reference_id)

    
    twitch.stop_stream(reference_id)

