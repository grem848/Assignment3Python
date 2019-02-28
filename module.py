import numpy as np
import country_codes_english
import country_codes

# list of country codes of native English-speaking countries
country_codes_english = country_codes_english.country_codes_english
english_ccs = list(country_codes_english.keys())

# list of country codes of native English-speaking countries
country_codes = country_codes.country_codes
other_ccs = list(country_codes.keys())

# getting the entire structure from the .csv file
def get_data(filename):
    return np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)

def number_of_nonenglish_vs_english(year, data):
    english_sum = 0
    non_english_sum = 0
    # for each country code in the two lists respectively, sum the number of citizens:
    for cc in english_ccs:
        mask = (data[:,0] == year) & (data[:,3] == cc)
        english_sum +=(sum(data[mask][:,4]))
    for cc in other_ccs:
        mask = (data[:,0] == year) & (data[:,3] == cc)
        non_english_sum +=(sum(data[mask][:,4]))    
    return english_sum, non_english_sum

#Now create another function that can take 2 arguments:
#1: the dataset in the form of a 2dimensional data array where y=data rows and x=[year, area, age nationality, amount].
#2: the mask in the form: data[:,3] == 5120 to find swedish or data[:,0] == 1999 to filter on year
#the return value must be the filtered dataset.

def mask_function(data, mask):
    return data[mask]

#Create another function that can take 2 arguments:
#a dataset with same characteristics as above and
#a value for the x-axis (either year, area, age or nationality)
#return value should be the accumulated population for all x-values.
#hint: if year is chosen for x then y is all accumulated amounts from all areas, ages and nationalities.

def get_dict_of_x_values_and_corresponding_sums(data, x_value):
    params = {'year':0, 'area':1, 'age':2, 'nationality': 3}
    x = params[x_value]
    # array of the unique codes of the chosen x_value:
    array_of_unique_codes = np.unique(data[:,x])
    bef_sum_dict = {}
    for code in array_of_unique_codes:
        # masking to only sum data for the unique code, and then adding the k/v-pair to the dict
        mask = (data[:,x] == code)
        bef_sum_dict[code] = sum(data[mask][:,4])
    return bef_sum_dict

def get_age_group_per_year(data, min, max, year):
    year_mask = (data[:,0] == year)
    age_group = data[year_mask]
    age_mask = (age_group[:,2] >= min) & (age_group[:,2] <= max)
    age_group = age_group[age_mask]
    return age_group

def get_list_of_age_group_sums(area, year, data):
    area_mask = (data[:,1] == area)
    data = data[area_mask]
    year_mask = (data[:,0] == year)
    data = data[year_mask]

    age_0_10 = sum(get_age_masked_data(data,0,10)[:,4])
    age_11_20 = sum(get_age_masked_data(data,11,20)[:,4])
    age_21_30 = sum(get_age_masked_data(data,21,30)[:,4])
    age_31_40 = sum(get_age_masked_data(data,31,40)[:,4])
    age_41_50 = sum(get_age_masked_data(data,41,50)[:,4])
    age_51_60 = sum(get_age_masked_data(data,51,60)[:,4])
    age_61_70 = sum(get_age_masked_data(data,61,70)[:,4])
    age_71_80 = sum(get_age_masked_data(data,71,80)[:,4])
    age_81_90 = sum(get_age_masked_data(data,81,90)[:,4])
    age_above_90 = sum(get_age_masked_data(data,91,150)[:,4])

    list_of_age_group_sums = []
    list_of_age_group_sums.append(age_0_10)
    list_of_age_group_sums.append(age_11_20)
    list_of_age_group_sums.append(age_21_30)
    list_of_age_group_sums.append(age_31_40)
    list_of_age_group_sums.append(age_41_50)
    list_of_age_group_sums.append(age_51_60)
    list_of_age_group_sums.append(age_61_70)
    list_of_age_group_sums.append(age_71_80)
    list_of_age_group_sums.append(age_81_90)
    list_of_age_group_sums.append(age_above_90)

    return list_of_age_group_sums

def get_age_masked_data(data, low_age, high_age):
    age_mask = ((data[:,2] >= low_age) & (data[:,2] <= high_age))
    return data[age_mask]