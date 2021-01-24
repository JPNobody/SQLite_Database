"""
This program is used to create a monster_database in SQLite3 
according to the database diagram created.
"""




import sqlite3
from sqlite3 import Error


def create_table(conn, create_table_sqlite):
   """
   This function takes in perameters and creates
   a sqlite3 table in the database. It also checks
   for errors with the connection.
   *parameter conn -> connection object
   *perameter create_table_sqlite -> a CREATE TABLE statement
   """
   try:
      c = conn.cursor()
      c.execute(create_table_sqlite)
   except Error as e:
      print(e)

def main():


   connection = sqlite3.connect("tabletop_monsters.db")

   # This part stores the sqlite3 statements as variables.
   sql_create_monsters_table = """ CREATE TABLE IF NOT EXISTS monsters (
                                       id integer PRIMARY KEY AUTOINCREMENT,
                                       name text NOT NULL,
                                       CR text,
                                       level integer NOT NULL,
                                       game text,
                                       alignment text NOT NULL,
                                       size text NOT NULL,
                                       Family text,
                                       creature_type text NOT NULL
                                    ); """

   sql_create_attributes_table = """ CREATE TABLE IF NOT EXISTS attributes (
                                       id integer PRIMARY KEY AUTOINCREMENT,
                                       strength text NOT NULL,
                                       dexterity text NOT NULL,
                                       constitution text NOT NULL,
                                       intelligence text NOT NULL,
                                       wisdom text NOT NULL,
                                       charisma text NOT NULL,
                                       armor_class integer NOT NULL,
                                       fortitude text NOT NULL,
                                       reflex text NOT NULL,
                                       will text NOT NULL,
                                       hit_points integer NOT NULL,
                                       monster_id integer NOT NULL,
                                       FOREIGN KEY (monster_id) REFERENCES monsters (id)      
                                          );"""

   sql_create_abilities_table =  """ CREATE TABLE IF NOT EXISTS abilities (
                                       id integer PRIMARY KEY AUTOINCREMENT,
                                       name text NOT NULL,
                                       description text NOT NULL
                                    );""" 

   sql_create_monster_abilities_table = """ CREATE TABLE IF NOT EXISTS monster_abilities (
                                                id integer PRIMARY KEY AUTOINCREMENT,
                                                monster_id integer NOT NULL,
                                                ability_id integer NOT NULL,
                                                FOREIGN KEY (monster_id) REFERENCES monsters (id),
                                                FOREIGN KEY (ability_id) REFERENCES abilities (id)
                                             );"""                

   sql_create_skills_table =  """ CREATE TABLE IF NOT EXISTS skills (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    name text NOT NULL,
                                    description text NOT NULL
                                 );""" 

   sql_create_skill_value_table = """ CREATE TABLE IF NOT EXISTS skill_value (
                                                id integer PRIMARY KEY AUTOINCREMENT,
                                                monster_id integer NOT NULL,
                                                skill_id integer NOT NULL,
                                                value text NOT NULL,
                                                FOREIGN KEY (monster_id) REFERENCES monsters (id),
                                                FOREIGN KEY (skill_id) REFERENCES skills (id)
                                             );"""                                                          


   sql_create_attacks_table =  """ CREATE TABLE IF NOT EXISTS attacks (
                                       id integer PRIMARY KEY AUTOINCREMENT,
                                       name text NOT NULL,
                                       description text NOT NULL,
                                       range text NOT NULL,
                                       damage_dice text NOT NULL
                                    );""" 

   sql_create_monster_attacks_table = """ CREATE TABLE IF NOT EXISTS monster_attacks (
                                                id integer PRIMARY KEY AUTOINCREMENT,
                                                monster_id integer NOT NULL,
                                                attack_id integer NOT NULL,
                                                FOREIGN KEY (monster_id) REFERENCES monsters (id),
                                                FOREIGN KEY (attack_id) REFERENCES attacks (id)
                                             );"""            
   

   # This part of the code actually creates the tables
   if connection is not None:
      # creates the monsters table
      create_table(connection, sql_create_monsters_table)

      # creates the attributes table
      create_table(connection, sql_create_attributes_table)

      # creates the abilities table
      create_table(connection, sql_create_abilities_table)

      # creates the monster_abilities table
      create_table(connection, sql_create_monster_abilities_table)

      # creates the skills table
      create_table(connection, sql_create_skills_table)

      # creates the monster skills table
      create_table(connection, sql_create_skill_value_table)

      # creates the attacks table
      create_table(connection, sql_create_attacks_table)

      # creates the monster attacks table
      create_table(connection, sql_create_monster_attacks_table)

      

   else: 
      print("Error! cannot connect to database.")

   c = connection.cursor()
   #c.execute("ALTER TABLE monsters RENAME COLUMN id TO monster_id;" ) 
   #c.execute("ALTER TABLE monsters RENAME COLUMN Family TO family;" ) 
   c.execute("SELECT * \
                     FROM monsters m \
                     INNER JOIN monster_abilities mab \
                     ON mab.monster_id = m.monster_id \
                     INNER JOIN abilities ab \
                     ON ab.id = mab.ability_id \
                     INNER JOIN attributes attr \
                     ON attr.monster_id = m.monster_id \
                     INNER JOIN monster_attacks mat \
                     ON mat.monster_id = m.monster_id \
                     INNER JOIN attacks atta \
                     ON atta.id = mat.attack_id \
                     INNER JOIN skill_value sv \
                     ON sv.monster_id = m.monster_id \
                     INNER JOIN skills s \
                     ON s.id = sv.skill_id \
                     WHERE m.name = ? \
                     ;", ("Boar",))
   for record in c.fetchall():
      print(record)
   c.execute("SELECT * FROM monsters WHERE name = ?", ("Boar",))
   for record in c.fetchall():
      print(record)
   connection.close()



main()





