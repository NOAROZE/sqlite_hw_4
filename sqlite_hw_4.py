import sqlite3
import os
if os.path.exists('sqlite_hw_4.sqbpro.db'):
    os.remove('sqlite_hw_4.sqbpro.db')
conn = sqlite3.connect('sqlite_hw_4.sqbpro.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE taxis (
    id INTEGER PRIMARY KEY,
    driver_name TEXT NOT NULL,
    car_type TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE passengers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    destination TEXT,
    taxi_id INTEGER,
    FOREIGN KEY(taxi_id) REFERENCES taxis(id)
);
''')

cursor.execute('''
INSERT INTO taxis (id, driver_name, car_type) VALUES
(1, 'Moshe Levi', 'Van'),
(2, 'Rina Cohen', 'Sedan'),
(3, 'David Azulay', 'Minibus'),
(4, 'Maya Bar', 'Electric'),
(5, 'Yossi Peretz', 'SUV');
''')

cursor.execute('''
INSERT INTO passengers (id, name, destination, taxi_id) VALUES
(1, 'Tamar', 'Jerusalem', 1),
(2, 'Eitan', 'Haifa', 2),
(3, 'Noa', 'Tel Aviv', NULL),
(4, 'Lior', 'Eilat', 1),
(5, 'Dana', 'Beer Sheva', NULL),
(6, 'Gil', 'Ashdod', 3),
(7, 'Moran', 'Netanya', NULL);
''')

print("---נוסעים שהשיגו מונית יחד עם פרטי המונית: INNER JOIN")
cursor.execute('''
SELECT p.name, p.destination, t.driver_name, t.car_type 
FROM passengers p
INNER JOIN taxis t ON p.taxi_id = t.id;
''')
for row in cursor.fetchall():
    print(dict(row))
print()


print("--- כל הנוסעים כולל כאלה שמצאו מונית וכאלה שלא: LEFT JOIN")
cursor.execute('''
SELECT p.name, p.destination, t.driver_name, t.car_type 
FROM passengers p
LEFT JOIN taxis t ON p.taxi_id = t.id;
''')
for row in cursor.fetchall():
    print(dict(row))
print()


print("---נוסעים שאין להם taxi_id תואם: LEFT JOIN")
cursor.execute('''
SELECT p.name, p.destination
FROM passengers p
LEFT JOIN taxis t ON p.taxi_id = t.id
WHERE t.driver_name IS NULL;
''')
for row in cursor.fetchall():
    print(dict(row))
print()


print("---כל הנוסעים וכל המוניות — גם אם אין התאמה ביניהם :LEFT EXCLUSIVE ")
cursor.execute('''
SELECT p.name, p.destination, t.driver_name, t.car_type 
FROM passengers p
FULL JOIN taxis t ON p.taxi_id = t.id;
''')
for row in cursor.fetchall():
    print(dict(row))
print()


print("---צירופים האפשריים בין נוסעים למוניות: CROSS JOIN")
cursor.execute('''
SELECT p.*, t.driver_name, t.car_type 
FROM passengers p
CROSS JOIN taxis t;
''')
for row in cursor.fetchall():
    print(dict(row))

conn.commit()
conn.close()
