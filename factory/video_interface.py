from abc import ABC, abstractmethod

class VideoExport(ABC):
    """
        Representacion del interface para exportar video de distinta calidad de audio y video
    """

    @abstractmethod
    def prepare_export(self, video_data):
        """
            Preparar los datos del video para exportar
        """

    @abstractmethod
    def do_export(self, folder):
        """
            Export the video data to a folder
        """