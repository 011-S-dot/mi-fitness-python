"""二维码扫码登录，获取 Token。"""

from __future__ import annotations

import asyncio
from pathlib import Path

from mi_fitness.auth import XiaomiAuth
from mi_fitness.exceptions import AuthError

TOKEN_FILE = Path("token.json")


async def _qr_login() -> None:
    async def show_qr(qr_image_url: str, login_url: str) -> None:
        print("\n📱 请用小米账号 APP 扫描二维码登录")
        print(f"   二维码图片: {qr_image_url}")
        if login_url:
            print(f"   或在浏览器打开: {login_url}")
        print("\n⏳ 等待扫码...\n")

    async with XiaomiAuth() as auth:
        try:
            await auth.login_qr(qr_callback=show_qr)
        except AuthError as e:
            print(f"❌ 扫码登录失败: {e}")
            raise

        auth.save_token(TOKEN_FILE)
        print(f"✅ 扫码登录成功！user_id = {auth.token.user_id}")
        print(f"   Token 已保存至 {TOKEN_FILE.resolve()}")


def main() -> None:
    """CLI 入口。"""
    asyncio.run(_qr_login())


if __name__ == "__main__":
    main()
