import sqlite3
import random
import time

class Database:
	def __init__(self, db_file):
		self.connection = sqlite3.connect(db_file)
		self.cursor = self.connection.cursor()

	#ФЕРМА----------------------------------------------------------------------------------------------

	def add_user(self, userID, username, kol = 0, kol_time = 0):
		with self.connection:
			return self.cursor.execute("INSERT INTO ferma (userID, username , kol , kol_time) VALUES (?, ?, ?, ?)", (userID, username, kol, kol_time,))		

	def user_ex(self, userID):
		with self.connection:
			result = self.cursor.execute("SELECT * FROM ferma WHERE userID = ?", (userID,)).fetchall()
			return bool(len(result))

	def balance_update(self, kol, username, userID):
		with self.connection:
			return self.cursor.execute("UPDATE ferma SET kol = ?, username = ? WHERE userID = ?", (kol,username, userID,))


	def get_balance(self, userID):
		with self.connection:
			result = self.cursor.execute("SELECT kol FROM ferma WHERE userID = ?", (userID,)).fetchall()
			for row in result:
			    kol = str(row[0])
			return kol

	def set_time(self, kol_time, userID):
		with self.connection:
			return self.cursor.execute("UPDATE ferma SET kol_time = ? WHERE userID = ?", (kol_time ,userID,)) 

	def get_time(self, userID):
		with self.connection:
			result = self.cursor.execute("SELECT kol_time FROM ferma WHERE userID = ?", (userID,)).fetchall()
			for row in result:
			    kol_time = int(row[0])
			return kol_time

        #ТОП ИЗ ГОВНА И ПАЛОК---------------------------------------------------------------------------------

#1
	def get_kollNAME(self):
		with self.connection:
			result = self.cursor.execute("SELECT username FROM ferma ORDER BY KOL").fetchall()
			for row in result:
			    name = str(row[0])
			return name
	def get_koll(self):
		with self.connection:
			result = self.cursor.execute("SELECT kol FROM ferma ORDER BY KOL").fetchall()
			for row in result:
			    kol = str(row[0])
			return kol
#2
	def get_kollNAME2(self):
		with self.connection:
			result = self.cursor.execute("SELECT username FROM ferma ORDER BY KOL DESC LIMIT 1,1").fetchall()
			for row in result:
			    name = str(row[0])
			return name
	def get_koll2(self):
		with self.connection:
			result = self.cursor.execute("SELECT kol FROM ferma ORDER BY KOL DESC LIMIT 1,1").fetchall()
			for row in result:
			    kol = str(row[0])
			return kol

#3
	def get_kollNAME3(self):
		with self.connection:
			result = self.cursor.execute("SELECT username FROM ferma ORDER BY KOL DESC LIMIT 2,1").fetchall()
			for row in result:
				name = str(row[0])
			return name

	def get_koll3(self):
		with self.connection:
			result = self.cursor.execute("SELECT kol FROM ferma ORDER BY KOL DESC LIMIT 2,1").fetchall()
			for row in result:
				kol = str(row[0])
			return kol

#4
	def get_kollNAME4(self):
		with self.connection:
			result = self.cursor.execute("SELECT username FROM ferma ORDER BY KOL DESC LIMIT 3,1").fetchall()
			for row in result:
				name = str(row[0])
			return name

	def get_koll4(self):
		with self.connection:
			result = self.cursor.execute("SELECT kol FROM ferma ORDER BY KOL DESC LIMIT 3,1").fetchall()
			for row in result:
				kol = str(row[0])
			return kol

#5
	def get_kollNAME5(self):
		with self.connection:
			result = self.cursor.execute("SELECT username FROM ferma ORDER BY KOL DESC LIMIT 4,1").fetchall()
			for row in result:
				name = str(row[0])
			return name

	def get_koll5(self):
		with self.connection:
			result = self.cursor.execute("SELECT kol FROM ferma ORDER BY KOL DESC LIMIT 4,1").fetchall()
			for row in result:
				kol = str(row[0])
			return kol

#6
	def get_kollNAME6(self):
		with self.connection:
			result = self.cursor.execute("SELECT username FROM ferma ORDER BY KOL DESC LIMIT 5,1").fetchall()
			for row in result:
				name = str(row[0])
			return name

	def get_koll6(self):
		with self.connection:
			result = self.cursor.execute("SELECT kol FROM ferma ORDER BY KOL DESC LIMIT 5,1").fetchall()
			for row in result:
				kol = str(row[0])
			return kol

#7
	def get_kollNAME7(self):
		with self.connection:
			result = self.cursor.execute("SELECT username FROM ferma ORDER BY KOL DESC LIMIT 6,1").fetchall()
			for row in result:
				name = str(row[0])
			return name

	def get_koll7(self):
		with self.connection:
			result = self.cursor.execute("SELECT kol FROM ferma ORDER BY KOL DESC LIMIT 6,1").fetchall()
			for row in result:
				kol = str(row[0])
			return kol

#8
	def get_kollNAME8(self):
		with self.connection:
			result = self.cursor.execute("SELECT username FROM ferma ORDER BY KOL DESC LIMIT 7,1").fetchall()
			for row in result:
				name = str(row[0])
			return name

	def get_koll8(self):
		with self.connection:
			result = self.cursor.execute("SELECT kol FROM ferma ORDER BY KOL DESC LIMIT 7,1").fetchall()
			for row in result:
				kol = str(row[0])
			return kol

#9
	def get_kollNAME9(self):
		with self.connection:
			result = self.cursor.execute("SELECT username FROM ferma ORDER BY KOL DESC LIMIT 8,1").fetchall()
			for row in result:
				name = str(row[0])
			return name

	def get_koll9(self):
		with self.connection:
			result = self.cursor.execute("SELECT kol FROM ferma ORDER BY KOL DESC LIMIT 8,1").fetchall()
			for row in result:
				kol = str(row[0])
			return kol

#10
	def get_kollNAME10(self):
		with self.connection:
			result = self.cursor.execute("SELECT username FROM ferma ORDER BY KOL DESC LIMIT 9,1").fetchall()
			for row in result:
				name = str(row[0])
			return name

	def get_koll10(self):
		with self.connection:
			result = self.cursor.execute("SELECT kol FROM ferma ORDER BY KOL DESC LIMIT 9,1").fetchall()
			for row in result:
				kol = str(row[0])
			return kol

#11
	def get_kollNAME11(self):
		with self.connection:
			result = self.cursor.execute("SELECT username FROM ferma ORDER BY KOL DESC LIMIT 10,1").fetchall()
			for row in result:
				name = str(row[0])
			return name

	def get_koll11(self):
		with self.connection:
			result = self.cursor.execute("SELECT kol FROM ferma ORDER BY KOL DESC LIMIT 10,1").fetchall()
			for row in result:
				kol = str(row[0])
			return kol

#12
	def get_kollNAME12(self):
		with self.connection:
			result = self.cursor.execute("SELECT username FROM ferma ORDER BY KOL DESC LIMIT 11,1").fetchall()
			for row in result:
				name = str(row[0])
			return name

	def get_koll12(self):
		with self.connection:
			result = self.cursor.execute("SELECT kol FROM ferma ORDER BY KOL DESC LIMIT 11,1").fetchall()
			for row in result:
				kol = str(row[0])
			return kol

#13
	def get_kollNAME13(self):
		with self.connection:
			result = self.cursor.execute("SELECT username FROM ferma ORDER BY KOL DESC LIMIT 12,1").fetchall()
			for row in result:
				name = str(row[0])
			return name

	def get_koll13(self):
		with self.connection:
			result = self.cursor.execute("SELECT kol FROM ferma ORDER BY KOL DESC LIMIT 12,1").fetchall()
			for row in result:
				kol = str(row[0])
			return kol

#14
	def get_kollNAME14(self):
		with self.connection:
			result = self.cursor.execute("SELECT username FROM ferma ORDER BY KOL DESC LIMIT 13,1").fetchall()
			for row in result:
				name = str(row[0])
			return name

	def get_koll14(self):
		with self.connection:
			result = self.cursor.execute("SELECT kol FROM ferma ORDER BY KOL DESC LIMIT 13,1").fetchall()
			for row in result:
				kol = str(row[0])
			return kol

#15
	def get_kollNAME15(self):
		with self.connection:
			result = self.cursor.execute("SELECT username FROM ferma ORDER BY KOL DESC LIMIT 14,1").fetchall()
			for row in result:
				name = str(row[0])
			return name

	def get_koll15(self):
		with self.connection:
			result = self.cursor.execute("SELECT kol FROM ferma ORDER BY KOL DESC LIMIT 14,1").fetchall()
			for row in result:
				kol = str(row[0])
			return kol

	#МУТЫ----------------------------------------------------------------------------------------------

	def user_ex2(self, user_id):
		with self.connection:
			result = self.cursor.execute("SELECT * FROM ct_users WHERE user_id = ?", (user_id,)).fetchall()
			return bool(len(result))

	def add_user_mute(self, user_id, username):
		with self.connection:
			return self.cursor.execute("INSERT INTO ct_users (user_id, username) VALUES (?,?)", (user_id, username,))	

	def mute(self, user_id):
		with self.connection:	
		    user = self.cursor.execute("SELECT * FROM ct_users WHERE user_id = ?", (user_id,)).fetchone()	
		    return int(user[3]) >= int(time.time())		

	def add_mute(self, user_id, mute_time):
		with self.connection:
			return self.cursor.execute("UPDATE ct_users SET mute_time = ? WHERE user_id = ?", (int(time.time()) + mute_time, user_id,))

    # БОНУСЫ----------------------------------------------------------------------------------------------

#vroraya jizn'

	def bonus_ex(self, userID):
			result = self.cursor.execute("SELECT * FROM bonuses WHERE userID = ?", (userID,)).fetchall()
			return bool(len(result))

	def add_bonus(self, userID, username, bonusID = 1, bonusNAME = 'Вторая жизнь'):
		with self.connection:
			return self.cursor.execute("INSERT INTO bonuses (userID, username, bonusID, bonusNAME) VALUES (?, ?, ?, ?)", (userID, username, bonusID, bonusNAME,))

#lastochka

	def bonus2_ex(self, userID):
		result = self.cursor.execute("SELECT * FROM lastochka WHERE userID = ?", (userID,)).fetchall()
		return bool(len(result))

	def add_bonus2(self, userID, username, bonusID=2):
		with self.connection:
			return self.cursor.execute(	"INSERT INTO lastochka (userID, username, bonusID) VALUES (?, ?, ?)", (userID, username, bonusID,))

#lakomka

	def bonus3_ex(self, userID):
		result = self.cursor.execute("SELECT * FROM lakomka WHERE userID = ?", (userID,)).fetchall()
		return bool(len(result))

	def add_bonus3(self, userID, username, bonus_time, bonusID=3):
		with self.connection:
			return self.cursor.execute(	"INSERT INTO lakomka (userID, username, bonus_time, bonusID) VALUES (?, ?, ?, ?)", (userID, username,bonus_time, bonusID,))


	

async def get_all(self):
	with self.connection:
		products = self.cursor.execute("SELECT * FROM bonuses").fatchall()
		return products
