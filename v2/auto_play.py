from app_controller import AppController
import constant

def main():
    app = AppController()
    app.addVM(constant.VM_NAME)
    app.run()

if __name__ == "__main__":
    main()