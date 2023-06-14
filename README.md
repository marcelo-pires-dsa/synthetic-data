# Synthetic Data with SDV

This project demonstrate how to create syntetic datasets using real data samples as a starting point.
On the of the main advantages is to be alr to generate a big amount of data, otherwise would be very difficult
or even **impossible** due project scope or resources.

## Requirements
 - Python >= 3.9
 - Pip
 - Pipenv

## Repository Structure
```shell
├───dataset
│   ├───raw -> Real data
│   └───synthetic -> Synthesized data
├───output -> Output for synthesizer, etc
└───R -> Data Wrangling project (not pushed yet)
└─── synthetic-data-modeling.py
└─── synthetic-metadata.py
└─── synthetic-data-metadata.json
```
NOTE: For this example, I added the datasets as LFS, that´s not the way I really do it. Usually all my datasets
are versioned with appropriate method and only metadata is stored in Git for tracking.

## Installing 
### Installing Python
Check the official Python documentation

### Installing pip

### Installing pipenv
This project uses pipenv to manage virtual environment in an easy and straight forward way. All dependencies are
defined in the **Pipfile** and **Pipfile.lock**

When using pipenv, avoid to manually changing both **Pipfile** and **Pipfile.lock**, thus use the Pipenv command to manage the 
dependencies.

### Generating Synthetic data