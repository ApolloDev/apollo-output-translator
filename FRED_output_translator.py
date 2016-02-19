import base_output_translator

df = base_output_translator.hdf5_to_dataframe('output.allegheny.county_age.race.gender.location.hdf5')

rows = base_output_translator.get_row_count(df)

for i in range(1, rows):
    age = df['age'][i]
    race = df['race'][i]
    location = df['location'][i]
    gender = df['gender'][i]
    day = df['day'][i]
    pop_inc = df['N_i'][i]
    pop_prev = df['N_p']
    s_inc = df['S_i']
    s_prev = df['S_p']
    e_inc = df['E_i']
    e_prev = df['E_p']
    i_inc = df['I_i']
    i_prev = df['I_p']
    symp_inc = df['Y_i']
    symp_prev = df['Y_p']
    r_inc = df['R_i']
    r_prev = df['R_p']