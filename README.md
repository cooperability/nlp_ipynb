# nlp_ipynb
These Python notebooks serve as a ground-up educational resource to work through NLP with minimal prior experience/setup. Also included are sets of python and NLP templates to be used piecemeal in my other projects. This repo is a hybridization of Stanford course learnings, personal research, and my condensed notes from the "NLP-Natural Language Processing with Python" course by Jose Portilla with Pierian Data.

*Setup instructions are for MacOS, but can be easily extrapolated to a linux shell on any OS.

---

## Setup
**1.** Use Linux/Terminal to clone the repository into a local directory and `cd` there.

**2.** Install [Anaconda](https://www.anaconda.com/download) and [initialize](https://docs.conda.io/projects/conda/en/latest/commands/init.html) as desired. \
-I used `conda init bash` . This adds code to your `.bash_profile` which activates the `base` environment by default. [This post](https://stackoverflow.com/questions/54429210/how-do-i-prevent-conda-from-activating-the-base-environment-by-default) describes how to suppress this automatic env activation. \
-Ensure the (base) environment tag appears before your next command prompt line, or activate the env manually (`conda activate base`).

**3.** Create(`conda env create -f nlp_ipynb_env.yml`) and activate(`conda activate nlp_ipynb`) the (nlp_ipynb) Python environment. The (nlp_ipynb) tag should appear before your next command prompt line.

**4.** From the nlp_ipynb directory & environment, type `jupyter notebook` to open the notebooks in a browser.

---

##Usage \
-Folders are numbered in order of increasing difficulty/complexity. \
-Those new to Python should be able to start here from scratch. \
-In each notebook, hit `shift + enter` or `command/control + enter` to see function output. \


---
##Extra Links \
-[Remove DS_Store files](https://stackoverflow.com/questions/107701/how-can-i-remove-ds-store-files-from-a-git-repository) and [stop automatic .DS_Store creation](https://buildthis.com/ds_store-files-and-why-you-should-know-about-them/) \
-[Converting jupyter notebooks between formats](https://mljar.com/blog/convert-jupyter-notebook-python/) and an [Intro to jupytext](https://jupytext.readthedocs.io/en/latest/), the tool I used. \

###Environments
-[Update existing Conda environment](https://stackoverflow.com/questions/42352841/how-to-update-an-existing-conda-environment-with-a-yml-file) \
-[CRUD guide for Python Environments](https://www.askpython.com/python/environment-variables-in-python)
