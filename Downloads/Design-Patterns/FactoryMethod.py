from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class PDFDocument(Document):
    def render(self) -> str:
        return "Rendering PDF Document"


class WordDocument(Document):
    def render(self) -> str:
        return "Rendering Word Document"


class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        pass

    def render_document(self) -> str:
        document = self.create_document()
        return document.render()


class PDFCreator(DocumentCreator):
    def create_document(self) -> Document:
        return PDFDocument()


class WordCreator(DocumentCreator):
    def create_document(self) -> Document:
        return WordDocument()


if __name__ == "__main__":
    creator: DocumentCreator = PDFCreator()
    print(creator.render_document())

    creator = WordCreator()
    print(creator.render_document())
