

# This function is only using in getting date values from filenames
# It was necessary because I could not name files like 10/08/2021
# It thinks this filename as directory
def string_to_date_refactor(filename):
    temp = filename.split(' ')
    temp_date_str = temp[1].strip('.csv')
    date_str = temp_date_str.split('-')
    month = date_str[0]
    day = date_str[1]
    year = date_str[2]
    return month, day, year
