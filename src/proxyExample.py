from abc import ABC, abstractmethod


class ThirdPartyYouTubeLib(ABC):
    @abstractmethod
    def list_videos(self):
        pass

    @abstractmethod
    def get_video_info(self, video_id):
        pass

    @abstractmethod
    def download_video(self, video_id):
        pass



class ThirdPartyYouTubeClass(ThirdPartyYouTubeLib):
    def list_videos(self):
        print("Conectando a YouTube API para obtener la lista de videos...")
        return ["video1", "video2", "video3"]

    def get_video_info(self, video_id):
        print(f"Obteniendo información del video {video_id} desde YouTube...")
        return {"id": video_id, "title": f"Título de {video_id}", "duration": "5:00"}

    def download_video(self, video_id):
        print(f"Descargando video {video_id} desde YouTube...")


class CachedYouTubeClass(ThirdPartyYouTubeLib):
    def __init__(self, service: ThirdPartyYouTubeLib):
        self._service = service
        self._list_cache = None
        self._video_cache = {}
        self.need_reset = False

    def list_videos(self):
        if self._list_cache is None or self.need_reset:
            print("Caché vacío o reiniciado. Consultando servicio real...")
            self._list_cache = self._service.list_videos()
        else:
            print("Usando lista de videos desde caché.")
        return self._list_cache

    def get_video_info(self, video_id):
        if video_id not in self._video_cache or self.need_reset:
            print(f"Caché vacío para {video_id} o reiniciado. Consultando servicio real...")
            self._video_cache[video_id] = self._service.get_video_info(video_id)
        else:
            print(f"Usando información de {video_id} desde caché.")
        return self._video_cache[video_id]

    def download_video(self, video_id):
        print(f"Verificando si {video_id} ya está descargado...")

        self._service.download_video(video_id)



class YouTubeManager:
    def __init__(self, service: ThirdPartyYouTubeLib):
        self._service = service

    def render_video_page(self, video_id):
        info = self._service.get_video_info(video_id)
        print(f"Renderizando página del video: {info['title']} ({info['duration']})")

    def render_list_panel(self):
        videos = self._service.list_videos()
        print(f"Renderizando lista de videos: {videos}")

    def react_on_user_input(self):
        self.render_list_panel()
        self.render_video_page("video1")



if __name__ == "__main__":
    youtube_service = ThirdPartyYouTubeClass()
    youtube_proxy = CachedYouTubeClass(youtube_service)
    manager = YouTubeManager(youtube_proxy)

    print("=== Primera llamada ===")
    manager.react_on_user_input()

    print("\n=== Segunda llamada (debería usar caché) ===")
    manager.react_on_user_input()
