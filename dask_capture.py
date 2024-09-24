import argparse as ap
import warnings

import pandas as pd
from dask_md_objs import SchedulerEvent, TaskHandler

## TODO :: REMOVE ipykernel from UV

# desired arguments:
# - location of scheduler_transition file
# - location of worker file
# - location of worker_transfer file
# - location of worker_transition file
# - debug mode on/off
file_meta_info = {
    "sched_file"        : ("-s", "data/scheduler_transition.csv"),
    "worker_file"       : ("-w", "data/worker.csv"),
    "worker_trans_file" : ("-t", "data/worker_transition.csv"),
    "worker_xfer_file"  : ("-x", "data/worker_transfer.csv"),
    "output_file"       : ("-o", "data/compiled_tasks.txt")
}

def extract_scheduler_metadata(sched_file: str, out_file:str, debug: bool = False) -> TaskHandler:
    sched_x = pd.read_csv(sched_file)
    nrow, ncol = sched_x.shape
    #begins_lt_ends(sched_x["begins"], sched_x["ends"], debug=True)
    #begins_eq_gt_time(sched_x["begins"], sched_x["time"], debug=True)
    #t = Event(sched_x.iloc(axis=0)[0])
    
    th = TaskHandler()
    for i in range(0, nrow) :
        th.add_event(SchedulerEvent(sched_x.iloc(axis=0)[i]))

    if debug:
        print(len(th.tasks))
        print(th.tasks[list(th.tasks.keys())[0]])

    with open(out_file, "w") as f:
        keys = list(th.tasks.keys())
        for i in range(0, len(keys)) :
            f.write(th.tasks[keys[i]].__str__())
        return

def extract_worker_xfer_metadata(worker_xfer_file: str, debug: bool = False) -> TaskHandler :

    return

if __name__ == "__main__":
    sched_file = file_meta_info["sched_file"][1]
    worker_file = file_meta_info["worker_file"][1]
    worker_trans_file = file_meta_info["worker_trans_file"][1]
    worker_xfer_file = file_meta_info["worker_xfer_file"][1]
    out_file = file_meta_info["output_file"][1]
    debug = False

    parser = ap.ArgumentParser(
                        prog='DaskParser',
                        description='Extracts metadata objects from Dask-Mofka .csv files')

    # add all expected files as arguments
    for argname in list(file_meta_info.keys()) :
        parser.add_argument(file_meta_info[argname][0], '--{n}'.format(n=argname))
    parser.add_argument('-d', '--debug', action="store_true")

    # parse
    args = parser.parse_args()

    # set whichever ones aren't None; warn for every input left as default.
    for argname in list(file_meta_info.keys()) :
        if getattr(args,argname) is not None :
            locals()[argname] = args[argname]
        else :
            warnings.warn("Parameter {argname} defaulted to {argloc}.".format(argname=argname, argloc=file_meta_info[argname][1]), UserWarning)
    debug = args.debug

    # off to the races
    extract_scheduler_metadata(sched_file, out_file, debug)