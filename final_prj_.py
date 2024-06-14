import pandas as pd
bus_df = pd.read_csv('./노선별버스이용객수.csv', header=0, engine='python', encoding='cp949')

print(bus_df.info())

#%% 그룹 비교
region = bus_df.groupby('지역', '지역코드')['전체 총승객인원'].describe()
region_code = bus_df.groupby('지역', '지역코드')['전체 총승객인원'].describe()


from scipy import stats
from statsmodels.formula.api import ols, glm
bus_df
