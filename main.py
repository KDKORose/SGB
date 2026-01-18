import asyncio
from app import BotApp

def main():
    app = BotApp()
    asyncio.run(app.run())

if __name__ == "__main__":
    main()
