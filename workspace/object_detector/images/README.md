# Modified Dataset Description
The dataset was modified from Kaggle's original dataset to include additional classes,  
modifying annotations, and augmenting images.

Modified dataset consist of 6 distinct classes:
* trafficlight (155 labels)
* stop (93 labels)
* speedlimit (788 labels)
* crosswalk (218 labels)
* nostop (107 labels)
* yield (15 labels)

Total data from dataset + augmented images:
* trafficlight (176 labels)
* stop (93 labels)
* speedlimit (862 labels)
* crosswalk (298 labels)
* nostop (107 labels)
* yield (111 labels)

The dataset was split with a 9:1 ratio (9:1 training:test) using partition_dataset.py.

Training set:
* trafficlight (162 labels)
* stop (77 labels)
* speedlimit (780 labels)
* crosswalk (263 labels)
* nostop (97 labels)
* yield (94 labels)

Test set:
* trafficlight (14 labels)
* stop (16 labels)
* speedlimit (82 labels)
* crosswalk (35 labels
* nostop (10 labels)
* yield (17 labels)
