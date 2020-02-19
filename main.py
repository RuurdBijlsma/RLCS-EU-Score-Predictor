from torch import nn
import torch
from torch import optim
from torch.autograd import Variable
from model import model

inputs = [[0,5],[0,6],[0,5],[0,4],[0,2],[0,3],[0,7],[0,1],[0,4],[0,7],[1,3],[1,4],[1,2],[1,7],[1,5],[1,0],[1,2],[1,0],[1,0],[1,4],[1,0],[1,5],[1,0],[1,7],[1,0],[1,5],[1,7],[1,4],[1,2],[2,7],[2,4],[2,7],[2,5],[2,0],[2,1],[2,3],[2,1],[2,3],[2,0],[2,5],[2,7],[2,5],[2,4],[2,0],[2,1],[2,0],[2,4],[2,0],[2,5],[2,0],[3,1],[3,5],[3,7],[3,1],[3,0],[3,4],[3,2],[3,2],[3,4],[3,4],[3,4],[3,5],[3,0],[3,7],[4,9],[4,7],[4,2],[4,0],[4,1],[4,5],[4,3],[4,0],[4,3],[4,0],[4,3],[4,5],[4,1],[4,0],[4,3],[4,5],[4,7],[4,2],[4,1],[4,0],[4,0],[4,2],[4,0],[4,5],[4,5],[4,0],[5,0],[5,3],[5,2],[5,4],[5,1],[5,7],[5,7],[5,2],[5,4],[5,3],[5,4],[5,0],[5,1],[5,1],[5,2],[5,7],[5,0],[5,0],[5,0],[5,2],[5,4],[5,0],[5,0],[5,4],[5,0],[6,4],[6,0],[6,8],[7,2],[7,4],[7,2],[7,3],[7,1],[7,0],[7,5],[7,0],[7,5],[7,2],[7,0],[7,1],[7,3],[7,4],[7,1],[7,5],[7,0],[8,2],[8,5],[8,6],[8,9],[9,0],[5,0],[6,0],[5,0],[4,0],[2,0],[3,0],[7,0],[1,0],[4,0],[7,0],[3,1],[4,1],[2,1],[7,1],[5,1],[0,1],[2,1],[0,1],[0,1],[4,1],[0,1],[5,1],[0,1],[7,1],[0,1],[5,1],[7,1],[4,1],[2,1],[7,2],[4,2],[7,2],[5,2],[0,2],[1,2],[3,2],[1,2],[3,2],[0,2],[5,2],[7,2],[5,2],[4,2],[0,2],[1,2],[0,2],[4,2],[0,2],[5,2],[0,2],[1,3],[5,3],[7,3],[1,3],[0,3],[4,3],[2,3],[2,3],[4,3],[4,3],[4,3],[5,3],[0,3],[7,3],[9,4],[7,4],[2,4],[0,4],[1,4],[5,4],[3,4],[0,4],[3,4],[0,4],[3,4],[5,4],[1,4],[0,4],[3,4],[5,4],[7,4],[2,4],[1,4],[0,4],[0,4],[2,4],[0,4],[5,4],[5,4],[0,4],[0,5],[3,5],[2,5],[4,5],[1,5],[7,5],[7,5],[2,5],[4,5],[3,5],[4,5],[0,5],[1,5],[1,5],[2,5],[7,5],[0,5],[0,5],[0,5],[2,5],[4,5],[0,5],[0,5],[4,5],[0,5],[4,6],[0,6],[8,6],[2,7],[4,7],[2,7],[3,7],[1,7],[0,7],[5,7],[0,7],[5,7],[2,7],[0,7],[1,7],[3,7],[4,7],[1,7],[5,7],[0,7],[2,8],[5,8],[6,8],[9,8],[0,9]]
outputs = [4,4,5,0,5,2,4,3,2,1,2,5,1,5,2,2,3,1,4,1,4,4,4,2,3,5,2,0,4,3,3,5,0,0,4,2,2,5,2,3,4,5,0,0,1,4,3,5,4,3,2,4,1,3,3,1,3,0,1,0,0,4,2,2,4,3,2,5,0,2,4,3,4,5,5,2,4,3,5,4,4,5,5,4,0,2,5,1,2,3,0,1,5,3,3,2,2,2,3,1,1,2,1,0,0,1,2,0,1,1,4,1,2,3,0,3,1,4,2,2,0,4,0,1,3,4,3,1,1,3,3,1,3,4,4,1,1,1,4,2,1,1,0,5,0,3,1,2,3,4,3,0,4,0,3,3,2,4,1,4,1,1,1,3,2,0,3,5,1,2,2,0,5,5,1,3,3,0,3,2,1,0,5,5,4,1,2,0,1,2,3,1,4,2,2,4,2,5,4,5,5,1,3,3,1,2,3,0,5,3,1,2,1,0,0,3,1,2,0,1,1,0,0,1,5,3,0,4,3,2,5,4,0,2,2,3,3,3,2,4,4,3,4,5,5,4,3,5,4,4,1,4,3,2,5,2,4,1,3,3,5,1,5,4,2,1,2,4,4,2,2,4,2,1,1,4,4,4,1,3]


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print("Using ", device)
inputs = list(map(lambda s: Variable(torch.Tensor([s])), inputs))
targets = list(map(lambda s: Variable(torch.Tensor([s])), outputs))

net = model()
net.to(device)
optimizer = optim.Adam(net.parameters(), lr=0.00002)
criterion = nn.CrossEntropyLoss()
epochs = 1000

for epoch in range(epochs):
    correct = 0.
    total = 0.
    running_loss = 0
    for i, (data, target) in enumerate(zip(inputs, targets)):
        # print(data, target)
        data, target = data.to(device), target.to(device)

        optimizer.zero_grad()

        output = net(data)
        loss = criterion(output, target.long())
        loss.backward()
        optimizer.step()

        _, predicted = torch.max(output, 1)
        total += 1
        correct += (predicted == target).item()
        running_loss += loss.item()

    accuracy = correct / total
    print("[%d / %d] Acc: %f%%, Loss: %f" % (epoch + 1, epochs, accuracy * 100, running_loss / len(inputs)))

torch.save(net.state_dict(), 'network.pth')
print("Complete")