from abc import ABC, abstractmethod


class AudioExported(ABC):
    """
        Interface para manejar el audio export
    """
    
    @abstractmethod
    def prepare_export(self, audio_data):
        """
            Preparar los datos del audio para exportar
        """

    @abstractmethod
    def do_export(self, folder):
        """
            Export the audio data to a folder
        """