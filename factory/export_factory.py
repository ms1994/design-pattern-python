from abc import ABC, abstractmethod

class ExportFactory(ABC):
    """
        Interface para las factorias que representa una familia de clases que combina el audio y el video
        de distintos tipos.

        La factoria no mantiene una referencia a estos objetos, solo los devuelve como productos terminados.
    """

    def get_video_export(self):
        """
            Devuelve una instancia a un tipo de video (class VideoExport)
        """

    
    def get_audio_export(self):
        """
            Devuelve una instancia a un tipo de audio (class AudioExport)
        """