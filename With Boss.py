import random

class Player:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mp = 50
        self.attackDamage = 10
        self.armor = 5
        self.isDead = False

    def __repr__(self):
        return self.name

    def printTest(self):
        print (self.name, self.health, self.attackDamage, self.armor, self.isDead)

    def hitEnemy(self, enemy):
        enemy.takeDamage(self.attackDamage)

    def luckyTrash(self, enemy):
        enemy.takeDamage(5)

    def pyroPanic(self, enemy):
        if self.mp >= 20:
         enemy.takeDamage(15)
         self.mp -= 20
         print(self.name + " spins around and begins to glow red. Fire shoots at the enemy from your hands  "+ str(
            self.health) + " Hp" + ", and " + str(
            self.mp) + " Mp")
        else:
            print("You don't have enough mana.")

    def blazingInferno(self, enemy):
        if self.mp >= 50:
         enemy.takeDamage(30)
         self.mp -= 50
         print(self.name + " casts a flaming bubble around the enemy. It implodes, and shoots out pillars of fire  "+ str(
            self.health) + " Hp" + ", and " + str(
            self.mp) + " Mp")
        else:
            print("You don't have enough mana.")

    def lightBlessing(self):
        if self.mp >= 40:
         self.mp -= 40
         self.health += 40
         print(self.name + " Your armor begins to glow. You feel slightly refreshed  "+ str(
            self.health) + " Hp" + ", and " + str(
            self.mp) + " Mp")
        else:
            print("You don't have enough mana.")

    def meditationStance(self):

         self.mp += 15
         print("You enter a defensive state of meditation. Your armor feeds your Mp  "+ str(
            self.health) + " Hp" + ", and " + str(
            self.mp) + " Mp")

    # damage the player, and kill them if they run out of health

    def takeDamage(self, damageAmount):
      if self.armor > 0:
          self.health -= (damageAmount * 0.50)
          self.armor -= 1
          print(self.name + " " + str(self.health) + " Hp" + ", and " + str(
            self.mp) + " Mp")

      else:
        self.health -= damageAmount
        #For test code.
        print(self.name + " " + str(self.health) + " Hp")

        # check if we're dead
      if (self.health <= 0):
            self.die()

    def die(self):
        self.isDead = True
        #For test code.
        #print(self.name + " has died.")

    def equipWeapon(self,weapon ):
           weapon.wielder = self
           self.attackDamage = weapon.damage
           print(self.name + " has equipped " + weapon.name + ". Attack damage is now " + str(self.attackDamage))

    def weaponEvolution(self,weapon ):
           weapon.wielder = self
           self.attackDamage = weapon.damage +10
           print(self.name + " 's " + weapon.name + " has increased in power. Attack damage is now " + str(self.attackDamage))

    def equipArmor(self,armor ):
           self.armor = armor.armor
           self.health += 50
           print(self.name + " has equipped " + armor.name + ". Armor is now " + str(self.armor) + ". The armor increases your health, and unlocks advanced magical abilities")

    def drinkPotion(self, potion):
        self.health += potion.heal
        self.mp += potion.mp
        #For test code.
        print(self.name + " drinks the "  + potion.name + ". The bottle vanishes.  "  + str(self.health) + " Hp" + ", and " + str(
            self.mp) + " Mp")

class Enemy:

    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attackDamage = attack

    def __repr__(self):
        return self.name


    def takeDamage(self, damageAmount):
        pass

    def getDamage(self):
         return self.attackDamage

    def printTest(self):
        print (self.name, self.health, self.attackDamage)

class Shroomba(Enemy):
    def __init__(self):
        super(Shroomba, self).__init__(name="Shroomba", health=10, attack=2)

    def takeDamage(self, damage):
        self.health -= damage * 2
        # For test code.
        print(self.name + " " + str(self.health) + " Hp")

class MegaShroomba(Shroomba):
    def __init__(self):
        super(MegaShroomba, self).__init__()
        self.name = "Mega Shroomba"
        self.health = 25
        self.attackDamage = 7

    def getDamage(self):
         return (random.randint(self.attackDamage, self.attackDamage + 10))

    def takeDamage(self, damage):
        self.health -= damage
        # For test code.
        print(self.name + " " + str(self.health) + " Hp")

class Toopa(Enemy):
    def __init__(self):
        super(Toopa, self).__init__(name="Toopa", health=15, attack=5)

    def takeDamage(self, damage):
        self.health -= damage
        # For test code.
        print(self.name + " " + str(self.health) + " Hp")

class BulletPhil(Enemy):
    def __init__(self):
        super(BulletPhil, self).__init__(name="Bullet Phil", health=20, attack=30)

    def takeDamage(self, damage):
        self.health -= damage * 0.5
        # For test code.
        print(self.name + " " + str(self.health) + " Hp")

class TestBoss(Enemy):
    def __init__(self):
        super(TestBoss, self).__init__(name="The Void", health=100, attack=30)

    def takeDamage(self, damage):
        self.health -= damage * 0.5
        # For test code.
        print(self.name + " " + str(self.health) + " Hp")
class Weapon:

    def __init__(self, name, damage, accuracy):
        self.name = name
        self.damage = damage
        self.accuracy = accuracy
        self.wielder = None

    def __repr__(self):
        return self.name

    def canAttack(self):
        pass

    def onAttack(self):
        pass

    #Will take an Enemy object as a parameter.
    def onHit(self):
        pass

    def onMiss(self):
        pass

    def printTest(self):
        print (self.name, self.damage, self.accuracy, self.wielder)

class MeleeWeapon(Weapon):
    def __init__(self,name, damage, accuracy,):
        super(MeleeWeapon, self).__init__(name, damage, accuracy)

    def canAttack(self):
        return True

class RockSword(MeleeWeapon):
    def __init__(self):
        super(RockSword, self).__init__(name="Rock Sword", damage=12, accuracy=70)

class CursedSword(MeleeWeapon):
    def __init__(self):
        super(CursedSword, self).__init__(name="Cursed Sword", damage=25, accuracy=90)

    def onAttack(self):
        self.player.takeDamage(2)

    def onHit(self, enemy):
        if (enemy.attackDamage > 1):
            enemy.attackDamage -= 1

class RangedWeapon(Weapon):
    def __init__(self, name, damage, accuracy, ammunition):
        self.ammunition = ammunition
        super(RangedWeapon, self).__init__(name, damage, accuracy)

    def canAttack(self):
        if self.ammunition > 0:
         return True
        else:
         return False

    def onAttack(self):
        self.ammunition -=1

    def printTest(self):
        print (self.name, self.damage, self.accuracy, self.ammunition, self.wielder)

class RockBow(RangedWeapon):
    def __init__(self):
        super(RockBow, self).__init__(name="Rock Bow", damage=15, accuracy=80,  ammunition=20)

class Loot:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return self.name

class Potion(Loot):
    def __init__(self, name, description, heal, mp):
        self.heal = heal
        self.mp = mp
        super(Potion, self).__init__(name, description)

class RedPotion(Potion):
    def __init__(self):
        super(RedPotion, self).__init__(name="Red Potion", description=" ", heal=5, mp=0)

class BluePotion(Potion):
    def __init__(self):
        super(BluePotion, self).__init__(name="Blue Potion", description=" ", heal=10, mp=15)

class MonsterJuice(Potion):
    def __init__(self):
        super(MonsterJuice, self).__init__(name="Monster Juice", description=" ", heal=(random.randint(-15, 15)), mp=(random.randint(-20, 20)))

class GodlyJaggerBomb(Potion):
    def __init__(self):
        super(GodlyJaggerBomb, self).__init__(name="Godly Jagger Bomb", description=" ", heal=(random.randint(0, 100)), mp=(random.randint(0, 100)))

class Armor(Loot):
    def __init__(self, name, description, armor):
        self.armor = armor
        super(Armor, self).__init__(name, description)

class SuperArmor(Armor):
    def __init__(self):
        super(SuperArmor, self).__init__(name="Lilah's Blessing", description=" ", armor=100)

def main():

 print("""=====Welcome to SIMULATION THEORY=====
        *You wake up in a daze.*

    *Neon lightening flickers and crackles around you.
    Shards of floating rock and metal debris flicker
    in and out of reality.*

     *A strange voice echoes in you brain.*
                """)
 playerName = input("What should we call you?")
 player = Player(playerName)
 print ("Hello " + playerName + "!")

 weapons = [RockSword(),
            CursedSword(),
            RockBow()]

 enemies = [Shroomba(),
            Toopa(),
            BulletPhil(),
            MegaShroomba()]

 loot = [RedPotion(),
         BluePotion(),
         MonsterJuice()]

 currentEnemy = None

 currentLoot = None

 currentBoss = None

 armor =SuperArmor()

 #weaponChoiceString = ""
 print("These tools might help you out:")
 for weapon in weapons:
     print (weapons.index(weapon) +1, end= '')
     print("",weapon)

 playerWeaponChoice = int(input("Choose your weapon: "))
 player.equipWeapon(weapons[playerWeaponChoice -1])

 while True:

  if len(enemies) == 0 and (currentEnemy == None):

      while True:

       if (currentBoss == None):

          currentBoss = TestBoss()

          print("Congratulations  " + playerName + ". You are worthy. The real fight with " + str(currentBoss) + " begins now!")
          print("Your foe has " + str(currentBoss.health) + " health and " + str(currentBoss.attackDamage) + " damage")
          player.equipArmor(armor)
          player.weaponEvolution(weapons[playerWeaponChoice - 1])
       else:
          print("The fight with " + str(currentBoss) + " continues! " + str(currentBoss) + " has " + str(
              currentBoss.health) + " health and " + str(currentBoss.attackDamage) + " damage")

       print("""=====ADVANCED BATTLE MENU=====
                   1. Attack
                   2. Run away
                   3. Drink potion
                   4. Discard potion
                   5. Fire magic plus
                   6. Minor heal
                   7. Meditation
                     """)
       playerAction = int(input("Enter Your Choice:"))
       if playerAction == 1:
          toHit = (random.randint(1, 100))
          if toHit <= (weapons[playerWeaponChoice - 1]).accuracy:
              print("It's battle time!")
              player.hitEnemy(currentBoss)
          else:
              print("Epic Fail! You have the aim of a Stormtrooper.")

       elif playerAction == 2:
          print("You heroically flee in terror.")
          exit()

       elif playerAction == 3:
          if (currentLoot == None):
              print(
                  "You don't have a potion. The enemy takes advantage of you standing idly. If you bothered to attack, an enemy might drop one.")
          else:
              player.drinkPotion(currentLoot)
              currentLoot = None
              print("You still look like an easy target to your opponent.")

       elif playerAction == 4:
          if (currentLoot == None):
              print(
                  "You don't have a potion. Maybe you drank it? Maybe you are drunk? The enemy takes advantage of you standing idly. If you bothered to attack, an enemy might drop one.")
          else:
              bottleSmash = (random.randint(1, 100))
              if bottleSmash <= 30:
                  player.luckyTrash(currentBoss)
                  currentLoot = None
                  print("Epic Win! Your bottle hits the enemy.")
              else:
                  currentLoot = None
                  print("The enemy takes a swing at you while you discard your item.")

       elif playerAction == 5:

              player.blazingInferno(currentBoss)
              if (currentBoss.health > 0):
                  print("The enemy makes it's move.")

       elif playerAction == 6:
           player.lightBlessing()
           if (currentBoss.health > 0):
               print("The enemy makes it's move.")

       elif playerAction == 7:
           player.meditationStance()
           if (currentBoss.health > 0):
               print("The enemy makes it's move.")

       if (currentBoss.health <= 0):
          print("The " + currentBoss.name + " has been slain!")
          print("You win. Thanks for playing!")
          exit()
          #if (currentLoot == None):
              #currentLoot = random.choice(loot)
          #print("The " + currentBoss.name + " has dropped " + str(currentLoot) + ".")
          #currentBoss = None

       if (currentBoss != None):
          enemyHit = (random.randint(1, 100))
          if enemyHit <= 60:
              player.takeDamage(currentBoss.attackDamage)
          else:
              print("Your fast reflexes dodge the enemy attack.")

       if (player.isDead):
          print("You have been slain by the ferocious " + currentBoss.name + "! Game Over")
          exit()

      #print (" Congratulations "  + playerName + ". You have defeated all enemies!")
      #exit()
  if (currentEnemy == None):

   currentEnemy = random.choice(enemies)
   enemies.remove(currentEnemy)

   print ( "A wild " + str(currentEnemy) + " appears...")
   print ("Your foe has "+ str(currentEnemy.health) + " health and "+ str(currentEnemy.attackDamage) + " damage")
  else:
      print("The fight with "+ str(currentEnemy) +" continues! " +  str(currentEnemy) +" has " + str(currentEnemy.health) + " health and " + str(currentEnemy.attackDamage) + " damage")

  print("""=====BATTLE MENU=====
               1. Attack
               2. Run away
               3. Drink potion
               4. Discard potion
               5. Fire magic
                 """)
  playerAction = int(input("Enter Your Choice:"))
  if playerAction == 1:
     toHit = (random.randint(1, 100))
     if toHit <= (weapons[playerWeaponChoice -1]).accuracy:
      print ("It's battle time!")
      player.hitEnemy(currentEnemy)
     else:
         print ("Epic Fail! You have the aim of a Stormtrooper.")

  elif playerAction == 2:
    print ("You heroically flee in terror.")
    exit()

  elif playerAction == 3:
      if (currentLoot == None):
          print ("You don't have a potion. The enemy takes advantage of you standing idly. If you bothered to attack, an enemy might drop one.")
      else:
       player.drinkPotion(currentLoot)
       currentLoot = None
       print ("You still look like an easy target to your opponent.")

  elif playerAction == 4:
      if (currentLoot == None):
          print ("You don't have a potion. Maybe you drank it? Maybe you are drunk? The enemy takes advantage of you standing idly. If you bothered to attack, an enemy might drop one.")
      else:
          bottleSmash = (random.randint(1, 100))
          if bottleSmash <= 30:
              player.luckyTrash(currentEnemy)
              currentLoot = None
              print("Epic Win! Your bottle hits the enemy.")
          else:
              currentLoot = None
              print("The enemy takes a swing at you while you discard your item.")

  elif playerAction == 5:

      tooHot = (random.randint(1, 100))
      if tooHot <= 50 and player.mp >= 20:
          player.takeDamage(10)
          player.pyroPanic(currentEnemy)
          print(player.name + " is on fire. You manage to damage both the enemy, and yourself! Practice makes perfect.  " )
          if (currentEnemy.health > 0):
           print ("The enemy makes it's move.")
      else:
          player.pyroPanic(currentEnemy)
          if (currentEnemy.health > 0):
           print("The enemy makes it's move.")

  if (currentEnemy.health <= 0):
         print ("The " + currentEnemy.name + " has been slain!")
         if (currentLoot == None):
          currentLoot = random.choice(loot)
          print("The " + currentEnemy.name + " has dropped "+ str(currentLoot) + ".")
         currentEnemy = None

  if (currentEnemy != None):
      enemyHit = (random.randint(1, 100))
      if enemyHit <= 60:
         player.takeDamage(currentEnemy.attackDamage)
      else:
          print("Your fast reflexes dodge the enemy attack.")

  if (player.isDead):
    print("You have been slain by the ferocious " + currentEnemy.name + "! Game Over")
    break

main()