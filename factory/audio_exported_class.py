from audio_interface import AudioExported

class AACAudioExport(AudioExported):
    """
        Clase para manejar los audios de tipo AAC
    """

    def prepare_export(self, audio_data):
        print("Preparing audio data to export in format AAC")

    def do_export(self, folder):
        print("Exporting the audio in format AAC to the folder %s" % folder)


class WAVAudioExport(AudioExported):
    """
        Clase para manejar los audios de tipo WAV
    """

    def prepare_export(self, audio_data):
        print("Preparing audio data to export in format WAV")

    def do_export(self, folder):
        print("Exporting the audio in format WAV to the folder %s" % folder)