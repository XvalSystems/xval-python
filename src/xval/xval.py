import ctypes
from enum import IntEnum
import os
from pathlib import Path


class OutputFileType(IntEnum):
    XLSX = 0
    CSV = 1
    TERM = 2

lib = ctypes.CDLL( Path(__file__).resolve().parent / "xval.dll" )
lib.run.argtypes = [
    ctypes.c_char_p, # xact_path
    ctypes.c_bool, # has_audit
    ctypes.c_size_t, # num_hardcode
    ctypes.c_bool, # has_timestamp
    ctypes.c_bool, # has_wav
    ctypes.c_bool, # has_wai
    ctypes.c_bool, # has_out_name
    ctypes.c_bool, # has_out_dir
    ctypes.c_bool, # has_out_ft

    ctypes.c_bool, # audit
    ctypes.POINTER(ctypes.c_char_p), # hardcode
    ctypes.c_bool, # timestamp
    ctypes.c_bool, # write_all_vtables
    ctypes.c_bool, # write_all_inputs
    ctypes.c_char_p, # out_name
    ctypes.c_char_p, # out_dir
    ctypes.c_int, # out_ft
] 
lib.run.restype = None

lib.template.argtypes = [
    ctypes.c_size_t, # argc
    ctypes.POINTER(ctypes.c_char_p), # argv
]
lib.template.restype = None


TEMPLATE_LIST = [
    "fda_stat_ag33"
]

def run(
        xact_path:str, 
        current_working_directory: str|None = None, 
        audit: bool|None = False, 
        hardcode: list[str]|None = None,
        timestamp: bool|None = None, 
        write_all_vtables: bool|None = None,
        write_all_inputs: bool|None = None, 
        out_name: str|None = None, 
        out_dir: str|None = None, 
        out_ft: str|OutputFileType|None = None, 
    ):

    original_cwd = os.getcwd()
    if current_working_directory is not None:
        os.chdir(current_working_directory)

    if hardcode is None:
        hardcode = []

    if isinstance(out_ft, str):
        match out_ft:
            case "xlsx":
                out_ft = OutputFileType.XLSX
            case "csv":
                out_ft = OutputFileType.CSV
            case "term":
                out_ft = OutputFileType.TERM
            case _:
                raise Exception(f"Invalid out_ft passed to run. Options are: {
                    [oft.name.lower() for oft in OutputFileType]
                    }.")

    HardcodeType = ctypes.c_char_p * len(hardcode)
    hardcode_param = HardcodeType(*[hc.encode("utf-8") for hc in hardcode])


    lib.run(
        xact_path.encode("utf-8"),

        False if audit is None else True,
        len(hardcode),
        False if timestamp is None else True,
        False if write_all_vtables is None else True,
        False if write_all_inputs is None else True,
        False if out_name is None else True,
        False if out_dir is None else True,
        False if out_ft is None else True,
        
        False if audit is None else audit,
        hardcode_param,
        False if timestamp is None else timestamp,
        False if write_all_vtables is None else write_all_vtables,
        False if write_all_inputs is None else write_all_inputs,
        b"" if out_name is None else out_name.encode("utf-8"),
        b"" if out_dir is None else out_dir.encode("utf-8"),
        OutputFileType.XLSX if out_ft is None else out_ft,
    )
    os.chdir(original_cwd)


TEMPLATE_LIST = [
    "fda_stat_ag33"
]


def template(
        name:str, 
        path:str|None = None, 
    ):
    py_argv = [name]
    if (path is not None):
        py_argv.append(path) 

    argc = len(py_argv)
    ArgvType = ctypes.c_char_p * argc 
    argv = ArgvType( *[arg.encode("utf-8") for arg in py_argv] )

    lib.template(argc, argv)




if __name__ == "__main__":
    run("example.xact", current_working_directory = "example", out_dir = "out", out_ft = "csv")
    template("fda_stat_ag33", "example/fda_stat_ag33")
    run("fda_stat_ag33.xact", current_working_directory = "example/fda_stat_ag33", out_dir = "out", out_ft = "term")
