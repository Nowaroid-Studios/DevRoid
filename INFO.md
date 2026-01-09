# devroid - Minimale Library

## 📦 Inhalt

```
devroid/
├── devroid/           # Python Package
│   ├── __init__.py
│   └── wizzycolor.py
├── README.md          # Dokumentation
├── LICENSE            # MIT Lizenz
├── setup.py           # Setup-Skript
├── pyproject.toml     # Moderne Build-Config
├── MANIFEST.in        # Distribution
└── .gitignore        # Git Ignore
```

## 🚀 Installation

### Lokal (Development)
```bash
cd devroid
pip install -e .
```

### Von GitHub
```bash
pip install git+https://github.com/Nowaroid-Studios/devroid.git
```

### Als Package bauen
```bash
pip install build
python -m build
```

## 💻 Verwendung

```python
import devroid
from devroid import Fore, Color, create_exact_table

# ANSI-Farben aktivieren
devroid.init()

# Farbiger Text
print(f"{Fore.GREEN}✓ Erfolg!{Fore.RESET}")

# Tabelle
table = create_exact_table("Bot", "Owner", 42.5, 15, 50)
print(table)

# Discord Embeds
import discord
embed = discord.Embed(title="Test", color=Color.SUCCESS)
```

## 📦 Auf GitHub hochladen

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/Nowaroid-Studios/devroid.git
git push -u origin main
```

Das war's! ✅
