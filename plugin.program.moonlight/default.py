import xbmc
import xbmcaddon
import xbmcgui
import os

# Add-on settings
ADDON = xbmcaddon.Addon()
HOSTNAME = ADDON.getSetting("hostname")
APP = ADDON.getSetting("app")

def launch_moonlight():
    """Launch Moonlight with configured settings."""
    if not HOSTNAME or not APP:
        xbmcgui.Dialog().ok("Moonlight Launcher", "Please configure the add-on settings.")
        return

    command = f"moonlight stream {HOSTNAME} \"{APP}\""
    xbmc.log(f"Executing: {command}", level=xbmc.LOGINFO)

    result = os.system(command)
    if result != 0:
        xbmcgui.Dialog().notification("Moonlight Launcher", "Failed to launch Moonlight!", xbmcgui.NOTIFICATION_ERROR)
    else:
        xbmcgui.Dialog().notification("Moonlight Launcher", f"Launched {APP} on {HOSTNAME}", xbmcgui.NOTIFICATION_INFO)

if __name__ == "__main__":
    launch_moonlight()
