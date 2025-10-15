from typing import List, Optional, Tuple
from rpi_ws281x import PixelStrip, Color
from .config import ( 
    LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS_BOOT, LED_CHANNEL 
)

def _hex_to_rgb(hex_color: str):
    h = hex_color.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

class LedController:
    """
    Controls an LED strip using the rpi_ws281x library.
    """
    def __init__(self):
        self.strip = PixelStrip(
            LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS_BOOT, LED_CHANNEL
        )
        self.strip.begin()

        # API side (brightness en % 0..100, color as hex string list)
        self.state = {
            "brightness": 50,
            "color": ["#FFFFFFFF"]
        }
        self._apply_hw(self.state["colors"], self.state["brightness"])
    
    def _apply_hw(self, colors: List[str], brightness_percent: int):
        """
        Apply the given colors and brightness to the LED strip.
        """
        n = max (1, len(colors))
        seg = max(1, self.strip.numPixels() // n)

        for i in range(self.strip.numPixels()):
            c = colors[min(i // seg, n - 1)]
            r, g, b, a = _hex_to_rgb(c)
            self.strip.setPixelColor(i, Color(r, g, b))
        self.strip.setBrightness(int(255 * (max(0, min(100, brightness_percent)) / 100)))
        self.strip.show()
    
    def apply(self, colors: Optional[List[str]] = None, brightness: Optional[int] = None):
        """
        Update the LED strip with new colors and/or brightness.
        """
        if colors:
            self.state["colors"] = [
                c if c.startswith('#') else f'#{c}' for c in colors
            ]
        if brightness is not None:
            self.state["brightness"] = max(0, min(100, int(brightness)))
        
        self._apply_hw(self.state["colors"], self.state["brightness"])
        return self.state
    
    def get_state(self):
        return self.state
    
    def clear(self):
        """
        Turn off all LEDs.
        """
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(0, 0, 0))
        self.strip.setBrightness(0)
        self.strip.show()

led = LedController()