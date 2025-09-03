import os
import ctypes

# Thresholds in mm
THRESHOLD_MM = 0.1
TOTAL_TRAVEL_MM = 4.0

# Maximum number of keys on Wooting 2 HE
MAX_KEYS = 256

class KeyPreselect:
    def __init__(self, key_map):
        self.sdk = None
        try:        
            # Load the Wooting SDK DLL
            self.sdk = ctypes.CDLL(self.full_path("wooting_analog_sdk.dll"))

            # Define function prototypes
            self.sdk.wooting_analog_initialise.restype = ctypes.c_int
            self.sdk.wooting_analog_read_analog.argtypes = [ctypes.c_int]
            self.sdk.wooting_analog_read_analog.restype = ctypes.c_float

            # Initialise SDK
            if self.sdk.wooting_analog_initialise() == 1:
                self.preselect_available = True
            else:
                self.preselect_available = False

            self.key_map = key_map
        except:
            self.preselect_available = False

    def poll_keys(self):
        if self.preselect_available == False:
            return
        
        for keycode in range(MAX_KEYS):
            if keycode not in self.key_map:
                continue

            value = self.sdk.wooting_analog_read_analog(keycode)
            if value > 0.0:
                button = self.key_map[keycode]
                if button:
                    if button.preselect == False:
                        button.preselect = True
                        button.update()
            else:
                button = self.key_map[keycode]
                if button:
                    if button.preselect:
                        button.preselect = False
                        button.update()

    def full_path(self, filename: str) -> str:
        #Sucht eine Datei in allen PATH-Ordnern.
        for path_dir in os.environ["PATH"].split(os.pathsep):
            full_path = os.path.join(path_dir.strip('"'), filename)
            if os.path.isfile(full_path):
                return full_path
        return ""