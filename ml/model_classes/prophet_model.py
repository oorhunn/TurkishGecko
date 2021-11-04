from prophet import Prophet
import numpy as np
import pandas as pd
from ml.model_utils.supressor import suppress_stdout_stderr


class Model:
    """Model class to do training and prediction."""

    def __init__(
        self,
        train,
        test,
        additional_feature=None,
        market=None,
        growth="logistic",
        seasonality_mode="additive",
        changepoint_range=0.9,
        changepoint_prior_scale=0.01,
        seasonality_prior_scale=10,
        holidays_prior_scale=10,
        horizon=None,
        outlier_remove_window=0,
    ):
        self.train = train
        self.test = test
        self.additional_feature = additional_feature
        self.market = market

        # Get 99th and 20th percentile of historical data to determine cap and floor.
        self.max_y = self.train["y"].quantile(0.99)
        self.min_y = self.train["y"].quantile(0.3)

        self.growth = growth

        # If we have more than 1 year data, use yearly seasonality.
        if self.train.shape[0] < 730:
            ys = False
        else:
            ys = True

        # Create model prophet model object.
        self.prophet = Prophet(
            growth=growth,
            seasonality_mode=seasonality_mode,
            seasonality_prior_scale=seasonality_prior_scale,
            changepoint_range=changepoint_range,
            changepoint_prior_scale=changepoint_prior_scale,
            yearly_seasonality=ys,
            weekly_seasonality=True,
            daily_seasonality=False,
            holidays_prior_scale=holidays_prior_scale,
        )

        # Add monthly seasonality if enough data.
        if self.train.shape[0] > 90:
            self.prophet.add_seasonality(period=30.5, fourier_order=seasonality_prior_scale, name="monthly")

        # Add country specific holidays.
        self.prophet.add_country_holidays(country_name="US")
        self.horizon = horizon
        self.outlier_remove_window = outlier_remove_window

        # If it has cars data, add to model.
        if self.additional_feature is not None:
            self.prophet.add_regressor("additional_feature", prior_scale=10, standardize=False, mode="additive")

    def fit(self):
        """Fit prophet model."""
        if self.outlier_remove_window != 0:
            self.train = self.median_filter(df=self.train, window=self.outlier_remove_window, col_name="y").copy()

        if self.growth == "logistic":
            self.train["cap"] = self.max_y * 2
            self.train["floor"] = self.min_y

        with suppress_stdout_stderr():  # To eliminate write outputs to terminal.
            self.prophet.fit(self.train)

    def predict(self):
        """Do prediction with trained model.

        :return: Forecasted data.
        :rtype: Pandas.DataFrame
        """
        # Create future data to do prediction for these dates.
        if self.horizon is None:
            future = self.prophet.make_future_dataframe(periods=self.test.shape[0], include_history=True)
        else:
            future = self.prophet.make_future_dataframe(periods=self.horizon, include_history=False)

        # If car data is used for modeling, it needs to be added to the future data.
        if self.cars is not None:
            future = self.add_additional_feature(future, self.cars)

        # If logistic model is used with cap and floor, it also needs to be added to the future data.
        if self.growth == "logistic":
            future["cap"] = self.max_y * 2
            future["floor"] = self.min_y

        forecast = self.prophet.predict(future)
        return forecast

    @staticmethod
    def add_additional_feature(df, additional_data):
        # add additional features to the future df
        df["the_year"] = df.ds.dt.year
        df["the_month"] = df.ds.dt.month
        additional_data["the_year"] = additional_data.the_date.dt.year
        additional_data["the_month"] = additional_data.the_date.dt.month
        df_f = pd.merge(
            df, additional_data, how="left", on=["the_year", "the_month"], sort=False, copy=True
        ).drop(columns=["the_year", "the_month", "the_date"])
        return df_f

    @staticmethod
    def median_filter(df, window=7, col_name=None):
        # TODO: Create a better outlier filter. Right now, we are not using any outlier removal technique.
        """
        A simple median filter, removes (i.e. replace by np.nan) observations that exceed N (default = 3)
        standard deviation from the median over window of length P (default = 24) centered around
        each observation.
        Parameters
        ----------
        df : pandas.DataFrame
            The pandas.DataFrame containing the column to filter.
        col_name : string
            Column to filter in the pandas.DataFrame. No default.
        window : integer
            Size of the window around each observation for the calculation
            of the median and std. Default is 7 (time-steps).
        Returns
        -------
        dfc : pandas.Dataframe
            A copy of the pandas.DataFrame `df` with filtered column.
        """

        dfc = df.loc[:, [col_name]].copy()
        dfc["median"] = dfc[col_name].rolling(window, center=True).median()
        dfc["std"] = dfc[col_name].rolling(window, center=True).std()
        median_std = dfc["std"].median()
        dfc.loc[dfc.loc[:, col_name] >= dfc["median"] + median_std, col_name] = np.nan
        dfc.loc[dfc.loc[:, col_name] <= dfc["median"] - median_std, col_name] = np.nan
        df_n = df.copy()
        df_n[col_name] = dfc.loc[:, col_name]
        return df_n
