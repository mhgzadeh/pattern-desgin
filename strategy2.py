from abc import ABC, abstractmethod

ALLOWED_EXTENSIONS = ['html', 'csv', 'mp3', 'mp4', 'txt']


class AbstractRenderer(ABC):
    @abstractmethod
    def render(self):
        pass


class HTMLRenderer(AbstractRenderer):
    def render(self):
        print("Render using HTMLRemderer.")


class Mp4Renderer(AbstractRenderer):
    def render(self):
        print("Render mp3 streamer.")


class Mp3Renderer(AbstractRenderer):
    def render(self):
        print("Render mp4 streamer.")


class FileHandler:
    created_files = list()

    def __init__(self, filename):
        self.filename = filename

    @property
    def extension(self):
        return self.filename.split('.')[-1]

    @classmethod
    def create(cls, filename):
        if filename.split('.')[-1] not in ALLOWED_EXTENSIONS:
            print(f"{filename}: Not accepted")
            return False
        print(f"{filename}: Accepted successfully.")
        FileHandler.created_files.append(filename)
        return cls(filename)

    def render(self):
        handler_dict = {
            "html": HTMLRenderer,
            'mp3': Mp3Renderer,
            'mp4': Mp4Renderer
        }
        handler = handler_dict[self.extension]
        return handler().render()


if __name__ == "__main__":
    f1 = FileHandler.create('doc.pdf')
    f2 = FileHandler.create('doc.html')
    f3 = FileHandler.create('doc.mp2')
    f4 = FileHandler.create('doc.mp4')

    for file_name in FileHandler.created_files:
        FileHandler(file_name).render()
