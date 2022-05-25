import mlflow
import mlflow.sklearn
import dvc.api

path = 'data/data.csv'
repo = ''      # path to git repository
version = 'v1' # git sha1, branch, or tag

data_url = dvc.api.get_url(
    path=path,
    repo=repo,
    rev=version,
)

mlflow.set_experiment('demo')

df = pd.read_csv(data_url)

mlflow.log_param('data_url', data_url)
mlflow.log_param('data_version', version)
mlflow.log_param('input_rows', df.shape[0])
mlflow.log_param('input_cols', df.shape[1])


cols_y = pd.DataFrame(list(train_y.columns))
cols_y.to_csv('features.csv', header=False, index=False)

mlflow.log_artifact('features.csv')
