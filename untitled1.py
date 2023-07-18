# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 23:45:45 2023

@author: cinshalewolfe
"""

import sqlite3
import pandas as pd

#connect to the SQLite database
conn = sqlite3.connect('ufc_database.db')
cursor = conn.cursor()

#add the weight class info to the current fighters table
#cursor.execute(''' ALTER TABLE joined_current_fighters ADD COLUMN weight_class TEXT''')

#query = '''
 #              UPDATE joined_current_fighters
  #             SET weight_class = (
   #                SELECT weight_class FROM joined_current_fighters_history
    #               WHERE joined_current_fighters.full_nm = joined_current_fighters_history.fighter1
     #              OR joined_current_fighters.full_nm = joined_current_fighters_history.fighter2
      #             )
               
#'''
#cursor.execute(query)

fighters_query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM joined_current_fighters
                               ''', conn)

current_fighters = pd.DataFrame(fighters_query)

#commit + close database
conn.commit()
conn.close()

cols = ['full_nm', 'ht', 'weight_class']

test = pd.DataFrame(current_fighters[cols])
test.weight_class.unique()