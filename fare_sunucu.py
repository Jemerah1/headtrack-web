import _asyncio
import json
import pyautogui
import websockets

pyautogui.PUASE = 0

genislik, yukseklik = pyautogui.size()

async def isle(websocket):
    print("Tarayıcı bağlandı.")
    async for mesaj in websocket:
        veri = json.loads(mesaj)

        x = genislik / 2 + veri["x"] * (genislik / 2)
        y = yukseklik / 2 + veri["y"] * (yukseklik / 2)

        x = max(1, min(genislik - 2, x))
        y = max(1, min(yukseklik - 2, y))

        pyautogui.moveTo(x, y)

async def main():
    async with websockets.serve(isle, "localhost", 8765):
        print("Fare programı çalışıyor. Durdurmak için Ctrl+C.")
        await _asyncio.Future()  

asyncio.run(main())
       