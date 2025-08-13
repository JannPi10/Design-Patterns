from abc import ABC, abstractmethod


class GameAI(ABC):
    def turn(self):
        self.collect_resources()
        self.build_structures()
        self.build_units()
        self.attack()

    def collect_resources(self):
        for structure in getattr(self, "built_structures", []):
            structure.collect()

    @abstractmethod
    def build_structures(self):
        pass

    @abstractmethod
    def build_units(self):
        pass

    def attack(self):
        enemy = self.closest_enemy()
        if enemy is None:
            self.send_scouts("map_center")
        else:
            self.send_warriors(enemy["position"])

    @abstractmethod
    def send_scouts(self, position):
        pass

    @abstractmethod
    def send_warriors(self, position):
        pass

    def closest_enemy(self):
        return {"position": "enemy_base"}


class OrcsAI(GameAI):
    def __init__(self):
        self.resources = 100
        self.scouts = []
        self.warriors = []
        self.built_structures = []

    def build_structures(self):
        if self.resources >= 30:
            print("Orcos: Construyendo granja...")
            self.built_structures.append("Granja")
        if self.resources >= 60:
            print("Orcos: Construyendo cuartel...")
            self.built_structures.append("Cuartel")
        if self.resources >= 90:
            print("Orcos: Construyendo fortaleza...")
            self.built_structures.append("Fortaleza")

    def build_units(self):
        if self.resources >= 20:
            if not self.scouts:
                print("Orcos: Creando peón (scout)...")
                self.scouts.append("Peón")
            else:
                print("Orcos: Creando soldado...")
                self.warriors.append("Soldado")

    def send_scouts(self, position):
        if self.scouts:
            print(f"Orcos: Enviando exploradores a {position}")

    def send_warriors(self, position):
        if len(self.warriors) > 5:
            print(f"Orcos: Enviando guerreros a {position}")
        else:
            print("Orcos: No hay suficientes guerreros para atacar")


class MonstersAI(GameAI):
    def build_structures(self):
        print("Monstruos: No construyen estructuras.")

    def build_units(self):
        print("Monstruos: No construyen unidades.")

    def collect_resources(self):
        print("Monstruos: No recolectan recursos.")

    def send_scouts(self, position):
        print(f"Monstruos: Enviando monstruos pequeños a explorar {position}")

    def send_warriors(self, position):
        print(f"Monstruos: Enviando monstruos grandes a atacar {position}")


def main():
    print("=== TURNO DE LOS ORCOS ===")
    orcs = OrcsAI()
    orcs.turn()

    print("\n=== TURNO DE LOS MONSTRUOS ===")
    monsters = MonstersAI()
    monsters.turn()


if __name__ == "__main__":
    main()
