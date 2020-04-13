# Data Description: Wine Reviews Dataset 2

The dataset is from  [Sanyam Kapoor](https://github.com/activatedgeek/winemag-dataset). It contains 250,000 reviews of wines from the website [Winemag](https://www.wineenthusiast.com/).

The character attributes are:

| **Field**  | **Type**  | **Description**  | **Example**  |
|---|---|---|---|
| _url_  | `str`  | Full URL to the review  |  [https://www.winemag.com/buying-guide/laurent-...-morgon/](https://www.winemag.com/buying-guide/laurent-gauthier-2016-vieilles-vignes-cote-du-py-morgon/) |
| _title_ | `str` | Title/Name of the wine. **WARNING**: May include scraping errors.  | Laurent Gauthier 2016 Vieilles Vignes Côte du Py (Morgon)  |
| _rating_  | `int` | Wine rating on the 100-point scale  | 91 |
| _description_  | `str` | Review of the wine  | Wood aging has given spice to this rich, structured wine. Tannins and generous black fruits show through the still-young structure. This powerful wine, from one of the top vineyards in Morgon, will age well. Drink from 2020. |
| _price_  | `float`, `NULL` | Price in $ |  25  |
| _designation_  | `str`, `NULL` | Quality level of wine  | Vieilles Vignes Côte du Py |
| _varietal_ | `str`  | Grape Varietal/Blend name  | Gamay |
| _country_  | `str`  | Name of Country  | France |
| _region_  | `str`, `NULL`  | Region within a Country  | Beaujolais  |
| _subregion_  | `str`, `NULL`  | Sub-region within a region  | Morgon  |
| _subsubregion_  | `str`, `NULL`  | Detailed region  |  |
| _winery_ | `str`  |  Name of producer/winery | Laurent Gauthier |
| _vintage_  | `int`, `NULL`  | Vintage (Year) of production  | 2016  |
| _alcohol_  | `float`, `NULL`  | Alcohol By Volume (ABV) in %  | 13.5  |
| _category_ | `str`  |  Category of wine | Red |