
class VideoFile:
    def __init__(self, filename):
        self.filename = filename
        print(f"[VideoFile] Archivo de video cargado: {filename}")


class OggCompressionCodec:
    def __str__(self):
        return "Códec OGG"


class MPEG4CompressionCodec:
    def __str__(self):
        return "Códec MPEG4"


class CodecFactory:
    def extract(self, file: VideoFile):
        print(f"[CodecFactory] Extrayendo códec del archivo {file.filename}")
        return OggCompressionCodec() if file.filename.endswith(".ogg") else MPEG4CompressionCodec()


class BitrateReader:
    @staticmethod
    def read(filename, codec):
        print(f"[BitrateReader] Leyendo {filename} usando {codec}")
        return f"Datos de {filename} en formato {codec}"

    @staticmethod
    def convert(buffer, codec):
        print(f"[BitrateReader] Convirtiendo datos a {codec}")
        return f"Datos convertidos a {codec}"


class AudioMixer:
    def fix(self, result):
        print("[AudioMixer] Ajustando y mezclando el audio")
        return f"{result} con audio ajustado"


class VideoConverter:
    def convert(self, filename, format):
        file = VideoFile(filename)
        source_codec = CodecFactory().extract(file)

        if format == "mp4":
            destination_codec = MPEG4CompressionCodec()
        else:
            destination_codec = OggCompressionCodec()

        buffer = BitrateReader.read(filename, source_codec)
        result = BitrateReader.convert(buffer, destination_codec)
        result = AudioMixer().fix(result)

        return ConvertedFile(result)



class ConvertedFile:
    def __init__(self, data):
        self.data = data

    def save(self, output_name="output_file"):
        print(f"[ConvertedFile] Guardando archivo convertido como {output_name}")



if __name__ == "__main__":
    converter = VideoConverter()
    mp4_file = converter.convert("funny-cats-video.ogg", "mp4")
    mp4_file.save("funny-cats-video.mp4")
