# Investigating Changes on Bug Reports of Mozilla's Bugzilla

This is the repository of TCC "Investigando Mudanças em Relatórios de Bugs do Bugzilla da Mozilla".

## Files organization
All the data used across the scripts is in [data](https://github.com/felipeemerson/Bugzilla-mozilla-investigation). Scripts used to download the dataset are in [dataset-download-scripts](https://github.com/felipeemerson/Bugzilla-mozilla-investigation). The script and model used for saving bug reports on MongoDB are in [mongo-db-scripts](https://github.com/felipeemerson/Bugzilla-mozilla-investigation). The scripts used to process data are in [processing-scripts](https://github.com/felipeemerson/Bugzilla-mozilla-investigation). And, the notebooks used for data analysis are in [notebooks](https://github.com/felipeemerson/Bugzilla-mozilla-investigation).

## How to use downloads scripts
The download of the dataset was divided into three steps:
1. First, we need to download the ids of the bugs that are in time period that we want. We had to downloads the ids in interval of 15 days, because Bugzilla's API limit the download to a maximum of 10k BRs (Bug Reports). This was made with the script [get_bugs_id_by_15days.py](https://github.com/felipeemerson/Bugzilla-mozilla-investigation);
2.After that, the script [create_urls_with_100_ids_each.py](https://github.com/felipeemerson/Bugzilla-mozilla-investigation) will combine each 100 ids into one URL. This was necessary to optimize download time;
3.And, lastly, the script [concurrent_100ids.py](https://github.com/felipeemerson/Bugzilla-mozilla-investigation) will download the dataset with all the fields.

## How to save bug reports on MongoDB
Now, that we have the file with all bug reports, the script [save_bug_reports.py](https://github.com/felipeemerson/Bugzilla-mozilla-investigation) will save the bug reports to MongoDB. If you added some new fields, you may need to change the model [Bug.py](https://github.com/felipeemerson/Bugzilla-mozilla-investigation).

**Obs.**: Note that you need to have MongoDB installed on your machine.

## Data analysis
The notebooks used for respond the **RQ1** (Research Question) are [analysis_intro.ipynb]() and [analysis_not_cf_fields.ipynb](). For RQ2, the notebooks are [analysis_changes_groupby_resolution.ipynb](), [analysis_changes_groupby_priority_severity.ipynb]() and [analysis_changes_groupby_product.ipynb](). And, for RQ3, the notebooks are [analysis_not_cf_fields.ipynb]().

## Used Dataset
The used dataset can be downloaded separately [here](https://drive.google.com/file/d/1qXG8YySGBxFd7pTxr3LF39f2IzzV4Hlx/view?usp=sharing). Put all the files in [data]() folder and for each file save it into MongoDB. The data needed to run the analysis' notebooks files are [here](https://drive.google.com/file/d/1WKJjZBKB0oNAx1vgJ8xWdVCLmzG_B4XO/view?usp=sharing), put them on [data]() folder as well.