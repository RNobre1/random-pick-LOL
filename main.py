# importar o App, Builder (GUI)
# # criar o nosso aplicativo
# # criar a função build

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
import requests
import random

GUI = Builder.load_file("tela.kv")


class MeuAplicativo(App):
    def build(self):
        return GUI
    
    
    def on_start(self):
        lane = ["Top", "Adc", "Mid", "Sup", "Jungle"]
        builds = ["Tank", "AD", "AP", "OFF-TANK", "Crítico", "Attack Speed"]
        spells = ["ignite", "smite", "shield", "ghost", "heal", "flash", "exhaust"]
        runes = [
                    "Glacial", "First_Strike", "Lethal_Tempo", "Kraken", "Aftershock", "Grasp", "Fleet_Footwork",
                    "Conqueror", "Phase_Rush", "Aery", "Electrocute"
                ]
        
        champs = [
                    "Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Annie", "Ashe", 
                    "Aurelion Sol", "Blitz", "Brand", "Braum", "Caitlyn", "Camille", "Corki", 
                    "Darius", "Diana", "Draven", "Ekko", "Evelynn", "Ez", "Fiora", "Fizz", 
                    "Galio", "Garen", "Gragas", "Graves", "Gwen", "Irelia", "Janna", "Jarvan", 
                    "Jax", "Jayce", "Jhin", "Jinx", "Kaisa", "Karma", "Kassadin", "Katarina", 
                    "Kayle", "Kayn", "Kennen", "KhaZix", "Leesin", "Leona", "Lillia", "Lucian", 
                    "Lulu", "Lux", "Malphite", "Master", "MF", "Morgana", "Mundo", "Nami", 
                    "Nasus", "Nautilus", "Nilah", "Nunu", "Olaf", "Orianna", 
                    "Ornn", "Pantheon", "Pyke", "Rakan", "Rammus", "Renekton", "Rengar", 
                    "Riven", "Samira", "Senna", "Seraphine", "Sett", "Shen", "Shyvana", 
                    "Singed", "Sion", "Sona", "Soraka", "Swain", "Teemo", "TF", "Thresh", 
                    "Tristana", "Trynda", "Twitch", "Urgot", "Varus", "Vayne", "Veigar", 
                    "Vex", "Vi", "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", 
                    "Xinzhao", "Yasuo", "Yone", "Yuumi", "Zed", "Zeri", "Ziggs", "Zoe"
                ]

        
        spell_samples = random.sample(spells, 2)
        spell_1 = spell_samples[0]
        spell_2 = spell_samples[1]

        self.root.ids["champ"].source = f"champs/{random.choice(champs)}.jpg"
        self.root.ids["lane"].source = f"lanes/{random.choice(lane)}.jpg"
        self.root.ids["rune"].source = f"runes/{random.choice(runes)}.jpg"
        self.root.ids["build"].text = f"{random.choice(builds)}"
        self.root.ids["spell_1"].source = f"spells/{spell_1}.jpg"
        self.root.ids["spell_2"].source = f"spells/{spell_2}.jpg"

MeuAplicativo().run()