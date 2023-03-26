# few-shot-Video-Data-Sampling (AICITY 2023-TRACK 5)
The aim of this framework is to aid in the selection of the most suitable frames from a video dataset, while reducing the requirement to annotate every frame. This framework is most effective when dealing with video data that has already been partially annotated, and where the goal is to identify the most appropriate sample for further annotation to improve the performance of the model.

## Step 1: Run Proc.Sort_videos()
This sorts the videos into different time of day 

## Step 2: Run Proc.Train_frame_selection
This step calculates the approprate sampling rate for each video and samples the most representative frames for training.

## Step 3: Run Proc.convert_text2toml
Converts the initial text annotations into toml files

## Step 4: Run Proc.get_train_toml
Select the corresponding annotations of the selected frames (Step 2) from Step 3.

## Step 5: Run Proc.move_imgs
Select the corresponding images of the selected frames (Step 2) from the image folder.

## Step 6: Run Proc.convert_toml2cvat
Convert selected toml files to cvat format for reannotations of the selected frames.

