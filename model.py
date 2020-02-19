from torch import nn

teams = ('REC', 'FCB', 'DIG', 'VEL', 'RV', 'MOUZ', 'SNG', 'TSM', 'ASM', 'END')
output_labels = ('0-3', '1-3', '2-3', '3-2', '3-1', '3-0')


def model():
    return nn.Sequential(
        nn.Linear(2, 80),
        nn.ReLU(inplace=True),
        nn.Dropout(),
        nn.Linear(80, 400),
        nn.ReLU(inplace=True),
        nn.Dropout(),
        nn.Linear(400, 800),
        nn.ReLU(inplace=True),
        nn.Dropout(),
        nn.Linear(800, 60),
        nn.ReLU(inplace=True),
        nn.Dropout(),
        nn.Linear(60, 6),
        nn.Softmax(dim=1),
    )
