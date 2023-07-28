"""
    First child class from service
"""
from data import generate_id
from service import Service

class YoutubeStream(Service):
    
    def start_stream(self):
        stream_reference = generate_id(10)

        print("Start stream %s en youtube" % stream_reference)

        return stream_reference

    def fill_buffer(self, stream_reference):
        
        buffer = self.retrieve_buffer_data()

        for buf in buffer:

            print("Estos devices %s estan enviandos datos a tu stream %s en youtube" % (buf, stream_reference))

    def stop_stream(self, stream_reference):
        print('Cerrando stream %s en youtube' % stream_reference)
        
        
        