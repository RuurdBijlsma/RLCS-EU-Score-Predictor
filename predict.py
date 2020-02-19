import torch
from torch.autograd import Variable
from model import model, teams, output_labels

show_confidence = False
matches = [
    ['DIG', 'SNG'],
    ['ASM', 'END'],
    ['MOUZ', 'SNG'],
    ['RV', 'TSM'],
    ['REC', 'VEL'],
    ['RV', 'FCB'],
]
net = model()
net.load_state_dict(torch.load('network.pth'))

for [team1, team2] in matches:
    net_input = [teams.index(team1), teams.index(team2)]

    output = net(Variable(torch.tensor([net_input]).float()))
    conf, predicted = torch.max(output, 1)
    score_index = predicted.item()
    score = output_labels[score_index]
    print('{0} vs {1}: Predicted score: {2}'.format(team1, team2, score) +
          (', confidence: {0}'.format(conf.item()) if show_confidence else ''))
