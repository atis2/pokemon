from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   
        self.hp = 100
        self.power = randint(10,20)
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.type = self.get_type()
        self.lve = 0
        self.food = 5
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/121.png"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name} hp {self.hp} , ego level {self.lve}, type your pokemon {self.type}" 

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    

    def get_type(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(data["types"])
            tmp = ""
            for i in data["types"]:
                tmp += i ["type"]["name"] + " "
            return (tmp)
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/121.png"
    
    def fight(self , enemy):
        enemy.hp -= self.power
        if enemy.hp <= 0 :
            return f"Pokemon {enemy.name}  lose"
        else:
            return f"Mi atakovli i u vroga ostalos {enemy.hp} hp , sila ataki {self.power}"  

    def korm_pokem(self):
            self.lve += self.food / 5
            if self.hp < 100:
                self.hp += self.food * 5
            return f"Имя твоего покеомона: {self.name} hp {self.hp}, ti ego pokormil na {self.food} i level {self.lve}"


class Fighter(Pokemon):
    def info(self):
        return f"Имя твоего покеомона: {self.name} hp {self.hp}, ego level {self.lve}, type your pokemon {self.type}, vas  pokemon boets" 
    

    def fight(self , enemy):
        enemy.hp -= self.power * 2 
        if enemy.hp <= 0 :
            return f"Pokemon {enemy.name}  lose"
        else:
            return f"Mi atakovli i u vroga ostalos {enemy.hp} hp , sila ataki {self.power}"  
    
    

class Wizard(Pokemon):
    def info(self):
        return f"Имя твоего покеомона: {self.name} hp {self.hp} , ego level {self.lve}, type your pokemon {self.type}, vas pokemon mag" 
    

    def fight(self , enemy):
        enemy.hp -= self.power 
        sobitie = randint(1,3)
        if enemy.hp <= 0 :
            return f"Pokemon {enemy.name}  lose"
        if sobitie == 2:
            enemy.hp -= self.power * 0.5
            return f"Ataka ulucena ,u vroga ostalos {enemy.hp} hp , sila ataki {self.power}"
        elif sobitie == 3:
            self.hp -= randint(1,10)
            return f"vi ne pravilno atakavali {self.hp} ,u vroga ostalos {enemy.hp} hp , sila ataki {self.power}"
        else:
            return f"Mi atakovli i u vroga ostalos {enemy.hp} hp , sila ataki {self.power}"


    

