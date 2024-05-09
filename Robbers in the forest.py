import random
from phrases import phrases
class Player:
    def __init__(self, name):
        self.experience = 0
        self.name = name
        self.max_health = 10
        self.health = self.max_health
        self.attack = 3
        self.lvl = 1
    def lvl_up(self):
        if 2 <= self.experience < 5:
            self.lvl = 2
            print('Твой уровень повысился до 2!')
            self.attack = 4
            self.max_health = 12
        elif  5 <= self.experience <= 10:
            self.lvl = 3
            self.attack = 5
            self.max_health = 14
            print('Твой уровень повысился до 3!')
        elif 10 <= self.experience <= 15:
            self.attack = 6
            self.lvl = 4
            self.max_health = 15
            print('Максимальный уровень! Твой уровень повысился до 4!')
        else:
            pass
    def check_max_health(self):
        if self.health > self.max_health:
            self.health = self.max_health
    def leave(self):
        print('Вы решили покинуть бой')
    def get_experience(self, experience):
        self.experience += experience
    def state(self):
        if self.health < 0:
            self.health = 0
        print(f"У вас {self.health} здоровья и {self.attack} урона! Ваш уровень {self.lvl}.")
    def heal(self):
        rh = random.randint(1, 5)
        self.health += rh
        print(f"Вы восстанавливаете {rh} здоровья")
    def check_win(self, experience):
        if experience >= 20:
            print('Вы прошли игру!')
class Enemy:
    def __init__(self):
        self.health = random.randint(1, 10)
        self.attack = random.randint(1, 5)
    def state(self):
        if self.health < 0:
            self.health = 0
        print(f"У него {self.health} здоровья и {self.attack} урона!")



class Game:
    def __init__(self):
        self.player = None
        self.enemy = None


    def start(self):
        player_name = input('Введите имя игрока:')
        player = Player(player_name)
        life = True
        while (life) and (player.experience < 20):
            print(phrases[random.randint(0, len(phrases)-1)])
            enemy = Enemy()
            enemy.state()
            player.state()
            action = ''
            while action != 'драться' and action != 'уйти' and player.experience < 20:
                action = input("Ваши действия: АТАКОВАТЬ или УЙТИ?")
                if action.lower().strip() == 'атаковать':
                    while True:
                        enemy.health -= player.attack
                        player.health -= enemy.attack
                        enemy.state()
                        player.state()
                        if enemy.health <=0 and player.health > 0:
                            exp = random.randint(1, 10)
                            player.get_experience(exp)
                            print(f"Вы победили и заработали {exp} опыта. Ваш суммарный опыт: {player.experience}")
                            player.heal()
                            player.lvl_up()
                            player.check_max_health()
                            break
                        elif player.health <= 0:
                            print("Вы погибли. Игра окончена")
                            life = False
                            break
                        else:
                            action_fight = ''
                            while action_fight.strip() != 'уйти' and action_fight.lower().strip() != 'атаковать':
                                action_fight = input("Бой продолжается. УЙТИ или АТАКОВАТЬ опять?")
                                if action_fight.lower().strip() == 'уйти':
                                    player.leave()
                                    break
                                elif action_fight.lower().strip() == 'атаковать':
                                    continue
                elif action.lower().strip() == 'уйти':
                    print("Вы решили уйти от боя")
                    continue
        player.check_win(player.experience)
if __name__ == "__main__":
    game = Game()
    game.start()










