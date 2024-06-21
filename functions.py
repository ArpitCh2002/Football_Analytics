import seaborn as sns

def plot_heatmaps(heat_df, teamId, p_type, ax):
    heat_df = heat_df.copy()
    heat_df = heat_df.loc[(heat_df['teamId'] == teamId) & (heat_df['type'] == p_type)]
    
    kde = sns.kdeplot(x=heat_df.x, y=heat_df.y, data=heat_df, fill=True, cmap='magma', ax=ax)