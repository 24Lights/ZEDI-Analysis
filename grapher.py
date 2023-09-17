### GRAPHS FOR CLUSTERS-TOWERS 

for clust in all_tow_clusters:
    
    weather_accu=[]
    tower='000'
    mark='000'
    house_id=str(clust.iloc[0,-2])
    percentile=clust.iloc[2,-1]
    markers=["*",">","^","v","X","D","H","s","+","8","p","P","o","d","h"]
    clust_columns=list(clust.describe().columns[:-3])
    clust_describe=clust.describe()
    clust_means=list(clust_describe.iloc[1,:-3])
    clust_maxes=list(clust_describe.iloc[7,:-3])
    clust_mines=list(clust_describe.iloc[3,:-3])
    
    clust_temp=clust.iloc[:,:-3]
    sum_alg_months=list(clust_temp.sum(axis=0))
    clust_melted=clust_temp.melt(var_name="Month",value_name="Consumption")

    for i in weather:
        w_temp=i
        corr=np.corrcoef(w_temp,sum_alg_months)
        corr=corr[0,1]
        weather_accu.append(corr)
        del w_temp
        del corr
    
    
    clust_corr_data=clust.iloc[:,:-3]
    clust_corr_matrix=clust_corr_data.corr()
    
    print("house id ",house_id[0])
    print("\n")
    print("percentile is ",percentile)
    
    if percentile<0.25:
        mark='L25'
        print("l25 mark chk")
    elif 0.25<percentile<0.50:
        mark='25T50'
        print("25t50 mark chk")
    elif 0.50<percentile<0.75:
        mark='50T75'
        print("50t75 mark chk")
    elif 0.75<percentile:
        mark='75M'
        print("75m mark chk")
        
    if house_id[0]=='1':
        tower='A'
    elif house_id[0]=='2':
        tower='B'
    elif house_id[0]=='3':
        tower='C'
        
    
        
    clust_keys=[i for i in clust.iloc[:,-2]]
    clust_months=clust.columns[:-3]

    master_clust={}
    for i in range(len(clust_keys)):
        month_tuple=[]
        
        for j in range(len(months)):
            temp=(months[j],clust.iloc[i,j])
            month_tuple.append(temp)
        
        master_clust[clust_keys[i]]=month_tuple
        del month_tuple
        




    #############################################################################################################################################################
    plt.figure(figsize=(20, 15)) 
    sb.set_context("paper", font_scale=1.5)
    sb.set(style="whitegrid", rc={"lines.linestyle": "-", "lines.markersize": 6})
    sb.set(style="whitegrid", rc={"axes.grid": True, "grid.linestyle": "--", "grid.alpha": 0.7})
    sb.set(style="whitegrid", font="serif")

    for i in range(len(clust_keys)):
        color = plt.cm.jet(i / len(clust_keys))
        x=[]
        y=[]
        temp_key=clust_keys[i]
        
        temp_list=master_clust[temp_key]
        
        for j in range(len(temp_list)):
            temp_tuple=temp_list[j]
            
            x.append(temp_tuple[0])
            y.append(temp_tuple[1])
            
        sb.lineplot(x=x,y=y,marker=markers[i], markersize=12,label=f'{code_house[clust_keys[i]]}')
        
    sb.lineplot(x=x,y=clust_means, label='Mean ',marker=True, markersize=20,color='red', linestyle='-.', linewidth=3)
    std=np.std(clust_means)
    plt.fill_between(x,clust_means-std,clust_means+std,color='red',alpha=0.1)
    
    
    
    
    plt.xticks(rotation=45)
    plt.locator_params(axis='y', nbins=40)
    plt.xlabel(' TIME ')
    plt.ylabel('  CONSUMPTION')
    sb.set(style='whitegrid', palette='viridis')  
    plt.title(f'TOWER {tower} HOUSEHOLD CONSUMPTION TREND - {mark}')
    plt.legend(bbox_to_anchor=(1.05, 1.0),loc='upper right', fontsize='medium')
    # plt.xlim(datetime.datetime(2022, 3, 1, 0, 0), datetime.datetime(2023, 5, 1, 0, 0))

    plt.show()
    
    
    
    
    ############################################################################################################################################################3
    plt.figure(figsize=(20, 15)) 
    sb.set_context("paper", font_scale=1.5)
    sb.set(style="whitegrid", rc={"lines.linestyle": "-", "lines.markersize": 6})
    sb.set(style="whitegrid", rc={"axes.grid": True, "grid.linestyle": "--", "grid.alpha": 0.7})
    sb.set(style="whitegrid", font="serif")

    sb.heatmap(clust_corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5) 

    plt.xticks(rotation=45)
    plt.locator_params(axis='y', nbins=40)
    plt.xlabel(' TIME ')
    plt.ylabel('  CONSUMPTION')
    sb.set(style='whitegrid', palette='viridis')  
    plt.title(f'TOWER {tower} Correlation  - {mark}')
    plt.legend(bbox_to_anchor=(1.05, 1.0),loc='upper right', fontsize='medium')
    
    plt.show()
    
    
    
    
    
    ###########################################################################################################################################################
    plt.figure(figsize=(20, 15)) 
    sb.set_context("paper", font_scale=1.5)
    sb.set(style="whitegrid", rc={"lines.linestyle": "-", "lines.markersize": 6})
    sb.set(style="whitegrid", rc={"axes.grid": True, "grid.linestyle": "--", "grid.alpha": 0.7})
    sb.set(style="whitegrid", font="serif")
    
    x = np.arange(len(clust_columns))
    bar_width=0.2
    plt.bar(x,clust_means , color='skyblue',label='mean',width=bar_width)
    plt.bar(x+bar_width,clust_maxes , color='lightcoral',label='max',width=bar_width)
    plt.bar(x-bar_width,clust_mines , color='lightgreen',label='min',width=bar_width)
    
    plt.xticks(x, clust_columns, rotation=45, fontsize=10)
    plt.locator_params(axis='y', nbins=40)
    plt.xlabel(' TIME ')
    plt.ylabel('  CONSUMPTION')
    sb.set(style='whitegrid', palette='viridis')  
    plt.title(f'TOWER {tower} Min-Max-Mean  - {mark}')
    plt.legend(bbox_to_anchor=(1.05, 1.0),loc='upper right', fontsize='medium')
    
    plt.show()
    
    
    #############################################################################################################################################################
    plt.figure(figsize=(10, 6)) 
    sb.set_context("paper", font_scale=1.5)
    sb.set(style="whitegrid", rc={"lines.linestyle": "-", "lines.markersize": 6})
    sb.set(style="whitegrid", rc={"axes.grid": True, "grid.linestyle": "--", "grid.alpha": 0.7})
    sb.set(style="whitegrid", font="serif")
    
    sb.heatmap([weather_accu], cmap='coolwarm', cbar=True, xticklabels=weather_lab, annot=True, fmt=".2f")
   
    plt.xticks(rotation=45, fontsize=10)
    plt.locator_params(axis='y', nbins=40)
    plt.xlabel(' VARIABLES ')
    plt.ylabel(' CUMMULATIVE CONSUMPTION CORRELATION')
    sb.set(style='whitegrid', palette='viridis')  
    plt.title(f'TOWER {tower} weather correlations  - {mark}')
    plt.legend(bbox_to_anchor=(1.05, 1.0),loc='upper right', fontsize='medium')
    
    plt.show()
    ##############################################################################################################################################################
    fig,axes=plt.subplots(nrows=3,ncols=1,figsize=(25,20))
    # sb.set_context("paper", font_scale=1.5)
    # sb.set(style="whitegrid", rc={"lines.linestyle": "-", "lines.markersize": 6})
    # sb.set(style="whitegrid", rc={"axes.grid": True, "grid.linestyle": "--", "grid.alpha": 0.7})
    # sb.set(style="whitegrid", font="serif")
    
    sb.kdeplot(data=clust_melted,x='Consumption', hue='Month', fill=True, ax=axes[0])
    axes[0].set_title('Kernel Density Estimate (KDE)')

    for month in clust_melted['Month'].unique():
        sb.kdeplot(data=clust_melted[clust_melted['Month'] == month]['Consumption'], cumulative=True, ax=axes[1])
        axes[1].set_title('Cumulative Distribution Function (CDF)')
        axes[1].legend(title='Month')

        # # PL25 plot
        sb.histplot(data=clust_melted, x='Consumption', hue='Month', element='step', stat='density', common_norm=False, ax=axes[2])
        axes[2].set_title('Probability Density Function (PDF)')
        axes[2].legend(title='Month')
   
    plt.xticks(rotation=45, fontsize=10)
    plt.locator_params(axis='y', nbins=30)
    plt.locator_params(axis='x', nbins=40)
    
    
    
    sb.set(style='whitegrid', palette='viridis')  
    # plt.title(f'TOWER {tower} PROBABILISTIC PLOTS  - {mark}')
    plt.legend(bbox_to_anchor=(1.05, 1.0),loc='upper right', fontsize='medium')
    
    plt.show()
    #######################################################################################################################################################
  

    
    
    print("--------------------PLOT EXIT -------------------")
    del tower
    del mark
    del house_id
    del percentile
    del clust_keys
    del clust_months
    del master_clust
    del clust_corr_data
    del clust_corr_matrix
    del clust_describe
    del clust_means
    del weather_accu
    #sb.heatmap(clust_corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)  
    

        
