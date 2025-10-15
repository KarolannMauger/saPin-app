import os

# rpi_ws281x docs
# We need to modify this to match LED strip configuration
LED_COUNT   = int(os.getenv("LED_COUNT", "60"))
LED_PIN     = int(os.getenv("LED_PIN", "18"))     # GPIO18 = PWM
LED_FREQ_HZ = int(os.getenv("LED_FREQ_HZ", "800000"))
LED_DMA     = int(os.getenv("LED_DMA", "10"))
LED_INVERT  = os.getenv("LED_INVERT", "0") == "1"
LED_BRIGHTNESS_BOOT = int(os.getenv("LED_BRIGHTNESS_BOOT", "255"))
LED_CHANNEL = int(os.getenv("LED_CHANNEL", "0"))

# App
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))
DEBUG = os.getenv("DEBUG", "0") == "1"
