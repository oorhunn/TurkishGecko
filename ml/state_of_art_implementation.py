from ml.model_classes.prophet_model import Model


m_params = \
    {
        "changepoint_prior_scale": 0.01,
        "seasonality_prior_scale": 5,
        "holidays_prior_scale": 5,
        "changepoint_range": 0.9,
        "outlier_remove_window": 0,
    }

train = []  # a dataframe containing training data
test = []  # a dataframe containing test data
additional_data = []  # a dataframe containing additional columns as input features

model = Model(
    train=train,
    test=test,
    additional_data=additional_data,
    changepoint_prior_scale=m_params.get("changepoint_prior_scale"),
    seasonality_prior_scale=m_params.get("seasonality_prior_scale"),
    holidays_prior_scale=m_params.get("holidays_prior_scale"),
    changepoint_range=m_params.get("changepoint_range"),
    outlier_remove_window=m_params.get("outlier_remove_window"),
    horizon=180,
)

model.fit()
trained_model = model.prophet
forecast = model.predict()
