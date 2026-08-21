import subprocess


APPLICATIONS = {
    "notepad": "notepad.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "calculator": "calc.exe",
}

def open_application(app_name):
    executable = APPLICATIONS.get(app_name)

    if executable is None:
        return False
    
    try:
        subprocess.Popen([executable])
        return True

    except OSError:
        return False