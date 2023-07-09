import sqlite3

#connect to the SQLite database
conn = sqlite3.connect('ufc_database.db')
cursor = conn.cursor()

#create a new table to add data from all_fighters to the current active fighters
cursor.execute('''
CREATE TABLE IF NOT EXISTS joined_current_fighters AS
SELECT
all_fighters.full_nm,
all_fighters.nickname,
all_fighters.ht,
all_fighters.wt,
all_fighters.reach,
all_fighters.stance,
all_fighters.w,
all_fighters.l,
all_fighters.d,
all_fighters.belt,
active_fighters.country,
active_fighters.age_in_2023,
active_fighters.sig_str_pm,
active_fighters.str_acc_percentage,
active_fighters.str_abs_pm,
active_fighters.str_def_percentage,
active_fighters.td_avg_15m,
active_fighters.td_acc_percentage,
active_fighters.td_def_percentage,
active_fighters.sub_avg_15m
FROM active_fighters
LEFT JOIN all_fighters ON active_fighters.full_nm = all_fighters.full_nm
''')

#commit + close
conn.commit()
conn.close()