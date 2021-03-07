""" Filter the encounter details from OP files """

from itertools import islice
from datetime import datetime
from os import path


def filter_msh_from_text_file(tread):
    """ to filter out the MSH index from the given text file """
    msh_line_list, line_number = [], 0
    with open(tread, "r") as read_file:
        for line in read_file:
            if line.strip().split('|')[0] == 'MSH':
                msh_line_list.append(line_number)
            line_number += 1
        msh_line_list.append(line_number)
    return msh_line_list


def filter_encounter_list_from_msh_list(tread, msh_line_list, encounter):
    """ to filter encounter pairs from this msh_list """
    length, filtered_encounter_list = len(msh_line_list) - 1, []
    with open(tread, "r") as read_file:
        for i in range(length):
            temp_start, temp_end = msh_line_list[i], msh_line_list[i + 1]
            start, end = 0, (temp_end - temp_start)
            for line in islice(read_file, start, end):
                if line.strip().split('|')[0] == 'PID' and encounter in line.strip():
                    filtered_encounter_list.append((temp_start, temp_end))
    return filtered_encounter_list


def create_new_modified_filtered_text_file(enc_list, tencounter, tread, twrite):
    """ Create a new file with filtered details of the particular encounter """
    for enc_pair in enc_list:
        start, end = enc_pair[0], enc_pair[1]
        with open(tread, "r") as text_file:
            with open(f"FilteredFiles/{twrite}", "a") as mod_file:
                for line in islice(text_file, start, end):
                    mod_file.write(line.strip())
                    mod_file.write("\n")
    print(f"Filtered encounter {tencounter} details from {tread} and inserted those into {twrite}")


def get_encounter_details(file_read, encounter):
    """ This is the main function which executes everything. """
    file_write = f"{encounter}_filtered.txt"
    msh_line_list = filter_msh_from_text_file(file_read)
    filtered_enc_list = filter_encounter_list_from_msh_list(file_read, msh_line_list, encounter)
    create_new_modified_filtered_text_file(filtered_enc_list, encounter, file_read, file_write)


def get_encounter_list(file_read):
    """ to get encounters in a list from a text file """
    encounter_list = []
    with open(file_read, "r") as enc_file:
        for line in enc_file:
            encounter_list.append(line.rstrip("\n"))
    return encounter_list


def execute():
    """ calling main function """
    month_start = int(input("Starting month: "))
    month_end = int(input("Ending month: "))
    start_time = datetime.now()
    encounter_file_read = "EncounterList.txt"
    encounters = get_encounter_list(encounter_file_read)
    for cur_encounter in encounters:
        set_date_and_execute(cur_encounter, month_start, month_end)
    print("\nTime taken to fetch encounter details: ", str(datetime.now() - start_time).split('.')[0])


def set_date_and_execute(curt_encounter, m_start, m_end):
    """ Set the day and month as per requirements """
    for t_month in range(m_start,m_end+1):
        for i_day in range(1, 32):
            temp_file = f"RawFiles/2020-{t_month:02}-{i_day:02}.txt"
            if path.exists(temp_file):
                get_encounter_details(temp_file, curt_encounter)


execute()
