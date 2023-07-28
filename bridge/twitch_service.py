"""
    First child class from service
"""
from data import generate_id
from service import Service

class TwitchStream(Service):
    
    def start_stream(self):
        stream_reference = generate_id(10)

        print("Start stream %s en twitch" % stream_reference)

        return stream_reference

    def fill_buffer(self, stream_reference):
        
        buffer = self.retrieve_buffer_data()

        print("Estos devices %s estan enviandos datos a tu stream %s en twitch" % (buffer, stream_reference))

    def stop_stream(self, stream_reference):
        print('Cerrando stream %s en twitch' % stream_reference)
        self.devices.clear()
