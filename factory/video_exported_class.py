from video_interface import VideoExport

class LossLessVideoExport(VideoExport):
    """
        Video exported de tipo loss less
    """

    def prepare_export(self, video_data):
        print("Preparing video data for lossless export.")

    def do_export(self, folder):
        print("Export video en format lossless in folder %s" % folder)


class H264BPVideoExport(VideoExport):
    """
        Video exported de tipo H264BP
    """

    def prepare_export(self, video_data):
        print("Preparing video data for H264BP export.")

    def do_export(self, folder):
        print("Export video en format H264BP in folder %s" % folder)

class H264Hi422PVideoExport(VideoExport):
    """
        Video exported de tipo H264Hi422P
    """

    def prepare_export(self, video_data):
        print("Preparing video data for H264Hi422P export.")

    def do_export(self, folder):
        print("Export video en format H264Hi422P in folder %s" % folder)