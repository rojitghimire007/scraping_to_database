import sqlite3

conn = sqlite3.connect("my_friends.db")
c = conn.cursor()

'''
people = [
	("Roald","Amundsen", 5),
	("Rosa", "Parks", 8),
	("Henry", "Hudson", 7),
	("Neil","Armstrong", 7),
	("Daniel", "Boone", 3)]

average = 0
for person in people:
	c.execute("INSERT INTO friends VALUES(?,?,?)",person)
	average += person[2]
print(average / len(people))
'''

'''
c.execute("SELECT * FROM friends")
for result in c:
	print(result)
print("IT WORKED")
'''
u = input("please enter username: ")
p = input("please enter password: ")

query = f"SELECT * FROM friends WHERE username ='{u}' AND password = '{p}'"

c = con.cursor()
c.execute(query)

result = c.fetchone()
if (result):
	print("WECLOME BACK")
print("WRONG PASSWORD")

conn.commit()
conn.close()

