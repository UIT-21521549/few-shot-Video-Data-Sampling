from utils import read_textfile, vis_data, create_dir, text2yolo, get_images,text2toml,toml2cvac,combine_folders,toml2cvact,sort_videos,get_images_per_time_of_day,select_training_images,select_anno_train_images,move_images
from scipy.stats import skew




class data_proc():
    def __init__(self,video_folder):
        self.video_folder=video_folder


    def visualize_data(self):
        # Visualize data
        vis_data(video_folder, anno_csv)
    
    def sort_videos(self):
        sort_videos(self.video_folder)
        print('========================')
        print('Video Sorting Completed')
        print('========================')


    def train_frame_selection(self):
        select_training_images()
        print('========================')
        print('Frame Selection Completed')
        print('========================')

    def convert_text2toml(self,anno,width,height):
        text2toml(anno,width,height)
        print('===========================')
        print('TOML conversion Completed')
        print('===========================') 


    def convert_toml2cvat(self):
        cls=['motorbike','DHelmet','DNoHelmet','P1Helmet','P1NoHelmet','P2Helmet','P2NoHelmet']
        toml2cvact('images','selected toml files', 'cvats',cls)
        print('===========================')
        print('CVAT conversion Completed')
        print('===========================')        
    

    def convert_text2yolo(self,anno,width,height):
        text2toml(anno,width,height)
        print('=================================')
        print('Text 2 YOLO conversion Completed')
        print('=================================') 

    def get_train_toml(self):
        select_anno_train_images()
        print('=================================')
        print('Train Toml conversion Completed')
        print('=================================')         

    def move_imgs(self):
        move_images()
        print('=================================')
        print('Image Folder Move Completed')
        print('=================================') 


if __name__ == "__main__":
    
    width=1920
    height=1080

    video_folder='Videos/*'
    # video_folder='D:/aicity2023_track5_test/aicity2023_track5_test/videos/*'
    anno='gt.txt'
    anno_csv=read_textfile('gt.txt')


    proc=data_proc(video_folder)
    proc.visualize_data()
    # proc.sort_videos()
    # proc.train_frame_selection()
    # proc.convert_text2toml(anno,width,height)
    # proc.get_train_toml()
    # proc.move_imgs()
    # proc.convert_toml2cvat()


