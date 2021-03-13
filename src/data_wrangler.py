import pandas as pd
from pathlib import Path


def get_sales_data() -> pd.DataFrame:
    parent_folder: Path = Path(__file__).parents[1] / "data"
    sales = pd.read_csv(parent_folder / "sales_train.csv").assign(date = lambda df:pd.to_datetime(df.date,format='%d.%m.%Y'))

    items = pd.read_csv(parent_folder / "items_en.csv")

    shops = pd.read_csv(parent_folder / "shops_en.csv")

    item_category = pd.read_csv(parent_folder / "item_categories_en.csv")

    return (
        sales.merge(items, on="item_id", how="left", validate="many_to_one")
        .merge(shops, on="shop_id", validate="many_to_one", how="left")
        .merge(item_category, on="item_category_id", validate="many_to_one", how="left").rename_axis('order_id')
    )
