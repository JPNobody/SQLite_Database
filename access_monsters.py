"""
This program gives a user access to the monsters database 
in order to view, add, edit, or delete monsters. 
"""

import sqlite3

# connect to the database



def create_update_table(table, column, column_id):
   """
   This function creates functions that update columns in a table.
   """
   sqlite_query = "UPDATE "+ table +" SET " + column + " = ? WHERE " + str(column_id) + " = ?"
   def update_monster(conn, values):
      """
      Th function is passed in the cursor of the database, and a
      tuple of values which includes the table to be edited, what column
      to edit, what to set the new column value to, and the monster_id
      for the monster to edit.
      """
      c = conn.cursor()
      c.execute(sqlite_query, values)
      conn.commit()
   return update_monster

# def create_print_instructions(conn):
#    def print_instructions(conn):
#       c = conn.cursor()
#    c = conn.cursor()
#    return print_instructions
#    # Make it so that this function creates functions that print out instructions

# def print_monster():
"""
This function makes functions that print out monsters based on different things.
"""

# create a function that creates these types of functions.
def print_out_monster_table(cursor):
   """
   This function prints out the monster table in the database.
   """
   print("{:>20}  {:>10}  {:>10}  {:>15}  {:>10}  {:>10}  {:>10}  {:>20}".format("Name", "CR", "level", "game", "alignment", "size", "Family", "Creature type"))
   for record in cursor.fetchall():
      print("{:>20}  {:>10}  {:>10}  {:>15}  {:>10}  {:>10}  {:>10}  {:>20}".format(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]))
   print()

def print_out_monster(cursor):
   """
   This function prints out all the information for a particular monster 
   """
   for record in cursor.fetchall():
      print(cursor.description[cursor.fetchall.index(record)], " ", record)
   pass

def displayPart2(c):
   """
   This function fully displays a monster with all it's attacks and abilities and such.
   """
   sqlite_query = """SELECT * 
                     FROM monsters m
                     INNER JOIN monster_abilities mab 
                     ON mab.monster_id = m.monster_id
                     INNER JOIN abilities ab 
                     ON ab.id = mab.ability_id
                     INNER JOIN attributes attr
                     ON attr.monster_id = m.monster_id
                     INNER JOIN monster_attacks mat
                     ON mat.monster_id = m.monster_id
                     INNER JOIN attacks atta
                     ON atta.id = mat.attack_id
                     INNER JOIN skill_value sv
                     ON sv.monster_id = m.monster_id
                     INNER JOIN skills s
                     ON s.id = sv.skill_id
                     WHERE m.name = ?
                     ;"""
   print("Would you like to see a monster? y/n")
   choice = input("> ")
   if choice == "y":
      name = input("Monster: ")
      value = (name,)
      c.execute(sqlite_query, value)

def display(conn):
   """
   This function should display all the monsters
   and connected tables

   which it only displays the basic monster table right now.
   """
   c = conn.cursor()
   choice = None
   while choice != "6":
      print("1) Display by name")
      print("2) Display by level")
      print("3) Display by alignment")
      print("4) Display by size")
      print("5) Display by creature type")
      print("6) Back")
      choice = input("> ")
      print()
      if choice == "1":
         c.execute("SELECT * FROM monsters ORDER BY name")
         print_out_monster_table(c)

      elif choice == "2":
         c.execute("SELECT * FROM monsters ORDER BY level")
         print_out_monster_table(c)

      elif choice == "3":
         c.execute("SELECT * FROM monsters ORDER BY alignment")
         print_out_monster_table(c)

      elif choice == "4":
         c.execute("SELECT * FROM monsters ORDER BY size")
         print_out_monster_table(c)

      elif choice == "5":
         c.execute("SELECT * FROM monsters ORDER BY creature_type")
         print_out_monster_table(c)


      elif choice == "6":
         print()
      
      else: 
         print("invalid choice. try again.")




def add_monster(conn):
   """
   This function should add a new monster to 
   all the tables

   It should also be able to add ablilities and attacks to the 
   monsters. 

   right now it only inserts into the monster table 
   """
   c = conn.cursor()
   name = input("Name: ")
   CR = input("CR(optional): ")
   level = int(input("Level: "))
   game = input("Game(optional): ")
   alignment = input("Alignment: ")
   size = input("size: ")
   family = input("Monster family(optional): ")
   creature_type = input("Creature Type: ")
   values = (name, CR, level, game, alignment, size, family, creature_type)
   c.execute("INSERT INTO monsters (name, CR, level, game, alignment, size, family, creature_type) VALUES (?,?,?,?,?,?,?,?)", values)
   conn.commit()
   print()

def add_attack(conn):
   """
   This function adds an attack to the attacks table and connects it
   to a monster via the monster_attacks column
   """
   pass

def add_ability(conn):
   """
   This function adds an ability to the abilities table and connects it
   to a monster via the monster_abilities column
   """
   pass

def add_skill(conn):
   """
   This function adds an skill to the skill table
   """
   pass

def add_skill_value(conn):
   """
   This function adds an value for a monster to the 
   skill_value table
   """
   pass

def update(conn):
   """
   This function should update a monster in 
   all the tables

   which it does not do rn
   """
   choice = None
   c = conn.cursor()
   name = (input("Monster to update: "),)
   c.execute("SELECT monster_id FROM monsters WHERE name = ?", name)
   if len(c.description) > 0:
      monster_id = c.fetchone()[0]
   else:
      print("Error! Monster not found.")
      print()
      return
   table = "monsters"
   column_id = "monster_id"
   update_monster_name = create_update_table(table, "name", column_id)
   update_monster_CR = create_update_table(table, "CR", column_id)
   update_monster_level = create_update_table(table, "level", column_id)
   update_monster_game = create_update_table(table, "game", column_id)
   update_monster_alignment = create_update_table(table, "alignment", column_id)
   update_monster_size = create_update_table(table, "size", column_id)
   update_monster_family = create_update_table(table, "family", column_id)
   update_monster_creature_type = create_update_table(table, "creature_type", column_id)

   while choice != "9":
      print("1) Update name")
      print("2) Update CR")
      print("3) Update level")
      print("4) Update game")
      print("5) Update alignment")
      print("6) Update size")
      print("7) Update creature family")
      print("8) Update creature type")
      print("9) Back")
      choice = input("> ")
      print()
      if choice == "1":
         value = (input("Change value to: "))
         values = (value, monster_id)
         update_monster_name(conn, values)

      elif choice == "2":
         value = (input("Change value to: "))
         values = (value, monster_id)
         update_monster_CR(conn, values)

      elif choice == "3":
         value = input("Change value to: ")
         values = (value, monster_id)
         c = conn.cursor()
         update_monster_level(conn, values)
         print()

      elif choice == "4":
         value = (input("Change value to: "))
         values = (value, monster_id)
         update_monster_game(conn, values)
         print()

      elif choice == "5":
         value = (input("Change value to: "))
         values = (value, monster_id)
         update_monster_alignment(conn, values)
         print()

      elif choice == "6":
         value = (input("Change value to: "))
         values = (value, monster_id)
         update_monster_size(conn, values)
         print()

      elif choice == "7":
         value = (input("Change value to: "))
         values = (value, monster_id)
         update_monster_family(conn, values)
         print()

      elif choice == "8":
         value = (input("Change value to: "))
         values = (value, monster_id)
         update_monster_creature_type(conn, values)
         print()

      elif choice == "9":
         print()
      
      else: 
         print("invalid choice. try again.")

   

def delete(conn):
   """
   This function should delete a monster from 
   all the tables

   which it does not do rn
   """
   c = conn.cursor()
   name = input("Name: ")
   values = (name,)
   c.execute("DELETE FROM monsters WHERE name = ?", values)
   conn.commit()
         



def main():
   conn = sqlite3.connect("tabletop_monsters.db")
   

   choice = None

   while choice != "5":
      print("1) Display Monsters")
      print("2) Add Monster")
      print("3) Update Monster")
      print("4) Delete Monster")
      print("5) Quit")
      choice = input("> ")
      print()
      if choice == "1":
         # Display Monsters
         display(conn)
         

      elif choice == "2":
         # Add New Monster
         add_monster(conn)

      elif choice == "3":
         # Update Monster 
         update(conn) 

      elif choice == "4":
         # Delete Monster
         delete(conn)

      elif choice == "5":
         print()
         # Close the database connection before exiting
         conn.close()
      
      else: 
         print("invalid choice. try again.")


main()
         


   