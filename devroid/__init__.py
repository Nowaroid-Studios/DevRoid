"""
devroid - A utility library for Pycord bots
"""

from .wizzycolor import (
    Fore,
    Style,
    Color,
    BOX_CHARS,
    init,
    create_exact_table,
    create_exact_status_box,
    display_cogs,
    display_bot_interface,
    create_message_line,
    display_status_line
)

from .help_system import (
    create_help_embed,
    create_command_help_embed,
    create_categories_embed,
    create_simple_help_embed
)

__version__ = "0.1.0"
__author__ = "Florian"

__all__ = [
    # Color classes
    "Fore",
    "Style",
    "Color",
    "BOX_CHARS",
    
    # Functions
    "init",
    "create_exact_table",
    "create_exact_status_box",
    "display_cogs",
    "display_bot_interface",
    "create_message_line",
    "display_status_line",
    
    # Help System
    "create_help_embed",
    "create_command_help_embed",
    "create_categories_embed",
    "create_simple_help_embed",
]
