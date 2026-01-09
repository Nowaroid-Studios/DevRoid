"""
devroid Help System
Erstellt automatisch schöne Help-Embeds für Discord-Bots
"""

import discord
from .wizzycolor import Color


def create_help_embed(bot, prefix="!", title=None, description=None, color=None):
    """
    Erstellt ein Help-Embed mit allen verfügbaren Befehlen
    
    Parameters:
    - bot: Der Discord Bot (commands.Bot)
    - prefix: Command Prefix (Standard: "!")
    - title: Titel des Embeds (optional)
    - description: Beschreibung des Embeds (optional)
    - color: Farbe des Embeds (optional, Standard: Color.BLURPLE)
    
    Returns:
    - discord.Embed mit allen Befehlen
    """
    
    # Standardwerte
    if title is None:
        title = f"📚 {bot.user.name} - Befehle"
    if description is None:
        description = f"Hier sind alle verfügbaren Befehle (Prefix: `{prefix}`)"
    if color is None:
        color = Color.BLURPLE
    
    # Embed erstellen
    embed = discord.Embed(
        title=title,
        description=description,
        color=color
    )
    
    # Befehle nach Kategorien gruppieren
    # Wenn Cogs vorhanden sind, nach Cogs gruppieren
    if bot.cogs:
        for cog_name, cog in bot.cogs.items():
            commands = cog.get_commands()
            if commands:
                commands_text = ""
                for cmd in commands:
                    # Aliases anzeigen falls vorhanden
                    aliases = f" [{', '.join(cmd.aliases)}]" if cmd.aliases else ""
                    cmd_help = cmd.help or "Keine Beschreibung"
                    commands_text += f"`{prefix}{cmd.name}{aliases}` - {cmd_help}\n"
                
                embed.add_field(
                    name=f"📁 {cog_name}",
                    value=commands_text,
                    inline=False
                )
    
    # Befehle ohne Cog
    uncategorized = [cmd for cmd in bot.commands if cmd.cog is None]
    if uncategorized:
        commands_text = ""
        for cmd in uncategorized:
            aliases = f" [{', '.join(cmd.aliases)}]" if cmd.aliases else ""
            cmd_help = cmd.help or "Keine Beschreibung"
            commands_text += f"`{prefix}{cmd.name}{aliases}` - {cmd_help}\n"
        
        embed.add_field(
            name="📝 Befehle",
            value=commands_text,
            inline=False
        )
    
    # Footer
    embed.set_footer(text=f"Gesamt: {len(bot.commands)} Befehle | Erstellt mit devroid")
    
    return embed


def create_command_help_embed(command, prefix="!", color=None):
    """
    Erstellt ein detailliertes Help-Embed für einen einzelnen Befehl
    
    Parameters:
    - command: Der Command (discord.ext.commands.Command)
    - prefix: Command Prefix (Standard: "!")
    - color: Farbe des Embeds (optional, Standard: Color.BLURPLE)
    
    Returns:
    - discord.Embed mit Befehlsdetails
    """
    
    if color is None:
        color = Color.BLURPLE
    
    # Embed erstellen
    embed = discord.Embed(
        title=f"ℹ️ Befehl: {prefix}{command.name}",
        description=command.help or "Keine Beschreibung verfügbar",
        color=color
    )
    
    # Verwendung
    usage = f"{prefix}{command.name}"
    if command.signature:
        usage += f" {command.signature}"
    embed.add_field(
        name="📝 Verwendung",
        value=f"`{usage}`",
        inline=False
    )
    
    # Aliases
    if command.aliases:
        aliases = ", ".join([f"`{prefix}{alias}`" for alias in command.aliases])
        embed.add_field(
            name="🔗 Aliases",
            value=aliases,
            inline=False
        )
    
    # Kategorie (Cog)
    if command.cog:
        embed.add_field(
            name="📁 Kategorie",
            value=command.cog.qualified_name,
            inline=True
        )
    
    return embed


def create_categories_embed(bot, prefix="!", color=None):
    """
    Erstellt ein Embed mit allen Kategorien/Cogs
    
    Parameters:
    - bot: Der Discord Bot (commands.Bot)
    - prefix: Command Prefix (Standard: "!")
    - color: Farbe des Embeds (optional, Standard: Color.BLURPLE)
    
    Returns:
    - discord.Embed mit allen Kategorien
    """
    
    if color is None:
        color = Color.BLURPLE
    
    embed = discord.Embed(
        title="📁 Befehlskategorien",
        description=f"Nutze `{prefix}help <kategorie>` für Details",
        color=color
    )
    
    if bot.cogs:
        for cog_name, cog in bot.cogs.items():
            commands = cog.get_commands()
            if commands:
                embed.add_field(
                    name=f"📁 {cog_name}",
                    value=f"{len(commands)} Befehle\n{cog.description or 'Keine Beschreibung'}",
                    inline=True
                )
    
    # Nicht kategorisierte Befehle
    uncategorized = [cmd for cmd in bot.commands if cmd.cog is None]
    if uncategorized:
        embed.add_field(
            name="📝 Allgemein",
            value=f"{len(uncategorized)} Befehle",
            inline=True
        )
    
    embed.set_footer(text=f"Gesamt: {len(bot.commands)} Befehle")
    
    return embed


def create_simple_help_embed(commands_dict, prefix="!", title=None, color=None):
    """
    Erstellt ein einfaches Help-Embed aus einem Dictionary
    Nützlich wenn du keine Cogs verwendest
    
    Parameters:
    - commands_dict: Dictionary mit Kategorien und Befehlen
                    {"Kategorie": [("befehl", "Beschreibung"), ...]}
    - prefix: Command Prefix (Standard: "!")
    - title: Titel (optional)
    - color: Farbe (optional, Standard: Color.BLURPLE)
    
    Returns:
    - discord.Embed
    
    Beispiel:
        commands = {
            "Info": [
                ("ping", "Zeigt Latenz"),
                ("info", "Bot-Info")
            ],
            "Fun": [
                ("test", "Test-Befehl")
            ]
        }
        embed = create_simple_help_embed(commands)
    """
    
    if color is None:
        color = Color.BLURPLE
    if title is None:
        title = "📚 Befehle"
    
    embed = discord.Embed(
        title=title,
        description=f"Prefix: `{prefix}`",
        color=color
    )
    
    total_commands = 0
    for category, commands in commands_dict.items():
        commands_text = ""
        for cmd_name, cmd_desc in commands:
            commands_text += f"`{prefix}{cmd_name}` - {cmd_desc}\n"
            total_commands += 1
        
        embed.add_field(
            name=f"📁 {category}",
            value=commands_text,
            inline=False
        )
    
    embed.set_footer(text=f"Gesamt: {total_commands} Befehle | Erstellt mit devroid")
    
    return embed
