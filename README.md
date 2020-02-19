# RLCS-EU-Score-Predictor
Not so good neural network trained to predict series scores of Rocket League Championship Series (RLCS) season 9 EU teams. 

## Sample output

When inputting the matches to be played in week 3 of RLCS S9, the network outputs the following:
```
DIG vs SNG: Predicted score: 3-1
ASM vs END: Predicted score: 3-1
MOUZ vs SNG: Predicted score: 2-3
RV vs TSM: Predicted score: 3-1
REC vs VEL: Predicted score: 2-3
RV vs FCB: Predicted score: 0-3
```

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
