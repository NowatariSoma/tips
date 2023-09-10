import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from make_graph import make_graph_pdf
from sklearn.preprocessing import StandardScaler
from scipy.stats import norm

def preprocess_profile(df_objective:pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    columns = ["Number", "Ave_depth", "Std_depth", "Ave_top", "Std_top", "Ave_min", "Std_min", "Collapse", "Distortion", "Mask", "Roughness"]
    ndarray = np.array([[-1, 180, 0, 12.5, 0, 12.5, 0, 0, 0, 0, 0]])
    df = pd.DataFrame(data = ndarray, columns = columns)
    df_merged = pd.concat([df_objective, df], axis = 0)
    droped_columns = ['Number','Collapse','Distortion',"Mask","Roughness"]
    df = df_merged.drop(columns=droped_columns)

    scaler = StandardScaler()
    df_scaled =pd.DataFrame(scaler.fit_transform(df),columns=df.columns)
    return df_scaled

def preprocess_errors(df_objective:pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    columns = ["Number", "Ave_depth", "Std_depth", "Ave_top", "Std_top", "Ave_min", "Std_min", "Collapse", "Distortion", "Mask", "Roughness"]
    ndarray = np.array([[-1, 180, 0, 12.5, 0, 12.5, 0, 0, 0, 0, 0]])
    df = pd.DataFrame(data = ndarray, columns = columns)
    df_merged = pd.concat([df_objective, df], axis = 0)
    droped_columns = ['Number','Ave_depth', 'Std_depth', 'Ave_top', 'Std_top', 'Ave_min', 'Std_min']
    df = df_merged.drop(columns=droped_columns)
    return df

def calc_rsme(df:pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    N = df.shape[0]
    rsme = []
    for i in range(N):
        rsme.append(np.sqrt(mean_squared_error(df[i:i+1], df[25:26])))
    df_rsme = pd.DataFrame(data=rsme)
    df_rsme.drop([22])
    return df_rsme

def profile(df:pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    df = preprocess_profile(df)
    return calc_rsme(df)

def errors(df:pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    df = preprocess_errors(df)
    return calc_rsme(df)


if __name__ == '__main__':
    df_objective = pd.read_csv('data/profile.csv')
    # df_objective.head()
    # print(df_objective)
    rsme = calc_rsme(df_objective)

    scaler = StandardScaler()

    normalized_data = scaler.fit_transform(rsme)
    normalized_data = normalized_data.flatten().tolist()

    # print(normalized_data)

    norm_frozen = norm.freeze(loc=0, scale=1)

    x = np.linspace(-3, 3, 10000)

    make_graph_pdf(x, normalized_data, norm_frozen.pdf(x), "profile", "θ", "Normal distribution")










