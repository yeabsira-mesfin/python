class Honda:
    def __init__(self):
        self.models = ['Activa', 'Shine', 'CBZ', 'Hunk','Unicorn']
    def outModels(self):
        print("These are the available models for Honda")
        for model in self.models:
            print(f"\t{model}")