class ActionGui:
    def __init__(self) -> None:
        self.vm = None
        self.isActionRequired = False

    def setVM(self, vm):
        self.vm = vm

    def doAction(self):
        pass

    def isRequired(self):
        return self.isActionRequired