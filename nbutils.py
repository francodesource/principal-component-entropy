import matplotlib.pyplot as plt
from pathlib import Path

class ImageSaver:
    def __init__(self, save_imgs=True, destination_folder='imgs'):
        self.save_imgs=save_imgs
        self.destination_folder=destination_folder

    def save_img(self, filename: str, desitination_folder='imgs'):
        output_path = Path("imgs/"+filename)
        output_path.parent.mkdir(parents=True, exist_ok=True) 
        if self.save_imgs:
            plt.savefig(f'{desitination_folder}/{filename}')

def set_plt_params():
    plt.rcParams.update({
    'font.size': 11,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.linestyle': '--',
})