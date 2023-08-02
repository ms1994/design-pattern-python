"""
    Los concrete factory son las que devuelven el objeto como tal, haciendo uso de las funciones de la clase padre
    factoryInterface
"""
from video_exported_class import H264BPVideoExport, H264Hi422PVideoExport, LossLessVideoExport
from export_factory import ExportFactory
from audio_exported_class import AACAudioExport, WAVAudioExport

class FastExport(ExportFactory):
    """
        Clase que devuelve una instancia de un tipo de formato con video de baja calidad y audio de baja calidad
    """

    def get_video_export(self):
        return H264BPVideoExport()

    def get_audio_export(self):
        return AACAudioExport()


class HighQualityExport(ExportFactory):
    """
        Clase que devuelve una instancia de un tipo de formato con video de alta calidad y audio de baja calidad
    """

    def get_video_export(self):
        return H264Hi422PVideoExport()

    def get_audio_export(self):
        return AACAudioExport()

class MasterQualityExport(ExportFactory):
    """
        Clase que devuelve una instancia de un tipo de formato con video de alta calidad y audio de alta calidad
    """

    def get_video_export(self):
        return LossLessVideoExport()

    def get_audio_export(self):
        return WAVAudioExport()