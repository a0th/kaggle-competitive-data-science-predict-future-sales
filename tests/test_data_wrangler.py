
import pytest
import pandas as pd
from src import data_wrangler


@pytest.fixture(scope="module")
def sales_data() -> pd.DataFrame:
    return data_wrangler.get_sales_data()


def test_data_wragler_returns_df(sales_data):
    assert isinstance(sales_data, pd.DataFrame)


def test_data_wrangler_values(sales_data):
    assert sales_data.date.dt.year.agg(["max", "min"]).tolist() == [2015, 2013]
    assert sales_data.date.isnull().sum() == 0
    assert sales_data.date.iloc[0] == pd.Timestamp(year=2013,month=1,day=2)

def test_shop_names(sales_data):
    assert sales_data.shop_name.isnull().sum() == 0


def test_item_names(sales_data):
    assert sales_data.item_name.isnull().sum() == 0


def test_item_categories(sales_data):
    assert sales_data.item_category_name.isnull().sum() == 0
    assert sales_data.item_category_name.eq("").sum() == 0

def test_index_name(sales_data):
    assert sales_data.index.name == 'order_id'