# Gzkeyboard

> Gzkeyboard is a keyboard for typing in Ge'ez alphabets (Tigrinya and Amharic)

## Overview

Gzkeyboard enables typing in Tigrinya and Amharic using standard QWERTY keyboards. It converts Latin character combinations into the corresponding Ge'ez characters, making it easy to type in these languages without specialized keyboard layouts.

## Features

The improved implementation includes:

- **Multiple input modes**: Support for Tigrinya, Amharic, and Latin modes
- **Efficient keystroke processing**: Optimized algorithms for key combination matching
- **Configurable timeouts**: Adjustable timeouts that adapt to user typing speed
- **Visual feedback**: Real-time indicators showing what's being typed
- **Customizable mappings**: Support for custom character mappings
- **Hotkey support**: Configurable keyboard shortcuts for controlling the input method
- **Autocorrection**: Basic support for correcting common typing mistakes
- **Modern code organization**: Modular design for easier maintenance and extension

## Installation

Install the latest version from GitHub:

```bash
pip install git+https://github.com/AI4Basics/gzkeyboard.git
```

Or from PyPI:

```bash
pip install gzkeyboard
```

## Usage

### Basic Usage

To start the Geez keyboard with default settings:

```python
from gzkeyboard.improved_gzkeyboard import GeezKeyboardApp

# Create and start the app
app = GeezKeyboardApp()
app.start()

# To stop the app
app.stop()
```

### Command Line Usage

You can also start the keyboard from the command line:

```bash
python -m gzkeyboard.improved_gzkeyboard --mode tigrinya
```

Available options:
- `--mode`: Choose input mode (tigrinya, amharic, or latin)
- `--config`: Specify path to a custom configuration file

### Default Hotkeys

- `Ctrl+Space`: Toggle input method on/off
- `Alt+T`: Switch to Tigrinya mode
- `Alt+A`: Switch to Amharic mode
- `Alt+L`: Switch to Latin mode
- `Escape`: Cancel current buffer

### Typing Examples

Here are some examples of character combinations:

| Latin Input | Ge'ez Output | Description |
|-------------|--------------|-------------|
| ha          | ሃ            | 'h' family, 4th order |
| he          | ሄ            | 'h' family, 5th order |
| se          | ሴ            | 's' family, 5th order |
| ma          | ማ            | 'm' family, 4th order |
| shengo      | ሸንጎ          | Multiple characters |

## Configuration

You can customize the keyboard behavior by creating a configuration file:

```python
from gzkeyboard.improved_gzkeyboard import KeyboardConfig, InputMode

# Create a custom configuration
config = KeyboardConfig(
    sequence_timeout=0.7,  # Longer timeout for slower typing
    show_preview=True,     # Show visual feedback
    autocorrect=True,      # Enable autocorrection
    default_mode=InputMode.TIGRINYA
)

# Save the configuration
config.save_to_file("~/.config/gzkeyboard/config.json")
```

## Custom Mappings

You can create custom character mappings:

```python
from gzkeyboard.improved_gzkeyboard import KeyboardMappings

# Create a custom mapping
custom_mapping = {
    'se': 'ሴ',
    'ez': 'ዝ',
    # Add your own custom mappings
}

# Save the mapping
KeyboardMappings.save_custom_mapping(
    custom_mapping, 
    "~/.config/gzkeyboard/custom_mappings.json"
)
```

## Development

This project uses [nbdev](https://nbdev.fast.ai/) for development. To set up the development environment:

```bash
# Clone the repository
git clone https://github.com/AI4Basics/gzkeyboard.git
cd gzkeyboard

# Install in development mode
pip install -e ".[dev]"

# Install git hooks
nbdev_install_hooks

# Run the notebook server
jupyter notebook
```

## Documentation

For more detailed documentation, see the [notebook documentation](https://AI4Basics.github.io/gzkeyboard/).

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
