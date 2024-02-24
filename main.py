import time
from typing import Optional

from pydantic import Field, BaseModel
import pyautogui


class KeyboardClicker(BaseModel):
    button: str = Field(..., description="要連點的按鈕名稱")
    clicks: Optional[int] = Field(..., description="點擊次數 None為無限")
    interval: float = Field(..., description="每次點擊之間的間隔時間(單位為秒)")

    def click_button(self):
        """連點指定的按鈕。

        :param button: 要連點的按鈕名稱
        :param clicks: 連點次數
        :param interval: 每次點擊之間的間隔時間(單位為秒)
        """
        if self.clicks:
            for _ in range(self.clicks):
                pyautogui.press(self.button)
                time.sleep(self.interval)
        else:
            while True:
                pyautogui.press(self.button)
                time.sleep(self.interval)


if __name__ == "__main__":
    KeyboardClicker(button="ctrl", clicks=None, interval=0.0).click_button()
