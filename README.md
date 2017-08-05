# WeightCompare

## Description
WeightCompare pulls your weight data from myfitnesspal and calculates averages from your weight history.  Your weight naturally fluctuates day to day based on food and water intake.  If you are only looking at your most recent weigh-in, you could be fooled by these fluctuations.  By taking moving averages, you smooth these fluctuations and better understand if your weight is trending upwards or downwards.

## Depedencies
All dependencies are listed in the environment.yml file.

### python-myfitnesspal
WeightCompare uses coddingtonbear's excellent [library](https://github.com/coddingtonbear/python-myfitnesspal) to pull data from myfitnesspal.   The python-myfitnesspal library enables you to store your password into your system keyring.  This is a good security practice and saves you a step while running WeightCompare.  Before using WeightCompare for the first time, you'll need to execute this terminal command to save your password into your system keyring.  Replace my_username with your myfitnesspal username.

```
myfitnesspal store-password my_username
```

## Run WeightCompare
1. Clone or download this repopsitory
2. Install python dependencies (environment.yml)
3. Store myfitnesspal password to system keyring
4. Run WeightCompare

```
python weightcompare.py
```