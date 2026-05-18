# 🔑 KeyLogger

A simple Python keylogger that records keystrokes to a log file, with support for special keys and automatic daily separators.

---

## 📋 Features

- Logs all typed characters to `keyfile.txt`
- Records the **Enter** key as a real newline
- Records **Space** and **Tab** properly
- Logs **Backspace** as `[BACKSPACE]`
- Automatically adds a **daily separator** every 24 hours with the current date

---

## 📁 Output Format

The log file (`keyfile.txt`) is organized by day:

```
------------------------------------------------
--- 2026-05-18 ---
------------------------------------------------
Hello world
This is a new line
[BACKSPACE]fixed typo
```

---

## ⚙️ Requirements

- Python 3.x
- [`pynput`](https://pypi.org/project/pynput/) library

---

## 📦 Installation

**1. Clone or download the script**

```bash
git clone https://github.com/your-username/keylogger.git
cd keylogger
```

**2. Install the required dependency**

```bash
pip install pynput
```

---

## 🚀 Usage

Run the script with Python:

```bash
python keylogger.py
```

- The program starts listening to all keystrokes immediately.
- Press **Enter** in the terminal to stop the logger.
- All keystrokes are saved in `keyfile.txt` in the same directory.

---

## 🗂️ File Structure

```
keylogger/
│
├── keylogger.py       # Main script
├── keyfile.txt        # Output log file (auto-created)
└── README.md          # This file
```

---

## ⌨️ Key Mapping

| Key       | Logged As       |
|-----------|-----------------|
| Letters / Numbers | As-is    |
| Enter     | Newline `\n`    |
| Space     | Space ` `       |
| Tab       | Tab `\t`        |
| Backspace | `[BACKSPACE]`   |
| Other special keys | Ignored |

---

## ⚠️ Disclaimer

> This tool is intended **for educational purposes only**.  
> Only use it on your **own device** and with **full consent** of anyone whose input may be recorded.  
> Unauthorized use of keyloggers is **illegal** and unethical.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
