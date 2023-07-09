# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 22:20:33 2023

@author: cinshalewolfe
"""

import sqlite3

#connect to the SQLite database
conn = sqlite3.connect('ufc_database.db')
cursor = conn.cursor()

#create a new table adding data from all_fighters to historic fight info
cursor.execute('''
CREATE TABLE IF NOT EXISTS joined_historical_fight_stats AS
SELECT
af.w_l,
af.weight_class,
af.method,
af.round,
af.time,
af.event,
af.date,
af.location,
af.fighter1,
af.fighter2,
af.kd_f1,
af.kd_f2,
af.str_f1,
af.str_f2,
af.td_f1,
af.td_f2,
af.sub_f1,
af.sub_f2,
ff1.ht AS ht_f1,
ff2.ht AS ht_f2,
ff1.wt AS wt_f1,
ff2.wt AS wt_f2,
ff1.reach AS reach_f1,
ff2.reach AS reach_f2,
ff1.stance AS stance_f1,
ff2.stance AS stance_f2,
ff1.w AS w_f1,
ff2.w AS w_f2,
ff1.l AS l_f1,
ff2.l AS l_f2,
ff1.d AS d_f1,
ff2.d AS d_f2,
ff1.belt AS belt_f1,
ff2.belt AS belt_f2,
ff1.country AS country_f1,
ff2.country AS country_f2,
ff1.age_in_2023 AS age_in_2023_f1,
ff2.age_in_2023 AS age_in_2023_f2,
ff1.active AS active_f1,
ff2.active AS active_f2

FROM all_fights af
JOIN all_fighters ff1 ON af.fighter1 = ff1.full_nm
JOIN all_fighters ff2 ON af.fighter2 = ff2.full_nm
'''
)

#commit + close database
conn.commit()
conn.close()