# ✨ Tic Tac Toe

This is a polished **Tic Tac Toe game** built using [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter), giving it a modern and glowing UI flair. It supports both **2-player mode** and **vs Computer** (AI using Minimax algorithm).

## 📸 Screenshots

> 🖼️ Ensure you place `glow_x.png` and `glow_o.png` in the project folder for glowing effect!

## 🚀 Features

- ✅ Modern dark-themed GUI using CustomTkinter
- ✅ Glowing icons for X and O using Pillow
- ✅ Minimax-based unbeatable AI for single player mode
- ✅ Game reset and mode switching
- ✅ Clean UI with hover effects

## 🧠 Tech Stack

- Python 3.x
- customtkinter
- tkinter (Standard Library)
- Pillow (for image handling)

## 🗂️ Project Structure

```
tic-tac-toe/
├── assets/
│   ├── glow_x.png
│   └── glow_o.png
├── main.py
├── requirements.txt
└── README.md
```

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/swordboom/tic-tac-toe.git
cd tic-tac-toe
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

> 🐧 Linux Users: If tkinter is not preinstalled, install it using:
> ```bash
> sudo apt-get install python3-tk
> ```

### 3. Run the Game
```bash
cd src
python main.py
```

## ⚠️ Notes

- Make sure `glow_x.png` and `glow_o.png` are in an `assets/` folder in the same directory as `main.py`.
- AI is implemented using the Minimax algorithm (difficulty: hard-coded to perfect play).

## 📄 License

MIT License

Copyright (c) 2025 Soham Chakraborty

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
