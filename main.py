from backend.system_manager import SystemManager
from ui.ui_flow import UIFlow

def main():
    system = SystemManager()
    ui = UIFlow(system)
    ui.start()

if __name__ == "__main__":
    main()
