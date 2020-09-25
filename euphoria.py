import pygame as pg
import library as lib


class Texts(pg.sprite.Sprite):
    def __init__(self, text_position, screen, text, text_size, typography=4, color=lib.cts.WHITE):
        super(Texts, self).__init__()

        # Text
        self.txt = lib.write(text, text_size, typography, color)
        self.screen = screen

        # Position
        self.x, self.y = text_position
        self.velocity = [0, -1]
        self.limit = text_size

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.screen.blit(self.txt, [self.x, self.y])


class Things(pg.sprite.Sprite):
    def __init__(self, position, selected_thing):
        super(Things, self).__init__()

        # Images
        self.thing = selected_thing
        self.image = lib.cts.Tree
        self.change_image()

        # Position issues
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.thing_velocity = [0, 0]

    def change_image(self):
        if self.thing == 1:
            self.image = lib.cts.Room_limit_1
        elif self.thing == 2:
            self.image = lib.cts.Room_limit_2
        elif self.thing == 3:
            self.image = lib.cts.Bed
        elif self.thing == 4:
            self.image = lib.cts.Decoration_1
        elif self.thing == 5:
            self.image = lib.cts.Decoration_2
        elif self.thing == 6:
            self.image = lib.cts.Decoration_3
        elif self.thing == 7:
            self.image = lib.cts.Decoration_4
        elif self.thing == 8:
            self.image = lib.cts.Decoration_5
        elif self.thing == 9:
            self.image = lib.cts.Nightstand_1
        elif self.thing == 10:
            self.image = lib.cts.Nightstand_2
        elif self.thing == 11:
            self.image = lib.cts.Chair_e
        elif self.thing == 12:
            self.image = lib.cts.Chair_n
        elif self.thing == 13:
            self.image = lib.cts.Chair_s
        elif self.thing == 14:
            self.image = lib.cts.Chair_w
        elif self.thing == 15:
            self.image = lib.cts.Table
        elif self.thing == 16:
            self.image = lib.cts.Tree
        elif self.thing == 17:
            self.image = lib.cts.Bush
        elif self.thing == 18:
            self.image = lib.cts.Plant_2
        elif self.thing == 19:
            self.image = lib.cts.Plant_1
        elif self.thing == 20:
            self.image = lib.cts.Flower
        elif self.thing == 21:
            self.image = lib.cts.Player_house
        elif self.thing == 22:
            self.image = lib.cts.NPC_House_1
        elif self.thing == 23:
            self.image = lib.cts.NPC_House_2
        elif self.thing == 24:
            self.image = lib.cts.NPC_House_3
        elif self.thing == 25:
            self.image = lib.cts.NPC_House_4
        elif self.thing == 26:
            self.image = lib.cts.NPC_shop
        elif self.thing == 27:
            self.image = lib.cts.Portal

    def update(self):
        self.rect.x += self.thing_velocity[0]
        self.rect.y += self.thing_velocity[1]


class Items(pg.sprite.Sprite):
    def __init__(self, position, item):
        super(Items, self).__init__()

        # Sprites
        self.image = lib.cts.Apple
        self.item = item
        self.change_image()

        # Position
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]

        # Id
        self.item_number = 0

    def change_image(self):
        if self.item == 1:
            self.image = lib.cts.Apple
        elif self.item == 2:
            self.image = lib.cts.Ring_1
        elif self.item == 3:
            self.image = lib.cts.Ring_2
        elif self.item == 4:
            self.image = lib.cts.Ring_3
        elif self.item == 5:
            self.image = lib.cts.Ring_4
        elif self.item == 6:
            self.image = lib.cts.Ring_5
        elif self.item == 7:
            self.image = lib.cts.Ring_6
        elif self.item == 8:
            self.image = lib.cts.Bear_1
        elif self.item == 9:
            self.image = lib.cts.Bear_2
        elif self.item == 10:
            self.image = lib.cts.Bear_3
        elif self.item == 11:
            self.image = lib.cts.Chest_0
        elif self.item == 12:
            self.image = lib.cts.Chest_1
        elif self.item == 13:
            self.image = lib.cts.Chest_2
        elif self.item == 14:
            self.image = lib.cts.Chest_3
        elif self.item == 15:
            self.image = lib.cts.Chest_4
        elif self.item == 16:
            self.image = lib.cts.Chest_5
        elif self.item == 17:
            self.image = lib.cts.Helmet_0
        elif self.item == 18:
            self.image = lib.cts.Helmet_1
        elif self.item == 19:
            self.image = lib.cts.Helmet_2
        elif self.item == 20:
            self.image = lib.cts.Helmet_3
        elif self.item == 21:
            self.image = lib.cts.Helmet_4
        elif self.item == 22:
            self.image = lib.cts.Helmet_5
        elif self.item == 23:
            self.image = lib.cts.Shield_0
        elif self.item == 24:
            self.image = lib.cts.Shield_1
        elif self.item == 25:
            self.image = lib.cts.Shield_2
        elif self.item == 26:
            self.image = lib.cts.Shield_3
        elif self.item == 27:
            self.image = lib.cts.Shield_4
        elif self.item == 28:
            self.image = lib.cts.Shield_5
        elif self.item == 29:
            self.image = lib.cts.Sword_0
        elif self.item == 30:
            self.image = lib.cts.Sword_1
        elif self.item == 31:
            self.image = lib.cts.Sword_2
        elif self.item == 32:
            self.image = lib.cts.Sword_3
        elif self.item == 33:
            self.image = lib.cts.Sword_4
        elif self.item == 34:
            self.image = lib.cts.Sword_5
        elif self.item == 35:
            self.image = lib.cts.Necklace

    def take_item(self):
        return self.item_number

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


class Buffs(pg.sprite.Sprite):
    def __init__(self, position, buff):
        super(Buffs, self).__init__()

        # Settings
        self.radio = 10

        # Sprites
        self.image = lib.cts.Extra_life
        self.buff = buff
        self.change_image()

        # Position
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]

    def change_image(self):
        if self.buff == 1:
            self.image = lib.cts.Extra_life
        elif self.buff == 2:
            self.image = lib.cts.Extra_energy
        elif self.buff == 3:
            self.image = lib.cts.Drake_smash
        elif self.buff == 4:
            self.image = lib.cts.Wings
        elif self.buff == 5:
            self.image = lib.cts.Coffee

    def get_buff(self):
        return self.image

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


class Generator(pg.sprite.Sprite):
    def __init__(self, position):
        super(Generator, self).__init__()

        self.image = lib.cts.Hole
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]

        self.temp = 60

    def update(self):
        self.temp -= 1
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


class GeneratedEnemy(pg.sprite.Sprite):
    def __init__(self, position, sprite_sets):
        super(GeneratedEnemy, self).__init__()

        # Settings
        self.current_animation = 1
        self.current_direction = 0

        # Setting sprites sets
        self.angle = lib.rd.randrange(360)
        self.velocity = [6, 6]

        # Images
        self.set = sprite_sets
        self.image = self.set[self.current_direction][self.current_animation]

        # Position
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def selected(self):
        if self.angle <= 315:
            self.current_direction = 3
        if self.angle <= 225:
            self.current_direction = 2
        if self.angle <= 135:
            self.current_direction = 1
        if self.angle <= 45:
            self.current_direction = 0

    def animate(self):
        self.selected()
        if self.velocity != [0, 0]:
            if self.current_animation < 2:
                self.current_animation += 1
            else:
                self.current_animation = 0
        self.image = self.set[self.current_direction][self.current_animation]

    def update(self, scenario_velocity):
        self.rect.x += self.velocity[0] * lib.mt.cos(lib.mt.radians(self.angle))
        self.rect.y -= self.velocity[1] * lib.mt.sin(lib.mt.radians(self.angle))
        self.rect.x -= scenario_velocity[0]
        self.rect.y += scenario_velocity[1]
        self.animate()


class SimpleEnemy(pg.sprite.Sprite):
    def __init__(self, position, sprite_sets):
        super(SimpleEnemy, self).__init__()

        # Statistics
        self.life = 0
        self.armor = 0
        self.dodge = 0
        self.damage = 0
        self.lose_turn = 0
        self.progressive_damage = 0

        self.enemy_attacks = None

        self.statistics = [1110, 0]

        # Animation
        self.current_animation = 1

        # Enemy images
        self.set = sprite_sets
        self.attacks_set = sprite_sets
        self.change_images()
        self.image = self.set[self.current_animation]

        # Position
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]
        self.radius = 50
        self.angle = 0

    def get_position(self):
        return [self.rect.x, self.rect.y]

    def enemy_attack(self, damage):
        if self.attacks_set == 1:
            chosen = lib.random_range(0, 2)
            if chosen == 0:
                self.damage = 2
                lib.play_music(lib.cts.Snake_Attack)
            if chosen == 1:
                self.progressive_damage += 3
                lib.play_music(lib.cts.Snake_Poison)
            if chosen == 2:
                self.dodge = True

            if self.dodge:
                self.dodge = False
                lib.play_music(lib.cts.Dodge)
            else:
                if self.armor > self.life:
                    self.armor -= damage
                else:
                    self.life -= damage

            attack = lib.write(self.enemy_attacks[chosen], 30, 2)
            return attack
        if self.attacks_set == 2:
            chosen = lib.random_range(0, 2)
            if chosen == 0:
                lib.play_music(lib.cts.Smash)
                self.damage = 4
            if chosen == 1:
                lib.play_music(lib.cts.Growl)
                self.lose_turn = 1
            if chosen == 2:
                lib.play_music(lib.cts.Eating)
                self.life += 1
            if self.armor > self.life:
                self.armor -= damage
            else:
                self.life -= damage

            attack = lib.write(self.enemy_attacks[chosen], 30, 2)
            return attack
        if self.attacks_set == 3:
            chosen = lib.random_range(0, 4)
            if chosen == 0:
                lib.play_music(lib.cts.Magic_Spell)
                self.damage = 4
            if chosen == 1:
                lib.play_music(lib.cts.Amaterasu)
                self.progressive_damage += 2
            if chosen == 2:
                self.dodge = True
                self.life += 1
            if chosen == 3:
                lib.play_music(lib.cts.Magic_Spell)
                self.lose_turn = 1

            if self.dodge:
                lib.play_music(lib.cts.Magic_Shield)
                self.dodge = False
            else:
                if self.armor > self.life:
                    self.armor -= damage
                else:
                    self.life -= damage

            attack = lib.write(self.enemy_attacks[chosen], 30, 2)
            return attack
        if self.attacks_set == 4:
            chosen = lib.random_range(0, 2)
            if chosen == 0:
                lib.play_music(lib.cts.Smash)
                self.damage = 6
            if chosen == 1:
                lib.play_music(lib.cts.Growl)
                self.life += 3
            if chosen == 2:
                lib.play_music(lib.cts.Eating)
                self.life += 6
            if self.armor > self.life:
                self.armor -= damage
            else:
                self.life -= damage

            attack = lib.write(self.enemy_attacks[chosen], 30, 2)
            return attack
        if self.attacks_set == 5:
            chosen = lib.random_range(0, 2)
            if chosen == 0:
                lib.play_music(lib.cts.Smash)
                self.damage = 3
            if chosen == 1:
                lib.play_music(lib.cts.Growl)
                self.armor += 6
                self.life += 6
            if chosen == 2:
                lib.play_music(lib.cts.Eating)
                self.damage = 7
            if self.armor > self.life:
                self.armor -= damage
            else:
                self.life -= damage

            attack = lib.write(self.enemy_attacks[chosen], 30, 2)
            return attack
        if self.attacks_set == 6:
            chosen = lib.random_range(0, 2)
            if chosen == 0:
                lib.play_music(lib.cts.Smash)
                self.armor += 1
            if chosen == 1:
                lib.play_music(lib.cts.Growl)
                self.damage = 2
            if chosen == 2:
                lib.play_music(lib.cts.Eating)
                self.armor += 12
                self.life += 3
            if self.armor > self.life:
                self.armor -= damage
            else:
                self.life -= damage

            attack = lib.write(self.enemy_attacks[chosen], 30, 2)
            return attack

    def change_images(self):
        if self.set == 1:
            self.life = 5
            self.armor = 2
            self.set = lib.cts.Enemy_1
            self.enemy_attacks = lib.cts.Enemy_1_attacks
        elif self.set == 2:
            self.life = 8
            self.armor = 5
            self.set = lib.cts.Enemy_2
            self.enemy_attacks = lib.cts.Enemy_2_attacks
        elif self.set == 3:
            self.life = 12
            self.armor = 7
            self.set = lib.cts.Enemy_3
            self.enemy_attacks = lib.cts.Enemy_3_attacks
        elif self.set == 4:
            self.life = 10
            self.armor = 5
            self.set = lib.cts.Enemy_4
            self.enemy_attacks = lib.cts.Enemy_4_attacks
        elif self.set == 5:
            self.life = 10
            self.armor = 1
            self.set = lib.cts.Enemy_5
            self.enemy_attacks = lib.cts.Enemy_5_attacks
        elif self.set == 6:
            self.life = 5
            self.armor = 10
            self.set = lib.cts.Enemy_6
            self.enemy_attacks = lib.cts.Enemy_6_attacks

    def show_statistics(self, screen):
        screen.blit(lib.cts.HUD_enemy, [1130, 0])

        screen.blit(self.set[2], [1140, 15])

        for _ in range(self.life):
            screen.blit(lib.cts.Hearts, [self.statistics[0], self.statistics[1]])
            self.statistics[1] += 20

        self.statistics = [1130, 55]

        for _ in range(self.armor):
            screen.blit(lib.cts.Armor, [self.statistics[0], self.statistics[1]])
            self.statistics[1] += 20

        self.statistics = [1170, 55]

    def in_combat(self, screen):
        if self.attacks_set == 1:
            screen.blit(self.set[1], [700, 50])
        if self.attacks_set == 2:
            screen.blit(self.set[1], [700, 100])
        if self.attacks_set == 3:
            screen.blit(self.set[1], [600, 200])
        if self.attacks_set == 4:
            screen.blit(self.set[1], [600, 200])
        if self.attacks_set == 5:
            screen.blit(self.set[1], [600, 200])
        if self.attacks_set == 6:
            screen.blit(self.set[1], [700, 100])

    def animate(self):
        if self.velocity != [0, 0]:
            if self.current_animation < 2:
                self.current_animation += 1
            else:
                self.current_animation = 0
        else:
            self.current_animation = 1
        self.image = self.set[0][self.current_animation]

    def update(self, scenario_velocity):
        self.animate()
        self.rect.x += self.velocity[0] * lib.mt.cos(self.angle) - scenario_velocity[0]
        self.rect.y += self.velocity[1] * lib.mt.sin(self.angle) + scenario_velocity[1]


class Boss(pg.sprite.Sprite):
    def __init__(self, position, boss_set=lib.cts.Enemy_3):
        super(Boss, self).__init__()

        # Animation
        self.current_animation = 1

        # Boss images
        self.set = boss_set
        self.image = self.set[0][self.current_animation]

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]
        self.angle = 0

        # Setting
        self.attack = 30
        self.temp = 100
        self.cont = 40

        # Statistics
        self.live = 1

    def get_position(self):
        return [self.rect.x, self.rect.y]

    def animate(self):
        if self.velocity != [0, 0]:
            if self.current_animation < 2:
                self.current_animation += 1
            else:
                self.current_animation = 0
        else:
            self.current_animation = 1
        self.image = self.set[0][self.current_animation]

    def update(self, scenario_velocity):
        self.animate()
        self.rect.x += self.velocity[0] * lib.mt.cos(self.angle)
        self.rect.y += self.velocity[1] * lib.mt.sin(self.angle)
        self.rect.x -= scenario_velocity[0]
        self.rect.y += scenario_velocity[1]


class Attacks_Architect(pg.sprite.Sprite):
    def __init__(self, position):
        super(Attacks_Architect, self).__init__()

        self.image = lib.cts.Bullet

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 80]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


class Attack_Balzar(pg.sprite.Sprite):
    def __init__(self, position):
        super(Attack_Balzar, self).__init__()

        # Bullet creation
        self.image = pg.Surface([10, 10])
        self.image.fill(lib.cts.WHITE)

        #
        self.rect = self.image.get_rect()
        self.velocity = 0
        self.angle = 0

        # Setting
        self.rect.x, self.rect.y = position

    def update(self, scenario_velocity):
        self.rect.x += self.velocity * lib.mt.cos(self.angle)
        self.rect.y += self.velocity * lib.mt.sin(self.angle)
        self.rect.x -= scenario_velocity[0]
        self.rect.y += scenario_velocity[1]


class Attack_God(pg.sprite.Sprite):
    def __init__(self, position):
        super(Attack_God, self).__init__()

        self.image = pg.Surface([10, 10])
        self.image.fill(lib.cts.BLUE)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]
        self.angle = 0

    def update(self):
        self.rect.x += self.velocity[0] * lib.mt.cos(self.angle)
        self.rect.y += self.velocity[1] * lib.mt.sin(self.angle)


class NonPlayableCharacters(pg.sprite.Sprite):
    def __init__(self, position, npc_chosen):
        super(NonPlayableCharacters, self).__init__()

        # Setting
        self.id = None

        # NPC images
        self.image = lib.cts.Manuela
        self.change_image(npc_chosen)

        # Position issues
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.npc_velocity = [0, 0]
        self.radius = 10

    def change_image(self, background):
        if background == 1:
            self.image = lib.cts.Manuela
            self.id = 'Manuela'
        elif background == 2:
            self.image = lib.cts.Balzar
            self.id = 'Balzar'
        elif background == 3:
            self.image = lib.cts.Saku
            self.id = 'Saku'
        elif background == 4:
            self.image = lib.cts.Spidy
            self.id = 'Spidy'
        elif background == 5:
            self.image = lib.cts.Elise
            self.id = 'Elise'
        elif background == 6:
            self.image = lib.cts.Goldi
            self.id = 'Goldi'
        elif background == 7:
            self.image = lib.cts.Helen
            self.id = 'Helen'
        elif background == 8:
            self.image = lib.cts.Marian
            self.id = 'Marian'
        elif background == 9:
            self.image = lib.cts.Clarissa
            self.id = 'Clarissa'
        elif background == 10:
            self.image = lib.cts.Elizabeth
            self.id = 'Elizabeth'

    def update(self):
        self.rect.x += self.npc_velocity[0]
        self.rect.y += self.npc_velocity[1]


class Scenarios(pg.sprite.Sprite):
    def __init__(self, background, screen):
        super(Scenarios, self).__init__()

        self.screen = screen
        self.image = lib.cts.House_1
        self.background = background
        self.change_image()

        self.background_limits = self.image.get_rect()

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = [0, 0]
        self.background_velocity = [0, 0]

        self.screen_limits = [lib.cts.width - 50, lib.cts.height - 50]
        self.background_limits = [(lib.cts.width - self.background_limits[2]),
                                  (lib.cts.height - self.background_limits[3])]

    def change_image(self):
        if self.background == 1:
            self.image = lib.cts.House_1
            self.background_limits = self.image.get_rect()
            self.background_limits = [(lib.cts.width - self.background_limits[2]),
                                      (lib.cts.height - self.background_limits[3])]
        elif self.background == 2:
            self.image = lib.cts.House_2
            self.background_limits = self.image.get_rect()
            self.background_limits = [(lib.cts.width - self.background_limits[2]),
                                      (lib.cts.height - self.background_limits[3])]
        elif self.background == 3:
            self.image = lib.cts.Field_0
            self.background_limits = self.image.get_rect()
            self.background_limits = [(lib.cts.width - self.background_limits[2]),
                                      (lib.cts.height - self.background_limits[3])]
        elif self.background == 4:
            self.image = lib.cts.Field_1
            self.background_limits = self.image.get_rect()
            self.background_limits = [(lib.cts.width - self.background_limits[2]),
                                      (lib.cts.height - self.background_limits[3])]
        elif self.background == 5:
            self.image = lib.cts.Field_2
            self.background_limits = self.image.get_rect()
            self.background_limits = [(lib.cts.width - self.background_limits[2]),
                                      (lib.cts.height - self.background_limits[3])]
        elif self.background == 6:
            self.image = lib.cts.Field_3
            self.background_limits = self.image.get_rect()
            self.background_limits = [(lib.cts.width - self.background_limits[2]),
                                      (lib.cts.height - self.background_limits[3])]
        elif self.background == 7:
            self.image = lib.cts.Field_4
            self.background_limits = self.image.get_rect()
            self.background_limits = [(lib.cts.width - self.background_limits[2]),
                                      (lib.cts.height - self.background_limits[3])]
        elif self.background == 8:
            self.image = lib.cts.Field_5
            self.background_limits = self.image.get_rect()
            self.background_limits = [(lib.cts.width - self.background_limits[2]),
                                      (lib.cts.height - self.background_limits[3])]

    def move_enemies(self, enemy_list):
        for iteration, iterated in enumerate(enemy_list):
            enemy_list[iteration][0] -= self.background_velocity[0]
            enemy_list[iteration][1] += self.background_velocity[1]

        return enemy_list

    def update(self):
        self.rect.x -= self.background_velocity[0]
        self.rect.y += self.background_velocity[1]
        self.screen.blit(self.image, [self.rect.x, self.rect.y])


class Player(pg.sprite.Sprite):
    def __init__(self, position, sprite_sets, collides):
        super(Player, self).__init__()

        # Control
        self.speed = 0
        self.damage = 0
        self.radius = 50
        self.collides = collides
        self.writer = pg.sprite.Group()

        # Statistics

        # Current
        self.live = 0
        self.energy = 0
        self.gold_in_bag = 0
        self.life_list = [0, 0, 0, 0]
        self.armor_list = [0, 0, 0, 0]
        self.energy_list = [0, 0, 0, 0]
        self.damage_list = [0, 0, 0, 0]

        # Player statistics
        self.max_hp = 0
        self.max_gold = 0
        self.max_armor = 0
        self.max_energy = 0
        self.max_buffs_effect = 0

        # Buffs
        self.wings_buff = 0
        self.extra_live = 0
        self.drake_smash = 0
        self.extra_energy = 0

        # Animation
        self.action = 3
        self.current_animation = 1

        # Player images
        self.set = sprite_sets
        self.setting_player()
        self.image = self.set[self.action][self.current_animation]

        # Position
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]

        self.statistics = [125, 10]

        # Items
        self.armor = 0
        self.sword_buffs = 0
        self.hp_ring_buffs = 0
        self.mana_ring_buffs = 0
        self.position_in_sheet = [490, 280]
        self.current_armor = [-1, -1, -1, -1, -1, -1]
        self.inventory = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
                          [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
                          [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
                          [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
                          [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
                          [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

        # In combat
        self.transformation = False

        # Level
        self.level_points = 0
        self.skill_points = 0
        self.current_level = 1

    def setting_player(self):
        if self.set == 1:
            self.set = lib.cts.Luke
            self.life_list = [0, 0, 4, 0]
            self.armor_list = [0, 0, 0, 0]
            self.damage_list = [1, 4, 0, 6]
            self.energy_list = [-1, -3, -5, -3]

            self.max_hp = 8
            self.max_gold = 8
            self.max_armor = 5
            self.max_energy = 8
            self.max_buffs_effect = 1
        elif self.set == 2:
            self.set = lib.cts.Serafin

            self.armor_list = [0, 0, 0, 0]
            self.life_list = [1, 2, -3, -3]
            self.damage_list = [2, 2, 0, 8]
            self.energy_list = [-2, -4, -3, -6]

            self.max_hp = 15
            self.max_gold = 8
            self.max_armor = 5
            self.max_energy = 10
            self.max_buffs_effect = 1
        elif self.set == 3:
            self.set = lib.cts.Sonia

            self.life_list = [0, 0, 0, 0]
            self.armor_list = [0, 0, 0, 0]
            self.damage_list = [5, 4, 0, 5]
            self.energy_list = [-3 + 1, -5 + 2, -5, -1]

            self.max_hp = 8
            self.max_gold = 8
            self.max_armor = 6
            self.max_energy = 15
            self.max_buffs_effect = 1
        elif self.set == 4:
            self.set = lib.cts.Taun

            self.life_list = [0, 0, 0, 10]
            self.damage_list = [1, 7, 0, 0]
            self.armor_list = [1, -2, -3, 0]
            self.energy_list = [-2, -5, -7, -2]

            self.max_hp = 8
            self.max_gold = 8
            self.max_armor = 15
            self.max_energy = 8
            self.max_buffs_effect = 1
        elif self.set == 5:
            self.set = lib.cts.Xerath

            self.life_list = [0, 0, 3, 0]
            self.armor_list = [0, 0, 0, 0]
            self.damage_list = [3, 7, 0, 20]
            self.energy_list = [-2, -4, -8, -10]

            self.max_hp = 6
            self.max_gold = 10
            self.max_armor = 6
            self.max_energy = 12
            self.max_buffs_effect = 1

    def animate(self, key_pressed):
        if self.current_animation < 2 and key_pressed:
            self.current_animation += 1
        else:
            self.current_animation = 1
        self.image = self.set[self.action][self.current_animation]

    def get_position(self):
        return [self.rect.x, self.rect.y]

    def use_extras(self, choose):
        if choose == 1:
            self.extra_live -= 1
            self.live += 5
        if choose == 2:
            self.extra_energy -= 1
            self.energy += 5
        if choose == 3:
            self.drake_smash -= 1

    def in_combat(self, screen):
        if self.transformation:
            screen.blit(self.set[5], [50, 50])
        else:
            screen.blit(self.set[6], [50, 200])

        if self.live > self.max_hp:
            self.live = self.max_hp

        if self.armor > self.max_armor:
            self.armor = self.max_armor

        if self.energy > self.max_energy:
            self.energy = self.max_energy

    def hurts(self, enemy_damage):
        if self.armor > self.live:
            self.armor -= enemy_damage
        else:
            if self.live >= self.armor >= 0:
                self.armor -= 1
                self.live -= enemy_damage

    def attack(self, selected_attack):
        if selected_attack == 1:
            self.energy += self.energy_list[0]
            self.damage = self.damage_list[0]
            self.armor += self.armor_list[0]
            self.live += self.life_list[0]
        elif selected_attack == 2:
            self.energy += self.energy_list[1]
            self.damage = self.damage_list[1]
            self.armor += self.armor_list[1]
            self.live += self.life_list[1]
        elif selected_attack == 3:
            self.energy += self.energy_list[2]
            self.damage = self.damage_list[2]
            self.armor += self.armor_list[2]
            self.live += self.life_list[2]
        elif selected_attack == 4:
            self.energy += self.energy_list[3]
            self.damage = self.damage_list[3]
            self.armor += self.armor_list[3]
            self.live += self.life_list[3]

    def show_statistics(self, screen):

        screen.blit(lib.cts.HUD, [0, 0])

        screen.blit(self.set[8], [5, 15])

        for _ in range(self.max_hp):
            screen.blit(lib.cts.Without_hearts, [self.statistics[0], self.statistics[1]])
            self.statistics[0] += 20

        self.statistics = [55, 0]

        for _ in range(self.live):
            screen.blit(lib.cts.Hearts, [self.statistics[0], self.statistics[1]])
            self.statistics[0] += 20

        self.statistics = [64, 18]

        for _ in range(self.max_energy):
            screen.blit(lib.cts.Without_energy, [self.statistics[0], self.statistics[1]])
            self.statistics[0] += 20

        self.statistics = [64, 18]

        for _ in range(self.energy):
            screen.blit(lib.cts.Energy, [self.statistics[0], self.statistics[1]])
            self.statistics[0] += 20

        self.statistics = [55, 40]

        for _ in range(self.armor):
            screen.blit(lib.cts.Armor, [self.statistics[0], self.statistics[1]])
            self.statistics[0] += 20

        self.statistics = [0, 60]

        for _ in range(self.drake_smash):
            screen.blit(lib.cts.Drake_smash, [self.statistics[0], self.statistics[1]])
            self.statistics[1] += 20

        self.statistics = [25, 60]

        for _ in range(self.extra_live):
            screen.blit(lib.cts.Extra_life, [self.statistics[0], self.statistics[1]])
            self.statistics[1] += 20

        self.statistics = [45, 60]

        for _ in range(self.extra_energy):
            screen.blit(lib.cts.Extra_energy, [self.statistics[0], self.statistics[1]])
            self.statistics[1] += 20

        self.statistics = [65, 60]

        for _ in range(self.wings_buff):
            screen.blit(lib.cts.Wings, [self.statistics[0], self.statistics[1]])
            self.statistics[1] += 20

        self.statistics = [55, 0]

    def add_inventory(self, item):
        added = False
        for new_item in range(len(self.inventory)):
            if self.inventory[new_item][0] == item:
                self.inventory[new_item][1] += 1
                added = True
        if not added:
            for new_item in range(len(self.inventory)):
                if self.inventory[new_item][0] == 0 and not added:
                    self.inventory[new_item][0] = item
                    self.inventory[new_item][1] += 1
                    added = True

    def change_armor(self, armor, item):
        self.current_armor[armor] = item

    def update_armor(self):
        if self.current_armor[0] == 0:
            self.mana_ring_buffs = 0
        elif self.current_armor[0] == 1:
            self.mana_ring_buffs = 0
        elif self.current_armor[0] == 2:
            self.mana_ring_buffs = 0
        elif self.current_armor[0] == 3:
            self.mana_ring_buffs = 0

        if self.current_armor[1] == 0:
            self.armor = 1
        elif self.current_armor[1] == 1:
            self.armor = 2
        elif self.current_armor[1] == 2:
            self.armor = 3
        elif self.current_armor[1] == 3:
            self.armor = 4
        elif self.current_armor[1] == 4:
            self.armor = 5
        elif self.current_armor[1] == 5:
            self.armor = 6

        if self.current_armor[2] == 0:
            self.hp_ring_buffs = 0
        elif self.current_armor[2] == 1:
            self.hp_ring_buffs = 1
        elif self.current_armor[2] == 2:
            self.hp_ring_buffs = 2
        elif self.current_armor[2] == 3:
            self.hp_ring_buffs = 3

        if self.current_armor[3] == 0:
            self.armor += 1
        elif self.current_armor[3] == 1:
            self.armor += 2
        elif self.current_armor[3] == 2:
            self.armor += 3
        elif self.current_armor[3] == 3:
            self.armor += 4
        elif self.current_armor[3] == 4:
            self.armor += 5
        elif self.current_armor[3] == 5:
            self.armor += 6

        if self.current_armor[4] == 0:
            self.armor += 1
        elif self.current_armor[4] == 1:
            self.armor += 2
        elif self.current_armor[4] == 2:
            self.armor += 3
        elif self.current_armor[4] == 3:
            self.armor += 4
        elif self.current_armor[4] == 4:
            self.armor += 5
        elif self.current_armor[4] == 5:
            self.armor += 6

        if self.current_armor[5] == 0:
            self.sword_buffs += 0
        elif self.current_armor[5] == 1:
            self.sword_buffs += 1
        elif self.current_armor[5] == 2:
            self.sword_buffs += 2
        elif self.current_armor[5] == 3:
            self.sword_buffs += 3
        elif self.current_armor[5] == 4:
            self.sword_buffs += 4
        elif self.current_armor[5] == 5:
            self.sword_buffs += 5

    def modify_items(self, inventory_action, item):

        for _ in self.writer:
            self.writer.remove(_)

        inventory_item_position = item[0] + item[1] * 8

        if inventory_action == 1:
            if self.inventory[inventory_item_position][0] == 1:
                self.live += 1
                self.inventory[inventory_item_position][1] -= 1
            if self.inventory[inventory_item_position][0] == 2:
                self.energy += 1
                self.inventory[inventory_item_position][1] -= 1
            if self.inventory[inventory_item_position][0] == 3:
                self.energy += 2
                self.inventory[inventory_item_position][1] -= 1
            if self.inventory[inventory_item_position][0] == 4:
                self.energy += 3
                self.inventory[inventory_item_position][1] -= 1
            if self.inventory[inventory_item_position][0] == 5:
                self.hp_ring_buffs = 1
                self.change_armor(0, 1)
                self.inventory[inventory_item_position][0] = 0
                self.inventory[inventory_item_position][1] -= 1
            if self.inventory[inventory_item_position][0] == 6:
                self.hp_ring_buffs = 2
                self.change_armor(0, 2)
                self.inventory[inventory_item_position][0] = 0
                self.inventory[inventory_item_position][1] -= 1
            if self.inventory[inventory_item_position][0] == 7:
                self.hp_ring_buffs = 3
                self.change_armor(0, 3)
                self.inventory[inventory_item_position][0] = 0
                self.inventory[inventory_item_position][1] -= 1
            if self.inventory[inventory_item_position][0] == 8:
                self.change_armor(2, 1)
                self.mana_ring_buffs = 1
                self.inventory[inventory_item_position][0] = 0
                self.inventory[inventory_item_position][1] -= 1
            if self.inventory[inventory_item_position][0] == 9:
                self.change_armor(2, 2)
                self.mana_ring_buffs = 2
                self.inventory[inventory_item_position][0] = 0
                self.inventory[inventory_item_position][1] -= 1
            if self.inventory[inventory_item_position][0] == 10:
                self.change_armor(2, 3)
                self.mana_ring_buffs = 3
                self.inventory[inventory_item_position][0] = 0
                self.inventory[inventory_item_position][1] -= 1
            if self.inventory[inventory_item_position][0] == 11:
                player.current_armor = [0, 5, 0, 5, 5, 5]
                self.inventory[inventory_item_position][0] = 0
                self.inventory[inventory_item_position][1] -= 1
            if self.inventory[inventory_item_position][0] == 12:
                player.add_inventory(1)
                player.add_inventory(4)
                player.add_inventory(7)
                player.add_inventory(10)
                self.inventory[inventory_item_position][0] = 0
                self.inventory[inventory_item_position][1] -= 1
        if inventory_action == 2:
            self.inventory[inventory_item_position][1] -= 1

        self.update_armor()

    def display_item(self, screen):
        section = 0
        for item, values in self.inventory:
            if section == 8:
                self.position_in_sheet[0] = 490
                self.position_in_sheet[1] += 47
                section = 0

            if item == 1 and values > 0:
                blit = lib.cts.Apple
            elif item == 2 and values > 0:
                blit = lib.cts.Bear_1
            elif item == 3 and values > 0:
                blit = lib.cts.Bear_2
            elif item == 4 and values > 0:
                blit = lib.cts.Bear_3
            elif item == 5 and values > 0:
                blit = lib.cts.Ring_1
            elif item == 6 and values > 0:
                blit = lib.cts.Ring_2
            elif item == 7 and values > 0:
                blit = lib.cts.Ring_3
            elif item == 8 and values > 0:
                blit = lib.cts.Ring_4
            elif item == 9 and values > 0:
                blit = lib.cts.Ring_5
            elif item == 10 and values > 0:
                blit = lib.cts.Ring_6
            elif item == 11 and values > 0:
                blit = lib.cts.Necklace
            elif item == 12 and values > 0:
                blit = lib.cts.Gold_bag
            else:
                blit = lib.cts.Blank

            screen.blit(blit, self.position_in_sheet)
            if item > 0 < values:
                quantity = Texts([self.position_in_sheet[0] + 50, self.position_in_sheet[1] + 25],
                                 screen, str(values), 10, 2)
                quantity.velocity = [0, 0]

                self.writer.add(quantity)

            section += 1

            self.position_in_sheet[0] += 80

        self.position_in_sheet = [490, 280]

    def display_armor(self, screen):
        if self.current_armor[0] == 1:
            screen.blit(lib.cts.Ring_1, [660, 80])
        elif self.current_armor[0] == 2:
            screen.blit(lib.cts.Ring_2, [660, 80])
        elif self.current_armor[0] == 3:
            screen.blit(lib.cts.Ring_3, [660, 80])
        else:
            screen.blit(lib.cts.Blank, [660, 80])

        if self.current_armor[2] == 1:
            screen.blit(lib.cts.Ring_4, [900, 80])
        elif self.current_armor[2] == 2:
            screen.blit(lib.cts.Ring_5, [900, 80])
        elif self.current_armor[2] == 3:
            screen.blit(lib.cts.Ring_6, [900, 80])
        else:
            screen.blit(lib.cts.Blank, [900, 80])

        if self.current_armor[1] == 0:
            screen.blit(lib.cts.Helmet_0, [785, 80])
        elif self.current_armor[1] == 1:
            screen.blit(lib.cts.Helmet_1, [785, 80])
        elif self.current_armor[1] == 2:
            screen.blit(lib.cts.Helmet_2, [785, 80])
        elif self.current_armor[1] == 3:
            screen.blit(lib.cts.Helmet_3, [785, 80])
        elif self.current_armor[1] == 4:
            screen.blit(lib.cts.Helmet_4, [785, 80])
        elif self.current_armor[1] == 5:
            screen.blit(lib.cts.Helmet_5, [785, 80])
        else:
            screen.blit(lib.cts.Blank, [785, 80])

        if self.current_armor[3] == 0:
            screen.blit(lib.cts.Shield_0, [660, 190])
        elif self.current_armor[3] == 1:
            screen.blit(lib.cts.Shield_1, [660, 190])
        elif self.current_armor[3] == 2:
            screen.blit(lib.cts.Shield_2, [660, 190])
        elif self.current_armor[3] == 3:
            screen.blit(lib.cts.Shield_3, [660, 190])
        elif self.current_armor[3] == 4:
            screen.blit(lib.cts.Shield_4, [660, 190])
        elif self.current_armor[3] == 5:
            screen.blit(lib.cts.Shield_5, [660, 190])
        else:
            screen.blit(lib.cts.Blank, [660, 190])

        if self.current_armor[4] == 0:
            screen.blit(lib.cts.Chest_0, [785, 180])
        elif self.current_armor[4] == 1:
            screen.blit(lib.cts.Chest_1, [785, 180])
        elif self.current_armor[4] == 2:
            screen.blit(lib.cts.Chest_2, [785, 180])
        elif self.current_armor[4] == 3:
            screen.blit(lib.cts.Chest_3, [785, 180])
        elif self.current_armor[4] == 4:
            screen.blit(lib.cts.Chest_4, [785, 180])
        elif self.current_armor[4] == 5:
            screen.blit(lib.cts.Chest_5, [785, 180])
        else:
            screen.blit(lib.cts.Blank, [785, 180])

        if self.current_armor[5] == 0:
            screen.blit(lib.cts.Sword_0, [900, 180])
        elif self.current_armor[5] == 1:
            screen.blit(lib.cts.Sword_1, [900, 180])
        elif self.current_armor[5] == 2:
            screen.blit(lib.cts.Sword_2, [900, 180])
        elif self.current_armor[5] == 3:
            screen.blit(lib.cts.Sword_3, [900, 180])
        elif self.current_armor[5] == 4:
            screen.blit(lib.cts.Sword_4, [900, 180])
        elif self.current_armor[5] == 5:
            screen.blit(lib.cts.Sword_5, [900, 180])
        else:
            screen.blit(lib.cts.Blank, [900, 180])

    def show_inventory(self, screen):

        action = 0
        watching = True
        current_item = [485, 280]
        inventory_position = [0, 0]
        self.position_in_sheet = [490, 280]

        for _ in self.writer:
            self.writer.remove(_)

        self.update_armor()

        while watching:
            for player_event in pg.event.get():
                if player_event.type == pg.QUIT:
                    watching = False
                    pg.quit()
                if player_event.type == pg.KEYDOWN:
                    if player_event.key == pg.K_p:
                        watching = False
                    if player_event.key == pg.K_w:
                        current_item[1] -= 46
                        inventory_position[1] -= 1
                    if player_event.key == pg.K_s:
                        current_item[1] += 46
                        inventory_position[1] += 1
                    if player_event.key == pg.K_a:
                        current_item[0] -= 80
                        inventory_position[0] -= 1
                    if player_event.key == pg.K_d:
                        current_item[0] += 80
                        inventory_position[0] += 1

                    if player_event.key == pg.K_e:
                        action = 1
                    if player_event.key == pg.K_q:
                        action = 2

                    if current_item[1] < 280:
                        current_item[1] += 46
                        inventory_position[1] += 1
                    if current_item[0] < 485:
                        current_item[0] += 80
                        inventory_position[0] += 1
                    if current_item[1] > 510:
                        current_item[1] -= 46
                        inventory_position[1] -= 1
                    if current_item[0] > 1045:
                        current_item[0] -= 80
                        inventory_position[0] -= 1

            lib.fill(screen)

            screen.blit(lib.cts.Inventory_background, [0, 0])

            screen.blit(lib.cts.Current_item, current_item)

            screen.blit(self.set[9], [0, 50])

            self.display_item(screen)

            self.display_armor(screen)

            self.writer.update()

            if action > 0:
                self.modify_items(action, inventory_position)
                action = 0

            if action == 1:
                screen.blit(lib.cts.Dialog_box, [400, 400])
            elif action == 2:
                screen.blit(lib.cts.Dialog_box, [400, 400])

            lib.frames_per_second(fps, 1)

    def display_skill(self, screen):
        self.position_in_sheet = [500, 20]

        screen.blit(lib.cts.Hearts_effect, [self.position_in_sheet[0] - 80, self.position_in_sheet[1] + 20])

        for _ in range(self.max_hp):
            screen.blit(lib.cts.Points, self.position_in_sheet)
            self.position_in_sheet[0] += 20

        self.position_in_sheet = [500, 120]

        screen.blit(lib.cts.Energy_effect, [self.position_in_sheet[0] - 80, self.position_in_sheet[1] + 20])

        for _ in range(self.max_energy):
            screen.blit(lib.cts.Points, self.position_in_sheet)
            self.position_in_sheet[0] += 20

        self.position_in_sheet = [500, 220]

        screen.blit(lib.cts.Armor_effect, [self.position_in_sheet[0] - 80, self.position_in_sheet[1] + 20])

        for _ in range(self.max_armor):
            screen.blit(lib.cts.Points, self.position_in_sheet)
            self.position_in_sheet[0] += 20

        self.position_in_sheet = [500, 320]

        screen.blit(lib.cts.Buff_effect, [self.position_in_sheet[0] - 80, self.position_in_sheet[1] + 10])

        for _ in range(self.max_buffs_effect):
            screen.blit(lib.cts.Points, self.position_in_sheet)
            self.position_in_sheet[0] += 20

        self.position_in_sheet = [500, 420]

        screen.blit(lib.cts.Coin_effect, [self.position_in_sheet[0] - 80, self.position_in_sheet[1] + 20])

        for _ in range(self.max_gold):
            screen.blit(lib.cts.Points, self.position_in_sheet)
            self.position_in_sheet[0] += 20

    def upgrade_Skill(self, skill):
        if skill == 1:
            self.max_hp += 1
        elif skill == 2:
            self.max_energy += 1
        elif skill == 3:
            self.max_armor += 1
        elif skill == 4:
            self.max_buffs_effect += 1
        elif skill == 5:
            self.max_gold += 1

    def skill_sheet(self, screen):
        watching = True
        skill_sheet = 1
        current_skill = [1093, 15]

        for _ in self.writer:
            self.writer.remove(_)

        while watching:
            for player_event in pg.event.get():
                if player_event.type == pg.QUIT:
                    watching = False
                    pg.quit()
                if player_event.type == pg.KEYDOWN:
                    if player_event.key == pg.K_i:
                        watching = False
                    if player_event.key == pg.K_w:
                        current_skill[1] -= 100
                        skill_sheet -= 1
                    if player_event.key == pg.K_s:
                        current_skill[1] += 100
                        skill_sheet += 1
                    if player_event.key == pg.K_a:
                        if self.skill_points > 0:
                            self.skill_points -= 1
                            self.upgrade_Skill(skill_sheet)
                    if player_event.key == pg.K_d:
                        if self.skill_points > 0:
                            self.skill_points -= 1
                            self.upgrade_Skill(skill_sheet)

                    if current_skill[1] < 10:
                        current_skill[1] += 100
                    if current_skill[1] > 430:
                        current_skill[1] -= 100

            lib.fill(screen)

            screen.blit(lib.cts.Skill_sheet, [0, 0])
            screen.blit(lib.cts.Current_skill, current_skill)

            for _ in [[1100, 20], [1100, 120], [1100, 220], [1100, 320], [1100, 420]]:
                screen.blit(lib.cts.Icon, _)

            screen.blit(self.set[9], [0, 50])

            self.display_skill(screen)

            level = ("Lvl: " + str(self.current_level))
            quantity = Texts([10, 10], screen, level, 30, 2)
            quantity.velocity = [0, 0]
            self.writer.add(quantity)

            if self.skill_points > 0:
                points_info = ("You have: " + str(self.skill_points) + " points")
                quantity = Texts([420, 550], screen, points_info, 30, 2)
                quantity.velocity = [0, 0]

                self.writer.add(quantity)

            self.writer.update()

            for _ in self.writer:
                self.writer.remove(_)

            lib.frames_per_second(fps, 1)

    def update(self, key_pressed, screen):
        self.animate(key_pressed)

        if self.velocity[0] != 0 and self.wings_buff > 0:
            self.rect.x += self.velocity[0] * self.wings_buff * 2
        else:
            self.rect.x += self.velocity[0]
        list_collide = pg.sprite.spritecollide(self, self.collides, False)

        for things in list_collide:
            if self.velocity[0] > 0:
                if self.rect.right > things.rect.left:
                    self.rect.right = things.rect.left
                    self.velocity[0] = 0
            else:
                if self.rect.left < things.rect.right:
                    self.rect.left = things.rect.right
                    self.velocity[0] = 0

        if self.velocity[1] != 0 and self.wings_buff > 0:
            self.rect.y += self.velocity[1] * self.wings_buff * 2
        else:
            self.rect.y += self.velocity[1]
        list_collide = pg.sprite.spritecollide(self, self.collides, False)

        for things in list_collide:
            if self.velocity[1] > 0:
                if self.rect.bottom > things.rect.top:
                    self.rect.bottom = things.rect.top
                    self.velocity[1] = 0

            else:
                if self.rect.top < things.rect.bottom:
                    self.rect.top = things.rect.bottom
                    self.velocity[1] = 0

        self.show_statistics(screen)


def move_enemy(player_position, enemy_position):
    position_x = player_position[0] - enemy_position[0]
    position_y = player_position[1] - enemy_position[1]
    return [position_x, position_y]


def attack_bomb(boss_attacking):
    direction = 0
    while direction <= 360:
        bullet = Attack_Balzar(boss_attacking.rect.center)
        bullet.velocity = 8
        bullet.angle = direction
        attack_group.add(bullet)

        bullet = Attack_Balzar(boss_attacking.rect.center)
        bullet.velocity = -8
        bullet.angle = direction
        attack_group.add(bullet)
        direction += 30


def attack_angelic_bomb(boss_attacking):
    direction = 0
    while direction < 360:
        bullets = Attack_Balzar(boss_attacking.rect.center)
        bullets.velocity = 7
        bullets.angle = direction
        attack_group.add(bullets)

        bullets = Attack_Balzar(boss_attacking.rect.center)
        bullets.velocity = -7
        bullets.angle = direction
        attack_group.add(bullets)

        bullets = Attack_Balzar(boss_attacking.rect.center)
        bullets.velocity = 7
        bullets.angle = direction
        attack_group.add(bullets)

        bullets = Attack_Balzar(boss_attacking.rect.center)
        bullets.velocity = -7
        bullets.angle = direction
        attack_group.add(bullets)
        direction += 3


def attack_spiral(boss_attacking):
    bullets = Attack_Balzar(boss_attacking.rect.center)
    bullets.velocity = 10
    bullets.angle = 0
    attack_group.add(bullets)
    for bullets in attack_group:
        bullets.angle += 0.2


def god_attack(pos):
    attack_generator = Attack_God([pos[0] + 80, pos[1]])
    attack_group.add(attack_generator)

    attack_generator = Attack_God([pos[0], pos[1] + 80])
    attack_group.add(attack_generator)

    attack_generator = Attack_God([pos[0], pos[1] - 80])
    attack_group.add(attack_generator)

    attack_generator = Attack_God([pos[0] - 80, pos[1]])
    attack_group.add(attack_generator)


def heaven_shot_type_(attack_position, current_boss):
    attack_type_2 = Attack_God(attack_position.rect.center)
    attack_type_2.velocity = [5, 5]
    attack_type_2.angle = lib.mt.radians(lib.rd.randrange(360))
    attack_type_2_group.add(attack_type_2)


def heaven_shot_type_2(attack_position, current_boss):
    attack_type_2 = Attack_God(attack_position.rect.center)
    attack_type_2.velocity = [0, 0]
    attack_type_2.angle = lib.mt.radians(lib.rd.randrange(360))
    attack_type_2_group.add(attack_type_2)


if __name__ == '__main__':
    # init()

    pg.init()
    pg.font.init()
    pg.mixer.init()

    # Whiles

    run = True
    end = True
    intro = True
    story_1 = True
    story_2 = True
    story_3 = True
    room_1 = True
    room_2 = True
    death = False
    field_1 = True
    field_2 = True
    field_3 = True
    field_4 = True
    field_5 = True
    field_6 = True
    choosing = True
    in_combat = False

    # Windows constants

    window = lib.new_window("Choose a player")
    fps = lib.frames_per_second_basics()

    # Groups

    # while writing

    statistics_information = pg.sprite.Group()
    inventory_information = pg.sprite.Group()
    attacks_information = pg.sprite.Group()
    abilities_in_combat = pg.sprite.Group()
    npc_dialogue_group = pg.sprite.Group()
    lvl_information = pg.sprite.Group()
    holes_dialogue = pg.sprite.Group()
    dialogue_group = pg.sprite.Group()
    title_group = pg.sprite.Group()
    text_group = pg.sprite.Group()
    win_group = pg.sprite.Group()

    # while playing

    random_enemies_group = pg.sprite.Group()
    attack_type_2_group = pg.sprite.Group()
    enemies_in_combat = pg.sprite.Group()
    generators_group = pg.sprite.Group()
    players_group = pg.sprite.Group()
    enemies_group = pg.sprite.Group()
    flowers_group = pg.sprite.Group()
    portals_group = pg.sprite.Group()
    attack_group = pg.sprite.Group()
    things_group = pg.sprite.Group()
    buffs_group = pg.sprite.Group()
    items_group = pg.sprite.Group()
    boss_group = pg.sprite.Group()
    NPCs_group = pg.sprite.Group()

    # Variables

    key = 0
    cont = 0
    speed = 5
    catchable = 0
    next_level = 3
    interaction = []
    player_set = None
    player_story = None
    enemy_ability = None
    you_got_armor = False

    # Enemies variables

    angle = 0
    radio = 300
    distance = [0, 0]

    # Boss variables

    attack_before_pause = 4
    temp_while_shooting = 20
    attack_direction = 0
    current_attack = 1

    # Choosing player

    new_text_position = [[5, 300], [360, 300], [840, 300], [140, 580], [610, 580]]
    for _ in range(0, len(lib.cts.choosing_player) - 3):
        new_text = Texts(new_text_position[_], window, lib.cts.choosing_player[_], 20, 2)
        new_text.velocity = [0, 0]
        text_group.add(new_text)

    while run and choosing:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYUP:
                if event.key == pg.K_1:
                    player_set = 1
                    player_story = lib.cts.euphoria_intro_luke
                    interaction.append(lib.cts.dialogue_5_1)
                    interaction.append(lib.cts.dialogue_6_1)
                    interaction.append(lib.cts.Player_attacks_1)
                    interaction.append(lib.cts.Death_interaction_1)
                    choosing = False
                if event.key == pg.K_2:
                    player_set = 2
                    player_story = lib.cts.euphoria_intro_serafin
                    interaction.append(lib.cts.dialogue_5_2)
                    interaction.append(lib.cts.dialogue_6_2)
                    interaction.append(lib.cts.Player_attacks_2)
                    interaction.append(lib.cts.Death_interaction_2)
                    choosing = False
                if event.key == pg.K_3:
                    player_set = 3
                    player_story = lib.cts.euphoria_intro_sonia
                    interaction.append(lib.cts.dialogue_5_3)
                    interaction.append(lib.cts.dialogue_6_4)
                    interaction.append(lib.cts.Player_attacks_3)
                    interaction.append(lib.cts.Death_interaction_3)
                    choosing = False
                if event.key == pg.K_4:
                    player_set = 4
                    player_story = lib.cts.euphoria_intro_taun
                    interaction.append(lib.cts.dialogue_5_4)
                    interaction.append(lib.cts.dialogue_6_4)
                    interaction.append(lib.cts.Player_attacks_4)
                    interaction.append(lib.cts.Death_interaction_4)
                    choosing = False
                if event.key == pg.K_5:
                    player_set = 5
                    player_story = lib.cts.euphoria_intro_xerath
                    interaction.append(lib.cts.dialogue_5_5)
                    interaction.append(lib.cts.dialogue_6_5)
                    interaction.append(lib.cts.Player_attacks_5)
                    interaction.append(lib.cts.Death_interaction_5)
                    choosing = False

        # Drawing and control

        lib.fill(window)

        window.blit(lib.cts.Presentation[0], [70, 30])
        window.blit(lib.cts.Presentation[1], [500, 30])
        window.blit(lib.cts.Presentation[2], [950, 30])
        window.blit(lib.cts.Presentation[3], [250, 350])
        window.blit(lib.cts.Presentation[4], [730, 350])

        text_group.update()

        lib.frames_per_second(fps, 2)

    # Intro

    for _ in text_group:
        text_group.remove(_)

    # Game title

    Title = Texts([300, 250], window, lib.cts.euphoria, 200)
    Title.velocity = [0, 0]
    title_group.add(Title)

    # Game intro

    new_text_position = [50, 750]
    for _ in range(0, len(player_story)):
        lib.play_music(lib.cts.Intro_3)
        new_text = Texts(new_text_position, window, player_story[_], 30, 2)
        new_text_position[1] += 50
        text_group.add(new_text)

    # Game button skip

    Skip = Texts([1080, 550], window, lib.cts.skip, 20)
    Skip.velocity = [0, 0]
    title_group.add(Skip)

    window = lib.new_window("Intro")

    while run and intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                lib.stop_music()
            if event.type == pg.MOUSEBUTTONDOWN:
                intro = False
                lib.stop_music()

        # Drawing and control

        lib.fill(window)

        Title.update()

        if cont >= 100:
            Title.velocity = [0, -1]
            text_group.update()
            Skip.update()

        cont += 1

        for _ in text_group:
            if _.y < 0:
                text_group.remove(_)

        for _ in title_group:
            if _.y <= 0:
                title_group.remove(_)

        if len(text_group) == 0:
            intro = False

        lib.frames_per_second(fps, 2)

    # Cleaning and Updating window

    for _ in title_group:
        title_group.remove(_)

    for _ in text_group:
        text_group.remove(_)

    lib.change_window_name('Euphoria')

    lib.fill(window)

    # Scenario settings

    # Creating a new scenario
    lib.stop_music()
    current_scenario = 1
    scenario = Scenarios(current_scenario, window)
    scenario.rect.x, scenario.rect.y = [lib.cts.width / 3, lib.cts.height / 3]

    # Adding things

    bed = Things([447, 224], 3)
    things_group.add(bed)

    decoration1 = Things([738, 207], 4)
    things_group.add(decoration1)

    decoration2 = Things([653, 203], 5)
    things_group.add(decoration2)

    nightstand_1 = Things([414, 201], 9)
    things_group.add(nightstand_1)

    nightstand_2 = Things([553, 232], 10)
    things_group.add(nightstand_2)

    top_limit = Things([412, 232], 2)
    things_group.add(top_limit)

    left_limit = Things([412, 232], 1)
    things_group.add(left_limit)

    right_limit = Things([775, 232], 1)
    things_group.add(right_limit)

    bottom_limit = Things([412, 462], 2)
    things_group.add(bottom_limit)

    first_life = Buffs([560, 225], 1)
    buffs_group.add(first_life)

    # Adding a player

    player = Player([scenario.rect.x + 160, scenario.rect.y + 55], player_set, things_group)
    player.speed = speed
    player.radius = 50

    players_group.add(player)

    # Adding text interactions

    potion = Texts([300, 500], window, lib.cts.dialogue_1, 30, 2)
    text_group.add(potion)

    lvl_info = Texts([1050, 570], window, lib.cts.lvl_info[0], 25, 2)
    lvl_info.velocity = [0, 0]
    lvl_information.add(lvl_info)

    while run and room_1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            # Player movement & Interactions

            if event.type == pg.KEYDOWN:
                key = 1
                if event.key == pg.K_p:
                    player.show_inventory(window)
                if event.key == pg.K_s:
                    player.velocity[1] += player.speed
                    player.action = 3
                    lib.play_music(lib.cts.Running_Loud, -1)
                if event.key == pg.K_w:
                    player.velocity[1] -= player.speed
                    player.action = 1
                    lib.play_music(lib.cts.Running_Loud, -1)
                if event.key == pg.K_d:
                    player.velocity[0] += player.speed
                    player.action = 0
                    lib.play_music(lib.cts.Running_Loud, -1)
                if event.key == pg.K_a:
                    player.velocity[0] -= player.speed
                    player.action = 2
                    lib.play_music(lib.cts.Running_Loud, -1)
                if event.key == pg.K_e and catchable:
                    for _ in buffs_group:
                        lib.play_music(lib.cts.Grabing)
                        buffs_group.remove(_)
                    player.live = 10
                    catchable = 0
            if event.type == pg.KEYUP:
                lib.stop_music()
                player.velocity = [0, 0]
                key = 0

        # Next room condition

        if player.rect.bottom == 462 and player.rect.left < 505 and player.rect.right > 472:
            room_1 = False

        # Drawing

        lib.fill(window)

        scenario.update()

        if 550 < player.rect.x < 580 and 270 > player.rect.y > 230 and len(buffs_group) == 1:
            if potion.y < 490:
                potion.velocity = [0, 0]

            text_group.update()

            catchable = 1
        else:
            text_group.rect = [300, 500]
            catchable = 0

        things_group.update()
        things_group.draw(window)

        buffs_group.update()
        buffs_group.draw(window)

        lvl_information.update()

        players_group.update(key, window)
        players_group.draw(window)

        lib.frames_per_second(fps, 1)

    # Cleaning

    for _ in things_group:
        things_group.remove(_)

    for _ in buffs_group:
        buffs_group.remove(_)

    for _ in text_group:
        text_group.remove(_)

    for _ in lvl_information:
        lvl_information.remove(_)

    # Scenario settings

    # Background

    lib.play_music(lib.cts.Wooden_Door)
    current_scenario = 2
    scenario.background = current_scenario

    # Background position

    scenario.change_image()
    scenario.rect.x, scenario.rect.y = [lib.cts.width / 5, lib.cts.height / 5]

    # Repositioning player

    player.rect.x = 712
    player.rect.y = 181

    # Adding things

    decoration4 = Things([265, 158], 7)
    things_group.add(decoration4)

    decoration3 = Things([809, 162], 6)
    things_group.add(decoration3)

    nightstand_2 = Things([585, 131], 8)
    things_group.add(nightstand_2)

    table = Things([695, 405], 15)
    things_group.add(table)

    chair_e = Things([637, 413], 11)
    things_group.add(chair_e)

    chair_n = Things([718, 483], 12)
    things_group.add(chair_n)

    chair_s = Things([716, 354], 13)
    things_group.add(chair_s)

    chair_w = Things([800, 415], 14)
    things_group.add(chair_w)

    top_limit = Things([262, 180], 2)
    things_group.add(top_limit)

    top_limit = Things([682, 180], 2)
    things_group.add(top_limit)

    left_limit = Things([262, 232], 1)
    things_group.add(left_limit)

    right_limit = Things([920, 212], 1)
    things_group.add(right_limit)

    bottom_limit = Things([262, 520], 2)
    things_group.add(bottom_limit)

    bottom_limit = Things([682, 520], 2)
    things_group.add(bottom_limit)

    # Adding buffs

    energy = Buffs([705, 405], 2)
    buffs_group.add(energy)

    smash = Buffs([885, 185], 3)
    buffs_group.add(smash)

    coffee = Buffs([745, 435], 5)
    buffs_group.add(coffee)

    # Adding text interactions

    potion = Texts([250, 70], window, lib.cts.dialogue_2, 30, 2)
    potion.velocity = [0, 1]
    text_group.add(potion)

    ring_without_potion = Texts([250, 70], window, lib.cts.dialogue_2_1, 30, 2)
    ring_without_potion.velocity = [0, 1]
    text_group.add(ring_without_potion)

    ring = Texts([250, 70], window, lib.cts.dialogue_3, 30, 2)
    ring.velocity = [0, 1]
    text_group.add(ring)

    cup = Texts([250, 70], window, lib.cts.dialogue_3_1, 30, 2)
    cup.velocity = [0, 1]
    text_group.add(cup)

    lvl_info = Texts([760, 570], window, lib.cts.lvl_info[1], 25, 2)
    lvl_info.velocity = [0, 0]
    lvl_information.add(lvl_info)

    while run and room_2:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            # Player movement & interactions

            if event.type == pg.KEYDOWN:
                key = 1
                if event.key == pg.K_p:
                    player.show_inventory(window)
                if event.key == pg.K_s:
                    player.velocity[1] += player.speed
                    player.action = 3
                    lib.play_music(lib.cts.Running_Loud, -1)
                if event.key == pg.K_w:
                    player.velocity[1] -= player.speed
                    player.action = 1
                    lib.play_music(lib.cts.Running_Loud, -1)
                if event.key == pg.K_d:
                    player.velocity[0] += player.speed
                    player.action = 0
                    lib.play_music(lib.cts.Running_Loud, -1)
                if event.key == pg.K_a:
                    player.velocity[0] -= player.speed
                    player.action = 2
                    lib.play_music(lib.cts.Running_Loud, -1)
                if event.key == pg.K_e and catchable == 2:
                    if len(buffs_group) == 3:
                        player.energy += 5
                        lib.play_music(lib.cts.Grabing)
                    buffs_group.remove(energy)
                    text_group.remove(potion)
                    catchable = 0
                if event.key == pg.K_q and catchable == 3:
                    if len(buffs_group) == 2:
                        lib.play_music(lib.cts.Sell_Or_Buy)
                        player.drake_smash += 1
                    buffs_group.remove(smash)
                    catchable = 0
                if event.key == pg.K_r and catchable == 4 and player.live > 1:
                    player.energy += 1
                    player.live -= 1
                    catchable = 0
                    lib.play_music(lib.cts.Grabing)
            if event.type == pg.KEYUP:
                player.velocity = [0, 0]
                key = 0
                lib.stop_music()

        # Next field condition

        if player.rect.bottom == 520 and player.rect.left < 450 and player.rect.right > 430:
            room_2 = False

        # Drawing

        lib.fill(window)

        scenario.update()

        if 665 < player.rect.x < 690 and 385 > player.rect.y > 360:
            if potion.y > 80:
                potion.velocity = [0, 0]

            if len(buffs_group) > 2:
                potion.update()

            catchable = 2
        else:
            potion.rect = [250, 70]

            if 870 < player.rect.x < 900 and player.rect.y <= 232:
                if ring.y > 80:
                    ring.velocity = [0, 0]

                if ring_without_potion.y > 80:
                    ring_without_potion.velocity = [0, 0]

                if len(buffs_group) == 3:
                    ring_without_potion.update()
                else:
                    if len(buffs_group) == 2:
                        ring.update()
                        catchable = 3
            else:
                ring_without_potion.rect = [250, 70]
                ring.rect = [250, 70]
                catchable = 0

        if 760 < player.rect.x < 780 and 455 > player.rect.y > 420:
            if cup.y > 80:
                cup.velocity = [0, 0]

            if player.live > 1:
                cup.update()

            catchable = 4
        else:
            if len(buffs_group) == 1:
                catchable = 0

        things_group.update()
        things_group.draw(window)

        buffs_group.update()
        buffs_group.draw(window)

        lvl_information.update()

        players_group.update(key, window)
        players_group.draw(window)

        lib.frames_per_second(fps, 1)

    # Cleaning

    for _ in things_group:
        things_group.remove(_)

    for _ in text_group:
        text_group.remove(_)

    for _ in buffs_group:
        buffs_group.remove(_)

    # Background settings

    lib.play_music(lib.cts.Wooden_Door)
    current_scenario = 3
    scenario.background = current_scenario

    # Background position

    scenario.change_image()
    scenario.rect.x, scenario.rect.y = [-100, -250]

    # Repositioning player

    player.rect.x = 600
    player.rect.y = 350

    # Adding enemies

    angle = 0
    radio = 300
    distance = [0, 0]

    first_enemy_position = [[1400, 600]]

    enemy = SimpleEnemy(first_enemy_position[0], 1)
    enemies_group.add(enemy)

    # Adding things

    flowers = [[685, 20], [685, 35], [705, 20], [705, 35], [705, 50],
               [705, 65], [725, 20], [725, 35], [725, 50], [725, 65],
               [725, 80], [725, 95], [745, 20], [745, 35], [745, 50],
               [745, 65], [745, 80], [745, 95], [765, 20], [765, 35],
               [765, 50], [765, 65], [765, 80], [765, 95], [785, 20],
               [785, 35], [785, 50], [785, 65], [785, 80], [785, 95],
               [805, 50], [805, 65], [805, 80], [805, 95], [805, 20],
               [805, 35], [825, 80], [825, 95], [825, 20], [825, 35],
               [825, 50], [825, 65]]

    for _ in range(len(flowers)):
        flower = Things(flowers[_], lib.rd.randrange(19, 21))
        things_group.add(flower)

    trees = [[100, 800], [75, 80], [350, -180], [1450, 400]]

    for _ in range(len(trees)):
        flower = Things(trees[_], lib.rd.randrange(16, 17))
        things_group.add(flower)

    house = Things([500, 0], 21)
    things_group.add(house)

    # NPCs

    Manuela = NonPlayableCharacters([750, 300], 1)
    NPCs_group.add(Manuela)

    # Generators

    cont = [[1500, 30]]

    for _ in range(len(cont)):
        generator = Generator(cont[_])
        generators_group.add(generator)

    # Text interactions

    new_text_position = [30, 450]

    for _ in range(0, len(lib.cts.dialogue_4)):
        warden = Texts(new_text_position, window, lib.cts.dialogue_4[_], 30, 2)
        warden.velocity = [0, 0]
        new_text_position[1] += 25
        text_group.add(warden)

    new_text_position = [450, 450]

    for _ in range(0, len(interaction[0])):
        dialogue = Texts(new_text_position, window, interaction[0][_], 30, 2)
        dialogue.velocity = [0, 0]
        new_text_position[1] += 25
        dialogue_group.add(dialogue)

    holes_dialogue = Texts([450, 450], window, lib.cts.dialogue_7_2, 30, 2)
    holes_dialogue.velocity = [0, 0]

    new_text_position = [50, 450]

    for _ in range(0, len(interaction[2]) - 2):
        abilities = Texts(new_text_position, window, interaction[2][_], 20, 2)
        abilities.velocity = [0, 0]
        abilities_in_combat.add(abilities)
        new_text_position[1] += 50

    new_text_position = [450, 450]

    for _ in range(3, len(interaction[2])):
        abilities = Texts(new_text_position, window, interaction[2][_], 20, 2)
        abilities.velocity = [0, 0]
        abilities_in_combat.add(abilities)
        new_text_position[1] += 50

    new_text_position = [50, 450]

    for _ in range(0, len(lib.cts.Player_inventory)):
        inventory = Texts(new_text_position, window, lib.cts.Player_inventory[_], 20, 2)
        inventory.velocity = [0, 0]
        inventory_information.add(inventory)
        new_text_position[1] += 50

    new_text_position = [50, 450]

    for _ in range(0, len(interaction[1])):
        attack_information = Texts(new_text_position, window, interaction[1][_], 30, 2)
        attack_information.velocity = [0, 0]
        new_text_position[1] += 25
        attacks_information.add(attack_information)

    new_text_position = [50, 450]

    for _ in range(0, len(lib.cts.energy_material_info)):
        energy_information = Texts(new_text_position, window, lib.cts.energy_material_info[_], 30, 2)
        energy_information.velocity = [0, 0]
        new_text_position[1] += 25
        statistics_information.add(energy_information)

    lvl_info = Texts([820, 570], window, lib.cts.lvl_info[2], 25, 2, lib.cts.RED)
    lvl_info.velocity = [0, 0]
    lvl_information.add(lvl_info)

    win = Texts([400, 300], window, lib.cts.win_dialogue, 80, 2, lib.cts.GOLD)
    win_group.add(win)

    level_up = Texts([450, 400], window, lib.cts.lvl_up_dialogue, 40, 2, lib.cts.GOLD)
    win_group.add(level_up)

    # Setting variables

    catchable = False

    # Main loop (Field 1)

    while run and field_1 or in_combat:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        while field_1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
                    field_1 = False
                    run = False

                # Player movement

                if event.type == pg.KEYDOWN:
                    key = 1
                    if event.key == pg.K_p:
                        player.show_inventory(window)
                    if event.key == pg.K_i:
                        player.skill_sheet(window)
                    if event.key == pg.K_s:
                        player.velocity[1] += player.speed
                        player.action = 3
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_w:
                        player.velocity[1] -= player.speed
                        player.action = 1
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_d:
                        player.velocity[0] += player.speed
                        player.action = 0
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_a:
                        player.velocity[0] -= player.speed
                        player.action = 2
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_e:
                        catchable = False
                if event.type == pg.KEYUP:
                    player.velocity = [0, 0]
                    key = 0
                    lib.stop_music()

            # Control

            # Next field condition

            if player.rect.x == 1150 and 360 < player.rect.y < 520:
                if scenario.rect[0] == -600 and scenario.rect[1] == -625:
                    in_combat = False
                    field_1 = False

            # Scenario movement

            if player.rect.x > scenario.screen_limits[0]:
                player.rect.x = scenario.screen_limits[0]
                if scenario.rect.x > scenario.background_limits[0]:
                    scenario.background_velocity[0] = 5
                    for _ in things_group:
                        _.thing_velocity[0] = -5
                    for _ in generators_group:
                        _.velocity[0] = -5
                    for _ in buffs_group:
                        _.velocity[0] = -5
                    Manuela.npc_velocity[0] = -5

                else:
                    scenario.background_velocity[0] = 0
                    for _ in things_group:
                        _.thing_velocity[0] = 0
                    for _ in generators_group:
                        _.velocity[0] = 0
                    for _ in buffs_group:
                        _.velocity[0] = 0
                    Manuela.npc_velocity[0] = 0
            else:
                if player.rect.x < lib.cts.width - scenario.screen_limits[0]:
                    player.rect.x = lib.cts.width - scenario.screen_limits[0]
                    if scenario.rect.x < lib.cts.width + scenario.background_limits[0] * 2:
                        scenario.background_velocity[0] = -5
                        for _ in things_group:
                            _.thing_velocity[0] = 5
                        for _ in generators_group:
                            _.velocity[0] = 5
                        for _ in buffs_group:
                            _.velocity[0] = 5
                        Manuela.npc_velocity[0] = 5
                    else:
                        scenario.background_velocity[0] = 0
                        for _ in things_group:
                            _.thing_velocity[0] = 0
                        for _ in generators_group:
                            _.velocity[0] = 0
                        for _ in buffs_group:
                            _.velocity[0] = 0
                        Manuela.npc_velocity[0] = 0
                else:
                    if scenario.rect.x > lib.cts.width + scenario.background_limits[0]:
                        scenario.background_velocity[0] = 5
                        for _ in things_group:
                            _.thing_velocity[0] = -5
                        for _ in generators_group:
                            _.velocity[0] = -5
                        for _ in buffs_group:
                            _.velocity[0] = -5
                        Manuela.npc_velocity[0] = -5
                    else:
                        scenario.background_velocity[0] = 0
                        for _ in things_group:
                            _.thing_velocity[0] = 0
                        for _ in generators_group:
                            _.velocity[0] = 0
                        for _ in buffs_group:
                            _.velocity[0] = 0
                        Manuela.npc_velocity[0] = 0

            if player.rect.y > scenario.screen_limits[1]:
                player.rect.y = scenario.screen_limits[1]
                if scenario.rect.y > scenario.background_limits[1]:
                    scenario.background_velocity[1] = -5
                    for _ in things_group:
                        _.thing_velocity[1] = -5
                    for _ in generators_group:
                        _.velocity[1] = -5
                    for _ in buffs_group:
                        _.velocity[1] = -5
                    Manuela.npc_velocity[1] = -5
                else:
                    scenario.background_velocity[1] = 0
                    for _ in things_group:
                        _.thing_velocity[1] = 0
                    for _ in generators_group:
                        _.velocity[1] = 0
                    for _ in buffs_group:
                        _.velocity[1] = 0
                    Manuela.npc_velocity[1] = 0
            else:
                if player.rect.y < lib.cts.height - scenario.screen_limits[1]:
                    player.rect.y = lib.cts.height - scenario.screen_limits[1]
                    if scenario.rect.y < 0:
                        scenario.background_velocity[1] = 5
                        for _ in things_group:
                            _.thing_velocity[1] = 5
                        for _ in generators_group:
                            _.velocity[1] = 5
                        for _ in buffs_group:
                            _.velocity[1] = 5
                        Manuela.npc_velocity[1] = 5
                    else:
                        scenario.background_velocity[1] = 0
                        for _ in things_group:
                            _.thing_velocity[1] = 0
                        for _ in generators_group:
                            _.velocity[1] = 0
                        for _ in buffs_group:
                            _.velocity[1] = 0
                        Manuela.npc_velocity[1] = 0
                else:
                    if scenario.rect.y > lib.cts.height + scenario.background_limits[1]:
                        scenario.background_velocity[1] = -5
                        for _ in things_group:
                            _.thing_velocity[1] = -5
                        for _ in generators_group:
                            _.velocity[1] = -5
                        for _ in buffs_group:
                            _.velocity[1] = -5
                        Manuela.npc_velocity[1] = -5
                    else:
                        scenario.background_velocity[1] = 0
                        for _ in things_group:
                            _.thing_velocity[1] = 0
                        for _ in generators_group:
                            _.velocity[1] = 0
                        for _ in buffs_group:
                            _.velocity[1] = 0
                        Manuela.npc_velocity[1] = 0

            # Enemies

            enemy_collide = pg.sprite.spritecollide(player, enemies_group, True)

            for enemy in enemy_collide:
                enemies_in_combat.add(enemy)
                player.velocity = [0, 0]
                in_combat = True
                field_1 = False
                lib.play_music(lib.cts.Demon_Scream)

            i = 0
            for enemy in enemies_group:
                distance = move_enemy(first_enemy_position[i], player.rect)
                if lib.mt.sqrt(lib.mt.pow(distance[0], 2) + lib.mt.pow(distance[1], 2)) > radio:
                    distance = move_enemy(first_enemy_position[i], enemy.rect)
                else:
                    distance = move_enemy(player.rect, enemy.rect)
                if distance[0] > 0:
                    enemy.velocity = [4, 4]
                else:
                    enemy.velocity = [-4, -4]

                if ((distance[0] >= -2) and (distance[0] <= 2)) and ((distance[1] >= -2) and (distance[1] <= 2)):
                    enemy.velocity = [0, 0]
                else:
                    if distance[0] == 0:
                        enemy.velocity = [-4, -4]
                        if distance[1] > 0:
                            angle = lib.mt.radians(270)
                        if distance[1] < 0:
                            angle = lib.mt.radians(90)
                    else:
                        angle = lib.mt.atan(distance[1] / distance[0])
                        enemy.angle = angle
                i += 1

            # Generators

            generator_collide = pg.sprite.spritecollide(player, generators_group, False)

            for generator in generator_collide:
                if not catchable:
                    lib.play_music(lib.cts.GlassBreak)
                    potion = Buffs([generator.rect.x, generator.rect.y], 2)
                    buffs_group.add(potion)

                    lib.play_music(lib.cts.GlassBreak)
                    generators_group.remove(generator)

                    catchable = False

            for generator in generators_group:
                if generator.temp < 0:
                    raccoon = GeneratedEnemy(generator.rect.center, lib.cts.random_enemies_1)
                    random_enemies_group.add(raccoon)
                    generator.temp = 60

            # Cleaning raccoons

            for raccoon in random_enemies_group:
                if raccoon.rect.x < -50:
                    random_enemies_group.remove(raccoon)
                if raccoon.rect.y < -50:
                    random_enemies_group.remove(raccoon)
                if raccoon.rect.x > lib.cts.width:
                    random_enemies_group.remove(raccoon)
                if raccoon.rect.y > lib.cts.height:
                    random_enemies_group.remove(raccoon)

            # Generated enemies

            random_collide = pg.sprite.spritecollide(player, random_enemies_group, False)

            for random_enemies in random_collide:
                player.energy -= 1
                random_enemies_group.remove(random_enemies)
                lib.play_music(lib.cts.Raccoon_Sound)

            # Buffs

            buff_collide = pg.sprite.spritecollide(player, buffs_group, True)

            for buffs in buff_collide:
                if buffs.buff == 1:
                    player.extra_live += 1
                elif buffs.buff == 2:
                    player.extra_energy += 1
                elif buffs.buff == 3:
                    player.drake_smash += 1
                elif buffs.buff == 4:
                    player.wings_buff += 1

                buffs_group.remove(buffs)

            # Updating & Drawing

            lib.fill(window)

            scenario.update()

            first_enemy_position = scenario.move_enemies(first_enemy_position)

            generators_group.update()
            generators_group.draw(window)

            buffs_group.update()
            buffs_group.draw(window)

            random_enemies_group.update(scenario.background_velocity)
            random_enemies_group.draw(window)

            enemies_group.update(scenario.background_velocity)
            enemies_group.draw(window)

            things_group.update()
            things_group.draw(window)

            lvl_info.update()

            players_group.update(key, window)
            players_group.draw(window)

            NPCs_group.update()
            NPCs_group.draw(window)

            # Text interactions

            if 750 + scenario.rect.x < player.rect.x < 953 + scenario.rect.x:
                if 350 + scenario.rect.y > player.rect.y > 217 + scenario.rect.y:
                    lib.play_music(lib.cts.Hmm_Men, 0)
                    window.blit(lib.cts.Dialog_box, [0, 400])
                    text_group.update()
                    lib.stop_music()

            # npc
            for manuela in NPCs_group:
                if pg.sprite.collide_circle(manuela, player):
                    lib.play_music(lib.cts.Hmm_Women, 0)
                    window.blit(lib.cts.Dialog_box, [400, 400])
                    dialogue_group.update()
                    lib.stop_music()

                    lvl_info = Texts([900, 570], window, lib.cts.lvl_info[3], 25, 2, lib.cts.RED)
                    lvl_info.velocity = [0, 0]

            generator_collide = pg.sprite.spritecollide(player, generators_group, False)

            for _ in generator_collide:
                window.blit(lib.cts.Dialog_box, [400, 400])
                holes_dialogue.update()
                catchable = True
                lib.play_music(lib.cts.Hmm_Men, 0)

            lib.frames_per_second(fps, 1)

        # Settings variables

        turn = 1
        catchable = True
        get_point = True
        progressive = True

        while in_combat:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
                    run = False
                if event.type == pg.KEYDOWN and turn == 1:

                    # Player attacks

                    if event.key == pg.K_q:
                        if player.energy >= 1:
                            player.attack(1)
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.Punch)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    if event.key == pg.K_w:
                        if player.energy >= 3:
                            player.attack(2)
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.Sword_Swing)
                        else:
                            turn = 2
                    if event.key == pg.K_e:
                        if player.energy >= 5:
                            player.transformation = True
                            player.attack(3)
                            turn = 0
                            cont = 0
                            lib.play_music(lib.cts.Transformation_1)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    if event.key == pg.K_r:
                        if player.energy >= 3:
                            if player.transformation:
                                player.attack(4)
                                turn = 0
                                cont = 0
                                lib.play_music(lib.cts.Dragon_Roar_Breathe_Fire)
                            else:
                                catchable = False
                                cont = 0
                                turn = 1
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)

                    # Inventory

                    if event.key == pg.K_t:
                        turn = 3
                        cont = 0
                        lib.play_music(lib.cts.Inventory)

                    if event.key == pg.K_a:
                        if player.drake_smash >= 1:
                            player.use_extras(3)
                            enemy.life = 0
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.MagicFinal)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    if event.key == pg.K_s:
                        if player.extra_live >= 1:
                            player.use_extras(1)
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.Grabing)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    if event.key == pg.K_d:
                        if player.extra_energy >= 1:
                            player.use_extras(2)
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.Grabing)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    # Skip turn
                    if event.key == pg.K_f:
                        player.energy += 1
                        player.live += 1
                        cont = 0
                        turn = 0
                        lib.play_music(lib.cts.Lost)

                    # Restating variables

                    if turn == 0:
                        player.energy += 2

                    progressive = True

            # Drawing

            lib.fill(window)

            window.blit(lib.cts.Battle_ground, [0, 0])

            enemy.show_statistics(window)
            enemy.in_combat(window)

            player.in_combat(window)

            # Control

            # Enemies turn

            if turn == 0:
                for enemy in enemies_in_combat:
                    if cont == 0:
                        enemy_ability = enemy.enemy_attack(player.damage)
                        player.damage = 0

                    if enemy.life <= 0:
                        enemies_in_combat.remove(enemy)
                    else:
                        window.blit(lib.cts.Dialog_box, [400, 400])
                        window.blit(enemy_ability, [450, 450])

                if cont > 100:
                    turn = 1
                cont += 1

            if len(enemies_in_combat) == 0:
                win.update()

                if player.level_points == next_level:
                    player.current_level += 1
                    level_up.update()
                    get_point = True

                player.transformation = False

                if cont > 100:
                    player.velocity = [0, 0]
                    key = 0

                    in_combat = False
                    field_2 = True
                cont += 1

            # Player turn

            if turn == 1:
                for enemy in enemies_in_combat:
                    player.hurts(enemy.damage)

                    if enemy.progressive_damage > 0 and progressive:
                        enemy.progressive_damage -= 1
                        progressive = False
                        player.live -= 1
                        lib.play_music(lib.cts.Pain)

                    enemy.damage = 0

                if player.live <= 0:
                    in_combat = False
                    field_2 = False
                    death = True
                    lib.play_music(lib.cts.Fail)

                window.blit(lib.cts.Combat_box, [0, 400])

                player.show_statistics(window)

                if catchable:
                    abilities_in_combat.update()
                    cont = 0
                else:
                    attacks_information.update()
                    if cont > 100:
                        catchable = True
                        turn = 1
                    cont += 1

            # Informative turns

            if turn == 2:
                window.blit(lib.cts.Dialog_box, [0, 400])
                statistics_information.update()
                player.energy -= 2
                if cont > 100:
                    turn = 1
                cont += 1

            if turn == 3:
                window.blit(lib.cts.Dialog_box, [0, 400])
                inventory_information.update()
                if cont > 100:
                    turn = 1
                cont += 1

            lib.frames_per_second(fps, 1)

        # Resetting win label
        win.x, win.y = [400, 300]
        level_up.x, level_up.y = [450, 400]
        if player.level_points < next_level and get_point:
            player.level_points += 1
            get_point = False

    # Cleaning

    for _ in things_group:
        things_group.remove(_)

    for _ in enemies_group:
        enemies_group.remove(_)

    for _ in generators_group:
        generators_group.remove(_)

    for _ in text_group:
        text_group.remove(_)

    for _ in dialogue_group:
        dialogue_group.remove(_)

    for _ in NPCs_group:
        NPCs_group.remove(_)

    for _ in enemies_in_combat:
        enemies_in_combat.remove(_)

    for _ in lvl_information:
        lvl_information.remove(_)

    # Background

    current_scenario = 4
    scenario.background = current_scenario

    # Background position

    scenario.change_image()
    scenario.rect.x, scenario.rect.y = [0, -25]

    # Repositioning player

    player.rect.x = 40
    player.rect.y = 40
    player.radius = 50

    # Adding enemies

    angle = 0
    radio = 200
    distance = [0, 0]
    first_enemy_position = [[500, 500], [800, 1000]]

    for _ in range(len(first_enemy_position)):
        enemy = SimpleEnemy(first_enemy_position[_], 2)
        enemies_group.add(enemy)

    # Adding npc

    Saku = NonPlayableCharacters([400, 50], 3)
    NPCs_group.add(Saku)

    # Adding things

    trees = [[265, 300], [750, 500], [550, 80], [1250, 600]]

    for _ in range(len(trees)):
        flower = Things(trees[_], lib.rd.randrange(16, 17))
        things_group.add(flower)

    cont = [[700, 200], [300, 800]]

    for _ in range(len(cont)):
        generator = Generator(cont[_])
        generators_group.add(generator)

    # Adding text interactions

    holes_dialogue = Texts([450, 450], window, lib.cts.dialogue_7_2, 30, 2)
    holes_dialogue.velocity = [0, 0]
    dialogue_group.add(holes_dialogue)

    new_text_position = [450, 450]

    for _ in range(0, len(lib.cts.dialogue_7_1)):
        saku_dialogue = Texts(new_text_position, window, lib.cts.dialogue_7_1[_], 25, 2)
        saku_dialogue.velocity = [0, 0]
        new_text_position[1] += 25
        npc_dialogue_group.add(saku_dialogue)

    lvl_info = Texts([800, 570], window, lib.cts.lvl_info[4], 25, 2, lib.cts.RED)
    lvl_info.velocity = [0, 0]
    lvl_information.add(lvl_info)

    # Settings variables

    catchable = False

    # Main loop (Field 2)

    while run and field_2 or in_combat:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        while field_2:

            # Player control

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
                    field_2 = False
                    run = False
                if event.type == pg.KEYDOWN:
                    key = 1
                    if event.key == pg.K_p:
                        player.show_inventory(window)
                        if len(enemies_group) == 0:
                            you_got_armor = True
                    if event.key == pg.K_i:
                        player.skill_sheet(window)
                    if event.key == pg.K_s:
                        player.velocity[1] += player.speed
                        player.action = 3
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_w:
                        player.velocity[1] -= player.speed
                        player.action = 1
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_d:
                        player.velocity[0] += player.speed
                        player.action = 0
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_a:
                        player.velocity[0] -= player.speed
                        player.action = 2
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_e:
                        catchable = True
                if event.type == pg.KEYUP:
                    player.velocity = [0, 0]
                    lib.stop_music()
                    key = 0

            # Control

            # Next field condition

            if player.rect.x == 1150 and 360 < player.rect.y < 480:
                if scenario.rect[0] == -620 and scenario.rect[1] == -625:
                    in_combat = False
                    field_2 = False

            # Scenario movement

            if player.rect.x > scenario.screen_limits[0]:
                player.rect.x = scenario.screen_limits[0]
                if scenario.rect.x > scenario.background_limits[0]:
                    scenario.background_velocity[0] = 5
                    for _ in things_group:
                        _.thing_velocity[0] = -5
                    for _ in generators_group:
                        _.velocity[0] = -5
                    for _ in buffs_group:
                        _.velocity[0] = -5
                    Saku.npc_velocity[0] = -5

                else:
                    scenario.background_velocity[0] = 0
                    for _ in things_group:
                        _.thing_velocity[0] = 0
                    for _ in generators_group:
                        _.velocity[0] = 0
                    for _ in buffs_group:
                        _.velocity[0] = 0
                    Saku.npc_velocity[0] = 0
            else:
                if player.rect.x < lib.cts.width - scenario.screen_limits[0]:
                    player.rect.x = lib.cts.width - scenario.screen_limits[0]
                    if scenario.rect.x < lib.cts.width + scenario.background_limits[0] * 2:
                        scenario.background_velocity[0] = -5
                        for _ in things_group:
                            _.thing_velocity[0] = 5
                        for _ in generators_group:
                            _.velocity[0] = 5
                        for _ in buffs_group:
                            _.velocity[0] = 5
                        Saku.npc_velocity[0] = 5
                    else:
                        scenario.background_velocity[0] = 0
                        for _ in things_group:
                            _.thing_velocity[0] = 0
                        for _ in generators_group:
                            _.velocity[0] = 0
                        for _ in buffs_group:
                            _.velocity[0] = 0
                        Saku.npc_velocity[0] = 0
                else:
                    if scenario.rect.x > lib.cts.width + scenario.background_limits[0]:
                        scenario.background_velocity[0] = 5
                        for _ in things_group:
                            _.thing_velocity[0] = -5
                        for _ in generators_group:
                            _.velocity[0] = -5
                        for _ in buffs_group:
                            _.velocity[0] = -5
                        Saku.npc_velocity[0] = -5
                    else:
                        scenario.background_velocity[0] = 0
                        for _ in things_group:
                            _.thing_velocity[0] = 0
                        for _ in generators_group:
                            _.velocity[0] = 0
                        for _ in buffs_group:
                            _.velocity[0] = 0
                        Saku.npc_velocity[0] = 0
            if player.rect.y > scenario.screen_limits[1]:
                player.rect.y = scenario.screen_limits[1]
                if scenario.rect.y > scenario.background_limits[1]:
                    scenario.background_velocity[1] = -5
                    for _ in things_group:
                        _.thing_velocity[1] = -5
                    for _ in generators_group:
                        _.velocity[1] = -5
                    for _ in buffs_group:
                        _.velocity[1] = -5
                    Saku.npc_velocity[1] = -5
                else:
                    scenario.background_velocity[1] = 0
                    for _ in things_group:
                        _.thing_velocity[1] = 0
                    for _ in generators_group:
                        _.velocity[1] = 0
                    for _ in buffs_group:
                        _.velocity[1] = 0
                    Saku.npc_velocity[1] = 0
            else:
                if player.rect.y < lib.cts.height - scenario.screen_limits[1]:
                    player.rect.y = lib.cts.height - scenario.screen_limits[1]
                    if scenario.rect.y < 0:
                        scenario.background_velocity[1] = 5
                        for _ in things_group:
                            _.thing_velocity[1] = 5
                        for _ in generators_group:
                            _.velocity[1] = 5
                        for _ in buffs_group:
                            _.velocity[1] = 5
                        Saku.npc_velocity[1] = 5
                    else:
                        scenario.background_velocity[1] = 0
                        for _ in things_group:
                            _.thing_velocity[1] = 0
                        for _ in generators_group:
                            _.velocity[1] = 0
                        for _ in buffs_group:
                            _.velocity[1] = 0
                        Saku.npc_velocity[1] = 0
                else:
                    if scenario.rect.y > lib.cts.height + scenario.background_limits[1]:
                        scenario.background_velocity[1] = -5
                        for _ in things_group:
                            _.thing_velocity[1] = -5
                        for _ in generators_group:
                            _.velocity[1] = -5
                        for _ in buffs_group:
                            _.velocity[1] = -5
                        Saku.npc_velocity[1] = -5
                    else:
                        scenario.background_velocity[1] = 0
                        for _ in things_group:
                            _.thing_velocity[1] = 0
                        for _ in generators_group:
                            _.velocity[1] = 0
                        for _ in buffs_group:
                            _.velocity[1] = 0
                        Saku.npc_velocity[1] = 0

            # Enemies

            enemy_collide = pg.sprite.spritecollide(player, enemies_group, True)

            for enemy in enemy_collide:
                enemies_in_combat.add(enemy)
                in_combat = True
                field_2 = False
                lib.play_music(lib.cts.Demon_Scream)

            # Enemies movement

            i = 0
            for enemy in enemies_group:
                distance = move_enemy(first_enemy_position[i], player.rect)
                if lib.mt.sqrt(lib.mt.pow(distance[0], 2) + lib.mt.pow(distance[1], 2)) > radio:
                    distance = move_enemy(first_enemy_position[i], enemy.rect)
                else:
                    distance = move_enemy(player.rect, enemy.rect)
                if distance[0] > 0:
                    enemy.velocity = [4, 4]
                else:
                    enemy.velocity = [-4, -4]

                if ((distance[0] >= -2) and (distance[0] <= 2)) and ((distance[1] >= -2) and (distance[1] <= 2)):
                    enemy.velocity = [0, 0]
                else:
                    if distance[0] == 0:
                        enemy.velocity = [-4, -4]
                        if distance[1] > 0:
                            angle = lib.mt.radians(270)
                        if distance[1] < 0:
                            angle = lib.mt.radians(90)
                    else:
                        angle = lib.mt.atan(distance[1] / distance[0])
                        enemy.angle = angle
                i += 1

                # Generators

                for generator in generators_group:
                    if generator.temp < 0:
                        worm = GeneratedEnemy(generator.rect.center, lib.cts.random_enemies_2)
                        random_enemies_group.add(worm)
                        generator.temp = 60

                # Worms cleaning

                for worm in random_enemies_group:
                    if worm.rect.x < -50:
                        random_enemies_group.remove(worm)
                    if worm.rect.y < -50:
                        random_enemies_group.remove(worm)
                    if worm.rect.x > lib.cts.width:
                        random_enemies_group.remove(worm)
                    if worm.rect.y > lib.cts.height:
                        random_enemies_group.remove(worm)

                # Generated enemies

                random_collide = pg.sprite.spritecollide(player, random_enemies_group, False)

                for random_enemies in random_collide:
                    lib.play_music(lib.cts.worm)
                    random_enemies_group.remove(random_enemies)
                    player.live -= 1

                # Buffs

                buff_collide = pg.sprite.spritecollide(player, buffs_group, True)

                for buffs in buff_collide:
                    if buffs.buff == 1:
                        player.extra_live += 1
                    elif buffs.buff == 2:
                        player.extra_energy += 1
                    elif buffs.buff == 3:
                        player.drake_smash += 1
                    elif buffs.buff >= 4:
                        player.wings_buff += 1

                    buffs_group.remove(buffs)

                # Death by worms

                if player.live <= 0:
                    in_combat = False
                    field_2 = False
                    death = True
                    run = False
                    lib.play_music(lib.cts.Fail)

            # Drawing
            lib.fill(window)

            scenario.update()

            first_enemy_position = scenario.move_enemies(first_enemy_position)

            generators_group.update()
            generators_group.draw(window)

            buffs_group.update()
            buffs_group.draw(window)

            random_enemies_group.update(scenario.background_velocity)
            random_enemies_group.draw(window)

            enemies_group.update(scenario.background_velocity)
            enemies_group.draw(window)

            things_group.update()
            things_group.draw(window)

            lvl_information.update()

            NPCs_group.update()
            NPCs_group.draw(window)

            players_group.update(key, window)
            players_group.draw(window)

            # Generator interaction
            generator_collide = pg.sprite.spritecollide(player, generators_group, False)

            for generator in generator_collide:
                window.blit(lib.cts.Dialog_box, [400, 400])
                holes_dialogue.update()

                if catchable:
                    potion = Buffs([generator.rect.x, generator.rect.y], lib.rd.randrange(1, 5))
                    buffs_group.add(potion)

                    generators_group.remove(generator)
                    catchable = False

            # npc
            for saku in NPCs_group:
                if len(enemies_group) == 0:

                    player.radius = 50

                    for _ in npc_dialogue_group:
                        npc_dialogue_group.remove(_)

                    new_text_position = [450, 450]
                    for _ in range(0, len(lib.cts.dialogue_7_1_2)):
                        saku_dialogue = Texts(new_text_position, window, lib.cts.dialogue_7_1_2[_], 25, 2)
                        saku_dialogue.velocity = [0, 0]
                        new_text_position[1] += 25
                        npc_dialogue_group.add(saku_dialogue)

                    if you_got_armor:

                        player.current_armor = [0, 0, 0, 0, 0, 0]

                        for _ in npc_dialogue_group:
                            npc_dialogue_group.remove(_)

                        new_text_position = [450, 450]
                        for _ in range(0, len(lib.cts.dialogue_7_1_3)):
                            saku_dialogue = Texts(new_text_position, window, lib.cts.dialogue_7_1_3[_], 30, 2)
                            saku_dialogue.velocity = [0, 0]
                            new_text_position[1] += 25
                            npc_dialogue_group.add(saku_dialogue)

                if pg.sprite.collide_circle(saku, player):
                    lib.play_music(lib.cts.Hmm_Women, 0)
                    window.blit(lib.cts.Dialog_box, [400, 400])
                    npc_dialogue_group.update()
                    lib.stop_music()

            lib.frames_per_second(fps, 1)

        # Settings variables

        turn = 1
        catchable = True
        get_point = True
        progressive = True

        while in_combat:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
                    run = False
                if event.type == pg.KEYDOWN and turn == 1:

                    # Player attacks

                    if event.key == pg.K_q:
                        if player.energy >= 1:
                            player.attack(1)
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.Punch)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    if event.key == pg.K_w:
                        if player.energy >= 3:
                            player.attack(2)
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.Sword_Swing)
                        else:
                            turn = 2
                    if event.key == pg.K_e:
                        if player.energy >= 5:
                            player.transformation = True
                            player.attack(3)
                            turn = 0
                            cont = 0
                            lib.play_music(lib.cts.Transformation_1)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    if event.key == pg.K_r:
                        if player.energy >= 3:
                            if player.transformation:
                                player.attack(4)
                                turn = 0
                                cont = 0
                                lib.play_music(lib.cts.Dragon_Roar_Breathe_Fire)
                            else:
                                catchable = False
                                cont = 0
                                turn = 1
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)

                    # Inventory

                    if event.key == pg.K_t:
                        turn = 3
                        cont = 0
                        lib.play_music(lib.cts.Inventory)

                    if event.key == pg.K_a:
                        if player.drake_smash >= 1:
                            player.use_extras(3)
                            enemy.life = 0
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.MagicFinal)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    if event.key == pg.K_s:
                        if player.extra_live >= 1:
                            player.use_extras(1)
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.Grabing)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    if event.key == pg.K_d:
                        if player.extra_energy >= 1:
                            player.use_extras(2)
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.Grabing)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    # Skip turn
                    if event.key == pg.K_f:
                        player.energy += 1
                        player.live += 1
                        cont = 0
                        turn = 0
                        lib.play_music(lib.cts.Lost)

                    # Restating variables

                    if turn == 0:
                        player.energy += 2

                    progressive = True

            # Drawing

            lib.fill(window)

            window.blit(lib.cts.Battle_ground, [0, 0])

            enemy.show_statistics(window)
            enemy.in_combat(window)

            player.in_combat(window)

            # Control

            # Enemies turn

            if turn == 0:
                for enemy in enemies_in_combat:
                    if cont == 0:
                        enemy_ability = enemy.enemy_attack(player.damage)
                        player.damage = 0

                    if enemy.life <= 0:
                        enemies_in_combat.remove(enemy)
                    else:
                        window.blit(lib.cts.Dialog_box, [400, 400])
                        window.blit(enemy_ability, [450, 450])

                if cont > 100:
                    turn = 1
                cont += 1

            if len(enemies_in_combat) == 0:
                win.update()

                if player.level_points == next_level:
                    player.current_level += 1
                    level_up.update()
                    get_point = True

                player.transformation = False

                if cont > 100:
                    player.velocity = [0, 0]
                    key = 0

                    in_combat = False
                    field_2 = True
                cont += 1

            # Player turn

            if turn == 1:
                for enemy in enemies_in_combat:
                    player.hurts(enemy.damage)

                    if enemy.progressive_damage > 0 and progressive:
                        enemy.progressive_damage -= 1
                        progressive = False
                        player.live -= 1
                        lib.play_music(lib.cts.Pain)

                    enemy.damage = 0

                if player.live <= 0:
                    in_combat = False
                    field_2 = False
                    death = True
                    lib.play_music(lib.cts.Fail)

                window.blit(lib.cts.Combat_box, [0, 400])

                player.show_statistics(window)

                if catchable:
                    abilities_in_combat.update()
                    cont = 0
                else:
                    attacks_information.update()
                    if cont > 100:
                        catchable = True
                        turn = 1
                    cont += 1

            # Informative turns

            if turn == 2:
                window.blit(lib.cts.Dialog_box, [0, 400])
                statistics_information.update()
                player.energy -= 2
                if cont > 100:
                    turn = 1
                cont += 1

            if turn == 3:
                window.blit(lib.cts.Dialog_box, [0, 400])
                inventory_information.update()
                if cont > 100:
                    turn = 1
                cont += 1

            lib.frames_per_second(fps, 1)

        # Resetting win label
        win.x, win.y = [400, 300]
        level_up.x, level_up.y = [450, 400]
        if player.level_points < next_level and get_point:
            player.level_points += 1
            get_point = False

    for _ in enemies_group:
        enemies_group.remove(_)

    for _ in things_group:
        things_group.remove(_)

    for _ in NPCs_group:
        NPCs_group.remove(_)

    for _ in generators_group:
        generators_group.remove(_)

    for _ in enemies_in_combat:
        enemies_in_combat.remove(_)

    for _ in random_enemies_group:
        random_enemies_group.remove(_)

    for _ in dialogue_group:
        dialogue_group.remove(_)

    for _ in lvl_information:
        lvl_information.remove(_)

    # Background
    current_scenario = 5
    scenario.background = current_scenario

    # Background position
    scenario.change_image()
    scenario.rect.x, scenario.rect.y = [0, -25]

    # Repositioning player
    player.rect.x = 50
    player.rect.y = 50

    angle = 0
    radio = 300
    distance = [0, 0]

    """

    first_enemy_position = [[250, 300], [600, 500], [550, 850],
                            [1800, 700], [2000, 500], [1900, 300]]

    for _ in range(len(first_enemy_position) - 3):
        enemy = SimpleEnemy(first_enemy_position[_], 1)
        enemies_group.add(enemy)

    for _ in range(2, 5):
        enemy = SimpleEnemy(first_enemy_position[_], 2)
        enemies_group.add(enemy)
        
    """

    Balzar = NonPlayableCharacters([200, 80], 2)
    NPCs_group.add(Balzar)
    key = 0

    new_text_position = [450, 430]
    for _ in range(0, len(lib.cts.dialogue_8)):
        new_text = Texts(new_text_position, window, lib.cts.dialogue_8[_], 25, 2)
        new_text.velocity = [0, 0]
        new_text_position[1] += 40
        text_group.add(new_text)

    new_text_position = [450, 430]
    for _ in range(0, len(lib.cts.dialogue_9)):
        new_text = Texts(new_text_position, window, lib.cts.dialogue_9[_], 25, 2)
        new_text.velocity = [0, 0]
        new_text_position[1] += 40
        dialogue_group.add(new_text)

    cont = 0
    value = 1

    boss_spawn = [200, 80]
    boss = Boss(boss_spawn)
    boss_group.add(boss)

    lvl_info = Texts([730, 570], window, lib.cts.lvl_info[5], 25, 2, lib.cts.RED)
    lvl_info.velocity = [0, 0]
    lvl_information.add(lvl_info)

    player.live = player.max_hp
    player.energy = player.max_energy

    while run and field_3 or in_combat:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        while field_3:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
                    field_3 = False
                    run = False
                if event.type == pg.KEYDOWN:
                    key = 1
                    if event.key == pg.K_p:
                        player.show_inventory(window)
                    if event.key == pg.K_i:
                        player.skill_sheet(window)
                    if event.key == pg.K_s:
                        player.velocity[1] += player.speed
                        player.action = 3
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_w:
                        player.velocity[1] -= player.speed
                        player.action = 1
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_d:
                        player.velocity[0] += player.speed
                        player.action = 0
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_a:
                        player.velocity[0] -= player.speed
                        player.action = 2
                        lib.play_music(lib.cts.Running, -1, 2.0)
                if event.type == pg.KEYUP:
                    player.velocity = [0, 0]
                    key = 0
                    lib.stop_music()

            # Control

            # Background

            if player.rect.x > scenario.screen_limits[0]:
                player.rect.x = scenario.screen_limits[0]
                if scenario.rect.x > scenario.background_limits[0]:
                    scenario.background_velocity[0] = 5
                    for _ in things_group:
                        _.thing_velocity[0] = -5
                    Balzar.npc_velocity[0] = -5

                else:
                    scenario.background_velocity[0] = 0
                    for _ in things_group:
                        _.thing_velocity[0] = 0
                    Balzar.npc_velocity[0] = 0
            else:
                if player.rect.x < lib.cts.width - scenario.screen_limits[0]:
                    player.rect.x = lib.cts.width - scenario.screen_limits[0]
                    if scenario.rect.x < lib.cts.width * 2 + scenario.background_limits[0]:
                        scenario.background_velocity[0] = -5
                        for _ in things_group:
                            _.thing_velocity[0] = 5
                        Balzar.npc_velocity[0] = 5
                    else:
                        scenario.background_velocity[0] = 0
                        for _ in things_group:
                            _.thing_velocity[0] = 0
                        Balzar.npc_velocity[0] = 0
                else:
                    if scenario.rect.x > lib.cts.width - scenario.background_limits[0]:
                        scenario.background_velocity[0] = 5
                        for _ in things_group:
                            _.thing_velocity[0] = -5
                        Balzar.npc_velocity[0] = -5
                    else:
                        scenario.background_velocity[0] = 0
                        for _ in things_group:
                            _.thing_velocity[0] = 0
                        Balzar.npc_velocity[0] = 0

            if player.rect.y > scenario.screen_limits[1]:
                player.rect.y = scenario.screen_limits[1]
                if scenario.rect.y > scenario.background_limits[1]:
                    scenario.background_velocity[1] = -5
                    for _ in things_group:
                        _.thing_velocity[1] = -5
                    Balzar.npc_velocity[1] = -5
                else:
                    scenario.background_velocity[1] = 0
                    for _ in things_group:
                        _.thing_velocity[1] = 0
                    Balzar.npc_velocity[1] = 0
            else:
                if player.rect.y < lib.cts.height - scenario.screen_limits[1]:
                    player.rect.y = lib.cts.height - scenario.screen_limits[1]
                    if scenario.rect.y < 0:
                        scenario.background_velocity[1] = 5
                        for _ in things_group:
                            _.thing_velocity[1] = 5
                        Balzar.npc_velocity[1] = 5
                    else:
                        scenario.background_velocity[1] = 0
                        for _ in things_group:
                            _.thing_velocity[1] = 0
                        Balzar.npc_velocity[1] = 0
                else:
                    if scenario.rect.y > lib.cts.height - scenario.background_limits[1]:
                        scenario.background_velocity[1] = -5
                        for _ in things_group:
                            _.thing_velocity[1] = -5
                        Balzar.npc_velocity[1] = -5
                    else:
                        scenario.background_velocity[1] = 0
                        for _ in things_group:
                            _.thing_velocity[1] = 0
                        Balzar.npc_velocity[1] = 0

            # Enemies

            enemy_collide = pg.sprite.spritecollide(player, enemies_group, True)

            for enemy in enemy_collide:
                enemies_in_combat.add(enemy)
                in_combat = True
                field_3 = False
                lib.play_music(lib.cts.Demon_Scream)

            i = 0
            for enemy in enemies_group:
                distance = move_enemy(first_enemy_position[i], player.rect)
                if lib.mt.sqrt(lib.mt.pow(distance[0], 2) + lib.mt.pow(distance[1], 2)) > radio:
                    distance = move_enemy(first_enemy_position[i], enemy.rect)
                else:
                    distance = move_enemy(player.rect, enemy.rect)
                if distance[0] > 0:
                    enemy.velocity = [4, 4]
                else:
                    enemy.velocity = [-4, -4]

                if ((distance[0] >= -2) and (distance[0] <= 2)) and ((distance[1] >= -2) and (distance[1] <= 2)):
                    enemy.velocity = [0, 0]
                else:
                    if distance[0] == 0:
                        enemy.velocity = [-4, -4]
                        if distance[1] > 0:
                            angle = lib.mt.radians(270)
                        if distance[1] < 0:
                            angle = lib.mt.radians(90)
                    else:
                        angle = lib.mt.atan(distance[1] / distance[0])
                        enemy.angle = angle
                i += 1

            # Boss

            if len(enemies_group) == 0:
                attack_direction = 0
                i = 0
                for boss in boss_group:
                    if temp_while_shooting > 0:
                        boss.velocity = [0, 0]
                    else:
                        distance = move_enemy(player.rect, boss.rect)
                        lib.play_music(lib.cts.MonsterRun, -1)
                        if distance[0] > 0:
                            boss.velocity = [5, 5]
                        else:
                            boss.velocity = [-5, -5]

                        if ((distance[0] >= -2) and (distance[0] <= 2)) and (
                                (distance[1] >= -2) and (distance[1] <= 2)):
                            boss.velocity = [0, 0]
                        else:
                            if distance[0] == 0:
                                boss.velocity = [-5, -5]
                                if distance[1] > 0:
                                    angle = lib.mt.radians(270)
                                if distance[1] < 0:
                                    angle = lib.mt.radians(90)
                            else:
                                angle = lib.mt.atan(distance[1] / distance[0])
                                boss.angle = angle
                        i += 1

                    if current_attack == 1:
                        if boss.temp < 0:
                            attack_bomb(boss)
                            temp_while_shooting = 15
                            lib.play_music(lib.cts.MagicCaos, 2)
                            if attack_before_pause == -2:
                                boss.temp = 200
                                attack_before_pause = 4
                            else:
                                boss.temp = 15
                                attack_before_pause -= 1

                    elif current_attack == 2:
                        if boss.temp < 0:
                            lib.play_music(lib.cts.MagicCaos, 2)
                            attack_angelic_bomb(boss)
                            temp_while_shooting = 15
                            if attack_before_pause == -50:
                                boss.temp = 200
                                attack_before_pause = 4
                            else:
                                boss.temp = 3
                                attack_before_pause -= 1

                    elif current_attack == 3:
                        if boss.temp < 0:
                            lib.play_music(lib.cts.MagicCaos, 2)
                            attack_spiral(boss)
                            temp_while_shooting = 15
                            if attack_before_pause == -200:
                                boss.temp = 200
                                attack_before_pause = 4
                            else:
                                boss.temp = 1
                                attack_before_pause -= 1

                temp_while_shooting -= 1

            attack_collide = pg.sprite.spritecollide(player, attack_group, True)

            for _ in attack_collide:
                attack_group.remove(_)
                player.live -= 1

            if player.live <= 0:
                in_combat = False
                field_3 = False
                death = True
                run = False
                lib.play_music(lib.cts.Fail)

            # Drawing
            lib.fill(window)

            scenario.update()

            first_enemy_position = scenario.move_enemies(first_enemy_position)

            things_group.update()
            things_group.draw(window)

            lvl_info.update()

            players_group.update(key, window)
            players_group.draw(window)

            enemies_group.update(scenario.background_velocity)
            enemies_group.draw(window)

            if len(enemies_group) > 0:
                NPCs_group.update()
                NPCs_group.draw(window)

                if 200 + scenario.rect.x < player.rect.x < 250 + scenario.rect.x:
                    if 170 + scenario.rect.y > player.rect.y > 100 + scenario.rect.y:
                        window.blit(lib.cts.Dialog_box, [400, 400])
                        text_group.update()

                        lvl_info = Texts([730, 570], window, lib.cts.lvl_info[6], 25, 2, lib.cts.RED)
                        lvl_info.velocity = [0, 0]
            else:
                cont += value

                if cont < 230:
                    window.blit(lib.cts.Dialog_box, [400, 400])
                    dialogue_group.update()

                if cont == 230:
                    NPCs_group.remove(Balzar)
                    lvl_info = Texts([1030, 570], window, lib.cts.lvl_info[7], 25, 2, lib.cts.RED)
                    lvl_info.velocity = [0, 0]

                if cont > 230:
                    current_attack = 1

                if cont > 1030:
                    current_attack = 3

                if cont > 2050:
                    current_attack = 2

                if cont > 2350:
                    current_attack = 0

                if cont > 2500:
                    boss.live = 0
                    current_attack = 0

                if boss.live == 0:
                    player.drake_smash = 0

                    for _ in boss_group:
                        boss_group.remove(_)

                    for _ in attack_group:
                        attack_group.remove(_)

                    lvl_info = Texts([830, 570], window, lib.cts.lvl_info[8], 25, 2, lib.cts.RED)
                    lvl_info.velocity = [0, 0]

                    enemy_Balzar = SimpleEnemy(boss.get_position(), 3)
                    enemies_group.add(enemy_Balzar)

                    value = 0

                if cont > 230 and len(boss_group):
                    distance = [0, 0]
                    if len(enemies_group) == 0:
                        boss_group.update(scenario.background_velocity)
                        for boss in boss_group:
                            boss.cont -= 1
                            boss.temp -= 1
                        boss_group.draw(window)

                        attack_group.update(scenario.background_velocity)
                        attack_group.draw(window)

                        for _ in attack_group:
                            if _.rect.x < 0:
                                attack_group.remove(_)
                            if _.rect.y < 0:
                                attack_group.remove(_)
                            if _.rect.x > lib.cts.width:
                                attack_group.remove(_)
                            if _.rect.y > lib.cts.height:
                                attack_group.remove(_)

            lib.frames_per_second(fps, 1)

        # Settings variables

        turn = 1
        catchable = True
        get_point = True
        progressive = True

        while in_combat:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
                    run = False
                if event.type == pg.KEYDOWN and turn == 1:

                    # Player attacks

                    if event.key == pg.K_q:
                        if player.energy >= 1:
                            player.attack(1)
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.Punch)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    if event.key == pg.K_w:
                        if player.energy >= 3:
                            player.attack(2)
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.Sword_Swing)
                        else:
                            turn = 2
                    if event.key == pg.K_e:
                        if player.energy >= 5:
                            player.transformation = True
                            player.attack(3)
                            turn = 0
                            cont = 0
                            lib.play_music(lib.cts.Transformation_1)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    if event.key == pg.K_r:
                        if player.energy >= 3:
                            if player.transformation:
                                player.attack(4)
                                turn = 0
                                cont = 0
                                lib.play_music(lib.cts.Dragon_Roar_Breathe_Fire)
                            else:
                                catchable = False
                                cont = 0
                                turn = 1
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)

                    # Inventory

                    if event.key == pg.K_t:
                        turn = 3
                        cont = 0
                        lib.play_music(lib.cts.Inventory)

                    if event.key == pg.K_a:
                        if player.drake_smash >= 1:
                            player.use_extras(3)
                            enemy.life = 0
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.MagicFinal)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    if event.key == pg.K_s:
                        if player.extra_live >= 1:
                            player.use_extras(1)
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.Grabing)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    if event.key == pg.K_d:
                        if player.extra_energy >= 1:
                            player.use_extras(2)
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.Grabing)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    # Skip turn
                    if event.key == pg.K_f:
                        player.energy += 1
                        player.live += 1
                        cont = 0
                        turn = 0
                        lib.play_music(lib.cts.Lost)

                    # Restating variables

                    if turn == 0:
                        player.energy += 2

                    progressive = True

            # Drawing

            lib.fill(window)

            window.blit(lib.cts.Battle_ground, [0, 0])

            enemy.show_statistics(window)
            enemy.in_combat(window)

            player.in_combat(window)

            # Control

            # Enemies turn

            if turn == 0:
                for enemy in enemies_in_combat:
                    if cont == 0:
                        enemy_ability = enemy.enemy_attack(player.damage)
                        player.damage = 0

                    if enemy.life <= 0:
                        enemies_in_combat.remove(enemy)
                    else:
                        window.blit(lib.cts.Dialog_box, [400, 400])
                        window.blit(enemy_ability, [450, 450])

                if cont > 100:
                    turn = 1
                cont += 1

            if len(enemies_in_combat) == 0:
                win.update()

                if player.level_points == next_level:
                    player.current_level += 1
                    level_up.update()
                    get_point = True

                player.transformation = False

                if cont > 100:
                    player.velocity = [0, 0]
                    key = 0

                    in_combat = False
                    field_3 = True
                cont += 1

            # Player turn

            if turn == 1:
                for enemy in enemies_in_combat:
                    player.hurts(enemy.damage)

                    if enemy.progressive_damage > 0 and progressive:
                        enemy.progressive_damage -= 1
                        progressive = False
                        player.live -= 1
                        lib.play_music(lib.cts.Pain)

                    enemy.damage = 0

                if player.live <= 0:
                    in_combat = False
                    field_3 = False
                    death = True
                    lib.play_music(lib.cts.Fail)

                window.blit(lib.cts.Combat_box, [0, 400])

                player.show_statistics(window)

                if catchable:
                    abilities_in_combat.update()
                    cont = 0
                else:
                    attacks_information.update()
                    if cont > 100:
                        catchable = True
                        turn = 1
                    cont += 1

            # Informative turns

            if turn == 2:
                window.blit(lib.cts.Dialog_box, [0, 400])
                statistics_information.update()
                player.energy -= 2
                if cont > 100:
                    turn = 1
                cont += 1

            if turn == 3:
                window.blit(lib.cts.Dialog_box, [0, 400])
                inventory_information.update()
                if cont > 100:
                    turn = 1
                cont += 1

            lib.frames_per_second(fps, 1)

        # Resetting win label
        win.x, win.y = [400, 300]
        level_up.x, level_up.y = [450, 400]
        if player.level_points < next_level and get_point:
            player.level_points += 1
            get_point = False

    # Story # 1

    # Cleaning

    for _ in enemies_group:
        enemies_group.remove(_)

    for _ in boss_group:
        boss_group.remove(_)

    for _ in NPCs_group:
        NPCs_group.remove(_)

    for _ in enemies_in_combat:
        enemies_in_combat.remove(_)

    for _ in dialogue_group:
        dialogue_group.remove(_)

    for _ in lvl_information:
        lvl_information.remove(_)

    for _ in text_group:
        text_group.remove(_)

    # Chapter title

    Title = Texts([25, 250], window, lib.cts.Balzar_is_death, 200)
    Title.velocity = [0, 0]
    title_group.add(Title)

    # Chapter I intro

    new_text_position = [50, 750]
    for _ in range(0, len(lib.cts.Town_story)):
        lib.play_music(lib.cts.Intro_3)
        new_text = Texts(new_text_position, window, lib.cts.Town_story[_], 30, 2)
        new_text_position[1] += 50
        text_group.add(new_text)

    # Game button skip

    Skip = Texts([1080, 550], window, lib.cts.skip, 20)
    Skip.velocity = [0, 0]
    title_group.add(Skip)

    window = lib.new_window("Chapter I")

    while run and story_1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                lib.stop_music()
            if event.type == pg.MOUSEBUTTONDOWN:
                story_1 = False
                lib.stop_music()

        # Drawing and control

        lib.fill(window)

        Title.update()

        if cont >= 100:
            Title.velocity = [0, -1]
            text_group.update()
            Skip.update()

        cont += 1

        for _ in text_group:
            if _.y < 0:
                text_group.remove(_)

        for _ in title_group:
            if _.y <= 0:
                title_group.remove(_)

        if len(text_group) == 0:
            story_1 = False

        lib.frames_per_second(fps, 2)
    lib.stop_music()

    # Cleaning

    for _ in title_group:
        title_group.remove(_)

    for _ in text_group:
        text_group.remove(_)

    # Background

    current_scenario = 6
    scenario.background = current_scenario

    # Background position
    scenario.change_image()
    scenario.rect.x, scenario.rect.y = [0, 0]

    # Repositioning player
    player.rect.x = 90
    player.rect.y = 50
    player.radius = 50

    npc_position = [[540, 110], [1555, 670], [1630, 920], [1515, 3075],
                    [1325, 3120], [260, 3260], [110, 1560], [1525, 1325],
                    [1800, 1930]]

    cont = 3

    # Adding things
    current_house = 22
    for _ in [[175, 1075], [375, 2825], [1175, 2525], [1750, 1150], [1725, 400]]:
        house = Things(_, current_house)
        things_group.add(house)
        current_house += 1

    # Adding npc
    Saku = NonPlayableCharacters(npc_position[0], cont)
    NPCs_group.add(Saku)
    cont += 1
    Spidy = NonPlayableCharacters(npc_position[1], cont)
    NPCs_group.add(Spidy)
    cont += 1
    Elise = NonPlayableCharacters(npc_position[2], cont)
    NPCs_group.add(Elise)
    cont += 1
    Goldi = NonPlayableCharacters(npc_position[3], cont)
    NPCs_group.add(Goldi)
    cont += 1
    Helen = NonPlayableCharacters(npc_position[4], cont)
    NPCs_group.add(Helen)
    cont += 1
    Marian = NonPlayableCharacters(npc_position[5], cont)
    NPCs_group.add(Marian)
    cont += 1
    Clarissa = NonPlayableCharacters(npc_position[6], cont)
    NPCs_group.add(Clarissa)
    cont += 1
    Elizabeth = NonPlayableCharacters(npc_position[7], cont)
    NPCs_group.add(Elizabeth)

    Manuela = NonPlayableCharacters(npc_position[8], 1)
    NPCs_group.add(Manuela)

    lvl_info = Texts([900, 570], window, lib.cts.lvl_info[9], 25, 2, lib.cts.RED)
    lvl_info.velocity = [0, 0]
    lvl_information.add(lvl_info)

    key = 0
    open_portal = False
    add_item = [False, False, False]

    window = lib.new_window("Euphoria")

    while run and field_4:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        while field_4:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
                    field_4 = False
                    run = False

                # Player movement

                if event.type == pg.KEYDOWN:
                    key = 1
                    if event.key == pg.K_p:
                        player.show_inventory(window)
                    if event.key == pg.K_i:
                        player.skill_sheet(window)
                    if event.key == pg.K_s:
                        player.velocity[1] += player.speed
                        player.action = 3
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_w:
                        player.velocity[1] -= player.speed
                        player.action = 1
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_d:
                        player.velocity[0] += player.speed
                        player.action = 0
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_a:
                        player.velocity[0] -= player.speed
                        player.action = 2
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_e:
                        catchable = False
                if event.type == pg.KEYUP:
                    player.velocity = [0, 0]
                    key = 0
                    lib.stop_music()

            # Control

            # Scenario movement

            if player.rect.x > scenario.screen_limits[0]:
                player.rect.x = scenario.screen_limits[0]
                if scenario.rect.x > scenario.background_limits[0]:
                    scenario.background_velocity[0] = 5
                    for _ in things_group:
                        _.thing_velocity[0] = -5
                    for _ in NPCs_group:
                        _.npc_velocity[0] = -5
                else:
                    scenario.background_velocity[0] = 0
                    for _ in things_group:
                        _.thing_velocity[0] = 0
                    for _ in NPCs_group:
                        _.npc_velocity[0] = 0
            else:
                if player.rect.x < lib.cts.width - scenario.screen_limits[0]:
                    player.rect.x = lib.cts.width - scenario.screen_limits[0]
                    if scenario.rect.x < lib.cts.width + scenario.background_limits[0]:
                        scenario.background_velocity[0] = -5
                        for _ in things_group:
                            _.thing_velocity[0] = 5
                        for _ in NPCs_group:
                            _.npc_velocity[0] = 5
                    else:
                        scenario.background_velocity[0] = 0
                        for _ in things_group:
                            _.thing_velocity[0] = 0
                        for _ in NPCs_group:
                            _.npc_velocity[0] = 0
                else:
                    if scenario.rect.x > lib.cts.width + scenario.background_limits[0]:
                        scenario.background_velocity[0] = 5
                        for _ in things_group:
                            _.thing_velocity[0] = -5
                        for _ in NPCs_group:
                            _.npc_velocity[0] = -5
                    else:
                        scenario.background_velocity[0] = 0
                        for _ in things_group:
                            _.thing_velocity[0] = 0
                        for _ in NPCs_group:
                            _.npc_velocity[0] = 0

            if player.rect.y > scenario.screen_limits[1]:
                player.rect.y = scenario.screen_limits[1]
                if scenario.rect.y > scenario.background_limits[1]:
                    scenario.background_velocity[1] = -5
                    for _ in things_group:
                        _.thing_velocity[1] = -5
                    for _ in NPCs_group:
                        _.npc_velocity[1] = -5
                else:
                    scenario.background_velocity[1] = 0
                    for _ in things_group:
                        _.thing_velocity[1] = 0
                    for _ in NPCs_group:
                        _.npc_velocity[1] = 0
            else:
                if player.rect.y < lib.cts.height - scenario.screen_limits[1]:
                    player.rect.y = lib.cts.height - scenario.screen_limits[1]
                    if scenario.rect.y < 0:
                        scenario.background_velocity[1] = 5
                        for _ in things_group:
                            _.thing_velocity[1] = 5
                        for _ in NPCs_group:
                            _.npc_velocity[1] = 5
                    else:
                        scenario.background_velocity[1] = 0
                        for _ in things_group:
                            _.thing_velocity[1] = 0
                        for _ in NPCs_group:
                            _.npc_velocity[1] = 0
                else:
                    if scenario.rect.y > scenario.background_limits[1] + lib.cts.height * 5:
                        scenario.background_velocity[1] = -5
                        for _ in things_group:
                            _.thing_velocity[1] = -5
                        for _ in NPCs_group:
                            _.npc_velocity[1] = -5
                    else:
                        scenario.background_velocity[1] = 0
                        for _ in things_group:
                            _.thing_velocity[1] = 0
                        for _ in NPCs_group:
                            _.npc_velocity[1] = 0

            # Portal

            if open_portal:
                portal = Things([150, 300], 27)
                portals_group.add(portal)

                list_portal = pg.sprite.spritecollide(player, portals_group, False)

                for _ in list_portal:
                    field_4 = False
                    field_5 = True

            # Updating & Drawing

            lib.fill(window)

            scenario.update()

            things_group.update()
            things_group.draw(window)

            portals_group.update()
            portals_group.draw(window)

            lvl_info.update()

            NPCs_group.update()
            NPCs_group.draw(window)

            players_group.update(key, window)
            players_group.draw(window)

            # Text interactions

            # npc
            for npc in NPCs_group:
                size = 25
                npc_dialogue = None
                distance_between_paragraphs = 25

                if pg.sprite.collide_circle(npc, player):
                    lib.play_music(lib.cts.Hmm_Women, 0)
                    window.blit(lib.cts.Dialog_box, [400, 400])

                    for _ in npc_dialogue_group:
                        npc_dialogue_group.remove(_)

                    if npc.id == 'Saku':
                        npc_dialogue = lib.cts.dialogue_10
                        if not add_item[0]:
                            player.add_inventory(1)
                            player.add_inventory(2)
                            player.add_inventory(5)
                            add_item[0] = True
                        lvl_info = Texts([940, 570], window, lib.cts.lvl_info[10], 25, 2, lib.cts.RED)
                        lvl_info.velocity = [0, 0]
                        lvl_information.add(lvl_info)
                    elif npc.id == 'Spidy':
                        npc_dialogue = lib.cts.dialogue_11
                    elif npc.id == 'Elise':
                        npc_dialogue = lib.cts.dialogue_12
                    elif npc.id == 'Goldi':
                        npc_dialogue = lib.cts.dialogue_13
                    elif npc.id == 'Helen':
                        npc_dialogue = lib.cts.dialogue_14
                    elif npc.id == 'Marian':
                        npc_dialogue = lib.cts.dialogue_15
                        size = 20
                        open_portal = True
                        distance_between_paragraphs = 13
                        lvl_info = Texts([400, 570], window, lib.cts.lvl_info[12], 25, 2, lib.cts.RED)
                        lvl_info.velocity = [0, 0]
                        lvl_information.add(lvl_info)
                    elif npc.id == 'Clarissa':
                        size = 20
                        if not add_item[1]:
                            player.add_inventory(1)
                            add_item[1] = True
                        npc_dialogue = lib.cts.dialogue_16
                    elif npc.id == 'Elizabeth':
                        npc_dialogue = lib.cts.dialogue_17
                        if not add_item[2]:
                            player.current_armor = [0, 1, 0, 1, 1, 1]
                            add_item[2] = True
                    elif npc.id == 'Manuela':
                        size = 20
                        npc_dialogue = lib.cts.dialogue_18
                        lvl_info = Texts([960, 570], window, lib.cts.lvl_info[11], 25, 2, lib.cts.RED)
                        lvl_info.velocity = [0, 0]
                        lvl_information.add(lvl_info)

                    new_text_position = [450, 450]
                    for _ in range(0, len(npc_dialogue)):
                        current_npc_dialogue = Texts(new_text_position, window, npc_dialogue[_], size, 2)
                        current_npc_dialogue.velocity = [0, 0]
                        new_text_position[1] += distance_between_paragraphs
                        npc_dialogue_group.add(current_npc_dialogue)

                    lib.stop_music()

                    npc_dialogue_group.update()

            lib.frames_per_second(fps, 1)

    # Architect

    for _ in things_group:
        things_group.remove(_)

    for _ in NPCs_group:
        NPCs_group.remove(_)

    for _ in dialogue_group:
        dialogue_group.remove(_)

    for _ in lvl_information:
        lvl_information.remove(_)

    for _ in text_group:
        text_group.remove(_)

    # Background

    current_scenario = 7
    scenario.background = current_scenario

    # Background position
    scenario.change_image()
    scenario.rect.x, scenario.rect.y = [0, 0]

    # Repositioning player
    player.rect.x = 90
    player.rect.y = 50
    player.radius = 0

    lvl_info = Texts([880, 570], window, lib.cts.lvl_info[13], 25, 2, lib.cts.RED)
    lvl_info.velocity = [0, 0]
    lvl_information.add(lvl_info)

    # Architect creation

    current_position = 0

    angle = 0
    distance = [0, 0]
    bot_movement = [[1000, 0], [10, 0], [600, 250], [10, 500], [1100, 500],
                    [600, 0], [600, 500], [0, 250], [1100, 250]]

    bot = Boss(bot_movement[0], lib.cts.Enemy_6)
    bot.temp = 30
    bot.cont = 10
    bot.attack = 3
    boss_group.add(bot)
    iterator = 0

    key = 0
    cont = -1
    talking = False
    player.live += 5
    player.energy += 10

    while run and field_5 or in_combat:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        while field_5:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
                    field_5 = False
                    run = False

                # Player movement

                if event.type == pg.KEYDOWN:
                    key = 1
                    if event.key == pg.K_p:
                        player.show_inventory(window)
                    if event.key == pg.K_i:
                        player.skill_sheet(window)
                    if event.key == pg.K_s:
                        player.velocity[1] += player.speed
                        player.action = 3
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_w:
                        player.velocity[1] -= player.speed
                        player.action = 1
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_d:
                        player.velocity[0] += player.speed
                        player.action = 0
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_a:
                        player.velocity[0] -= player.speed
                        player.action = 2
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_e:
                        catchable = False
                if event.type == pg.KEYUP:
                    player.velocity = [0, 0]
                    key = 0
                    lib.stop_music()

            # Control

            if player.rect.x > 900 and not talking:
                cont = 1

            # Scenario movement

            if player.rect.x > scenario.screen_limits[0]:
                player.rect.x = scenario.screen_limits[0]
                if scenario.rect.x > scenario.background_limits[0]:
                    scenario.background_velocity[0] = 5
                else:
                    scenario.background_velocity[0] = 0
            else:
                if player.rect.x < lib.cts.width - scenario.screen_limits[0]:
                    player.rect.x = lib.cts.width - scenario.screen_limits[0]
                    if scenario.rect.x < scenario.background_limits[0] - lib.cts.width:
                        scenario.background_velocity[0] = -5
                    else:
                        scenario.background_velocity[0] = 0
                else:
                    if scenario.rect.x > lib.cts.width + scenario.background_limits[0]:
                        scenario.background_velocity[0] = 5
                    else:
                        scenario.background_velocity[0] = 0

            if player.rect.y > scenario.screen_limits[1]:
                player.rect.y = scenario.screen_limits[1]
                if scenario.rect.y > scenario.background_limits[1]:
                    scenario.background_velocity[1] = -5
                else:
                    scenario.background_velocity[1] = 0
            else:
                if player.rect.y < lib.cts.height - scenario.screen_limits[1]:
                    player.rect.y = lib.cts.height - scenario.screen_limits[1]
                    if scenario.rect.y < 0:
                        scenario.background_velocity[1] = 5
                    else:
                        scenario.background_velocity[1] = 0
                else:
                    if scenario.rect.y > scenario.background_limits[1] + lib.cts.height:
                        scenario.background_velocity[1] = -5
                    else:
                        scenario.background_velocity[1] = 0

            # Boss

            if talking:
                for bot in boss_group:
                    distance = move_enemy(bot_movement[iterator], bot.rect)
                    if distance[0] > 0:
                        bot.velocity = [6, 6]
                    else:
                        bot.velocity = [-6, -6]

                    range_attack = lib.rd.randrange(50)
                    if (range_attack == 5) and (bot.attack > 0):
                        bullet = Attacks_Architect(bot.get_position())
                        attack_group.add(bullet)
                        bot.attack -= 1
                    if ((distance[0] >= -2) and (distance[0] <= 2)) and ((distance[1] >= -2) and (distance[1] <= 2)):
                        bot.velocity = [0, 0]
                        bot.temp -= 1
                        if (bot.temp == 0) and (bot.cont > 0):
                            iterator = lib.rd.randrange(8)
                            while current_position == iterator:
                                iterator = lib.rd.randrange(8)
                            current_position = iterator
                            bot.temp = 30
                            bot.attack = 3
                            bot.cont -= 1
                    else:
                        if distance[0] == 0:
                            bot.velocity = [-6, -6]
                            if distance[1] > 0:
                                angle = lib.mt.radians(270)
                            if distance[1] < 0:
                                angle = lib.mt.radians(90)
                        else:
                            angle = lib.mt.atan(distance[1] / distance[0])
                            bot.angle = angle

            if boss.cont == 0:

                for _ in lvl_information:
                    lvl_information.remove(_)

                lvl_info = Texts([880, 570], window, lib.cts.lvl_info[13], 25, 2, lib.cts.RED)
                lvl_info.velocity = [0, 0]
                lvl_information.add(lvl_info)

            boss_collide = pg.sprite.spritecollide(player, boss_group, True)

            for boss in boss_collide:
                boss_group.remove(boss)
                enemies_in_combat.add(SimpleEnemy(boss.get_position(), 6))
                in_combat = True
                field_5 = False
                lib.play_music(lib.cts.Demon_Scream)

            # Bullets

            attack_collide = pg.sprite.spritecollide(player, attack_group, True)

            for _ in attack_collide:
                attack_group.remove(_)
                player.live -= 1

            if player.live <= 0:
                in_combat = False
                field_5 = False
                death = True
                run = False
                lib.play_music(lib.cts.Fail)

            for bullet in attack_group:
                if bullet.rect.y > lib.cts.height + 10:
                    attack_group.remove(bullet)

            # Updating & Drawing

            lib.fill(window)

            scenario.update()

            attack_group.update()
            attack_group.draw(window)

            lvl_info.update()

            players_group.update(key, window)
            players_group.draw(window)

            boss_group.update(scenario.background_velocity)
            boss_group.draw(window)

            if 55 > cont > -1:
                cont += 1
                new_text_position = [450, 450]
                for _ in range(0, len(lib.cts.dialogue_19)):
                    architect_dialogue = Texts(new_text_position, window, lib.cts.dialogue_19[_], 30, 2)
                    architect_dialogue.velocity = [0, 0]
                    new_text_position[1] += 25
                    dialogue_group.add(architect_dialogue)

                lib.play_music(lib.cts.Robotic_Sound, 0)
                window.blit(lib.cts.Dialog_box, [400, 400])
                dialogue_group.update()
                lib.stop_music()

                lib.stop_music()

            if cont == 50:
                talking = True

                for _ in lvl_information:
                    lvl_information.remove(_)

                lvl_info = Texts([1020, 570], window, lib.cts.lvl_info[14], 25, 2, lib.cts.RED)
                lvl_info.velocity = [0, 0]
                lvl_information.add(lvl_info)

            lib.frames_per_second(fps, 1)

        # Settings variables

        turn = 1
        catchable = True
        get_point = True
        progressive = True

        while in_combat:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
                    run = False
                if event.type == pg.KEYDOWN and turn == 1:

                    # Player attacks

                    if event.key == pg.K_q:
                        if player.energy >= 1:
                            player.attack(1)
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.Punch)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    if event.key == pg.K_w:
                        if player.energy >= 3:
                            player.attack(2)
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.Sword_Swing)
                        else:
                            turn = 2
                    if event.key == pg.K_e:
                        if player.energy >= 5:
                            player.transformation = True
                            player.attack(3)
                            turn = 0
                            cont = 0
                            lib.play_music(lib.cts.Transformation_1)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    if event.key == pg.K_r:
                        if player.energy >= 3:
                            if player.transformation:
                                player.attack(4)
                                turn = 0
                                cont = 0
                                lib.play_music(lib.cts.Dragon_Roar_Breathe_Fire)
                            else:
                                catchable = False
                                cont = 0
                                turn = 1
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)

                    # Inventory

                    if event.key == pg.K_t:
                        turn = 3
                        cont = 0
                        lib.play_music(lib.cts.Inventory)

                    if event.key == pg.K_a:
                        if player.drake_smash >= 1:
                            player.use_extras(3)
                            enemy.life = 0
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.MagicFinal)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    if event.key == pg.K_s:
                        if player.extra_live >= 1:
                            player.use_extras(1)
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.Grabing)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    if event.key == pg.K_d:
                        if player.extra_energy >= 1:
                            player.use_extras(2)
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.Grabing)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    # Skip turn
                    if event.key == pg.K_f:
                        player.energy += 1
                        player.live += 1
                        cont = 0
                        turn = 0
                        lib.play_music(lib.cts.Lost)

                    # Restating variables

                    if turn == 0:
                        player.energy += 2

                    progressive = True

            # Drawing

            lib.fill(window)

            window.blit(lib.cts.Battle_ground, [0, 0])

            enemy.show_statistics(window)
            enemy.in_combat(window)

            player.in_combat(window)

            # Control

            # Enemies turn

            if turn == 0:
                for enemy in enemies_in_combat:
                    if cont == 0:
                        enemy_ability = enemy.enemy_attack(player.damage)
                        player.damage = 0

                    if enemy.life <= 0:
                        enemies_in_combat.remove(enemy)
                    else:
                        window.blit(lib.cts.Dialog_box, [400, 400])
                        window.blit(enemy_ability, [450, 450])

                if cont > 100:
                    turn = 1
                cont += 1

            if len(enemies_in_combat) == 0:
                win.update()

                if player.level_points == next_level:
                    player.current_level += 1
                    level_up.update()
                    get_point = True

                player.transformation = False

                if cont > 100:
                    player.velocity = [0, 0]
                    key = 0

                    in_combat = False
                    field_6 = True
                cont += 1

            # Player turn

            if turn == 1:
                for enemy in enemies_in_combat:
                    player.hurts(enemy.damage)

                    if enemy.progressive_damage > 0 and progressive:
                        enemy.progressive_damage -= 1
                        progressive = False
                        player.live -= 1
                        lib.play_music(lib.cts.Pain)

                    enemy.damage = 0

                if player.live <= 0:
                    in_combat = False
                    field_5 = False
                    death = True
                    lib.play_music(lib.cts.Fail)

                window.blit(lib.cts.Combat_box, [0, 400])

                player.show_statistics(window)

                if catchable:
                    abilities_in_combat.update()
                    cont = 0
                else:
                    attacks_information.update()
                    if cont > 100:
                        catchable = True
                        turn = 1
                    cont += 1

            # Informative turns

            if turn == 2:
                window.blit(lib.cts.Dialog_box, [0, 400])
                statistics_information.update()
                player.energy -= 2
                if cont > 100:
                    turn = 1
                cont += 1

            if turn == 3:
                window.blit(lib.cts.Dialog_box, [0, 400])
                inventory_information.update()
                if cont > 100:
                    turn = 1
                cont += 1

            lib.frames_per_second(fps, 1)

        # Resetting win label
        win.x, win.y = [400, 300]
        level_up.x, level_up.y = [450, 400]
        if player.level_points < next_level and get_point:
            player.level_points += 1
            get_point = False

    # Story # 2

    # Cleaning

    for _ in enemies_group:
        enemies_group.remove(_)

    for _ in boss_group:
        boss_group.remove(_)

    for _ in enemies_in_combat:
        enemies_in_combat.remove(_)

    for _ in dialogue_group:
        dialogue_group.remove(_)

    for _ in lvl_information:
        lvl_information.remove(_)

    # Chapter title

    Title = Texts([50, 250], window, lib.cts.Architect_was_destroyed, 100)
    Title.velocity = [0, 0]
    title_group.add(Title)

    # Chapter II intro

    new_text_position = [50, 750]
    for _ in range(0, len(lib.cts.God_story)):
        lib.play_music(lib.cts.Intro_3)
        new_text = Texts(new_text_position, window, lib.cts.God_story[_], 30, 2)
        new_text_position[1] += 50
        text_group.add(new_text)

    # Game button skip

    Skip = Texts([1080, 550], window, lib.cts.skip, 20)
    Skip.velocity = [0, 0]
    title_group.add(Skip)

    window = lib.new_window("Chapter II")

    while run and story_2:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                lib.stop_music()
            if event.type == pg.MOUSEBUTTONDOWN:
                story_2 = False
                lib.stop_music()

        # Drawing and control

        lib.fill(window)

        Title.update()

        if cont >= 100:
            Title.velocity = [0, -1]
            text_group.update()
            Skip.update()

        cont += 1

        for _ in text_group:
            if _.y < 0:
                text_group.remove(_)

        for _ in title_group:
            if _.y <= 0:
                title_group.remove(_)

        if len(text_group) == 0:
            story_2 = False

        lib.frames_per_second(fps, 2)
    lib.stop_music()

    # God

    for _ in things_group:
        things_group.remove(_)

    for _ in dialogue_group:
        dialogue_group.remove(_)

    for _ in lvl_information:
        lvl_information.remove(_)

    for _ in text_group:
        text_group.remove(_)

    # Background

    current_scenario = 8
    scenario.background = current_scenario

    # Background position
    scenario.change_image()
    scenario.rect.x, scenario.rect.y = [0, 0]

    # Repositioning player
    player.rect.x = 90
    player.rect.y = 50
    player.radius = 0

    lvl_info = Texts([830, 0], window, lib.cts.lvl_info[15], 25, 2, lib.cts.RED)
    lvl_info.velocity = [0, 0]
    lvl_information.add(lvl_info)

    # God creation
    god = Boss([1000, 400], lib.cts.Enemy_5)
    god.temp = 30
    god.cont = 40
    boss_group.add(god)

    god_attack(god.rect.center)

    rotting_shot_angle = 0
    stop_while_attack = 20
    attack_direction = 0
    distance = [0, 0]
    attack_angle = 0
    shot_tmp = 350
    ammo = 2

    key = 0
    cont = -1
    talking = False
    player.add_inventory(11)
    player.add_inventory(12)
    player.current_level = 6
    player.skill_points = 6

    while run and field_6 or in_combat:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        while field_6:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
                    field_6 = False
                    run = False

                # Player movement

                if event.type == pg.KEYDOWN:
                    key = 1
                    if event.key == pg.K_p:
                        player.show_inventory(window)
                    if event.key == pg.K_i:
                        player.skill_sheet(window)
                    if event.key == pg.K_s:
                        player.velocity[1] += player.speed
                        player.action = 3
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_w:
                        player.velocity[1] -= player.speed
                        player.action = 1
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_d:
                        player.velocity[0] += player.speed
                        player.action = 0
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_a:
                        player.velocity[0] -= player.speed
                        player.action = 2
                        lib.play_music(lib.cts.Running, -1, 2.0)
                    if event.key == pg.K_e:
                        catchable = False
                if event.type == pg.KEYUP:
                    player.velocity = [0, 0]
                    key = 0
                    lib.stop_music()

            # Control

            # Scenario movement

            if player.rect.x > scenario.screen_limits[0]:
                player.rect.x = scenario.screen_limits[0]
                if scenario.rect.x > scenario.background_limits[0]:
                    scenario.background_velocity[0] = 5
                else:
                    scenario.background_velocity[0] = 0
            else:
                if player.rect.x < lib.cts.width - scenario.screen_limits[0]:
                    player.rect.x = lib.cts.width - scenario.screen_limits[0]
                    if scenario.rect.x < scenario.background_limits[0] - lib.cts.width:
                        scenario.background_velocity[0] = -5
                    else:
                        scenario.background_velocity[0] = 0
                else:
                    if scenario.rect.x > lib.cts.width + scenario.background_limits[0]:
                        scenario.background_velocity[0] = 5
                    else:
                        scenario.background_velocity[0] = 0

            if player.rect.y > scenario.screen_limits[1]:
                player.rect.y = scenario.screen_limits[1]
                if scenario.rect.y > scenario.background_limits[1]:
                    scenario.background_velocity[1] = -5
                else:
                    scenario.background_velocity[1] = 0
            else:
                if player.rect.y < lib.cts.height - scenario.screen_limits[1]:
                    player.rect.y = lib.cts.height - scenario.screen_limits[1]
                    if scenario.rect.y < 0:
                        scenario.background_velocity[1] = 5
                    else:
                        scenario.background_velocity[1] = 0
                else:
                    if scenario.rect.y > scenario.background_limits[1] + lib.cts.height:
                        scenario.background_velocity[1] = -5
                    else:
                        scenario.background_velocity[1] = 0

            # Boss

            if cont > 50:
                attack_direction = 0
                iterator = 0

                for current_boss in boss_group:
                    if stop_while_attack > 0:
                        current_boss.velocity = [0, 0]
                        for attack in attack_group:
                            attack.velocity = [0, 0]
                    else:
                        distance = move_enemy(player.rect, current_boss.rect)
                        if distance[0] > 0:
                            current_boss.velocity = [4, 4]
                            for attack in attack_group:
                                attack.velocity = [4, 4]
                        else:
                            current_boss.velocity = [-4, -4]
                            for attack in attack_group:
                                attack.velocity = [-4, -4]

                        if ((distance[0] >= -2) and (distance[0] <= 2)) and (
                                (distance[1] >= -2) and (distance[1] <= 2)):
                            current_boss.velocity = [0, 0]
                            for attack in attack_group:
                                attack.velocity = [0, 0]
                        else:
                            if distance[0] == 0:
                                current_boss.velocity = [-4, -4]
                                for attack in attack_group:
                                    attack.velocity = [-4, -4]
                                if distance[1] > 0:
                                    attack_angle = lib.mt.radians(270)
                                if distance[1] < 0:
                                    attack_angle = lib.mt.radians(90)
                            else:
                                attack_angle = lib.mt.atan(distance[1] / distance[0])
                            current_boss.angle = attack_angle
                            for attack in attack_group:
                                attack.angle = attack_angle
                        iterator += 1

                        if current_boss.temp < 0:
                            for attack in attack_group:
                                shot_cont = 2
                                while shot_cont > 0:
                                    heaven_shot_type_(attack, current_boss)
                                    shot_cont -= 1
                            stop_while_attack = 15
                            current_boss.temp = 30

                    for attack in attack_type_2_group:
                        if attack.rect.x < -50:
                            attack_group.remove(attack)
                        if attack.rect.y < -50:
                            attack_group.remove(attack)
                        if attack.rect.x > lib.cts.width:
                            attack_group.remove(attack)
                        if attack.rect.y > lib.cts.height:
                            attack_group.remove(attack)

            boss_collide = pg.sprite.spritecollide(player, boss_group, True)

            for boss in boss_collide:
                boss_group.remove(boss)
                enemies_in_combat.add(SimpleEnemy(boss.get_position(), 5))
                in_combat = True
                field_6 = False
                lib.play_music(lib.cts.Demon_Scream)

            # Bullets

            attack_collide = pg.sprite.spritecollide(player, attack_group, True)

            for _ in attack_collide:
                attack_group.remove(_)
                player.live -= 1

            if player.live <= 0:
                in_combat = False
                field_5 = False
                death = True
                run = False
                lib.play_music(lib.cts.Fail)

            for bullet in attack_group:
                if bullet.rect.y > lib.cts.height + 10:
                    attack_group.remove(bullet)

            # Updating & Drawing

            lib.fill(window)

            scenario.update()

            players_group.update(key, window)
            players_group.draw(window)

            stop_while_attack -= 1
            shot_tmp -= 1

            boss_group.update([0, 0])
            for boss in boss_group:
                boss.cont -= 1
                boss.temp -= 1
            boss_group.draw(window)

            attack_group.update()
            attack_group.draw(window)

            attack_type_2_group.update()
            attack_type_2_group.draw(window)
            lvl_info.update()

            if 100 > cont:
                cont += 1
                new_text_position = [450, 450]
                for _ in range(0, len(lib.cts.dialogue_20)):
                    god_dialogue = Texts(new_text_position, window, lib.cts.dialogue_20[_], 25, 2)
                    god_dialogue.velocity = [0, 0]
                    new_text_position[1] += 25
                    dialogue_group.add(god_dialogue)

                lib.play_music(lib.cts.Robotic_Sound, 0)
                window.blit(lib.cts.Dialog_box, [400, 400])
                dialogue_group.update()
                lib.stop_music()

                lib.stop_music()

            if cont == 100:
                talking = True

                for _ in lvl_information:
                    lvl_information.remove(_)

                lvl_info = Texts([1020, 570], window, lib.cts.lvl_info[16], 25, 2, lib.cts.RED)
                lvl_info.velocity = [0, 0]
                lvl_information.add(lvl_info)

            lib.frames_per_second(fps, 1)

        # Settings variables

        turn = 1
        catchable = True
        get_point = True
        progressive = True

        while in_combat:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
                    run = False
                if event.type == pg.KEYDOWN and turn == 1:

                    # Player attacks

                    if event.key == pg.K_q:
                        if player.energy >= 1:
                            player.attack(1)
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.Punch)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    if event.key == pg.K_w:
                        if player.energy >= 3:
                            player.attack(2)
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.Sword_Swing)
                        else:
                            turn = 2
                    if event.key == pg.K_e:
                        if player.energy >= 5:
                            player.transformation = True
                            player.attack(3)
                            turn = 0
                            cont = 0
                            lib.play_music(lib.cts.Transformation_1)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    if event.key == pg.K_r:
                        if player.energy >= 3:
                            if player.transformation:
                                player.attack(4)
                                turn = 0
                                cont = 0
                                lib.play_music(lib.cts.Dragon_Roar_Breathe_Fire)
                            else:
                                catchable = False
                                cont = 0
                                turn = 1
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)

                    # Inventory

                    if event.key == pg.K_t:
                        turn = 3
                        cont = 0
                        lib.play_music(lib.cts.Inventory)

                    if event.key == pg.K_a:
                        if player.drake_smash >= 1:
                            player.use_extras(3)
                            enemy.life = 0
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.MagicFinal)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    if event.key == pg.K_s:
                        if player.extra_live >= 1:
                            player.use_extras(1)
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.Grabing)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    if event.key == pg.K_d:
                        if player.extra_energy >= 1:
                            player.use_extras(2)
                            cont = 0
                            turn = 0
                            lib.play_music(lib.cts.Grabing)
                        else:
                            turn = 2
                            lib.play_music(lib.cts.Error)
                    # Skip turn
                    if event.key == pg.K_f:
                        player.energy += 1
                        player.live += 1
                        cont = 0
                        turn = 0
                        lib.play_music(lib.cts.Lost)

                    # Restating variables

                    if turn == 0:
                        player.energy += 2

                    progressive = True

            # Drawing

            lib.fill(window)

            window.blit(lib.cts.Battle_ground, [0, 0])

            enemy.show_statistics(window)
            enemy.in_combat(window)

            player.in_combat(window)

            # Control

            # Enemies turn

            if turn == 0:
                for enemy in enemies_in_combat:
                    if cont == 0:
                        enemy_ability = enemy.enemy_attack(player.damage)
                        player.damage = 0

                    if enemy.life <= 0:
                        enemies_in_combat.remove(enemy)
                    else:
                        window.blit(lib.cts.Dialog_box, [400, 400])
                        window.blit(enemy_ability, [450, 450])

                if cont > 100:
                    turn = 1
                cont += 1

            if len(enemies_in_combat) == 0:
                win.update()

                if player.level_points == next_level:
                    player.current_level += 1
                    level_up.update()
                    get_point = True

                player.transformation = False

                if cont > 100:
                    player.velocity = [0, 0]
                    key = 0

                    in_combat = False
                    field_6 = False
                cont += 1

            # Player turn

            if turn == 1:
                for enemy in enemies_in_combat:
                    player.hurts(enemy.damage)

                    if enemy.progressive_damage > 0 and progressive:
                        enemy.progressive_damage -= 1
                        progressive = False
                        player.live -= 1
                        lib.play_music(lib.cts.Pain)

                    enemy.damage = 0

                if player.live <= 0:
                    in_combat = False
                    field_6 = False
                    death = True
                    lib.play_music(lib.cts.Fail)

                window.blit(lib.cts.Combat_box, [0, 400])

                player.show_statistics(window)

                if catchable:
                    abilities_in_combat.update()
                    cont = 0
                else:
                    attacks_information.update()
                    if cont > 100:
                        catchable = True
                        turn = 1
                    cont += 1

            # Informative turns

            if turn == 2:
                window.blit(lib.cts.Dialog_box, [0, 400])
                statistics_information.update()
                player.energy -= 2
                if cont > 100:
                    turn = 1
                cont += 1

            if turn == 3:
                window.blit(lib.cts.Dialog_box, [0, 400])
                inventory_information.update()
                if cont > 100:
                    turn = 1
                cont += 1

            lib.frames_per_second(fps, 1)

        # Resetting win label
        win.x, win.y = [400, 300]
        level_up.x, level_up.y = [450, 400]
        if player.level_points < next_level and get_point:
            player.level_points += 1
            get_point = False

    # Story # 2

    # Cleaning

    for _ in enemies_group:
        enemies_group.remove(_)

    for _ in boss_group:
        boss_group.remove(_)

    for _ in enemies_in_combat:
        enemies_in_combat.remove(_)

    for _ in dialogue_group:
        dialogue_group.remove(_)

    for _ in lvl_information:
        lvl_information.remove(_)

    # Chapter title

    Title = Texts([50, 250], window, lib.cts.You_killed_god, 100)
    Title.velocity = [0, 0]
    title_group.add(Title)

    # Chapter II intro

    new_text_position = [50, 750]
    for _ in range(0, len(lib.cts.Chaos)):
        lib.play_music(lib.cts.Intro_3)
        new_text = Texts(new_text_position, window, lib.cts.Chaos[_], 30, 2)
        new_text_position[1] += 50
        text_group.add(new_text)

    # Game button skip

    Skip = Texts([1080, 550], window, lib.cts.skip, 20)
    Skip.velocity = [0, 0]
    title_group.add(Skip)

    window = lib.new_window("Chapter III")

    while run and story_3:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                lib.stop_music()
            if event.type == pg.MOUSEBUTTONDOWN:
                story_3 = False
                lib.stop_music()

        # Drawing and control

        lib.fill(window)

        Title.update()

        if cont >= 100:
            Title.velocity = [0, -1]
            text_group.update()
            Skip.update()

        cont += 1

        for _ in text_group:
            if _.y < 0:
                text_group.remove(_)

        for _ in title_group:
            if _.y <= 0:
                title_group.remove(_)

        if len(text_group) == 0:
            story_2 = False

        lib.frames_per_second(fps, 2)
    lib.stop_music()

    # Death

    for _ in title_group:
        title_group.remove(_)

    for _ in text_group:
        text_group.remove(_)

    cont = 0

    # Death title

    Title = Texts([200, 250], window, lib.cts.Death, 100)
    Title.velocity = [0, 0]
    title_group.add(Title)

    # Game end

    new_text_position = [50, 750]

    for _ in range(0, len(interaction[3])):
        new_text = Texts(new_text_position, window, interaction[3][_], 30, 2)
        new_text_position[1] += 50
        text_group.add(new_text)
        lib.play_music(lib.cts.Dead)

    # End button skip

    Skip = Texts([1080, 550], window, lib.cts.skip, 20)
    Skip.velocity = [0, 0]
    title_group.add(Skip)

    while not run and death:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = True
                lib.stop_music()
            if event.type == pg.MOUSEBUTTONDOWN:
                death = False
                lib.stop_music()

        # Drawing and control

        lib.fill(window)

        Title.update()

        if cont >= 100:
            Title.velocity = [0, -1]
            text_group.update()
            Skip.update()

        cont += 1

        for _ in text_group:
            if _.y < 0:
                text_group.remove(_)

        for _ in title_group:
            if _.y <= 0:
                title_group.remove(_)

        if len(text_group) == 0:
            death = False

        lib.frames_per_second(fps, 2)

    pg.quit()
