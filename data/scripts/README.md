# Additional Scripts

After looking at the data we noticed that although `dataset_2` had more observations (~250k) than `dataset_1` (150k), but it was lacking some characteristics like `taster_name` and `taster_twitter_handle`.


Therefore, to make `dataset_2` more robust we created a script to scrap addtional information from the website such as `taster_name`, `taster_twitter_handle`, `taster_website`, `taster_instagram`, `bottle_size `, `importer`,  `date_reviewed`, and `avg_user_rating`.


After running the code for 4 hours we realized the amount of time required to scrap all the information we needed with only 3 computers would take too long (>80 hours). Instead, we joined the two datasets to create a union datset, which provided us the best of both datasets at the cost of losing 50% of our larger dataset. However, our joined dataset has ~120k reivews, which would still provide us robust metrics for our data analysis.
