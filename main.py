import asyncio
from app import BotApp
from dotenv import load_dotenv

load_dotenv()

def main():
    app = BotApp()
    asyncio.run(app.run())

if __name__ == "__main__":
    main()
