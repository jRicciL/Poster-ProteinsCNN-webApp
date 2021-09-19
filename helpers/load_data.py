import pickle

with open('./data/app_data.pkl', 'rb') as f:
    data_source = pickle.load(f)

def get_df_crys_prot():
    return data_source['df_crys_prot']

def get_df_md():
    return data_source['df_md']

def get_df_dk_performances():
    return data_source['df_dk_performances']