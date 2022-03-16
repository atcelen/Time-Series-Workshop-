# Time Series Workshop
Welcome! You can find here the materials that will be used in the Time Series Workshop.

## Installing Anaconda
If you don't have Python3 installed on your computer, you can follow the guidelines provided in the links below for your own operating system:

MacOS : https://docs.anaconda.com/anaconda/install/mac-os/

Windows : https://docs.anaconda.com/anaconda/install/windows/

Linux : https://docs.anaconda.com/anaconda/install/linux/

## Creating a new environment for the workshop
In order to install the packages that we will need during the workshop, create a new virtual environment:
- Download this Repository as a zip file : Code -> Download Zip

- Extract the zip file

- Open Anaconda Prompt and navigate to the extracted folder:
```
cd the\path\goes\here
# The path should look something like this (for Windows):
cd C:\Users\atace\OneDrive\Documents
```

- Create the virtual environment using environment.yml:
```
conda env create -f environment.yml
```

- Activate the virtual environment:
```
conda activate workshop
```
- Install the scikit-optimize package:
```
pip install scikit-optimize
```

- Open up Jupyter Notebook:
```
jupyter notebook
```
