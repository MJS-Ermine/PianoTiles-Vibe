# 鋼琴磚塊（Piano Tiles）— Vibe Coding 強化版

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-swag.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

本專案基於 [原始 Piano Tiles](https://github.com/pyGuru123/Python-Games/tree/master/Piano%20Tiles) 改良，加入 Vibe Coding 特色功能。

---

## 🆕 Vibe Coding 特色功能

- **計時賽模式**：遊戲有倒數計時，時間到自動結算分數。
- **生命值機制**：預設 3 條命，失誤才扣命，命用完才 Game Over。
- **加命/加時道具**：隨機出現特殊方塊，點擊可+1命或+5秒。
- **一行簡潔狀態顯示**：畫面上方一行顯示剩餘時間、生命、分數、最高分。
- **可擴充多種模式**（如經典/無盡/計時賽，預設為計時賽）。

---

## 安裝方式

請先安裝 [Python 3.10+](https://www.python.org/downloads/)。

安裝必要套件：
```bash
pip install pygame
```

---

## 玩法說明

- 點擊黑色方塊以得分，漏點或誤點會扣 1 命。
- 綠色方塊（紅心）為加命道具，點擊可+1命。
- 藍色方塊（黃圓）為加時道具，點擊可+5秒。
- 遊戲上方一行會顯示剩餘時間（T）、生命（L）、分數（S）、最高分（H）。
- 時間歸零或生命用完即結束遊戲。

---

## 使用方式

雙擊 `main.py` 或於終端機執行：
```bash
python main.py
```

---

## 貢獻說明

歡迎提出 Pull Request 或 Issue 討論改進建議。

---

## 版本說明

本專案由 MJS-Ermine 依據原始 Piano Tiles 改良，加入多項 Vibe Coding 特色功能。

---

## 版權

本專案僅供學術與教學用途，原始授權請見 [pyGuru123/Python-Games](https://github.com/pyGuru123/Python-Games/tree/master/Piano%20Tiles)。

<p align='center'>
	<img src='app.png' width=200 height=300>
</p>

## How to Download

Download this project from here [Download Piano Tiles](https://downgit.github.io/#/home?url=https://github.com/pyGuru123/Python-Games/tree/master/Piano%20Tiles)

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install following packages :-
* Pygame

```bash
pip install pygame
```

## Usage

Double click the game.py to open the game, Click start to start playing the game. The objective of the game is to click the tiles to without clicking anywhere else inthe game screen to generate musical notes. Also if a block reaches ground without getting clicked, game will get over.

Controls:
* Use Mousemotion to move & Left Mouse key to click tiles. 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.