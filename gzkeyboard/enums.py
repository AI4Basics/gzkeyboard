"""Enums and config classes for the Gzkeyboard"""

from enum import Enum
from dataclasses import dataclass
from typing import Optional, List, Dict

class InputMode(Enum):
    """Defines the input modes available in the Geez keyboard."""
    TIGRINYA = "tigrinya"
    AMHARIC = "amharic"
    LATIN = "latin"  # For regular typing without conversion
    
@dataclass
class KeyboardConfig:
    """Configuration for the Geez keyboard input method."""
    sequence_timeout: float = 0.5
    max_combo_length: int = 4
    show_preview: bool = True
    autocorrect: bool = True
    default_mode: InputMode = InputMode.TIGRINYA
    custom_mappings_path: Optional[str] = None

class KeyboardMappings:
    """Manages character mappings for different languages and input modes."""
    @staticmethod
    def get_mapping_for_mode(mode):
        """Placeholder for getting mappings by mode"""
        return {}

class KeyboardHotkeyManager:
    """Manages hotkeys for controlling the Geez keyboard."""
    
    def __init__(self):
        self.hotkeys = {
            'toggle_input': ['ctrl+space'],  # Toggle between active and inactive
            'switch_to_tigrinya': ['alt+t'],  # Switch to Tigrinya
            'switch_to_amharic': ['alt+a'],  # Switch to Amharic
            'switch_to_latin': ['alt+l'],    # Switch to Latin
            'cancel_buffer': ['escape']      # Cancel current buffer
        }
    
    def register_hotkey(self, action: str, keys: List[str]):
        """Register a hotkey for a specific action."""
        self.hotkeys[action] = keys
    
    def get_hotkeys_for_action(self, action: str) -> List[str]:
        """Get the hotkeys registered for a specific action."""
        return self.hotkeys.get(action, [])

class GeezInputMethod:
    """An improved input method for typing in Ge'ez alphabets."""
    
    def __init__(self, config: Optional[KeyboardConfig] = None):
        """Initialize the input method with optional configuration."""
        self.config = config or KeyboardConfig()
        self.mode = self.config.default_mode
        self.mapping = KeyboardMappings.get_mapping_for_mode(self.mode)
        self.buffer = ""
        self.active = True
    
    def set_mode(self, mode: InputMode):
        """Set the input mode and update mappings accordingly."""
        self.mode = mode
    
    def _find_best_match(self) -> tuple:
        """Find the best match in the buffer and return result, length, and exact flag."""
        # Placeholder for documentation purposes
        return "", 0, False

class SystemInputHandler:
    """Handles system-wide keyboard input for the Geez keyboard."""
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialize the input handler with optional configuration path."""
        self.input_method = GeezInputMethod()
        
    def setup_keyboard_hook(self):
        """Set up system-wide keyboard hook using the keyboard library."""
        pass

class StatusIndicator:
    """A status indicator for the Geez keyboard."""
    
    def __init__(self, input_method: GeezInputMethod):
        """Initialize with the input method to monitor."""
        self.input_method = input_method
        self.visible = False
    
    def show(self, message: str, duration: float = 2.0):
        """Show the status indicator with a message."""
        # In a real implementation, this would show a GUI element
        print(f"STATUS: {message}")
        self.visible = True
    
    def hide(self):
        """Hide the status indicator."""
        self.visible = False

# Main function is now defined in gzkeyboard.py