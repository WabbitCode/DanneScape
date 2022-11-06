from item import Weapon
from item import Armor
from item import Potion
from item import Armor_Misc

# Weapons ----

fists = Weapon("Fists", 1, 1)
bronze_2h = Weapon("Bronze 2-handed Sword", 10, 10)
iron_2h = Weapon("Iron 2-handed Sword", 14, 14)
steel_2h = Weapon("Steel 2-handed Sword", 22, 22)
black_2h = Weapon("Black 2-handed Sword", 22, 28)
mithril_2h = Weapon("Mithril 2-handed Sword", 31, 31)
adamantite_2h = Weapon("Adamantite 2-handed Sword", 44, 44)
rune_2h = Weapon("Rune 2-handed Sword", 70, 70)
dragon_long = Weapon("Dragon Sword", 71, 71)
dragon_axe = Weapon("Dragon Axe", 75, 69)

# Necklace

ruby_amulet = Armor_Misc("Ruby Amulet of strength", 10)

# Armor ----

# Missing armor

missing_helmet = Armor("No helmet equiped", 1)
missing_body = Armor("No body equiped", 1)
missing_legs = Armor("No legs equiped", 1)

# Bronze

bronze_helmet = Armor("Large Bronze Helmet", 4)
bronze_body = Armor("Bronze Plate Mail Body", 14)
bronze_legs = Armor("Bronze Plate Mail Legs", 7)

# Iron
iron_helmet = Armor("Large Iron Helmet", 6)
iron_body = Armor("Iron Plate Mail Body", 20)
iron_legs = Armor("Iron Plate Mail Legs", 10)

# Steel
steel_helmet = Armor("Large Steel Helmet", 9)
steel_body = Armor("Steel Plate Mail Body", 31)
steel_legs = Armor("Steel Plate Mail Legs", 16)

# Black
black_helmet = Armor("Large Black Helmet", 12)
black_body = Armor("Black Plate Mail Body", 40)
black_legs = Armor("Black Plate Mail Legs", 21)

# Mitrhil
mithril_helmet = Armor("Large Mithril Helmet", 13)
mithril_body = Armor("Mithril Plate Mail Body", 44)
mithril_legs = Armor("Mithril Plate Mail Legs", 22)

# Adamantite
adamantite_helmet = Armor("Large Adamantite Helmet", 19)
adamantite_body = Armor("Adamantite Plate Mail Body", 63)
adamantite_legs = Armor("Adamantite Plate Mail Legs", 31)

# Rune
rune_helmet = Armor("Large Rune Helmet", 30)
rune_body = Armor("Rune Plate Mail Body", 80)
rune_legs = Armor("Rune Plate Mail Legs", 49)

# Potions
strength_potion = Potion("Strength Potion", 1.14)
super_strength_potion = Potion("Super Strength Potion", 1.205)
attack_potion = Potion("Attack Potion", 1.14)
super_attack_potion = Potion("Super Attack Potion", 1.205)
defense_potion = Potion("Defense Potion", 1.14)
super_defense_potion = Potion("Super Defense Potion", 1.205)
no_potion = Potion("No potion", 1)
