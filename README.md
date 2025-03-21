# Payments Automation

## Prerequisites
Make sure you have Python installed on your system. You can check your Python version using one of the following commands:

```bash
python --version
```
or
```bash
python3 --version
```

## Step 1: Create a Virtual Environment
To create a virtual environment, run the following command in your terminal:

### Windows
```bash
python -m venv myenv
```
or
```bash
python3 -m venv myenv
```

### macOS and Linux
```bash
python3 -m venv myenv
```

Replace `myenv` with the desired name of your virtual environment.

## Step 2: Activate the Virtual Environment
To start using the virtual environment, you must activate it.

### Windows
```bash
myenv\Scripts\activate
```

### macOS and Linux
```bash
source myenv/bin/activate
```

You will notice your terminal prompt changes to indicate the active environment:
```
(myenv) $
```

## Step 3: Install Packages
With the environment activated, you can now install packages using `pip`:

```bash
pip install -r requirements.txt
```

Packages installed this way will only be available within the virtual environment.


## Step 4: Considerations about csv file
1. The id of subscription plan suppose to be pregenerated in uuid v4 format
2. The empty fields should remain empty like in the example: plans_with_trial.csv file 
3. Trial and subscription durations is always better to convert to the days

## Step 4: Run the script

```bash
python add_ixopay_subscription.py
```

