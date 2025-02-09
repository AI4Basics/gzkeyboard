"""Gzkeyboard is a keyboard for typig in Ge’ez alphabets"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_gzkeyboard.ipynb.

# %% auto 0
__all__ = ['GeezInputMethod', 'SystemInputHandler']

# %% ../nbs/00_gzkeyboard.ipynb 3
import time
from typing import Optional, Tuple

class GeezInputMethod:
    def __init__(self):
        # Basic mapping of Latin characters to Ge'ez
        self.mapping =         self.mapping = {
            # ሀ family (h)
            'h'  : 'ሀ',   # 1st order (ä)
            'hu' : 'ሁ',  # 2nd order (u)
            'hi' : 'ሂ',  # 3rd order (i)
            'ha' : 'ሃ',  # 4th order (a)
            'he' : 'ሄ',  # 5th order (e)
            'h\'': 'ህ', # 6th order (ə)
            'ho' : 'ሆ',  # 7th order (o)

            # ለ family (l)
            'l' : 'ለ',  'lu' : 'ሉ',   'li': 'ሊ',
            'la': 'ላ',  'le' : 'ሌ',   'l\'': 'ል',
            'lo': 'ሎ',  'lwa': 'ሏ',

            # ሐ family (hh)
            'hh': 'ሐ',  'hhu': 'ሑ',  'hhi': 'ሒ',
            'hha': 'ሓ', 'hhe': 'ሔ',  'hh\'': 'ሕ',
            'hho': 'ሖ', 'hhwa': 'ሗ',

            # መ family (m)
            'm': 'መ',   'mu': 'ሙ',   'mi': 'ሚ',
            'ma': 'ማ',  'me': 'ሜ',   'm\'': 'ም',
            'mo': 'ሞ',  'mwa': 'ሟ',

            # ሠ family (sz)
            'sz': 'ሠ',  'szu': 'ሡ',  'szi': 'ሢ',
            'sza': 'ሣ', 'sze': 'ሤ',  'sz\'': 'ሥ',
            'szo': 'ሦ', 'szwa': 'ሧ',

            # ረ family (r)
            'r': 'ረ',   'ru': 'ሩ',   'ri': 'ሪ',
            'ra': 'ራ',  're': 'ሬ',   'r\'': 'ር',
            'ro': 'ሮ',  'rwa': 'ሯ',

            # ሰ family (s)
            's': 'ሰ',   'su': 'ሱ',   'si': 'ሲ',
            'sa': 'ሳ',  'se': 'ሴ',   'ss': 'ስ',
            'so': 'ሶ',  'swa': 'ሷ',

            # ሸ family (sh)
            'sh': 'ሸ',  'shu': 'ሹ',  'shi': 'ሺ',
            'sha': 'ሻ', 'she': 'ሼ',  'sh\'': 'ሽ',
            'sho': 'ሾ', 'shwa': 'ሿ',

            # ቀ family (q)
            'q': 'ቀ',   'qu': 'ቁ',   'qi': 'ቂ',
            'qa': 'ቃ',  'qe': 'ቄ',   'q\'': 'ቅ',
            'qo': 'ቆ',  'qwa': 'ቈ',  'qwi': 'ቊ',
            'qwaa': 'ቋ','qwe': 'ቌ',  'qw': 'ቍ',

            # በ family (b)
            'b': 'በ',   'bu': 'ቡ',   'bi': 'ቢ',
            'ba': 'ባ',  'be': 'ቤ',   'b\'': 'ብ',
            'bo': 'ቦ',  'bwa': 'ቧ',

            # ተ family (t)
            't': 'ተ',   'tu': 'ቱ',   'ti': 'ቲ',
            'ta': 'ታ',  'te': 'ቴ',   't\'': 'ት',
            'to': 'ቶ',  'twa': 'ቷ',

            # ቸ family (ch)
            'ch': 'ቸ',  'chu': 'ቹ',  'chi': 'ቺ',
            'cha': 'ቻ', 'che': 'ቼ',  'ch\'': 'ች',
            'cho': 'ቾ', 'chwa': 'ቿ',

            # ኀ family (x)
            'x': 'ኀ',   'xu': 'ኁ',   'xi': 'ኂ',
            'xa': 'ኃ',  'xe': 'ኄ',   'x\'': 'ኅ',
            'xo': 'ኆ',  'xwa': 'ኈ',  'xwi': 'ኊ',
            'xwaa': 'ኋ','xwe': 'ኌ',  'xw': 'ኍ',

            # ነ family (n)
            'n': 'ነ',   'nu': 'ኑ',   'ni': 'ኒ',
            'na': 'ና',  'ne': 'ኔ',   'nn': 'ን',
            'no': 'ኖ',  'nwa': 'ኗ',

            # ኘ family (ny)
            'ny': 'ኘ',  'nyu': 'ኙ',  'nyi': 'ኚ',
            'nya': 'ኛ', 'nye': 'ኜ',  'ny\'': 'ኝ',
            'nyo': 'ኞ', 'nywa': 'ኟ',

            # አ family (a/e)
            'a': 'አ',   'u': 'ኡ',    'i': 'ኢ',
            'aa': 'ኣ',  'e': 'ኤ',    'ea': 'እ',
            'o': 'ኦ',   'oa': 'ኧ',

            # ከ family (k)
            'k': 'ከ',   'ku': 'ኩ',   'ki': 'ኪ',
            'ka': 'ካ',  'ke': 'ኬ',   'k\'': 'ክ',
            'ko': 'ኮ',  'kwa': 'ኰ',  'kwi': 'ኲ',
            'kwaa': 'ኳ','kwe': 'ኴ',  'kw': 'ኵ',

            # ኸ family (kh)
            'kh': 'ኸ',  'khu': 'ኹ',  'khi': 'ኺ',
            'kha': 'ኻ', 'khe': 'ኼ',  'kh\'': 'ኽ',
            'kho': 'ኾ',

            # ወ family (w)
            'w': 'ወ',   'wu': 'ዉ',   'wi': 'ዊ',
            'wa': 'ዋ',  'we': 'ዌ',   'w\'': 'ው',
            'wo': 'ዎ',

            # ዐ family (aa)
            'aa': 'ዐ',  'aau': 'ዑ',  'aai': 'ዒ',
            'aaa': 'ዓ', 'aae': 'ዔ',  'aa\'': 'ዕ',
            'aao': 'ዖ',

            # ዘ family (z)
            'z': 'ዘ',   'zu': 'ዙ',   'zi': 'ዚ',
            'za': 'ዛ',  'ze': 'ዜ',   'z\'': 'ዝ',
            'zo': 'ዞ',  'zwa': 'ዟ',

            # ዠ family (zh)
            'zh': 'ዠ',  'zhu': 'ዡ',  'zhi': 'ዢ',
            'zha': 'ዣ', 'zhe': 'ዤ',  'zh\'': 'ዥ',
            'zho': 'ዦ', 'zhwa': 'ዧ',

            # የ family (y)
            'y': 'የ',   'yu': 'ዩ',   'yi': 'ዪ',
            'ya': 'ያ',  'ye': 'ዬ',   'y\'': 'ይ',
            'yo': 'ዮ',

            # ደ family (d)
            'd': 'ደ',   'du': 'ዱ',   'di': 'ዲ',
            'da': 'ዳ',  'de': 'ዴ',   'd\'': 'ድ',
            'do': 'ዶ',  'dwa': 'ዷ',

            # ጀ family (j)
            'j': 'ጀ',   'ju': 'ጁ',   'ji': 'ጂ',
            'ja': 'ጃ',  'je': 'ጄ',   'j\'': 'ጅ',
            'jo': 'ጆ',  'jwa': 'ጇ',

            # ገ family (g)
            'g': 'ገ',   'gu': 'ጉ',   'gi': 'ጊ',
            'ga': 'ጋ',  'ge': 'ጌ',   'g\'': 'ግ',
            'go': 'ጎ',  'gwa': 'ጐ',  'gwi': 'ጒ',
            'gwaa': 'ጓ','gwe': 'ጔ',  'gw': 'ጕ',

            # ጠ family (th)
            'th': 'ጠ',  'thu': 'ጡ',  'thi': 'ጢ',
            'tha': 'ጣ', 'the': 'ጤ',  'th\'': 'ጥ',
            'tho': 'ጦ', 'thwa': 'ጧ',

            # ጨ family (ch\')
            'ch\'': 'ጨ','ch\'u': 'ጩ','ch\'i': 'ጪ',
            'ch\'a': 'ጫ','ch\'e': 'ጬ','ch\'\'': 'ጭ',
            'ch\'o': 'ጮ','ch\'wa': 'ጯ',

            # ጰ family (ph)
            'ph': 'ጰ',  'phu': 'ጱ',  'phi': 'ጲ',
            'pha': 'ጳ', 'phe': 'ጴ',  'ph\'': 'ጵ',
            'pho': 'ጶ', 'phwa': 'ጷ',

            # ጸ family (ts)
            'ts': 'ጸ',  'tsu': 'ጹ',  'tsi': 'ጺ',
            'tsa': 'ጻ', 'tse': 'ጼ',  'ts\'': 'ጽ',
            'tso': 'ጾ', 'tswa': 'ጿ',

            # ፀ family (ts\')
            'ts\'': 'ፀ','ts\'u': 'ፁ','ts\'i': 'ፂ',
            'ts\'a': 'ፃ','ts\'e': 'ፄ','ts\'\'': 'ፅ',
            'ts\'o': 'ፆ',

            # ፈ family (f)
            'f': 'ፈ',   'fu': 'ፉ',   'fi': 'ፊ',
            'fa': 'ፋ',  'fe': 'ፌ',   'ff': 'ፍ',
            'fo': 'ፎ',  'fwa': 'ፏ',

            # ፐ family (p)
            'p': 'ፐ',   'pu': 'ፑ',   'pi': 'ፒ',
            'pa': 'ፓ',  'pe': 'ፔ',   'p\'': 'ፕ',
            'po': 'ፖ',  'pwa': 'ፗ',

            # Punctuation marks
            ':' : '፡',  # Word separator (hulet netib)
            ':-': '፤',  # Semi-colon
            '.' : '።',  # Full stop
            ':,': '፣',  # Comma
            ':!': '፥',  # Colon
            ':?': '፧',  # Question mark
            ':-:': '፦', # Preface colon
        }
        
        self.buffer              = ""
        self.max_combo_length    = 4
        self.last_keystroke_time = 0
        self.sequence_timeout    = 0.25
        self.pending_output      = None
        
    def should_process_key(self, key: str) -> bool:
        """
        Determine if a key should be processed by the input method.
        Only process single alphabetic characters.
        """
        return (len(key) == 1 and key.isalpha())
        
    def process_keystroke(self, key: str) -> Tuple[str, bool, Optional[int]]:
        """
        Process a single keystroke and return the corresponding Ge'ez character if available.
        """
        # If it's not a processable key, return immediately
        if not self.should_process_key(key):
            return "", False, None
            
        current_time = time.time()
        
        # If too much time has passed, clear the buffer
        if current_time - self.last_keystroke_time > self.sequence_timeout and self.buffer:
            if self.pending_output:
                result              = self.pending_output
                self.buffer         = ""
                self.pending_output = None
                return result, True, None
        
        self.last_keystroke_time = current_time
        self.buffer += key.lower()
        
        # Trim buffer if it exceeds max length
        if len(self.buffer) > self.max_combo_length:
            self.buffer = self.buffer[-self.max_combo_length:]
        
        # Try to match the current buffer
        if self.buffer in self.mapping:
            # If we have a match, store it as pending output
            self.pending_output = self.mapping[self.buffer]
            return "", False, None
        
        # Check if adding another character could make a valid combination
        has_potential_match = any(combo.startswith(self.buffer) 
                                for combo in self.mapping.keys() 
                                if len(combo) > len(self.buffer))
        
        if has_potential_match:
            # Wait for more keystrokes
            return "", False, None
        
        # No potential matches, output the best match we have
        result = ""
        backspace_count = 0
        
        # Try to find the longest matching sequence
        for i in range(len(self.buffer), 0, -1):
            combo = self.buffer[:-1]  # Exclude the last character
            if combo in self.mapping:
                result          = self.mapping[combo]
                self.buffer     = self.buffer[-1:]  # Keep the last character
                backspace_count = len(combo)
                break
        
        # If no matches found, output the first character as-is
        if not result and len(self.buffer) > 1:
            result          = self.buffer[0]
            self.buffer     = self.buffer[1:]
            backspace_count = 1
        
        self.pending_output = None
        return result, False, backspace_count

    def reset(self):
        """Reset the input buffer and pending output."""
        self.buffer              = ""
        self.pending_output      = None
        self.last_keystroke_time = 0

class SystemInputHandler:
    def __init__(self):
        self.input_method = GeezInputMethod()
        
    def setup_keyboard_hook(self):
        """
        Set up system-wide keyboard hook.
        """
        try:
            import keyboard
            
            def callback(event):
                if event.event_type == 'down':
                    # Only process the event if it's a key we want to handle
                    if self.input_method.should_process_key(event.name):
                        char, consumed, backspace_count = self.input_method.process_keystroke(event.name)
                        
                        if backspace_count:
                            # Delete previous character(s) if necessary
                            keyboard.write('\b' * backspace_count)
                        
                        if char:
                            # Output the Ge'ez character
                            keyboard.write(char)
                            return False  # Block the original keystroke
                        elif not consumed:
                            return True  # Let the original keystroke through
                    else:
                        return True  # Let non-alphabet keystrokes through
                return True
            
            keyboard.hook(callback)
            
        except ImportError:
            print("Keyboard library not available. Please install required dependencies.")

