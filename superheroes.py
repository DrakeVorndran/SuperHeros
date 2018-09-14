from random import randint

class Hero:
    def __init__(self, name):
        self.name = name
        self.abilities = list()

    def add_ability(self, ability):
        self.abilities.append(ability)
        #add ablility to ablility list

    def attack(self):
        attack_total = 0
        for x in self.abilities:
            attack_total+=x.attack()
        return attack_total
        #run attack() on every ability hero has

    def display(self):
        print("HERO: "+self.name)
        ability_names = []
        for ability in self.abilities:
            ability_names.append(ability.name)
        print("Abilities - "+", ".join(ability_names))


class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        return randint(self.attack_strength // 2, self.attack_strength)

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength
        #update attack val


class Team:
    def __init__(self, team_name):
        """Init resourses."""
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def remove_hero(self, name):
        hero_removed = False
        for i in range(len(self.heroes)):
            if heroes[x].name==name:
                heroes.pop(x)
                hero_removed=True
            if(not hero_removed):
                return 0
    def find_hero(self, name):
        for i in range(len(self.heroes)):
            if self.heroes[i].name==name:
                return self.heroes[i]

    def view_all_heroes(self):
        for hero in self.heroes:
            hero.display();




class Weapon(Ability):
    def attack(self):
        return randint(0, self.attack_strength)

if __name__=="__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Devine Speed",300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
    weapon = Weapon("CrossBow",600)
    hero.add_ability(weapon)
    print(hero.attack())
    team = Team("avengers")
    team.add_hero(hero)
    team.view_all_heroes()
    print(team.find_hero("Wonder Woman"))
    print(team.find_hero("apples"))
