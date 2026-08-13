import asyncio
import os
from pathlib import Path
from mi_fitness import MiHealthClient


async def main():
    async with MiHealthClient.from_token(Path("token.json")) as client:
        # 先获取亲友列表
        relatives = await client.get_relatives()
        print(f"已绑定 {len(relatives)} 位亲友：")
        for r in relatives:
            print(f"  - [{r.relative_uid}] {r.relative_note or '(未设置备注)'}")

        if not relatives:
            print("未找到亲友，请先在App中添加亲友关系")
            return

        # 查询第一位亲友的数据
        target = relatives[0]
        uid = target.relative_uid
        print(f"\n查询 [{target.relative_note}] 的健康数据：")

        latest = await client.get_latest_data(uid)

        if latest.heart_rate:
            print(f"❤️ 心率: {latest.heart_rate.bpm} bpm")
        if latest.sleep:
            print(f"😴 睡眠: {latest.sleep.total_duration}分钟 评分{latest.sleep.sleep_score}/100")
        if latest.steps:
            print(f"👣 步数: {latest.steps.steps}步 / {latest.steps.distance}米")


asyncio.run(main())
