""" Filter the encounter details from raw files """

from itertools import islice
from datetime import datetime


def filter_msh_from_text_file(tread):
    """ to filter out the MSH index from the given text file """
    try:
        msh_line_list, line_number = [], 0
        with open(tread, "r") as read_file:
            print("Filtering MSH List.... Please wait few seconds....")
            for line in read_file:
                if line.split("|")[0] == "MSH":
                    msh_line_list.append(line_number)
                line_number += 1
            msh_line_list.append(line_number)
            print("Completed Filtering\n")
        return msh_line_list
		
    except FileNotFoundError:
        print(f"There is no such {tread} file. Please check again!!")


def filter_encounter_list_from_msh_list(tread, msh_line_list, encounter):
    """ to filter encounter pairs from this msh_list """
    try:
        length = len(msh_line_list) - 1
        with open(tread, "r") as read_file:
            filtered_encounter_list = []
            print(f"\nStarted filtering encounter {encounter} from MSH List.. Please wait few seconds...")
            for i in range(length):
                temp_start, temp_end = msh_line_list[i], msh_line_list[i + 1]
                start, end = 0, (temp_end - temp_start)
                fetched_details = False
                for line in islice(read_file, start, end):
                    if encounter in line.strip():
                        fetched_details = True
                if fetched_details:
                    filtered_encounter_list.append([temp_start, temp_end])
        print("Filtering List Completed..")
        return filtered_encounter_list
		
    except FileNotFoundError:
        print(f"There is no such {tread} file. Please check again!!")


def create_new_modified_filtered_text_file(enc_list, tread, twrite):
    """ Create a new file with filtered details of the particular encounter """
    try:
        print(f"Started Writing Segregated Details of Encounter in new File {twrite}.. Please wait few seconds...")
        for enc_pair in enc_list:
            start, end = enc_pair[0], enc_pair[1]
            with open(tread, "r") as text_file:
                with open(twrite, "a") as mod_file:
                    for line in islice(text_file, start, end):
                        mod_file.write(line.strip())
                        mod_file.write("\n")
        print(f"Filtered and created new text file {twrite} with encounter details")
		
    except FileNotFoundError:
        print(f"There is no such {tread} file. Please check again!!")


def filter_op_file(encounter, file_read, msh_line_list):
    """ to filter op file """
    try:
        file_write = f"{encounter}_filtered.txt"
        filtered_enc_list = filter_encounter_list_from_msh_list(file_read, msh_line_list, encounter)
        create_new_modified_filtered_text_file(filtered_enc_list, file_read, file_write)
		
    except FileNotFoundError:
        print(f"There is no such {file_read} file. Please check again!!")


def get_encounter_list(file_read):
    """ to get encounters in a list from a text file """
    try:
        encounter_list = []
        with open(file_read, "r") as enc_file:
            for line in enc_file:
                encounter_list.append(line.rstrip("\n"))
        return encounter_list
		
    except FileNotFoundError:
        print(f"There is no such {file_read} file. Please check again!!")


def get_encounter_details(encounters_mode, file_read, single_encounter=None):
    """ This is the main function which executes everything. """
    try:
        msh_line_list = filter_msh_from_text_file(file_read)
        if encounters_mode == "m":
            encounter_file_read = "EncounterList.txt"
            encounters = get_encounter_list(encounter_file_read)
            for encounter in encounters:
                st_time = datetime.now()
                filter_op_file(encounter, file_read, msh_line_list)
                print("Time taken to get this encounter details: " + str(datetime.now() - st_time).split(".")[0] + "\n")
        elif encounters_mode == "s":
            filter_op_file(single_encounter, file_read, msh_line_list)
			
    except FileNotFoundError:
        print(f"There is no such {file_read} file. Please check again!!")


def execute_this_method():
    """ executing specific function based on single or multiple encounters """
    input_encounters_mode = input("\nType 'm' for multiple encounters or Type 's' for single encounter: ").rstrip().lower()
    combined_files_read = "comb_op_files.txt"
    if input_encounters_mode == "m":
        start_time = datetime.now()
        get_encounter_details(input_encounters_mode, combined_files_read)
        print("Time taken to fetch all encounter details: ", str(datetime.now() - start_time).split(".")[0])
    elif input_encounters_mode == 's':
        encounter = input("\nEnter the encounter no: ").rstrip()
        start_time = datetime.now()
        get_encounter_details(input_encounters_mode, combined_files_read, encounter)
        print("Time taken to fetch encounter details: ", str(datetime.now() - start_time).split(".")[0])
    else:
        print("\n Your input is wrong. Only 'm' (for multiple encounters) and 's' (for single encounter) is allowed. Please run the utility again.")


""" calling main function """
execute_this_method()