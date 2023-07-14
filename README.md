# nlp_ipynb
These Python notebooks serve as a ground-up educational resource to work through NLP from the ground up. Also included are sets of python and NLP templates to be used piecemeal in my other projects. This repo is a hybridization of Stanford course learnings, personal research, and my condensed notes from the "NLP-Natural Language Processing with Python" course by Jose Portilla with Pierian Data. I've attempted to make the learning flow naturally between MY phases of learning NLP. This won't work for everyone.


## Setup
**1.** Clone the repo into your desired local directory and open a linux shell in this directory.

**2.** Ensure [Anaconda](https://www.anaconda.com/download) is installed your machine.

**3.** [Initialize Anaconda](https://docs.conda.io/projects/conda/en/latest/commands/init.html) as desired.
* For my MacBook, I used `conda init bash` . 
* This adds a block of code to your `.bash_profile` which activates the base environment by default. [This answer](https://stackoverflow.com/questions/54429210/how-do-i-prevent-conda-from-activating-the-base-environment-by-default) describes how to suppress the automatic base env activation. 

**4.** Ensure you are in the (base) env, or activate it.
* For my MacBook, I used `conda activate base`. You should see the (base) tag appear before your next input line. 

**5.** Create and activate the Python environment from the `nlp_ipynb_env.yml` file.
* For my MacBook, I used `conda env create -f nlp_ipynb_env.yml`.

**6.** Activate the `nlp_ipynb` environment, using `conda activate nlp_ipynb`.

**7.** From the home directory, type `jupyter notebook` to begin using the formulas in a browser.


## Usage