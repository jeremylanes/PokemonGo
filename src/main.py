import json
from dataclasses import dataclass
from typing import Union

from fastapi import FastAPI

# Open json file

with open("../pokemons.json", "r") as f:
    pokemons = json.load(f)

# pokemon list
# print(list(enumerate(pokemons)))
pokemons_list = {k+1: v for k, v in enumerate(pokemons)}


# ------ pokemon class ------
@dataclass
class Pokemon:
    id: int
    name: str
    types: list[str]
    total: int
    hp: int
    attack: int
    defense: int
    attack_special: int
    defense_special: int
    speed: int
    evolution_id: Union[int, None] = None


# ------ app ------
app = FastAPI()

