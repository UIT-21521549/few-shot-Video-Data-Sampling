# few-shot-Video-Data-Sampling
This framework is designed to help select the most representative frames of the entire video dataset and minimize the need for annotating all frames. This framework works best if you have a partially annotated video data and you want to select the best representative sample to re-annotate for better model performance.

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

