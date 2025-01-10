"""
Cookiecutter-Cocotb script generation

Author: Kerman Perez

"""
import os
from pathlib import Path
from datetime import datetime
# pylint: disable=anomalous-backslash-in-string

# Root Directory
PROJECT_DIR = Path(os.getcwd())
# # Remaining directories created within the root
TESTS_DIR = Path(os.path.join(PROJECT_DIR, "tests"))
UTILS_DIR = Path(os.path.join(PROJECT_DIR, "utils"))  # Ruta a la carpeta "utils"
RUN_DIR = Path(os.path.join(PROJECT_DIR, "run"))  # Ruta a la carpeta "run"
DESIGN_DIR = Path(os.path.join(PROJECT_DIR, "top_design", "hdl"))

## Get the Cookiecutter JSON values (PONER EN ORDEN)
PROJECT_NAME = "{{cookiecutter.project_name}}"
COMPANY = "{{cookiecutter.company}}"
AUTHOR = "{{cookiecutter.author}}"
EMAIL = "{{cookiecutter.email}}"
PROJECT_VERSION = "{{cookiecutter.project_version}}"
IP_NAME = "{{cookiecutter.ip_name}}"
COMPILED_LIB = "{{cookiecutter.directory_for_compiled_libraries}}".lower()
SIMULATOR_NAME = "{{cookiecutter.simulator_support}}"
NUMBER_OF_TESTS = int("{{cookiecutter.number_of_tests}}")
TOP_MODULE = "{{cookiecutter.top_module_needed}}"
TOP_LANG = "{{cookiecutter.top_module_language}}"
IP_INSTANCES = int("{{cookiecutter.number_of_ip_instances}}")

# Get actual date
CURRENT_DATE = datetime.now().strftime("%Y/%m/%d")

# Default headers for Python, VHDL & Verilog files
# SoC-e official headers
SOCE_PY_HEADER = f"""\"\"\"
**************************************************************
                    _______               _______             
   _||_||_||_     / ____  |             / ____  |            
  |          |   | /    \_|   ______   | /    \_|     _____  
==|          |== | \_____    / ____ \  | |           / ___ \ 
==|          |==  \_____ \  | /    \ | | |          / /__/ / 
==|          |==  _     \ | | |    | | | |     _   / _____/  
  |__________|   | \____/ | | \____/ | | \____/ | / /____    
    || || ||     |_______/   \______/   \______/  \_____/    

                  Copyright (c) 2020-2025                    
              System on Chip engineering, S.L.               
                       www.soc-e.com                         

**************************************************************
            Licensing information, do not remove.             

No part of this source file may be reproduced or adapted in  
any form  or by any means, electronic or mechanical, without 
permission from System on Chip engineering, S.L.             

This source file is  confidential and  may not be  disclosed, 
or reverse engineered without permission in writing from     
System on Chip engineering, S.L.                             

**************************************************************

Revision list                                                
Author            Date               Changes                         
{AUTHOR}     {CURRENT_DATE}     {PROJECT_VERSION} Version
{EMAIL}

**************************************************************

! file: PYTHON FILE NAME HERE 
! brief: Brief Description HERE 

\"\"\"
"""

SOCE_VHDL_HEADER = f"""--**************************************************************--
--                    _______               _______             --
--    _||_||_||_     / ____  |             / ____  |            --
--   |          |   | /    \_|   ______   | /    \_|     _____  --
-- ==|          |== | \_____    / ____ \  | |           / ___ \ --
-- ==|          |==  \_____ \  | /    \ | | |          / /__/ / --
-- ==|          |==  _     \ | | |    | | | |     _   / _____/  --
--   |__________|   | \____/ | | \____/ | | \____/ | / /____    --
--     || || ||     |_______/   \______/   \______/  \_____/    --
--                                                              --
--                   Copyright (c) 2020-2025                    --
--               System on Chip engineering, S.L.               --
--                        www.soc-e.com                         --
--                                                              --
--**************************************************************--
--            Licensing information, do not remove.             --
--                                                              --
-- No part of this source file may be reproduced or adapted in  --
-- any form  or by any means, electronic or mechanical, without --
-- permission from System on Chip engineering, S.L.             --
--                                                              --
-- This source file is  confidential and  may not be  disclosed,--
-- or reverse engineered without permission in writing from     --
-- System on Chip engineering, S.L.                             --
--                                                              --
--**************************************************************--
--                                                              --
-- Revision list                                                --
-- Author            Date          Changes                      --
-- {AUTHOR}      {CURRENT_DATE}   {PROJECT_VERSION} Version     --
-- {EMAIL}                                                      --
--                                                              --
--**************************************************************--
--!
--! file: top_module.vhd
--! brief: IP instances top module
--!
"""

SOCE_VERILOG_HEADER = f"""//**************************************************************//
//                    _______               _______             //
//    _||_||_||_     / ____  |             / ____  |            //
//   |          |   | /    \_|   ______   | /    \_|     _____  //
// ==|          |== | \_____    / ____ \  | |           / ___ \ //
// ==|          |==  \_____ \  | /    \ | | |          / /__/ / //
// ==|          |==  _     \ | | |    | | | |     _   / _____/  //
//   |__________|   | \____/ | | \____/ | | \____/ | / /____    //
//     || || ||     |_______/   \______/   \______/  \_____/    //
//                                                              //
//                   Copyright (c) 2020-2025                    //
//               System on Chip engineering, S.L.               //
//                        www.soc-e.com                         //
//                                                              //
//**************************************************************//
//            Licensing information, do not remove.             //
//                                                              //
// No part of this source file may be reproduced or adapted in  //
// any form  or by any means, electronic or mechanical, without //
// permission from System on Chip engineering, S.L.             //
//                                                              //
// This source file is  confidential and  may not be  disclosed,//
// or reverse engineered without permission in writing from     //
// System on Chip engineering, S.L.                             //
//                                                              //
//**************************************************************//
//                                                              //
// Revision list                                                //
// Author            Date          Changes                      //
// {AUTHOR}     {CURRENT_DATE}    {PROJECT_VERSION} Version     //
// {EMAIL}                                                      //
//                                                              //
//**************************************************************//
//!
//! file: top_module.v
//! brief: IP instances top module
//!
"""

# Generic headers
PY_HEADER = f"""\"\"\"
Company: {COMPANY}

Author: {AUTHOR} / {EMAIL} 
                
Date: {CURRENT_DATE}
                
Description: <Set brief description HERE>
\"\"\"
"""

VHDL_HEADER = f"""-----------------------------------------------------
-- Company: {COMPANY} --
-- Author: {AUTHOR} / {EMAIL} --
-- Date: {CURRENT_DATE} --
-- Description: <Set brief description HERE> --
-----------------------------------------------------
"""
VERILOG_HEADER = f"""/////////////////////////////////////////////////////
// Company: {COMPANY} //
// Author: {AUTHOR} / {EMAIL}  //
// Date: {CURRENT_DATE} //
// Description: <Set brief description HERE> //
/////////////////////////////////////////////////////
"""
MAKEFILE_HEADER = f"""#####################################################
# Company: {COMPANY}
# Author: {AUTHOR} / {EMAIL} 
# Date: {CURRENT_DATE}
# Description: {IP_NAME} IP Core testbench Makefile
#####################################################"""

class FileGenerator:
    """
    Class which defines the files that will be created in terms on the input received
    """
    def __init__(self, file_name):
        """
        Initialisation of the file creator class
        Args:
            file_name (str): the file or directory name that will be generated
        """
        self.file_name = file_name

    def generate_files(self):
        """
        This method generates the files or directories and its headers depending on the company
        """
        if self.file_name == "extra_directories":
            if COMPILED_LIB == "yes":
                simulator_lib_map = {
                    "Questa Advanced Simulator": "LibQuesta",
                    "ModelSim Simulator": "LibModelSim",
                    "Riviera-PRO Simulator": "LibRiviera-PRO",
                    "Active-HDL Simulator": "LibActive-HDL"
                }
                compiled_lib_name = simulator_lib_map.get(SIMULATOR_NAME, f"Lib{SIMULATOR_NAME}")
                os.makedirs(compiled_lib_name, exist_ok=True)
                print(
                    "An extra folder has been created for the"
                    f" compiled libraries: {compiled_lib_name}\n"
                )
            else:
                print("No extra directories needed for compilated libraries\n")

        elif self.file_name == "test_files":
            for i in range(NUMBER_OF_TESTS):
                file_name = f"numtest_{i}.py"
                file_path = Path(TESTS_DIR / file_name)
                with open(file_path, "w") as file:
                    if COMPANY == "SoC-e":
                        # SoC-e official header
                        file.write(SOCE_PY_HEADER)
                    else:
                        # Generic header
                        file.write(PY_HEADER)

        elif self.file_name == "ip_class_file":
            ip_lower = IP_NAME.lower()
            file_name = f"{ip_lower}.py"  # The IP name in lowercase
            file_path = UTILS_DIR / file_name
            with open(file_path, "w") as file:
                if COMPANY == "SoC-e":
                    file.write(SOCE_PY_HEADER)
                else:
                    file.write(PY_HEADER)

        elif self.file_name == "runner_file":
            ip_lower = IP_NAME.lower()
            file_name = f"test_{ip_lower}_runner.py"
            file_path = RUN_DIR / file_name
            with open(file_path, "w") as file:
                if COMPANY == "SoC-e":
                    file.write(SOCE_PY_HEADER)
                else:
                    file.write(PY_HEADER)

        elif self.file_name == "top_module_file":
            if TOP_MODULE == "Yes":
                if TOP_LANG == "VHDL":
                    if COMPANY == "SoC-e":
                        file_name = "top_module.vhd"
                        file_path = DESIGN_DIR / file_name
                        with open(file_path, "w") as file:
                            file.write(SOCE_VHDL_HEADER)
                    else:
                        file_name = "top_module.vhd"
                        file_path = DESIGN_DIR / file_name
                        with open(file_path, "w") as file:
                            file.write(VHDL_HEADER)
                else:
                    if COMPANY == "SoC-e":
                        file_name = "top_module.sv"
                        file_path = DESIGN_DIR / file_name
                        with open(file_path, "w") as file:
                            file.write("`timescale 1ns / 1ps\n")
                            file.write(SOCE_VERILOG_HEADER)
                    else:
                        file_name = "top_module.sv"
                        file_path = DESIGN_DIR / file_name
                        with open(file_path, "w") as file:
                            file.write("`timescale 1ns / 1ps\n")
                            file.write(VERILOG_HEADER)

        elif self.file_name == "makefile":
            file_name = "Makefile"
            file_path = Path(RUN_DIR / file_name)
            with open(file_path, "r") as file:
                actual_content = file.readlines()
            with open(file_path, "w") as file:
                # Generic header
                file.write(MAKEFILE_HEADER)
                file.writelines(actual_content)

    def write_files(self):
        """
        This method generates all the content on the scripts, depending on the files
        """
        if self.file_name == "test_files":
            for i in range(NUMBER_OF_TESTS):
                file_name = f"numtest_{i}.py"
                test_name = f"numtest_{i}"
                file_path = Path(TESTS_DIR / file_name)
                with open(file_path, "a") as file:
                    ip_lower = IP_NAME.lower()
                    file.write("import cocotb\n")
                    file.write("from cocotb.triggers import Timer\n")
                    file.write(f"from utils.{ip_lower} import TB_{IP_NAME}\n")
                    file.write("# Import the rest of the required modules HERE\n")
                    file.write("\n")
                    file.write("# Set the total simulation time by default in ps\n")
                    file.write(
                        f"sim_time_{i} = 100000000 # 100 us, change if necessary\n\n"
                    )
                    file.write(
                        f"async def {test_name}(dut, total_sim_time : int = sim_time_{i}):"+
                        " # Set more arguments if necessary and document\n"
                    )
                    file.write("    \"\"\"\n")
                    file.write(f"    Test number {i}, 100 us of simulation time\n")
                    file.write("    Brief: <Short description of the test>\n")
                    file.write("    Args:\n")
                    file.write(f"        dut: Design Under Test, {IP_NAME} IP Core\n")
                    file.write(
                        "        total_sim_time (int): Set the total "+
                        "simulation time of the test in ps\n"
                    )
                    file.write("    \"\"\"\n")
                    file.write(f"    # {IP_NAME} testbench object instance\n")
                    file.write(f"    tb = TB_{IP_NAME}(dut)\n\n")
                    file.write("    ## Rest of the logic and instantiations HERE\n")
                    file.write("    # Clock & Reset signals initialization\n\n")
                    file.write("    # Force total simulation time\n")
                    file.write("    await tb.force_simulation_time(total_sim_time)\n")

        elif self.file_name == "ip_class_file":
            ip_lower = IP_NAME.lower()
            file_name = f"{ip_lower}.py"  # IP name in lowercase
            file_path = UTILS_DIR / file_name
            with open(file_path, "a") as file:
                file.write("# Import all the modules needed HERE\n")
                file.write("import cocotb\n")
                file.write("import logging\n")
                file.write("\n")
                file.write("# Import all the extra classes needed HERE\n")
                file.write("from cocotb.triggers import RisingEdge, Timer\n")
                file.write("\n")
                file.write("# Specific extra exception classes (if defined) HERE\n")
                file.write("\n")
                file.write("\n")
                file.write(f"# {IP_INSTANCES} {IP_NAME} core(s) testbench class\n")
                file.write(f"class TB_{IP_NAME}:\n")
                file.write("    \"\"\"\n")
                file.write(f"    {IP_NAME} IP Core testbench functonalities class\n")
                file.write("    \"\"\"\n")
                file.write("\n")
                file.write("    def __init__(self, dut):\n")
                file.write("        \"\"\"\n")
                file.write(
                    f"        Initialization of the {IP_NAME} cores "+
                    "and some signals, including constants\n"
                )
                file.write("        Args:\n")
                file.write(
                    f"            dut: Design Under Test. {IP_NAME} "+
                    "top module and all the instances below.\n"
                )
                file.write("        \"\"\"\n")
                file.write("        self.dut = dut\n")
                file.write("        self.log = logging.getLogger(\"cocotb.tb\")\n")
                file.write("        self.log.setLevel(logging.DEBUG)\n")
                file.write("\n")
                file.write(
                    "        ## VHDL generics, Verilog parameters "+
                    "and/or overall constants definitions HERE\n"
                )
                file.write("\n")
                file.write("        ## Clock and Reset signals initializations HERE\n")
                file.write("        # Example: \"self.dut.clk.setimmediatevalue(0)\"\n")
                file.write("\n")
                file.write(
                    "        ## Clock and Reset generation constants "+
                    "HERE(unit, period, offset...)\n"
                )
                file.write("\n")
                file.write("    # Overall behavior methods HERE\n")
                file.write("\n")
                file.write("    # Simulation time management method\n")
                file.write(
                    "    async def force_simulation_time(self, total_sim_time : int):\n"
                )
                file.write("        \"\"\"\n")
                file.write(
                    "        Force the total simulation time of the testbench object\n"
                )
                file.write("        Args:\n")
                file.write(
                    "            total_sim_time (int): Set the total simulation time"+
                    " in ps, lowest time scale\n"
                )
                file.write("        \"\"\"\n")
                file.write(
                    "        self.log.info(\"Total simulation time: \" +" +
                    " str(total_sim_time) + \"ps\")\n"
                )
                file.write(
                    "        # Get the actual simulation time " +
                    "(second element of the tuple, first " +
                    "element is a simulation constant)\n"
                )
                file.write("        actual_time = cocotb.simulator.get_sim_time()[1]\n\n")
                file.write(
                    "        # Then, if the actual time is lower than the " +
                    "required time, force the simulation time\n"
                )
                file.write("        if actual_time < total_sim_time:\n")
                file.write("            required_time = total_sim_time - actual_time\n")
                file.write("            await Timer(required_time, \"ps\")\n")

        elif self.file_name == "runner_file":
            ip_lower = IP_NAME.lower()
            file_name = f"test_{ip_lower}_runner.py"
            file_path = RUN_DIR / file_name
            # Top level HDL language
            top_lang = TOP_LANG.lower()
            key_str = "{}"
            # Change simulator names to simplified Makefile format
            simulator_map = {
            "Questa Advanced Simulator": "questa",
            "ModelSim Simulator": "modelsim",
            "Riviera-PRO Simulator": "riviera",
            "Active-HDL Simulator": "activehdl",
            "GHDL": "ghdl",
            "Icarus Verilog": "icarus",
            "Verilator": "verilator",
            "Synopsis VCS": "vcs",
            "Cadence Incisive": "ius",
            "Cadence Xcelium": "xcelium",
            "Tachyon DA CVC": "cvc"
            }
            sim_name = simulator_map.get(SIMULATOR_NAME, "unknown")
            with open(file_path, "a") as file:
                file.write("import cocotb\n")
                file.write("import pytest\n")
                file.write("import os\n")
                file.write("import sys\n")
                file.write("\n")
                file.write("from pathlib import Path\n")
                file.write(
                    "from cocotb.runner import get_runner # May be obsolete by the usage date\n"
                )
                file.write("\n")
                file.write(
                    "# Get the needed modules from the absolute path from project root\n"
                )
                for i in range(NUMBER_OF_TESTS):
                    file.write(f"from tests.numtest_{i} import numtest_{i}\n")
                file.write(
                    "# Get the necessary modules from the \"utils\" directory if needed\n"
                )
                file.write("\n")
                file.write(
                    "# Test caller, needs decorator \"@cocotb.test()\"" +
                    " to mark which test function must be run\n"
                )
                file.write(
                    "# This decorator indicates that the function below" +
                    " is a test and cocotb will run it\n"
                )
                file.write("@cocotb.test()\n")
                file.write(f"async def {ip_lower}_test_caller(dut):\n")
                file.write("    \"\"\"\n")
                file.write(
                    "    Parallel test caller, depending on each tests' and pytest parameters\n"
                )
                file.write("    Args:\n")
                file.write("        dut: Design Under Test\n")
                file.write("    \"\"\"\n")
                file.write("    test_number = int(os.getenv(\"test_number\"))\n")
                file.write("    ## Get the rest of the pytest parameters if needed HERE\n")
                file.write("    # Usage example below\n")
                i = 0
                while i < NUMBER_OF_TESTS - 1:
                    if i == 0:
                        file.write(f"    if test_number == {i}:\n")
                        file.write(f"        await numtest_{i}(dut)\n")
                        i += 1
                    else:
                        file.write(f"    elif test_number == {i}:\n")
                        file.write(f"        await numtest_{i}(dut)\n")
                        i += 1
                j = NUMBER_OF_TESTS - 1
                file.write("    else:\n")
                file.write(f"        await numtest_{j}(dut)\n\n")
                file.write(
                    "# Pytest parametrizations for parallel tests. An example below\n"
                )
                file.write("@pytest.mark.parametrize(\n")
                file.write("    \"sim_parameters\", [\n")
                for k in range(NUMBER_OF_TESTS):
                    file.write("        {\"test_number\": " + f"\"{k}\"" + "},\n")
                file.write("    ])\n\n")
                file.write(
                    "@pytest.mark.parametrize(\"seed\", " +
                    "range(2)) # This is an example for a random " +
                    "seed parameter with range 2\n"
                )
                file.write("# Testbench simulation main function\n")
                file.write(
                    f"def test_{ip_lower}_runner(seed, " +
                    "sim_parameters): # Set the defined pytest parameters as arguments\n"
                )
                file.write("    \"\"\"\n")
                file.write(f"    {IP_NAME} testbench runner\n")
                file.write("    Args:\n")
                file.write("        seed (int): Testbench random seed\n")
                file.write(
                    "        sim_parameters (str): Testbench simulation parameters\n"
                )
                file.write("    \"\"\"\n")
                file.write(
                    f"""    # Set HERE the testbench parameters (such as the simulator name)
    # Get the HDL files
    with open("fileset_vhdl.txt", "r") as file:
        vhdl_sources = file.read().splitlines()
    with open("fileset_verilog.txt", "r") as file:
        verilog_sources = file.read().splitlines()
    # Get the simulator to use
    sim = os.getenv("SIM", "{sim_name}")

    # Get the HDL top level language
    hdl_toplevel_lang = os.getenv("HDL_TOPLEVEL_LANG", "{top_lang}")

    # Project path:from root directory
    proj_path = Path(__file__).resolve().parent.parent

    # The path to the compiled libraries if necessary HERE
    # (e.g. path to modelsim.ini file in QuestaSim)

    sys.path.append(str(proj_path/"run"))
    runner = get_runner(sim)

    # Runner build (default, change parameters if needed)
    runner.build(
        # hdl_library=, # The library name to compile into
        verilog_sources=verilog_sources, # Verilog source files to build
        vhdl_sources=vhdl_sources, # VHDL source files to build
        # includes=, # Verilog include directories
        # defines=, # Defines to set
        # parameters=hdl_parameters, # Verilog parameters or VHDL generics
        # build_args=, # Extra build arguments for the simulator, get the compiled libraries
        hdl_toplevel="top_module", # Name of the HDL toplevel module
        always=True, # Always run the build step
        build_dir="./sim_build_numtest_"+sim_parameters["test_number"] +
                "/" + sim_parameters["test_number"] +
                "_"+ str(seed), # Directory to run the build step in (CHANGE)
        verbose=True # Enable verbose messages
        )

    # Runner test (default, change parameters if needed)
    runner.test(
        test_module = "test_{ip_lower}_runner",
        hdl_toplevel="top_module", # HDL toplevel module
        # hdl_toplevel_library=, # The library name for HDL toplvel
        hdl_toplevel_lang=hdl_toplevel_lang, # Language of the HDL toplevel module
        # gpi_interfaces={key_str}, # List of GPI interfaces to use
        # testcase="", # Name(s) of a specific testcase(s) to run
        seed=seed, # A specific random seed to use
        # test_args=, # Extra arguments for the simulator
        # plusargs="", # plusargs to set for the simulator
        extra_env=sim_parameters, # Extra environment variables to set
        waves=True, # To create the waveform file after simulating - Record signal traces
        # gui=False, # Run with simulator GUI
        # parameters=hdl_parameters, # Verilog parameters or VHDL generics
        build_dir="./sim_build_numtest_"+sim_parameters["test_number"] +
                "/" + sim_parameters["test_number"] +
                "_"+ str(seed), # Directory the build step has been run in (CHANGE)
        # test_dir="", # Directory to run the tests in
        # results_xml="", # Name of xUnit XML file to store the tests results in
        verbose=True, # Enable verbose messages
        )
    """
                )

        elif self.file_name == "top_module_file":
            fileset_vhdl_path = RUN_DIR / "fileset_vhdl.txt"
            fileset_verilog_path = RUN_DIR / "fileset_verilog.txt"
            if TOP_MODULE == "Yes":
                if TOP_LANG == "VHDL":
                    file_name = "top_module.vhd"
                    file_path = DESIGN_DIR / file_name
                    with open(file_path, "a") as file:
                        file.write("library IEEE;\n")
                        file.write("use IEEE.STD_LOGIC_1164.ALL;\n")
                        file.write("-- Define other libraries if necessary")
                        file.write("\n")
                        file.write("\n")
                        file.write("entity top_module is\n")
                        file.write(
                        """    generic (
        -- Set all the generics HERE
    );\n"""
                        )
                        file.write(
                        """    port (
        -- Set all the signals HERE
    );\n"""
                        )
                        file.write("end top_module;\n\n")
                        file.write("architecture Behavioral of top_module is\n")
                        file.write(
                        """
------------------------------------------
-- Component Declarations --
------------------------------------------"""
                        )
                        for i in range(IP_INSTANCES):
                            file.write(
                            f"""
component {IP_NAME}_{i} -- Change name if necessary
    generic(
        );
    port(
        );
end component;
"""
                            )
                        file.write(
                        """
-- Internal Signals Declarations
                        """
                        )
                        file.write(
                        """
begin
                        """
                        )
                        file.write(
                        """
------------------------------------------
-- Component Instantiations --
------------------------------------------"""
                        )
                        for i in range(IP_INSTANCES):
                            file.write(
                            f"""
-- {IP_NAME}_{i} (Change name if necessary)
inst_{IP_NAME}_{i}: {IP_NAME}_{i}
    generic map(
        );
    port map(
        );
"""
                            )
                        file.write(
                        """
-- Additional logic HERE

end Behavioral;
                        """
                        )
                    with open(fileset_vhdl_path, "w") as file:
                        file.write("../top_design/hdl/top_module.vhd")
                else:
                    file_name = "top_module.sv"
                    file_path = DESIGN_DIR / file_name
                    with open(file_path, "a") as file:
                        file.write("\n")
                        file.write(
                        """module top_module #(
    // Set all the parameters HERE
)(
    // Set all the ports HERE
);

"""
                        )
                        file.write(
                        """////////////////////////////////////////////
// Internal Signals Declarations //
////////////////////////////////////////////

////////////////////////////////////////////
// Component Instantiations //
////////////////////////////////////////////
"""
                        )
                        for i in range(IP_INSTANCES):
                            file.write(
                            f"""// {IP_NAME}_{i} (Change name if necessary)
{IP_NAME}_{i} #(
    // Parameter assignments
) inst_{IP_NAME}_{i} (
    // Port Connections
);

"""
                            )
                        file.write(
                        """// Additional logic HERE

endmodule
"""
                        )
                    with open(fileset_verilog_path, "w") as file:
                        file.write("../top_design/hdl/top_module.sv")

    def readme_file(self):
        """
        This method fills the specific README.md file depending on
        the cookiecutter variables and the created files
        """
        ip_lower = IP_NAME.lower()
        generated_files = []
        # Access to the test scripts
        for i in range(NUMBER_OF_TESTS):
            test_file = f"numtest_{i}.py"
            generated_files.append(f"tests/{test_file}")
        # Access to the utils directory script
        ip_file = f"{ip_lower}.py"
        generated_files.append(f"utils/{ip_file}")
        # Access to the runner script
        runner_file = f"test_{ip_lower}_runner.py"
        generated_files.append(f"run/{runner_file}")
        # Access to the top_module
        if TOP_MODULE == "Yes":
            if TOP_LANG == "VHDL":
                top_file = "top_module.vhd"
                generated_files.append(f"top_desing/hdl/{top_file}")
            elif TOP_LANG == "Verilog":
                top_file = "top_module.sv"
                generated_files.append(f"top_desing/hdl/{top_file}")
        file_path = Path(PROJECT_DIR / "README.md")
        # Add the compiled libraries directory if existing
        if COMPILED_LIB == "yes":
            simulator_lib_map = {
                "Questa Advanced Simulator": "LibQuesta",
                "ModelSim Simulator": "LibModelSim",
                "Riviera-PRO Simulator": "LibRiviera-PRO",
                "Active-HDL Simulator": "LibActive-HDL"
            }
            compiled_lib_name = simulator_lib_map.get(SIMULATOR_NAME, f"Lib{SIMULATOR_NAME}")
            generated_files.append(compiled_lib_name)

        with open(file_path, "r") as readme_file:
            readme_content = readme_file.readlines()
        updated_readme_content = []
        for line in readme_content:
            search_line = ("2. **Fill the created Python scripts"+
                      " according to the desired functionality:**")
            updated_readme_content.append(line)
            if line.strip() == search_line:
                updated_readme_content.append("\nThe following files and directory were"+
                                              " created dynamically based on your inputs:\n\n")
                for file in generated_files:
                    updated_readme_content.append(f"    - `{file}`\n")
                updated_readme_content.append("\n")
        with open(file_path, "w") as readme_file:
            readme_file.writelines(updated_readme_content)

    def create_full_files(self):
        """
        This method executes all the methods above one by one
        """
        self.generate_files()
        self.write_files()

if __name__ == "__main__":
    FileGenerator("extra_directories").create_full_files()
    FileGenerator("test_files").create_full_files()
    FileGenerator("ip_class_file").create_full_files()
    FileGenerator("runner_file").create_full_files()
    FileGenerator("top_module_file").create_full_files()
    FileGenerator("makefile").create_full_files()
    FileGenerator("extra_directories").readme_file()
