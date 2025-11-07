import os
import subprocess

# https://foreveryolo.top/posts/34987/index.html is referred!!!

cpu_path = r"C:\Users\Harudog\Desktop\Use\WorkingArea\SrcCode\coCode\2025\coHw\p4\automaVerilog"
ise_path = r"C:\Xilinx\14.7\ISE_DS\ISE"
run_time = "2500ns"

import os


def run_ise_simulation():
    """Run ISE simulation
    This function collect all .v file and compile them.
    Then, generate a .prj and a .tcl file to start generation
    """
    # print("Running ISE simulation...")

    file_list = []
    for root, dirs, files in os.walk(cpu_path):
        for file in files:
            if file.endswith(".v"):
                file_list.append(file)

    with open(os.path.join(cpu_path, "mips.prj"), "w") as prj:
        for file in file_list:
            prj.write(f'verilog work "{os.path.join(cpu_path, file)}"\n')

    with open(os.path.join(cpu_path, "mips.tcl"), "w") as tcl:
        tcl.write(f"run {run_time};\nexit")

    os.environ["XILINX"] = ise_path

    compile_cmd = [
        os.path.join(ise_path, "bin", "nt64", "fuse"),
        "-nodebug",
        "-prj", os.path.join(cpu_path, "mips.prj"),
        "-o", "mips.exe",
        "test_mips"
    ]

    with open("compile_log.txt", "w") as log:
        subprocess.run(compile_cmd, stdout=log, stderr=subprocess.STDOUT)

    sim_cmd = ["mips.exe", "-nolog", "-tclbatch", os.path.join(cpu_path, "mips.tcl")]

    with open("raw_out.txt", "w") as out:
        subprocess.run(sim_cmd, stdout=out, stderr=subprocess.STDOUT)


def process_simulation_output():
    """Handling simulation output"""
    # print("Simulating...")

    try:
        with open("raw_out.txt", "r", encoding="utf-8") as f:
            content = f.read()

        processed_output = ""
        lines = content.split('\n')

        for line in lines:
            if line.strip().startswith('@'):
                processed_output += line + '\n'

        with open("verilog.txt", "w", encoding="utf-8") as f:
            f.write(processed_output)

    except Exception as e:
        print(f"Error during simulation output handling: {e}")

run_ise_simulation()
process_simulation_output()