import pandas as pd
df_diet = pd.read_csv('/mnt/DSCoE/Fall-Army-Worm-Data/raw_data/FAW_diet_data.csv')
df_plant_assay =pd.read_csv('/mnt/DSCoE/Fall-Army-Worm-Data/raw_data/FAW_plant_disk_assay_data.csv')
df_sources_and_tax =pd.read_csv('/mnt/DSCoE/Fall-Army-Worm-Data/raw_data/FAW_sources_and_taxonomy.csv')
#df_toxin_seq =pd.read_csv('/mnt/DSCoE/Fall-Army-Worm-Data/raw_data/FAW_toxin_sequence.csv')
#df_mat_35 =pd.read_csv('/mnt/DSCoE/Fall-Army-Worm-Data/raw_data/matrix_of_35_mers_for_FAW_toxins.csv')
df_pfams_FAW =pd.read_csv('/mnt/DSCoE/Fall-Army-Worm-Data/raw_data/pfams_for_FAW_toxins.csv')
df_psi_dist =pd.read_csv('/mnt/DSCoE/Fall-Army-Worm-Data/raw_data/psi_distance_between_toxins_melted.csv')
#df_diet.head(10)
df_diet.columns.values

['Testset', 'Clone Id', 'Concentration', 'Concentration Units',
       'Stunting P>|t|(Pos)', 'Stunting P>|t|(Neg)', 'Stunting Mean',
       'Stunting Std Dev', 'Stunting Pos Con TRT', 'Stunting Pos Con Mean',
       'Stunting Pos Con Std Dev', 'Stunting Neg Con TRT',
       'Stunting Neg Con Mean', 'Stunting Neg Con Std Dev',
       'Mortality P>|t|(Pos)', 'Mortality P>|t|(Neg)', 'Mortality Mean',
       'Mortality Std Dev', 'Mortality Pos Con TRT',
       'Mortality Pos Con Mean', 'Mortality Pos Con Std Dev',
       'Mortality Neg Con TRT', 'Mortality Neg Con Mean',
       'Mortality Neg Con Std Dev', 'Activity Score']