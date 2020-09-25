import pygame as pg

# Window size
width = 1200
height = 600

# Points
Default = [800, 200]
Origin = [600, 300]
size = [500, 200]
A = [-50, -100]
B = [-100, 50]
C = [100, 100]
D = [50, -100]
E = [700, 150]
F = [900, 180]
G = [50, 100]
H = [850, 30]

# Color
# RGB
RED = pg.Color(255, 0, 0)
GREEN = pg.Color(0, 255, 0)
BLUE = pg.Color(0, 0, 255)
# BASICS
HIGH = pg.Color(200, 200, 200)
MIDDLE = pg.Color(155, 155, 155)
LOW = pg.Color(55, 55, 55)
# ELEMENTARY
BLACK = pg.Color(0, 0, 0)
WHITE = pg.Color(255, 255, 255)
# EXTRAS
GOLD = pg.Color(210, 175, 55)
# COLOR PALETTE DEFAULT
PALETTE = [RED, GREEN, BLUE, HIGH, MIDDLE, LOW, WHITE]
# COLOR PALETTE #1
PALETTE_1 = [WHITE, GREEN, BLUE]
# COLOR PALETTE #2
PALETTE_2 = [RED, RED, GREEN, GREEN, BLUE, BLUE]

# IMAGES

# Heroes

Ship = pg.image.load("Images/ship.png")

Presentation = [pg.image.load("Images/Heroes/Luke/p.png"),
                pg.image.load("Images/Heroes/Serafin/p.png"),
                pg.image.load("Images/Heroes/Sonia/p.png"),
                pg.image.load("Images/Heroes/Taun/p.png"),
                pg.image.load("Images/Heroes/Xerath/p.png"),
                pg.image.load("Images/Heroes/Angel/p.png"),
                pg.image.load("Images/Heroes/Sofia/p.png"),
                pg.image.load("Images/Heroes/Escanor/p.png")]

Angel = [
    [pg.image.load("Images/Heroes/Angel/e1.png"),
     pg.image.load("Images/Heroes/Angel/e2.png"),
     pg.image.load("Images/Heroes/Angel/e3.png")],
    [pg.image.load("Images/Heroes/Angel/n1.png"),
     pg.image.load("Images/Heroes/Angel/n2.png"),
     pg.image.load("Images/Heroes/Angel/n3.png")],
    [pg.image.load("Images/Heroes/Angel/o1.png"),
     pg.image.load("Images/Heroes/Angel/o2.png"),
     pg.image.load("Images/Heroes/Angel/o3.png")],
    [pg.image.load("Images/Heroes/Angel/s1.png"),
     pg.image.load("Images/Heroes/Angel/s2.png"),
     pg.image.load("Images/Heroes/Angel/s3.png")],
    [pg.image.load("Images/Heroes/Angel/t1.png"),
     pg.image.load("Images/Heroes/Angel/t2.png"),
     pg.image.load("Images/Heroes/Angel/t3.png")],
    pg.image.load("Images/Heroes/Angel/t.png"),
    pg.image.load("Images/Heroes/Angel/in_combat.png"),
    pg.image.load("Images/Heroes/Angel/p.png"),
    pg.image.load("Images/Heroes/Angel/1.png"),
    pg.image.load("Images/Heroes/Angel/2.png")]

Escanor = [
    [pg.image.load("Images/Heroes/Escanor/e1.png"),
     pg.image.load("Images/Heroes/Escanor/e2.png"),
     pg.image.load("Images/Heroes/Escanor/e3.png")],
    [pg.image.load("Images/Heroes/Escanor/n1.png"),
     pg.image.load("Images/Heroes/Escanor/n2.png"),
     pg.image.load("Images/Heroes/Escanor/n3.png")],
    [pg.image.load("Images/Heroes/Escanor/o1.png"),
     pg.image.load("Images/Heroes/Escanor/o2.png"),
     pg.image.load("Images/Heroes/Escanor/o3.png")],
    [pg.image.load("Images/Heroes/Escanor/s1.png"),
     pg.image.load("Images/Heroes/Escanor/s2.png"),
     pg.image.load("Images/Heroes/Escanor/s3.png")],
    [pg.image.load("Images/Heroes/Escanor/t1.png"),
     pg.image.load("Images/Heroes/Escanor/t2.png"),
     pg.image.load("Images/Heroes/Escanor/t3.png")],
    pg.image.load("Images/Heroes/Escanor/t.png"),
    pg.image.load("Images/Heroes/Escanor/in_combat.png"),
    pg.image.load("Images/Heroes/Escanor/p.png"),
    pg.image.load("Images/Heroes/Escanor/1.png"),
    pg.image.load("Images/Heroes/Escanor/2.png")]

Luke = [
    [pg.image.load("Images/Heroes/Luke/e1.png"),
     pg.image.load("Images/Heroes/Luke/e2.png"),
     pg.image.load("Images/Heroes/Luke/e3.png")],
    [pg.image.load("Images/Heroes/Luke/n1.png"),
     pg.image.load("Images/Heroes/Luke/n2.png"),
     pg.image.load("Images/Heroes/Luke/n3.png")],
    [pg.image.load("Images/Heroes/Luke/o1.png"),
     pg.image.load("Images/Heroes/Luke/o2.png"),
     pg.image.load("Images/Heroes/Luke/o3.png")],
    [pg.image.load("Images/Heroes/Luke/s1.png"),
     pg.image.load("Images/Heroes/Luke/s2.png"),
     pg.image.load("Images/Heroes/Luke/s3.png")],
    [pg.image.load("Images/Heroes/Luke/t1.png"),
     pg.image.load("Images/Heroes/Luke/t2.png"),
     pg.image.load("Images/Heroes/Luke/t3.png")],
    pg.image.load("Images/Heroes/Luke/t.png"),
    pg.image.load("Images/Heroes/Luke/in_combat.png"),
    pg.image.load("Images/Heroes/Luke/p.png"),
    pg.image.load("Images/Heroes/Luke/1.png"),
    pg.image.load("Images/Heroes/Luke/2.png")]

Serafin = [
    [pg.image.load("Images/Heroes/Serafin/e1.png"),
     pg.image.load("Images/Heroes/Serafin/e2.png"),
     pg.image.load("Images/Heroes/Serafin/e3.png")],
    [pg.image.load("Images/Heroes/Serafin/n1.png"),
     pg.image.load("Images/Heroes/Serafin/n2.png"),
     pg.image.load("Images/Heroes/Serafin/n3.png")],
    [pg.image.load("Images/Heroes/Serafin/o1.png"),
     pg.image.load("Images/Heroes/Serafin/o2.png"),
     pg.image.load("Images/Heroes/Serafin/o3.png")],
    [pg.image.load("Images/Heroes/Serafin/s1.png"),
     pg.image.load("Images/Heroes/Serafin/s2.png"),
     pg.image.load("Images/Heroes/Serafin/s3.png")],
    [pg.image.load("Images/Heroes/Serafin/t1.png"),
     pg.image.load("Images/Heroes/Serafin/t2.png"),
     pg.image.load("Images/Heroes/Serafin/t3.png")],
    pg.image.load("Images/Heroes/Serafin/t.png"),
    pg.image.load("Images/Heroes/Serafin/in_combat.png"),
    pg.image.load("Images/Heroes/Serafin/p.png"),
    pg.image.load("Images/Heroes/Serafin/1.png"),
    pg.image.load("Images/Heroes/Serafin/2.png")]

Sofia = [
    [pg.image.load("Images/Heroes/Sofia/e1.png"),
     pg.image.load("Images/Heroes/Sofia/e2.png"),
     pg.image.load("Images/Heroes/Sofia/e3.png")],
    [pg.image.load("Images/Heroes/Sofia/n1.png"),
     pg.image.load("Images/Heroes/Sofia/n2.png"),
     pg.image.load("Images/Heroes/Sofia/n3.png")],
    [pg.image.load("Images/Heroes/Sofia/o1.png"),
     pg.image.load("Images/Heroes/Sofia/o2.png"),
     pg.image.load("Images/Heroes/Sofia/o3.png")],
    [pg.image.load("Images/Heroes/Sofia/s1.png"),
     pg.image.load("Images/Heroes/Sofia/s2.png"),
     pg.image.load("Images/Heroes/Sofia/s3.png")],
    [pg.image.load("Images/Heroes/Sofia/t1.png"),
     pg.image.load("Images/Heroes/Sofia/t2.png"),
     pg.image.load("Images/Heroes/Sofia/t3.png")],
    pg.image.load("Images/Heroes/Sofia/t.png"),
    pg.image.load("Images/Heroes/Sofia/in_combat.png"),
    pg.image.load("Images/Heroes/Sofia/p.png"),
    pg.image.load("Images/Heroes/Sofia/1.png"),
    pg.image.load("Images/Heroes/Sofia/2.png")]

Sonia = [
    [pg.image.load("Images/Heroes/Sonia/e1.png"),
     pg.image.load("Images/Heroes/Sonia/e2.png"),
     pg.image.load("Images/Heroes/Sonia/e3.png")],
    [pg.image.load("Images/Heroes/Sonia/n1.png"),
     pg.image.load("Images/Heroes/Sonia/n2.png"),
     pg.image.load("Images/Heroes/Sonia/n3.png")],
    [pg.image.load("Images/Heroes/Sonia/o1.png"),
     pg.image.load("Images/Heroes/Sonia/o2.png"),
     pg.image.load("Images/Heroes/Sonia/o3.png")],
    [pg.image.load("Images/Heroes/Sonia/s1.png"),
     pg.image.load("Images/Heroes/Sonia/s2.png"),
     pg.image.load("Images/Heroes/Sonia/s3.png")],
    [pg.image.load("Images/Heroes/Sonia/t1.png"),
     pg.image.load("Images/Heroes/Sonia/t2.png"),
     pg.image.load("Images/Heroes/Sonia/t3.png")],
    pg.image.load("Images/Heroes/Sonia/t.png"),
    pg.image.load("Images/Heroes/Sonia/in_combat.png"),
    pg.image.load("Images/Heroes/Sonia/p.png"),
    pg.image.load("Images/Heroes/Sonia/1.png"),
    pg.image.load("Images/Heroes/Sonia/2.png")]

Taun = [
    [pg.image.load("Images/Heroes/Taun/e1.png"),
     pg.image.load("Images/Heroes/Taun/e2.png"),
     pg.image.load("Images/Heroes/Taun/e3.png")],
    [pg.image.load("Images/Heroes/Taun/n1.png"),
     pg.image.load("Images/Heroes/Taun/n2.png"),
     pg.image.load("Images/Heroes/Taun/n3.png")],
    [pg.image.load("Images/Heroes/Taun/o1.png"),
     pg.image.load("Images/Heroes/Taun/o2.png"),
     pg.image.load("Images/Heroes/Taun/o3.png")],
    [pg.image.load("Images/Heroes/Taun/s1.png"),
     pg.image.load("Images/Heroes/Taun/s2.png"),
     pg.image.load("Images/Heroes/Taun/s3.png")],
    [pg.image.load("Images/Heroes/Taun/t1.png"),
     pg.image.load("Images/Heroes/Taun/t2.png"),
     pg.image.load("Images/Heroes/Taun/t3.png")],
    pg.image.load("Images/Heroes/Taun/t.png"),
    pg.image.load("Images/Heroes/Taun/in_combat.png"),
    pg.image.load("Images/Heroes/Taun/p.png"),
    pg.image.load("Images/Heroes/Taun/1.png"),
    pg.image.load("Images/Heroes/Taun/2.png")]

Xerath = [
    [pg.image.load("Images/Heroes/Xerath/e1.png"),
     pg.image.load("Images/Heroes/Xerath/e2.png"),
     pg.image.load("Images/Heroes/Xerath/e3.png")],
    [pg.image.load("Images/Heroes/Xerath/n1.png"),
     pg.image.load("Images/Heroes/Xerath/n2.png"),
     pg.image.load("Images/Heroes/Xerath/n3.png")],
    [pg.image.load("Images/Heroes/Xerath/o1.png"),
     pg.image.load("Images/Heroes/Xerath/o2.png"),
     pg.image.load("Images/Heroes/Xerath/o3.png")],
    [pg.image.load("Images/Heroes/Xerath/s1.png"),
     pg.image.load("Images/Heroes/Xerath/s2.png"),
     pg.image.load("Images/Heroes/Xerath/s3.png")],
    [pg.image.load("Images/Heroes/Xerath/t1.png"),
     pg.image.load("Images/Heroes/Xerath/t2.png"),
     pg.image.load("Images/Heroes/Xerath/t3.png")],
    pg.image.load("Images/Heroes/Xerath/t.png"),
    pg.image.load("Images/Heroes/Xerath/in_combat.png"),
    pg.image.load("Images/Heroes/Xerath/p.png"),
    pg.image.load("Images/Heroes/Xerath/1.png"),
    pg.image.load("Images/Heroes/Xerath/2.png")]

# NPCs

Saku = pg.image.load("Images/Characters/npc/Saku.png")
Spidy = pg.image.load("Images/Characters/npc/Spidy.png")
Elise = pg.image.load("Images/Characters/npc/Elise.png")
Goldi = pg.image.load("Images/Characters/npc/Goldi.png")
Helen = pg.image.load("Images/Characters/npc/Helen.png")
Marian = pg.image.load("Images/Characters/npc/Marian.png")
Balzar = pg.image.load("Images/Characters/npc/Balzar.png")
Manuela = pg.image.load("Images/Characters/npc/Manuela.png")
Clarissa = pg.image.load("Images/Characters/npc/Clarissa.png")
Elizabeth = pg.image.load("Images/Characters/npc/Elizabeth.png")

# Enemies

Enemy_1 = [
    [pg.image.load("Images/Characters/Enemies/1_1.png"),
     pg.image.load("Images/Characters/Enemies/1_2.png"),
     pg.image.load("Images/Characters/Enemies/1_3.png")],
    pg.image.load("Images/Characters/Enemies/1_in_combat.png"),
    pg.image.load("Images/Characters/Enemies/1_h.png")]

Enemy_2 = [
    [pg.image.load("Images/Characters/Enemies/2_1.png"),
     pg.image.load("Images/Characters/Enemies/2_2.png"),
     pg.image.load("Images/Characters/Enemies/2_3.png")],
    pg.image.load("Images/Characters/Enemies/2_in_combat.png"),
    pg.image.load("Images/Characters/Enemies/2_h.png")]

Enemy_3 = [
    [pg.image.load("Images/Characters/Enemies/3_1.png"),
     pg.image.load("Images/Characters/Enemies/3_2.png"),
     pg.image.load("Images/Characters/Enemies/3_3.png")],
    pg.image.load("Images/Characters/Enemies/3_in_combat.png"),
    pg.image.load("Images/Characters/Enemies/3_h.png")]

Enemy_4 = [
    [pg.image.load("Images/Characters/Enemies/4_1.png"),
     pg.image.load("Images/Characters/Enemies/4_2.png"),
     pg.image.load("Images/Characters/Enemies/4_3.png")],
    pg.image.load("Images/Characters/Enemies/4_in_combat.png"),
    pg.image.load("Images/Characters/Enemies/4_h.png")]

Enemy_5 = [
    [pg.image.load("Images/Characters/Enemies/5_1.png"),
     pg.image.load("Images/Characters/Enemies/5_2.png"),
     pg.image.load("Images/Characters/Enemies/5_3.png")],
    pg.image.load("Images/Characters/Enemies/5_in_combat.png"),
    pg.image.load("Images/Characters/Enemies/5_h.png")]

Enemy_6 = [
    [pg.image.load("Images/Characters/Enemies/6_1.png"),
     pg.image.load("Images/Characters/Enemies/6_2.png"),
     pg.image.load("Images/Characters/Enemies/6_3.png")],
    pg.image.load("Images/Characters/Enemies/6_in_combat.png"),
    pg.image.load("Images/Characters/Enemies/6_h.png")]

random_enemies_1 = [[pg.image.load("Images/Things/raccoon_e_1.png"),
                     pg.image.load("Images/Things/raccoon_e_2.png"),
                     pg.image.load("Images/Things/raccoon_e_3.png")],
                    [pg.image.load("Images/Things/raccoon_n_1.png"),
                     pg.image.load("Images/Things/raccoon_n_2.png"),
                     pg.image.load("Images/Things/raccoon_n_3.png")],
                    [pg.image.load("Images/Things/raccoon_o_1.png"),
                     pg.image.load("Images/Things/raccoon_o_2.png"),
                     pg.image.load("Images/Things/raccoon_o_3.png")],
                    [pg.image.load("Images/Things/raccoon_s_1.png"),
                     pg.image.load("Images/Things/raccoon_s_2.png"),
                     pg.image.load("Images/Things/raccoon_s_3.png")]]

random_enemies_2 = [[pg.image.load("Images/Things/worm_e_1.png"),
                     pg.image.load("Images/Things/worm_e_2.png"),
                     pg.image.load("Images/Things/worm_e_3.png")],
                    [pg.image.load("Images/Things/worm_n_1.png"),
                     pg.image.load("Images/Things/worm_n_2.png"),
                     pg.image.load("Images/Things/worm_n_3.png")],
                    [pg.image.load("Images/Things/worm_o_1.png"),
                     pg.image.load("Images/Things/worm_o_2.png"),
                     pg.image.load("Images/Things/worm_o_3.png")],
                    [pg.image.load("Images/Things/worm_s_1.png"),
                     pg.image.load("Images/Things/worm_s_2.png"),
                     pg.image.load("Images/Things/worm_s_3.png")]]

# Others

Snake = pg.image.load("Images/snaky.png")

Invaders = [pg.image.load("Images/1.png"),
            pg.image.load("Images/2.png"),
            pg.image.load("Images/3.png"),
            pg.image.load("Images/mother.png")]

# Backgrounds / Scenarios

House_1 = pg.image.load("Images/Places/bedroom.png")
House_2 = pg.image.load("Images/Places/living_room.png")
Field_0 = pg.image.load("Images/Places/f_0.png")
Field_1 = pg.image.load("Images/Places/f_1.png")
Field_2 = pg.image.load("Images/Places/f_2.png")
Field_3 = pg.image.load("Images/Places/f_3.png")
Field_4 = pg.image.load("Images/Places/f_4.png")
Field_5 = pg.image.load("Images/Places/f_5.png")
Town_1 = pg.image.load("Images/Places/town1.png")
Town_2 = pg.image.load("Images/Places/town2.png")
Town_3 = pg.image.load("Images/Places/town3.png")
Battle_ground = pg.image.load("Images/Places/battle_ground.jpg")

background = pg.image.load("Images/f_1.png")

# Things
HUD = pg.image.load("Images/Things/HUD.png")
Bed = pg.image.load("Images/Things/bed.png")
Mud = pg.image.load("Images/Things/mud.png")
Tree = pg.image.load("Images/Things/tree.png")
Hole = pg.image.load("Images/Things/hole.png")
Bush = pg.image.load("Images/Things/bush.png")
Icon = pg.image.load("Images/Things/icon.png")
Blank = pg.image.load("Images/Things/blank.png")
Table = pg.image.load("Images/Things/table.png")
Portal = pg.image.load("Images/Things/portal.png")
Points = pg.image.load("Images/Things/points.png")
Bullet = pg.image.load("Images/Things/bullet.png")
NPC_shop = pg.image.load("Images/Things/shop.png")
Plant_1 = pg.image.load("Images/Things/plant_1.png")
Plant_2 = pg.image.load("Images/Things/plant_2.png")
Limit_1 = pg.image.load("Images/Things/limit_1.png")
Limit_2 = pg.image.load("Images/Things/limit_2.png")
Chair_e = pg.image.load("Images/Things/chair_e.png")
Chair_n = pg.image.load("Images/Things/chair_n.png")
Chair_s = pg.image.load("Images/Things/chair_s.png")
Chair_w = pg.image.load("Images/Things/chair_w.png")
Flower = pg.image.load("Images/Things/pink_flower.png")
HUD_enemy = pg.image.load("Images/Things/HUD_enemy.png")
NPC_House_1 = pg.image.load("Images/Things/house_1.png")
NPC_House_2 = pg.image.load("Images/Things/house_2.png")
NPC_House_3 = pg.image.load("Images/Things/house_3.png")
NPC_House_4 = pg.image.load("Images/Things/house_4.png")
Combat_box = pg.image.load("Images/Things/combat_box.png")
Dialog_box = pg.image.load("Images/Things/dialog_box.png")
Skill_sheet = pg.image.load("Images/Things/skill_sheet.png")
Nightstand_1 = pg.image.load("Images/Things/nightstand1.png")
Nightstand_2 = pg.image.load("Images/Things/nightstand2.png")
Decoration_1 = pg.image.load("Images/Things/decoration1.png")
Decoration_2 = pg.image.load("Images/Things/decoration2.png")
Decoration_3 = pg.image.load("Images/Things/decoration3.png")
Decoration_4 = pg.image.load("Images/Things/decoration4.png")
Decoration_5 = pg.image.load("Images/Things/decoration5.png")
Room_limit_1 = pg.image.load("Images/Things/room_limit_1.png")
Room_limit_2 = pg.image.load("Images/Things/room_limit_2.png")
Player_house = pg.image.load("Images/Things/player_house.png")
Current_item = pg.image.load("Images/Things/current_item.png")
Current_skill = pg.image.load("Images/Things/current_skill.png")
Inventory_background = pg.image.load("Images/Things/inventory.png")

# Items

Apple = pg.image.load("Images/Items/apple.png")

Necklace = pg.image.load("Images/Items/necklace.png")
Gold_bag = pg.image.load("Images/Items/gold_bag.png")

Ring_1 = pg.image.load("Images/Items/ring_bronze.png")
Ring_2 = pg.image.load("Images/Items/ring_silver.png")
Ring_3 = pg.image.load("Images/Items/ring_golden.png")
Ring_4 = pg.image.load("Images/Items/ring_blue.png")
Ring_5 = pg.image.load("Images/Items/ring_purple.png")
Ring_6 = pg.image.load("Images/Items/ring_pink.png")

Bear_1 = pg.image.load("Images/Items/bear_1.png")
Bear_2 = pg.image.load("Images/Items/bear_2.png")
Bear_3 = pg.image.load("Images/Items/bear_3.png")

Chest_0 = pg.image.load("Images/Items/chest_0.png")
Chest_1 = pg.image.load("Images/Items/chest_1.png")
Chest_2 = pg.image.load("Images/Items/chest_2.png")
Chest_3 = pg.image.load("Images/Items/chest_3.png")
Chest_4 = pg.image.load("Images/Items/chest_4.png")
Chest_5 = pg.image.load("Images/Items/chest_5.png")

Helmet_0 = pg.image.load("Images/Items/helmet_0.png")
Helmet_1 = pg.image.load("Images/Items/helmet_1.png")
Helmet_2 = pg.image.load("Images/Items/helmet_2.png")
Helmet_3 = pg.image.load("Images/Items/helmet_3.png")
Helmet_4 = pg.image.load("Images/Items/helmet_4.png")
Helmet_5 = pg.image.load("Images/Items/helmet_5.png")

Shield_0 = pg.image.load("Images/Items/shield_0.png")
Shield_1 = pg.image.load("Images/Items/shield_1.png")
Shield_2 = pg.image.load("Images/Items/shield_2.png")
Shield_3 = pg.image.load("Images/Items/shield_3.png")
Shield_4 = pg.image.load("Images/Items/shield_4.png")
Shield_5 = pg.image.load("Images/Items/shield_5.png")

Sword_0 = pg.image.load("Images/Items/sword_0.png")
Sword_1 = pg.image.load("Images/Items/sword_1.png")
Sword_2 = pg.image.load("Images/Items/sword_2.png")
Sword_3 = pg.image.load("Images/Items/sword_3.png")
Sword_4 = pg.image.load("Images/Items/sword_4.png")
Sword_5 = pg.image.load("Images/Items/sword_5.png")

# Buffs

Armor = pg.image.load("Images/Items/armor.png")
Wings = pg.image.load("Images/Items/wings.png")
Coffee = pg.image.load("Images/Items/coffee.png")
Extra_life = pg.image.load("Images/Items/extra_life.png")
Drake_smash = pg.image.load("Images/Items/drake_smash.png")
Extra_energy = pg.image.load("Images/Items/extra_energy.png")

# Statistics

Hearts = pg.image.load("Images/Items/heart.png")
Energy = pg.image.load("Images/Items/energy.png")
Coin_effect = pg.image.load("Images/Items/coin.png")
Buff_effect = pg.image.load("Images/Items/buff_effect.png")
Armor_effect = pg.image.load("Images/Items/armor_effect.png")
Hearts_effect = pg.image.load("Images/Items/hearts_effect.png")
Energy_effect = pg.image.load("Images/Items/energy_effect.png")
Without_hearts = pg.image.load("Images/Items/without_hearts.png")
Without_energy = pg.image.load("Images/Items/without_energy.png")

# Effects

Explosion_1 = pg.image.load("Images/Effects/1.png")
Explosion_2 = pg.image.load("Images/Effects/2.png")
Explosion_3 = pg.image.load("Images/Effects/3.png")

Player_Shots = pg.image.load("Images/shot.png")
Invader_Shots = pg.image.load("Images/invader_shot.png")

# Texts

euphoria = "Euphoria"

choosing_player = ["(1) Luke, dragon's son",
                   "(2) Serafin, the demonic angel",
                   "(3) Sonia, queen of sea",
                   "(4) Taun, the immortal beast",
                   "(5) Xerath, the last warrior",
                   "(6) Angel, an Angel...",
                   "(7) Sofia, god's daughter",
                   "(8) Escanor, demon's king"]

euphoria_intro_luke = ["Once upon a time, a lost continent; where",
                       "people around the big castle of Esfitia",
                       "used to live placefully like farmers,",
                       "warrior, markers and other Professions",
                       "",
                       "",
                       "One day, everyone near to the castle",
                       "saw a weird coming darkness the",
                       "the king, got worry about that",
                       "so, sent different ships to face",
                       "them...",
                       "",
                       "",
                       "Those ship never come back...",
                       "",
                       "",
                       "The cataclysm have just started",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "Heroes...",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "Were able to safe our world, but",
                       "each one of they have a story...",
                       "this is one of them",
                       "",
                       "",
                       "",
                       "",
                       "Luke, the dragons son",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "         ( Somebody in the front door )",
                       "",
                       "",
                       "",
                       "",
                       "               Z Z Z Z Z Z Z.... ",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "I'll defeat... ",
                       "",
                       "",
                       "",
                       "",
                       "       ( Fall from his bed )",
                       "",
                       "",
                       "",
                       "",
                       "What the...?",
                       "Who's knocking?"]

euphoria_intro_serafin = ["Some times... There in heaven some angels",
                          "make weird things, one of those weird",
                          "things are children; one of those things",
                          "is Serafin the madness incarnate... Born",
                          "on hell and made in heaven, his parents",
                          "couldn't be from more different places...",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "The cataclysm brought monsters, but not all",
                          "of them want Esfitia destroyed",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "Not all the Heroes are humans...",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "Serafin arrived a couple of days",
                          "after the cataclysm his parents",
                          "sent him as human to help...",
                          "",
                          "",
                          "",
                          "",
                          "Serafin, the demonic angel",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "         ( Somebody in the front door )",
                          "",
                          "",
                          "",
                          "",
                          "               Z Z Z Z Z Z Z.... ",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "",
                          "                 ( Wake up )",
                          "",
                          "",
                          "",
                          "",
                          "mmmmmmmmmmmmm... I want sleep more...",
                          "Who's knocking my door?"]

euphoria_intro_sonia = ["There's a kingdom in the deep sea near the",
                        "big castle of Esfitia, there's where this",
                        "queen born, a big kingdom destroyed by the",
                        "darkness",
                        "",
                        "",
                        "One day, everyone near to the castle",
                        "saw a weird darkness coming, Seanis",
                        "the kingdom of water, where Sonia used",
                        "to live face the that darkness...",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "'Massacre'...",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "Is not enough to express what Sonia's",
                        "kingdom lived, they were destroyed by",
                        "the cataclysm, no mercy, no hope, just",
                        "blood was what she left behind when she",
                        "was sent far away to preserve her legacy",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "Legacy...",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "The best way to preserve it...",
                        "'Facing the darkness she thought'",
                        "the hero of the legacy",
                        "",
                        "",
                        "",
                        "",
                        "Sonia, queen of sea",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "         ( Somebody in the front door )",
                        "",
                        "",
                        "",
                        "",
                        "               mmmmmm.........",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "It's 8 am..... ",
                        "",
                        "",
                        "",
                        "",
                        "       ( Stand up from her bed )",
                        "",
                        "",
                        "",
                        "",
                        "Who's knowing?"]

euphoria_intro_taun = ["In the lost jungle of Uh-Gar lies a many",
                       "towns allies of Esfitia's kingdom, rich in",
                       "culture and story that lost continent",
                       "belonging magic and amazing inhuman warriors",
                       "",
                       "",
                       "There's the monarchy where Taun Yir came",
                       "from... 'The immortal warrior', he was named",
                       "son of the powerful king and the best",
                       "enchantress his people have known",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "'The exiled one...'",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "'Taun' became an unnameable word",
                       "when the loved son went near the",
                       "humans kingdom...",
                       "",
                       "",
                       "",
                       "",
                       "near enough to left the protection of",
                       "the jungle... 'Heretic', he was called",
                       "after all in his conservative society",
                       "leaving the jungle was worse than death",
                       "'dishonor'...",
                       "",
                       "",
                       "",
                       "",
                       "H e was just a young children curious...",
                       "But the council forced him left the jungle",
                       "as a heretic, so became an heretic Taun went",
                       "where is heart told him to the humans world",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "         ( Somebody in the front door )",
                       "",
                       "",
                       "",
                       "",
                       "               Z Z Z Z Z Z Z.... ",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "                   * Purrs *",
                       "",
                       "",
                       "",
                       "",
                       "             ( Jump out of his bed )",
                       "",
                       "",
                       "",
                       "",
                       "Mmmmmm... I was dreaming with whiskas...",
                       "Who's pulling under my door?"]

euphoria_intro_xerath = ["The big castle of Esfitia used to be",
                         "a placefully place for farmers, warrior,",
                         "markers and other Professions",
                         "",
                         "",
                         "",
                         "One of its inhabitant was Xerath called",
                         "'The perfect warrior', he was known as",
                         "the general of the Esfitia army the",
                         "strongest warrior, smart and alone",
                         "'The survivor'...",
                         "",
                         "",
                         "",
                         "When a weird darkness arrived Seanis",
                         "Xerath sent ships to check their allies",
                         "status, they were closer the darkness",
                         "after all, but... those ships never come",
                         "back... He tried to get communication with",
                         "Seanis but nobody answered him, people in",
                         "Esfitia was worry about it, each day darkness",
                         "was closer, but the couldn't do anything to",
                         "stop it...",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "( June 17 th )",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "Soldier: 'General, the darkness arrived the",
                         "coast and left a old man who wants to talk",
                         "with you. Sir that man is using Seanis King's",
                         "Clothes...'",
                         "",
                         "",
                         "",
                         "Xerath thought it could be the Seanis king so",
                         "he open the castle door...",
                         "",
                         "",
                         "",
                         "He shouldn't have opened it...",
                         "",
                         "",
                         "",
                         "When the old man step on the castle he become",
                         "in a monster... It destroyed the main door",
                         "and an army of monster got into de castle",
                         "those things... They destroyed each house,",
                         "kill each children, each man and rape each",
                         "women... Xerath family...",
                         "",
                         "",
                         "",
                         "No one survived, except one",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "( June 18 th )",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "Xerath was seated in the king's chair and"
                         "a piece of paper was in his left hand, it",
                         "say: 'Thank you and please keep your new",
                         "friend well feed'...",
                         "",
                         "",
                         "",
                         "He can feel it... Something inside him",
                         "something evil..."
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "Not everything that is in the dark is evil",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "         ( Somebody in the front door )",
                         "",
                         "",
                         "",
                         "",
                         "Soldier, behind you!!!",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "Oh... It was that nightmare again...",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "Who's knowing my door?",
                         "mmmmmm... I'll be prepare this time..."
                         "",
                         "",
                         "",
                         "          ( Take his sword )"]

skip = "Click to skip"

dialogue_1 = "I should take this... (Press E)"

dialogue_2 = "I will need this... (Press E)"

dialogue_2_1 = "   This is really heavy..."

dialogue_3 = "The dragon's ring... (Press Q)"

dialogue_3_1 = "COFFEE!!! (Press R to drink)"

dialogue_4 = ["I don't want to step on my",
              "",
              "garden"]

dialogue_5_1 = ["LUUUUUUUUUUUKKKKEEEEEEE!!",
                "",
                "There are monsters in the",
                "",
                "town... Safe us!!!"]

dialogue_5_2 = ["Please!! Serafin there are",
                "",
                "monster in the town...",
                "",
                "Safe us!!!"]

dialogue_5_3 = ["My queen!! We need you",
                "",
                "Sonia, there are monsters",
                "",
                "in our town... Safe us!!!"]

dialogue_5_4 = ["Master Taun, there are monster",
                "",
                "we need you help, safe us master",
                "",
                "please, Safe us!!"]

dialogue_5_5 = ["Mr. Xerath please we need the",
                "",
                "legendary warrior, safe us!!!",
                "",
                "There are monster!!!"]

dialogue_6_1 = ["I need to be a dragon to",
                "",
                "use dragon fire"]

dialogue_6_2 = ["I need to be a demon to",
                "",
                "use light inside me..."]

dialogue_6_3 = ["I need to be a spirit to",
                "",
                "use water bomb"]

dialogue_6_4 = ["I'm immortal when I'm",
                "",
                "the beast"]

dialogue_6_5 = ["I have to use the curse",
                "",
                "to use death hand..."]

dialogue_7_1 = ["Those ogres kidnapped me!!, I'll give",
                "",
                "you something if you defeat them",
                ""]

dialogue_7_1_2 = ["Thank you!!! Look this is an armor",
                  "",
                  "I found... Please, safe our town...",
                  "",
                  "(Press P)"]

dialogue_7_1_3 = ["If you need me I'll be in the",
                  "",
                  "town... If you safe it"]

dialogue_7_2 = "Fill hole (Press E)"

dialogue_7_3 = "You found a potion"

dialogue_8 = ["I'm Balzar the cataclysm herald",
              "I can help, if the destroy those",
              "monster I will tell you how to",
              "stop the cataclysm"]

dialogue_9 = ["Now, I'm free... Thank you...",
              "Well you can die in peace. Those",
              "Idiots wanted kidnap people...",
              "IT BETTER KILL THEM RIGHT NOW!!!"]

dialogue_10 = ["Thank you... I guess you was hurt...",
               "",
               "Take this... I bought you a couple",
               "",
               "of things... (Press P)"]

dialogue_11 = ["Those idiots destroyed my shop, now",
               "",
               "I need to repair this, puffff"]

dialogue_12 = ["I have never seen Spidy that angry",
               "",
               "jeje, I'll help her"]

dialogue_13 = ["Look at this Helen your straw is",
               "",
               "still dry"]

dialogue_14 = ["I almost got roasted like a chicken,",
               "",
               "my straw is the least of my problems",
               "",
               "Goldi"]

dialogue_15 = ["Ohhhh, hi... I understand that you defeat those",
               "",
               "monsters... Thank you... Emmm... I'm worry",
               "",
               "about the est... I'll thank you if you check",
               "",
               "it... There's a portal... You don't need to",
               "",
               "walk to much..."]

dialogue_16 = ["It looks like everything is okay with my hose",
               "",
               "ohhhh... I found an apple... Take it, for you",
               "",
               "(You got a apple, press P)"]

dialogue_17 = ["Hey you, thank you... Emmmmm take,",
               "",
               "it's a gift for saving my house",
               "",
               "(You got a new armor, press P)"]

dialogue_18 = ["I knew I can trust in you... But I have",
               "",
               "another petition for you... Marian is our",
               "",
               "witch and she have been having strange",
               "",
               "visions Can you talk with her?"]

dialogue_19 = ["Intruder detected",
               "",
               "God's architect: Kill!!!"]

dialogue_20 = ["There no mercy for humans like you",
               "",
               "you destroyed my son... No mercy!,",
               "",
               "you will be destroyed... By angels"]

Balzar_is_death = "Balzar is death"

Town_story = ["In the last twilight of his life, the evil",
              "herald of chaos kept his word; he told our",
              "hero that the cataclysm was unstoppable and",
              "killing the herald of darkness...",
              "",
              "",
              "It was just the beginning of the end of the",
              "world",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "'Heroes'... We'll need more...",
              "",
              "",
              "",
              "",
              "",
              "",
              "After the long battle, Saku found our",
              "hero near the town, she take us there"]

Architect_was_destroyed = "The Architect was destroyed"

God_story = ["There's no mercy for that people that kill",
             "angels... 'The architect' was the father",
             "of almost each one of them... And now is",
             "dead we killed him...",
             "",
             "",
             "",
             "",
             "",
             "",
             "",
             "",
             "",
             "",
             "",
             "",
             "",
             "",
             "",
             "",
             "",
             "",
             "",
             "'Satan'... Bless me...",
             "",
             "",
             "",
             "",
             "",
             "",
             "A horde of angels take us to heaven...",
             "during the travel we saw Balzar... There",
             "burning in hell... He threw us, a heavy",
             "bag",
             "",
             "",
             "",
             "",
             "",
             "'Glory to the new herald!!!', he said",
             "(Press p...)"]

You_killed_god = "You killed god..."

Chaos = ["Maybe... Heroes are evil too... The world",
         "was destroyed by chaos...",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "'Satan'... Bless me... You're 'Satan'",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "",
         "Directed by:",
         "",
         "",
         "Andres Manuel Prieto Alvarez",
         "",
         "",
         "Monsters creation:",
         "",
         "",
         "Bryan Steven Cardona Rendon",
         "",
         "",
         "Art & Music:",
         "",
         "",
         "Jorge Alejandro Mejia Holgin",
         "",
         "",
         "UNIVERSIDAD TECNOLOGICA DE PEREIRA",
         "             (UTP)",
         "      Computacion grafica",
         "",
         "",
         "Mas de mil horas de diseno, creacion",
         "",
         "y aprendizaje"]

win_dialogue = "You won"

lvl_up_dialogue = "You level up"

energy_material_info = ["I don't have enough energy",
                        "",
                        "or material..."]

inventory_interactions = ["You have ate fruit (You recovered 1 of hp)",
                          "It's so pretty... (You recovered 1 of mana)",
                          "Smell like home... (You recovered 2 of mana)",
                          "It says: 'will be with you' (You recovered 3 of mana)",
                          "It looks expensive... (You can sell it)",
                          "Ohhhhhh shines"]

lvl_info = ["Go out", "Check the front door",
            "Talk with Manuela", "Save the town",
            "Defeat the monsters",
            "Talk with the weird guy",
            "Defeat all the monster",
            "Survive!!", "Defeat Balzar",
            "Talk with Saku", "Find Manuela",
            "Find Marian", "Use the portal and check the southern",
            "Check the robot", "Survive!!!", "Listen god's words",
            "Kill god"]

Player_attacks_1 = ["Q. Fire bomb (1/1)",
                    "W. Dragon claws (4/3)",
                    "E. Transformation (+4/5)",
                    "R. Dragon fire (6/3)",
                    "T. Inventory",
                    "F. Skip turn"]

Player_attacks_2 = ["Q. Demon's eyes (2/+1/2)",
                    "W. Angel's Edge (2/+2/4)",
                    "E. Transformation (-3/3)",
                    "R. Light inside me (8/-3/6)",
                    "T. Inventory",
                    "F. Skip turn"]

Player_attacks_3 = ["Q. Frozen punch (2/+1/3)",
                    "W. Water sword (4/+2/5)",
                    "E. Transformation (5)",
                    "R. Water bomb (5/1)",
                    "T. Inventory",
                    "F. Skip turn"]

Player_attacks_4 = ["Q. Solid body (1/*1/2)",
                    "W. Master's tack (7/~2/5)",
                    "E. Transformation (~3/7)",
                    "R. Immortal beast (+10/2)",
                    "T. Inventory",
                    "F. Skip turn"]

Player_attacks_5 = ["Q. Perfect warrior (3/2)",
                    "W. Perfect arrow (7/4)",
                    "E. Transformation (+3/8)",
                    "R. Death hand (20/10)",
                    "T. Inventory",
                    "F. Skip turn"]

Player_inventory = ["A. Dragon rings (It kills an enemy)",
                    "S. Live potion (You recover 5 life points)",
                    "D. Mana potion (You recover 5 energy points)"]

Enemy_1_attacks = ["Bite",
                   "Poison",
                   "Dodge"]

Enemy_2_attacks = ["SMASH!",
                   "Gurrrr!",
                   "EAT!"]

Enemy_3_attacks = ["Skull attack!",
                   "Fire from hell",
                   "You can't hurt me",
                   "NEW PET!"]

Enemy_4_attacks = ["Heaven bean",
                   "God, bless me!",
                   "I'm an angel..."]

Enemy_5_attacks = ["Perfect bean!",
                   "God, father save your angel",
                   "In god's name, I'll defeat you"]

Enemy_6_attacks = ["I'm god's architect",
                   "Faster than light!",
                   "Okay... I'll repair it"]

Death = "You have been slave"

Death_interaction_1 = ["",
                       "",
                       "",
                       "",
                       "Luke was defeat...",
                       "",
                       "",
                       "",
                       "",
                       "He was a heroes, but no all the heroes",
                       "",
                       "are able to safe the world...",
                       ""]

Death_interaction_2 = ["",
                       "",
                       "",
                       "",
                       "Heaven and hell are crying...",
                       "",
                       "",
                       "",
                       "",
                       "Serafin is death... But angels and",
                       "",
                       "loved him...",
                       ""]

Death_interaction_3 = ["",
                       "",
                       "",
                       "",
                       "Deep sea is a dark place, but...",
                       "",
                       "",
                       "",
                       "",
                       "Even there... lies more light than",
                       "",
                       "the deep hole were our queen...",
                       "",
                       "lies now",
                       ""]

Death_interaction_4 = ["",
                       "",
                       "",
                       "",
                       "Jungle is a dangerous place...",
                       "",
                       "",
                       "",
                       "",
                       "That's why Taun used to look so",
                       "",
                       "strong... Maybe he was not so...",
                       "",
                       "immortal",
                       ""]

Death_interaction_5 = ["",
                       "",
                       "",
                       "",
                       "Esfitia was a big place with the",
                       "",
                       "the biggest castle I've never seen",
                       "",
                       "nice people and those things, but...",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "",
                       "As Xerath showed us... Neither the",
                       "",
                       "best training or the experience can",
                       "",
                       "face death...",
                       ""]

# Music

Cave_Music_1 = "Sound/Music/AliensDream-FULL.mp3"
Cave_Music_2 = "Sound/Music/NazcaFULL.mp3"
Intro_1 = "Sound/Music/TheCrossover-FULL.mp3"
Intro_2 = "Sound/Music/InParadise-FULL.mp3"
Intro_3 = "Sound/Music/SepiaGuitarStrings-FULL.mp3"

# Effects
Transformation_1 = "Sound/Effects/Appear.wav"
Transformation_2 = "Sound/Effects/Magical_Sound.wav"

Sound_Explosion_1 = "Sound/Effects/Atomic_Bomb.wav"
Sound_Explosion_2 = "Sound/Effects/Big_Bomb.wav"
Sound_Explosion_3 = "Sound/Effects/Bomb_Exploding.wav"
Sound_Explosion_4 = "Sound/Effects/Depth_Charge.wav"
Sound_Explosion_5 = "Sound/Effects/Explosion_Ultra_Bass.wav"

Unfold_Paper = "Sound/Effects/Book_Pages.wav"

Bull = "Sound/Effects/Bull.wav"

End = "Sound/Music/EndGameMusic.mp3"

Sell_Or_Buy = "Sound/Effects/Coin_Drop.wav"

Wooden_Door = "Sound/Effects/Creaking_Door.wav"
Iron_Door = "Sound/Effects/Metal_Door.wav"

Evil_Laught_1 = "Sound/Effects/Creepy_Laught.wav"
Evil_Laught_2 = "Sound/Effects/Laughter.wav"

Dragon_Bite = "Sound/Effects/Dragon_Bite.wav"
Dragon_Roar_Breathe_Fire = "Sound/Effects/FireMagic.wav"

Draw_Bow_and_Fire = "Sound/Effects/Draw_bow_and_fire.wav"
Fire_Bow = "Sound/Effects/Fire_Bow.wav"
String_of_Bow = "Sound/Effects/String_Tension.wav"
Arrow_Fly_1 = "Sound/Effects/Swoosh_1.wav"
Arrow_Fly_2 = "Sound/Effects/Swoosh_3.wav"

MagicCaos = "Sound/Effects/MagicCaos.wav"
Boir = "Sound/Effects/Boir.wav"
Dead = "Sound/Music/Sad.mp3"
Ghost_Screams = "Sound/Effects/Dying_Soul.wav"
Ghost_Sounds_1 = "Sound/Effects/Spooky_Chains.wav"
Ghost_Sounds_2 = "Sound/Effects/Strange_Days.wav"

Fire_Burning = "Sound/Effects/Fire_Burning.wav"

Inventory = "Sound/Effects/Glove_Box_Open.wav"

Hmm_Men = "Sound/Effects/Hmm_Men.wav"
Hmm_Women = "Sound/Effects/Hmm_Women.wav"

Kiss_1 = "Sound/Effects/Kiss.wav"
Kiss_2 = "Sound/Effects/Kissing.wav"

Lion_Sound_1 = "Sound/Effects/Lion_Growling.wav"
Lion_Sound_2 = "Sound/Effects/Lion_Roar.wav"
Lion_Sound_3 = "Sound/Effects/Lion.wav"

Demon_Scream = "Sound/Effects/Monster_Growl.wav"
Growl = "Sound/Effects/SmallGrowl.wav"

Heaven_Chanting_1 = "Sound/Effects/Mystic_Chanting_1.wav"
Heaven_Chanting_2 = "Sound/Effects/Mystic_Chanting_2.wav"
Heaven_Chanting_3 = "Sound/Effects/Mystic_Chanting_3.wav"
Heaven_Chanting_4 = "Sound/Effects/Mystic_Chanting_4.wav"

Crickets = "Sound/Effects/Night_Sounds.wav"

Map = "Sound/Effects/Oppening_Map.wav"

Pain = "Sound/Effects/Pain.wav"

River_Sound = "Sound/Effects/River_Noise.wav"
Robotic_Sound = "Sound/Effects/robotic-noises.wav"
Swimming = "Sound/Effects/Water_Chunrning.wav"
MagicFinal = "Sound/Effects/MagicSuperAtack.wav"
Mud_Sound = "Sound/Effects/Slime.wav"

Lost = "Sound/Effects/LostItem.mp3"
Fail = "Sound/Effects/Fail.mp3"

Sword_Swing = "Sound/Effects/Sword_Swing.wav"

Footsteps_1 = "Sound/Effects/Footsteps_1.wav"
Footsteps_2 = "Sound/Effects/Footsteps_2.wav"
Running_Loud = "Sound/Effects/Running_Loud.wav"
Running = "Sound/Effects/Jogging-In-a-Forest.mp3"

Snake_Attack = "Sound/Effects/Snake_Attack.wav"
Punch = "Sound/Effects/Intense-punch.wav"
Snake_Poison = "Sound/Effects/SnakeyWoman.wav"
Dodge = "Sound/Effects/BambooSwing.wav"

Smash = "Sound/Effects/BigSmash.mp3"

Eating = "Sound/Effects/EatingChips.wav"

Magic_Spell = "Sound/Effects/MagicSpell.wav"
Amaterasu = "Sound/Effects/FireMagic.wav"
Youre_Mine = "Sound/Effects/YoureMine.wav"
Magic_Shield = "Sound/Effects/MagicShield.mp3"

worm = "Sound/Music/Worm.mp3"

Grabing = "Sound/Effects/Grab.mp3"

MonsterRun = "Sound/Effects/MonsterRun.mp3"

GlassBreak = "Sound/Effects/GlassSmash.wav"
StepInGrass = "Sound/Effects/WalkGrass.wav"

Raccoon_Sound = "Sound/Music/Worm.mp3"

Error = "Sound/Effects/ErrorBleep.mp3"
