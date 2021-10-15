# Object Detector for Roadsigns
 With so many potential objects on the road, one might get lost trying to locate certain roadsigns  
on the street. This is particularly true from the many potential distractions a driver might face  
in real-time. An automated detector could help allievate such issues by tracking and marking specific  
roadsigns for drivers.

# 1. Data Wrangling and Exploration
 The dataset for this project originates from:

 * [Kaggle](https://www.kaggle.com/andrewmvd/road-sign-detection)

From this original set of 877 images in PNG formate, we've modified the marked labels in PASCAL VOC  
format in XML files using LabelImg (graphical image annotation tool by Darren). New and modified  
labels are stored in a similar fashion (PASCAL VOC format in XML files).

 * [Link to LabelImg](https://github.com/tzutalin/labelImg)

Instead of the original 4 classes that was given, 6 classes was marked for identification (4 old,  
2 new):
 - trafficlight (155 labels)
 - stop (93 labels)
 - speedlimit (788 labels)
 - crosswalk (218 labels)
 - nostop (107 labels)
 - yield (15 labels)

100 additional PNG images were created through augmentation to increase the effective sample size of  
the final label (yield) from 5 images which contains yield. Overall, the modified set with the augment  
set consist of:
 - trafficlight (176 labels)
 - stop (93 labels)
 - speedlimit (862 labels)
 - crosswalk (298 labels)
 - nostop (107 labels)
 - yield (111 labels)

The dataset was split roughly into a 9:1 ratio using partition_dataset.py provided by tensorflow's object  
detection API. The preprocessing of training and test set files were done through generate_tfrecord.py  
also provided by tensorflow's object detection API. To fully test our object detection model, we'll be  
utilizing a 30 sec clip of a YouTube video consist of traffic in St. Petersburg.

[![YouTube Video](http://img.youtube.com/vi/vKD8_m88tuk/0.jpg)](https://www.youtube.com/watch?v=vKD8_m88tuk)

# 2. Model and Training
 The model used for this project was derived from a pre-trained ResNet model (SSD ResNet50 V1) using  
transfer learning. Model weights from the pre-trained model was used to fine-tune our custom model.

 * [ResNet50 Model](https://tfhub.dev/tensorflow/retinanet/resnet50_v1_fpn_640x640/1)

Out custom ResNet model was trained for 25000 steps, 2000 of which were warm-up steps). Validation of the  
dataset was performed parallel to training, of which detection loss, precision, and recall was measured (as  
shown below). Overall, the detection of large objects appears to be good (precision around 0.95, recall  
around 0.96). However, the performance gets worse for smaller objects (precision around 0.58, recall around  
0.64). This would have large consequences on the model, as we'll see in the video test. Other problems exist  
as well, of which we'll discuss in the following section.

Model Precision:
![Model Precision](https://github.com/leekahung/object_detector_roadsigns/blob/main/images/model_precision.png)
![Model Precision 2](https://github.com/leekahung/object_detector_roadsigns/blob/main/images/model_precision_2.png)

Model Recall:
![Model Recall](https://github.com/leekahung/object_detector_roadsigns/blob/main/images/model_recall.png)
![Model Recall 2](https://github.com/leekahung/object_detector_roadsigns/blob/main/images/model_recall_2.png)

Model Loss (training in orange, validation in blue):
![Model Loss](https://github.com/leekahung/object_detector_roadsigns/blob/main/images/model_loss.png)

Video Test:
 * [Video Test](https://github.com/leekahung/object_detector_roadsigns/blob/main/workspace/object_detector/videos/video_results_compressed.mp4)

# 3. Conclusion and Future Improvements
 While the results for static images appears excellent, this was not the case when we began to transition into  
more dynamic scenarios (i.e. videos). For an object to be registered by the model, it has to be close-by of  
which the object size would be fairly large. This has consequences since the model would not be able to detect  
the object until its fairly close to the camera. This is very apparent in the video as it could hardly register  
real traffic lights on the street unless it's fairly close to it. This issue might be remedied, if we were to  
include more instances of labels of which, the object themselves appear small in images.

Another strange problem that risen was the mislabeling of cars as traffic lights or objects on the road itself.  
This might be due to the features of tail light of the vehicles or the shape of objects on the road. We could  
attempt to fix this by including more instances of our 6 classes during training (perhaps around 200 images per  
class as oppose to around 100).

# Original Roadmap
[Proposed roadmap](https://docs.google.com/document/d/1pi7UyNj-fMED7Iy1oBeMUZ0Rag70NiQuSnHijzi65_8/edit)

# Credits
Special thanks to my mentor Ricardo Alanís for his continued support and mentorship. The advice given had
always been helpful during my journey into Data Science and AI.
