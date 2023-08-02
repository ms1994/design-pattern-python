"""
    Factory permite separar la creacion de objetos del uso, te ayuda a crear objetos relacionados de una misma familia
    en este caso objetos referentes a la calidad de un video, con su respectivo tipo de audio.

    Con esto podemos separar los codigos y tener toda una familia de tipos de objetos separados por fabrica
    como el pdf object en el saas.

    Concrete class devuelve el objeto a usar, el export_factory esta el interface (parent class) de la factoria
    para hacer los videos

"""

from concrete_factory import HighQualityExport, MasterQualityExport, FastExport

def read_input():
    """
        Funcion aux que lee el input del usuario, y devulve un objeto desde la factoria especificada por el usuario
    """

    factories = {
        'low': FastExport(),
        'high': HighQualityExport(),
        'master': MasterQualityExport()
    }

    while(True):
        export_quality = input("Choose a quality for you video export (Options are low, high, master)")

        if export_quality.lower() in factories:
            return factories[export_quality]
        else:
            print("Options are low, high, master")


def main():

    fac = read_input()

    # Factories return a instance for video and audio
    video_export = fac.get_video_export()
    audio_export = fac.get_audio_export()

    # Prepare export for the video and audio
    video_export.prepare_export("Some data or input in the buffer")
    audio_export.prepare_export("Some data for the audio input buffer")

    # do the export to a specific folder
    folder = 'some folder path'
    video_export.do_export(folder)
    audio_export.do_export(folder)


if __name__ == '__main__':
    main()