# Project Name

{{ cookiecutter.project_name }}

## Company & Author

{{ cookiecutter.company }} / {{ cookiecutter.author }}

## Description

This repository contains a Cookiecutter template for IP Core validation projects using the cocotb module mainly. Use this template to create scripted structured projects for IP Core design validation.

## Project Structure

Once you use this template to create a project, the structure will be as follows:

```
├── HISTORY.md         <- The HISTORY changes track.
├── README.md          <- The top-level README for developers using this project.
|
├── Lib<SimulatorName>        <- Optional directory which contains the compiled libraries for the third-party simulator
|
├── run
│   ├── requirements.txt        <- The requirements file for reproducing the analysis environment.
│   ├── fileset_vhdl.txt        <- Route to VHDL desing sources.
│   ├── fileset_verilog.txt     <- Route to Verilog desing sources.
|   ├── test_<IP_NAME>_runner.py     <- Python cocotb test runner.
│   └── Makefile                <- The Python script executor file, directory cleaner and requirements installer commands file.
|
├── tests              <- Test defining n Python scripts.
│   ├── numtest_0.py      <- First test defining Python script.
│   ├── ...               <- The following tests defining Python scripts.
│   └── numtest_n-1.py    <- Last  test defining Python script.
│
├── top_design         <- Directory which contains IP design sources.
│   ├── constraints    <- Constraints files of the design if needed.
│   ├── coregen        <- 
│   ├── hdl            <- Directory containing the full design HDL scripts (VHDL and Verilog).
|   ├── testbench      <- Directory containing the HDL versions of the tests (if needed).
│   └── vivado         <- The original Vivado project of the IP Core.
│  
│
└── utils              <- Directory which contains the auxiliar Python files, such as the IP Core class definitions and so on.
    ├── <IP_NAME>.py    <- IP Core class definition.
```

## Use

1. **Create a new project using Cookiecutter:**
   From the GitHub repository:
      ```bash
      cookiecutter https://github.com/PerezKerman/cookiecutter_cocotb.git
      ```
   or once downloaded the template, in your local directory:
      ```bash
      cookiecutter cocotb_template
      ```
   