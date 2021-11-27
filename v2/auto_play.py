from app_controller import AppController

def main():
    app = AppController()
    app.addVM('AutoTale')
    app.run()

if __name__ == "__main__":
    main()