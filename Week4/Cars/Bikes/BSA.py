class BSA:
    def __init__(self):
        self.model = ['Herclues', 'BSA', 'Xyz', 'Mny','abc']
    def outModels(self):
        print("These are the available models for Cycles")
        for model in self.model:
            print(f"\t{model}")