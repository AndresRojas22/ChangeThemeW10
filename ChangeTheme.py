import time
import ctypes
import winreg
from datetime import datetime, time

def set_dark_mode():
    try:
        # Habilitar el modo oscuro en el registro de Windows
        keyApp = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, keyApp, 0, winreg.KEY_WRITE) as reg_key:
            winreg.SetValueEx(reg_key, "AppsUseLightTheme", 0, winreg.REG_DWORD, 0)
        
        keySys = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, keySys, 0, winreg.KEY_WRITE) as reg_key:
            winreg.SetValueEx(reg_key, "SystemUsesLightTheme", 0, winreg.REG_DWORD, 0)

        # Forzar a Windows a aplicar los cambios
        ctypes.windll.user32.SystemParametersInfoW(20, 0, None, 3)
    except Exception as e:
        print("Error al cambiar al modo oscuro:", e)

def set_light_mode():
    try:
        # Deshabilitar el modo oscuro en el registro de Windows
        keyApp = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, keyApp, 0, winreg.KEY_WRITE) as reg_key:
            winreg.SetValueEx(reg_key, "AppsUseLightTheme", 0, winreg.REG_DWORD, 1)
        
        keySys = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, keySys, 0, winreg.KEY_WRITE) as reg_key:
            winreg.SetValueEx(reg_key, "SystemUsesLightTheme", 0, winreg.REG_DWORD, 1)

        # Forzar a Windows a aplicar los cambios
        ctypes.windll.user32.SystemParametersInfoW(20, 0, None, 3)
    except Exception as e:
        print("Error al cambiar al modo claro:", e)

def main():
    now = datetime.now().time()  # Hora actual

    change_time = time(19, 30)  # Hora determinada (por ejemplo, 14:30)
    light_time = time(7,1)

    if now > change_time or now < light_time:
        set_dark_mode()
    else:
        set_light_mode()

if __name__ == "__main__":
    main()
