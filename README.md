# RLCS-EU-Score-Predictor
Not so good neural network trained to predict series scores of Rocket League Championship Series (RLCS) season 9 EU teams. 

## How to run

### Requirements

* Python 3 with the following packages
* pytorch
* torchvision
* cudatoolkit=10.1

### Setting which teams to predict

Change the matches variable in `predict.py`, make sure to use abbreviations from Liquipedia. The network is only trained on matches of RLCS S9 EU teams, so the prediction is limited to these 10 teams.

### Command to predict scores

`python3 predict.py`

### Command to train network

`python3 main.py`

## FAQ

### Will this predict the correct score?

Probably not
