import asyncio
import os
from pathlib import Path
from mi_fitness import MiHealthClient


async def main():
    uid = os.environ["USER_ID"]
    async with MiHealthClient.from_token(Path("token.json")) as client:
        latest = await client.get_latest_data(uid)
        print("❤️ 心率:", latest.heart_rate.bpm if latest.heart_rate else "无数据", "bpm")
        print("😴 睡眠:", latest.sleep.total_duration if latest.sleep else "无数据", "分钟")
        print("👣 步数:", latest.steps.steps if latest.steps else "无数据", "步")


asyncio.run(main())
