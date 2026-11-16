import pandas as pd 
import matplotlib.pyplot as plt 

model = pd.read_csv('model_ak135.txt', sep='\t', comment='#', 
                    names=["depth", "radius", "alpha", "beta", "rho"]) 

fig, ax = plt.subplots() 
ax.plot(model['depth'], model['alpha'], label='Vp (alpha)')
ax.plot(model['depth'], model['beta'], label='Vs (beta)')
ax.plot(model['depth'], model['rho'], label='Density (rho)')
plt.legend() 
plt.savefig('model_ak135.jpg', dpi=300)

