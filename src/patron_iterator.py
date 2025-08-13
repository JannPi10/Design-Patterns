from abc import ABC, abstractmethod
from typing import List, Optional



class SocialNetwork(ABC):
    """Interfaz de la colección."""
    
    @abstractmethod
    def create_friends_iterator(self, profile_id: str):
        pass

    @abstractmethod
    def create_coworkers_iterator(self, profile_id: str):
        pass


class ProfileIterator(ABC):
    """Interfaz común para todos los iteradores."""
    
    @abstractmethod
    def get_next(self):
        pass

    @abstractmethod
    def has_more(self) -> bool:
        pass



class Profile:
    """Representa un perfil en la red social."""
    
    def __init__(self, profile_id: str, email: str):
        self.profile_id = profile_id
        self.email = email

    def get_id(self):
        return self.profile_id

    def get_email(self):
        return self.email



class Facebook(SocialNetwork):
    """Colección concreta."""
    
    def __init__(self):
        self.data = {
            "1": {
                "friends": [Profile("2", "amigo1@example.com"), Profile("3", "amigo2@example.com")],
                "coworkers": [Profile("4", "compa1@example.com")]
            }
        }

    def social_graph_request(self, profile_id: str, type_: str) -> List[Profile]:
        return self.data.get(profile_id, {}).get(type_, [])

    def create_friends_iterator(self, profile_id: str):
        return FacebookIterator(self, profile_id, "friends")

    def create_coworkers_iterator(self, profile_id: str):
        return FacebookIterator(self, profile_id, "coworkers")


class FacebookIterator(ProfileIterator):
    """Iterador concreto."""
    
    def __init__(self, facebook: Facebook, profile_id: str, type_: str):
        self.facebook = facebook
        self.profile_id = profile_id
        self.type = type_
        self.current_position = 0
        self.cache: Optional[List[Profile]] = None

    def lazy_init(self):
        if self.cache is None:
            self.cache = self.facebook.social_graph_request(self.profile_id, self.type)

    def get_next(self):
        if self.has_more():
            result = self.cache[self.current_position]
            self.current_position += 1
            return result

    def has_more(self) -> bool:
        self.lazy_init()
        return self.current_position < len(self.cache)



class SocialSpammer:
    def send(self, iterator: ProfileIterator, message: str):
        while iterator.has_more():
            profile = iterator.get_next()
            print(f"Enviando email a {profile.get_email()} -> {message}")


class Application:
    def __init__(self):
        self.network: Optional[SocialNetwork] = None
        self.spammer: Optional[SocialSpammer] = None

    def config(self, network_type: str):
        if network_type.lower() == "facebook":
            self.network = Facebook()
        self.spammer = SocialSpammer()

    def send_spam_to_friends(self, profile: Profile):
        iterator = self.network.create_friends_iterator(profile.get_id())
        self.spammer.send(iterator, "Mensaje muy importante para amigos")

    def send_spam_to_coworkers(self, profile: Profile):
        iterator = self.network.create_coworkers_iterator(profile.get_id())
        self.spammer.send(iterator, "Mensaje muy importante para compañeros")


if __name__ == "__main__":
    app = Application()
    app.config("facebook")

    my_profile = Profile("1", "yo@example.com")
    app.send_spam_to_friends(my_profile)
    app.send_spam_to_coworkers(my_profile)
