import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('ufc_database.db')
cursor = conn.cursor()

# Update the fights table to split the data into separate columns for each fighter


cursor.execute('ALTER TABLE all_fights ADD COLUMN fighter1 TEXT')
cursor.execute('ALTER TABLE all_fights ADD COLUMN fighter2 TEXT')
cursor.execute('ALTER TABLE all_fights ADD COLUMN kd_f1 INTEGER')
cursor.execute('ALTER TABLE all_fights ADD COLUMN kd_f2 INTEGER')
cursor.execute('ALTER TABLE all_fights ADD COLUMN str_f1 INTEGER')
cursor.execute('ALTER TABLE all_fights ADD COLUMN str_f2 INTEGER')
cursor.execute('ALTER TABLE all_fights ADD COLUMN td_f1 INTEGER')
cursor.execute('ALTER TABLE all_fights ADD COLUMN td_f2 INTEGER')
cursor.execute('ALTER TABLE all_fights ADD COLUMN sub_f1 INTEGER')
cursor.execute('ALTER TABLE all_fights ADD COLUMN sub_f2 INTEGER')

#delete the old columns
cursor.execute('ALTER TABLE all_fights DROP COLUMN fighters')
cursor.execute('ALTER TABLE all_fights DROP COLUMN kd')
cursor.execute('ALTER TABLE all_fights DROP COLUMN str')
cursor.execute('ALTER TABLE all_fights DROP COLUMN td')
cursor.execute('ALTER TABLE all_fights DROP COLUMN sub')


# Update the new columns with separated values
update_query = '''
    UPDATE all_fights
    SET
        fighter1 = TRIM(SUBSTR(fighters, 1, INSTR(fighters, '  '))),
        fighter2 = TRIM(SUBSTR(fighters, INSTR(fighters, '  ') + 2)),
        kd_f1 = CAST(TRIM(SUBSTR(kd, 1, INSTR(kd, '  '))) AS INTEGER),
        kd_f2 = CAST(TRIM(SUBSTR(kd, INSTR(kd, '  ') + 2)) AS INTEGER),
        str_f1 = CAST(TRIM(SUBSTR(str, 1, INSTR(str, '  '))) AS INTEGER),
        str_f2 = CAST(TRIM(SUBSTR(str, INSTR(str, '  ') + 2)) AS INTEGER),
        td_f1 = CAST(TRIM(SUBSTR(td, 1, INSTR(td, '  '))) AS INTEGER),
        td_f2 = CAST(TRIM(SUBSTR(td, INSTR(td, '  ') + 2)) AS INTEGER),
        sub_f1 = CAST(TRIM(SUBSTR(sub, 1, INSTR(sub, '  '))) AS INTEGER),
        sub_f2 = CAST(TRIM(SUBSTR(sub, INSTR(sub, '  ') + 2)) AS INTEGER)
'''

cursor.execute(update_query)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()


