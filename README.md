# nlp_ipynb
These Python notebooks serve as a ground-up educational resource to work through NLP with minimal prior experience/setup. Also included are sets of python and NLP templates to be used piecemeal in my other projects. This repo is a hybridization of Stanford course learnings, personal research, and my condensed notes from the "NLP-Natural Language Processing with Python" course by Jose Portilla with Pierian Data.

*Setup instructions are for MacOS, but can be easily extrapolated to a linux shell on any OS.
*Folders are numbered in order of increasing difficulty/complexity. 
*Those new to Python should be able to start here from scratch.

---

## Setup
**1.** Clone the repository into a local directory and `cd` into that directory in terminal.

**2.** Install [Anaconda](https://www.anaconda.com/download) and [initialize](https://docs.conda.io/projects/conda/en/latest/commands/init.html) as desired.
*I used `conda init bash` . This adds code to your `.bash_profile` which activates the `base` environment by default. [This post](https://stackoverflow.com/questions/54429210/how-do-i-prevent-conda-from-activating-the-base-environment-by-default) describes how to suppress this automatic env activation. 

**3.** Ensure the (base) env tag appears before your next command prompt line.
*Activate manually with `conda activate base`.

**4.** Create and activate the (nlp_ipynb) Python environment. The (nlp_ipynb) tag should appear before your next command prompt line.
*Create: `conda env create -f nlp_ipynb_env.yml`
*Activate: `conda activate nlp_ipynb`

**5.** From the nlp_ipynb directory & environment, type `jupyter notebook` to open the notebooks in a browser.

---