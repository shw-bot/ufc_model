import sqlite3

#connect to the SQLite database
conn = sqlite3.connect('ufc_database.db')
cursor = conn.cursor()

#create a new table to add data from all_fighters to the current active fighters
cursor.execute('''
CREATE TABLE IF NOT EXISTS joined_current_fighters_history AS
SELECT
w_l,
weight_class,
method,
round,
time,
event,
date,
location,
fighter1,
fighter2,
kd_f1,
kd_f2,
str_f1,
str_f2,
td_f1,
td_f2,
sub_f1,
sub_f2,
ht_f1,
ht_f2,
wt_f1,
wt_f2,
reach_f1,
reach_f2,
stance_f1,
stance_f2,
w_f1,
w_f2,
l_f1,
l_f2,
d_f1,
d_f2,
belt_f1,
belt_f2,
country_f1,
country_f2,
age_in_2023_f1,
age_in_2023_f2,
active_f1,
active_f2

FROM joined_historical_fight_stats
WHERE active_f1 = 'TRUE' OR active_f2 = 'TRUE'
''')

#commit + close database
conn.commit()
conn.close()