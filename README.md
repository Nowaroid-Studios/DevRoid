# devroid

A utility library for Pycord bots with colored console outputs and Discord embed colors.

## Installation

```bash
pip install devroid
```

Or from GitHub:
```bash
pip install git+https://github.com/Nowaroid-Studios/devroid.git
```

## Quick Start

```python
import devroid
from devroid import Fore, Color, create_exact_table

# Enable ANSI colors (Windows support)
devroid.init()

# Colored console output
print(f"{Fore.GREEN}✓ Bot started!{Fore.RESET}")

# Bot info table
table = create_exact_table(
    bot_name="MyBot",
    owner_name="Developer",
    ping=42.5,
    commands=15,
    servers=50
)
print(table)
```

## Features

- 🎨 **Colored Console Output** - ANSI colors with Windows support
- 🎭 **Discord Embed Colors** - Predefined color palette (BLURPLE, SUCCESS, WARNING, ERROR)
- 📊 **Formatted Tables** - Beautiful bot info tables with box characters
- 📦 **Status Boxes** - Formatted status displays
- 🖥️ **Bot Interface** - Complete dashboard for bot information
- 💬 **Status Messages** - Color-coded messages (Info, Success, Warning, Error)

## Usage with Pycord

```python
import discord
from discord.ext import commands
from devroid import display_bot_interface, Color

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    display_bot_interface(
        bot_name=bot.user.name,
        owner_name="Your Name",
        ping=round(bot.latency * 1000, 2),
        commands=len(bot.commands),
        servers=len(bot.guilds)
    )

@bot.command()
async def ping(ctx):
    embed = discord.Embed(
        title="🏓 Pong!",
        description=f"Latency: {round(bot.latency * 1000, 2)}ms",
        color=Color.BLURPLE
    )
    await ctx.send(embed=embed)

bot.run("YOUR_TOKEN")
```

## API Reference

### Color Classes

**`Fore`** - Console foreground colors
- `RED`, `GREEN`, `BLUE`, `YELLOW`, `CYAN`, `MAGENTA`, `WHITE`, `BLACK`, `RESET`

**`Style`** - Text styles
- `RESET_ALL`, `BOLD`, `UNDERLINE`

**`Color`** - Discord embed colors (hex values)
- `BLURPLE` (0x5865F2) - Discord purple
- `SUCCESS` (0x57F287) - Green
- `WARNING` (0xFEE75C) - Yellow
- `ERROR` (0xED4245) - Red
- `RED`, `GREEN`, `BLUE`, `YELLOW`, `CYAN`, `MAGENTA`, `WHITE`

### Functions

**`init()`** - Activate ANSI colors in Windows console

**`create_exact_table(bot_name, owner_name, ping, commands, servers)`** - Create formatted bot info table

**`create_exact_status_box(title, content, width=36)`** - Create status box with border

**`display_bot_interface(...)`** - Display complete bot interface

**`display_status_line(message, status)`** - Color-coded status messages
- `status`: "info", "success", "warning", "error"

**`create_message_line(message, width=60, color)`** - Formatted message with border

**`display_cogs(cogs)`** - Display formatted cog list

## Examples

### Console Colors
```python
from devroid import Fore, Style

print(f"{Fore.RED}Red text{Fore.RESET}")
print(f"{Fore.GREEN}Green text{Fore.RESET}")
print(f"{Style.BOLD}Bold text{Style.RESET_ALL}")
```

### Discord Embed Colors
```python
from devroid import Color
import discord

embed = discord.Embed(title="Success!", color=Color.SUCCESS)
```

### Status Messages
```python
from devroid import display_status_line

print(display_status_line("Bot started", "success"))   # Green
print(display_status_line("Warning", "warning"))       # Yellow
print(display_status_line("Error", "error"))           # Red
print(display_status_line("Info", "info"))             # Cyan
```

### Bot Interface
```python
from devroid import display_bot_interface

display_bot_interface(
    bot_name="MyBot",
    owner_name="Developer",
    ping=42.5,
    commands=15,
    servers=50,
    cogs=["Admin", "Moderation", "Fun"]
)
```

## License

MIT License - See LICENSE file

## Links

- **GitHub**: https://github.com/Nowaroid-Studios/devroid
- **PyPI**: https://pypi.org/project/devroid/
- **Issues**: https://github.com/Nowaroid-Studios/devroid/issues

## Help System

devroid enthält ein automatisches Help-System für Discord-Bots:

```python
from devroid import create_help_embed

@bot.command()
async def help(ctx):
    """Zeigt alle Befehle"""
    embed = create_help_embed(bot, prefix="!")
    await ctx.send(embed=embed)
```

**Verfügbare Help-Funktionen:**
- `create_help_embed(bot, prefix)` - Automatisches Help-Embed
- `create_simple_help_embed(commands_dict, prefix)` - Manuelles Help-Embed
- `create_command_help_embed(command, prefix)` - Detailliertes Command-Help
- `create_categories_embed(bot, prefix)` - Kategorien-Übersicht
