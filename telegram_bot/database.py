import aiosqlite

DB_NAME = "chat_history.db"

async def init():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''CREATE TABLE IF NOT EXISTS history
                          (user_id INT, role TEXT, content TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        await db.commit()

async def get(user_id, limit=5):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute('''SELECT role, content FROM history 
                                   WHERE user_id = ? 
                                   ORDER BY timestamp DESC LIMIT ?''', (user_id, limit))
        history = await cursor.fetchall()
        return reversed(history)   # type: ignore

async def save(user_id, role, content):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''INSERT INTO history (user_id, role, content) 
                          VALUES (?, ?, ?)''', (user_id, role, content))
        await db.commit()