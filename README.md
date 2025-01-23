# DASK Metadata Capture

![tests](https://github.com/RECUP-DOE/dask_capture/actions/workflows/run_tests.yaml/badge.svg)
![tests](https://github.com/RECUP-DOE/dask_capture/actions/workflows/lint.yaml/badge.svg)

A script that takes the output of Amal Gueroudji's [Mofka-Dask coupler](https://github.com/GueroudjiAmal/MofkaDask/) to consolidate the generated `.csv` files into a singular, object-focused output.

Developed and tested by Polina Shpilker for the RECUP project.

Expected inputs:
- `-s` `--sched_file` : default `scheduler_transition.csv` \
The location of the file that contains all messages sent by the DASK scheduler.
- `-w` `--worker_file` : default `workers.csv` \
The location of the file that stores all worker creation messages.
- `-t` `--worker_trans_file` : default `worker_transition.csv` \
The location of the file that stores all worker state transition messages.
- `-x` `--worker_xfer_file` : default `worker_transfer.csv` \
The location of the file that stores all messages pertaining to file transfers between workers.
- `-o` `--output_file` : default `compiled_tasks.txt` \
Where to save the consolidated output.
- `-c` `--output_compressed` : default `compressed_out.pickle` \
Filename for the compressed consolidated output.

Usage:
```bash
python dask_capture.py -s scheduler_transition.csv -w workers.csv -t worker_transition.csv -x worker_transfer.csv -o compiled_tasks.txt
```

Note the dependencies that are described by `pyproject.toml`, until this script is packaged.

## Background
The Mofka-Dask coupler generates a series of `.csv` files based on the process that generated the event and the type of event (e.g. `scheduler_transition.csv` describes the transition of any `Task` states as witnessed by the scheduler, while `worker_transfer.csv` describes the transfer of files as witnessed by a worker.) 

In order for this data to be most useful, it should be collected in a centralized place.
This way, metadata from other sources (such as Darshan) can be consolidated with all the metadata available from DASK.

This script is being developed using the example outputs generated by Amal Gueroudji's example runs, all available [here](https://github.com/GueroudjiAmal/XPDaMoDa).

## Documentation
Documentation is available on [readthedocs](https://infispiel-dask-capture.readthedocs.io/en/latest/).
