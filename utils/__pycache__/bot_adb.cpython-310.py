o
    1^Zd�6  �                   @   s�   d dl Z d dlmZ d dlmZ d dlmZ d dlmZ	 d dl
Z
d dlZd dlmZmZmZ d dlmZmZmZmZmZmZmZ d dlZd dlZd dlmZ d d	lmZmZm Z m!Z! d
e_"dZ#d dl$m%Z% G dd� d�Z&dd� Z'dd� Z(dS )�    N)�date)�exists)�sleep)�Client)�array�where�ndarray)�cvtColor�matchTemplate�	minMaxLoc�COLOR_BGR2RGB�TM_CCOEFF_NORMED�COLOR_BGR2HSV�inRange)�Image)�current_time�get_data�get_path�writeT)�ImageSingletonc                   @   s�   e Zd Zd2dd�Zdd� Zd3dd�Zd	d
� Zd3dd�Zdefdd�Z	dd� Z
dd� Zdd� Zdd� Zd4dd�Zd5dedefdd�Zd d!� Zd5d"d#�Zd$d%� Zd&d'� Zd(d)� Zd*d+� Zd,d-� Zd.d/� Zd0d1� ZdS )6�Adb�	127.0.0.1�  c                 C   sD   t � }t||�| _|| _|| _|| _|t| j� d | _t� | _	d S )N�name)
r   �PPADBClient�client�host�port�number�strr   r   �images)�selfr   r   r   �data� r#   �`C:\Users\Administrator\Documents\Projets\Rise of kingdom\Bluestacks Version\bot\utils\bot_adb.py�__init__   s   zAdb.__init__c                 C   s,   t d| j� d| j� �� d| j� d| j� �S )NzJsonNumber:z port:)�printr   r   �r!   r#   r#   r$   �__str__   s   zAdb.__str__c                 C   sZ   t � }t� }t|t| j� d �| _|d �dd�� }|� d|� d| j� �}t�|� d S )Nr   �	HD-Player�Playerr   �	 connect �:)	r   r   �intr   r   r   �replace�
subprocess�Popen)r!   r   r"   �path�adb_path�cmdr#   r#   r$   �connect_to_device$   s   zAdb.connect_to_devicec                 C   s
   | j �� S �N)r   �devicesr'   r#   r#   r$   �get_client_devices-   s   
zAdb.get_client_devicesc              
   C   s\  zPt � }t|t| j� d �| _| j�|� d| j� ��}|d u rN| �d� t� }|d �dd�� }|� d|� d| j� �}t	�
|� td� |d u rN| �� W S |W S  ty� } zQt��  | �d	� t� }|d �dd�� d
�}t	�
|� | �d� td� | �d� |d �dd�� }|� d|� d| j� �}t	�
|� td� | �� W  Y d }~S d }~ww )Nr   r,   z,INFO : Device is None, trying to reconnect..r)   r*   r   r+   �   z&EXCEPTION : Error in connect to devicez start-serverzAdb restarting..�   zConnecting to the device..�   )r   r   r   r   r   �devicer&   r   r.   r/   r0   r   �
get_device�	Exception�	traceback�	print_exc)r!   r   r"   r;   r1   r2   r3   �er#   r#   r$   r<   0   s<   







��zAdb.get_device�textc              	   C   sJ   t � }tdt�� � dt� � d|t| j� d � d|� �� t| j|� d S )Nz[ � z ] [ r   z ] )	r   r&   r   �todayr   r   r   r   r   )r!   rA   r"   r#   r#   r$   r&   U   s   4z	Adb.printc                 C   s.   z| � � �� W S    td� | � � ��  Y S �N�   )r<   �	screencapr   r'   r#   r#   r$   �%get_curr_device_screen_img_byte_arrayZ   s
   z)Adb.get_curr_device_screen_img_byte_arrayc              
   C   s�   z| � � }|d u rtd� | ��  t�|�� �}t�|�}|W S  tyB } z| �d� t	d� | ��  | �
� W  Y d }~S d }~ww )Nz)get_curr_device_screen_img device is nullzEXCEPTION : get_screen_devicerE   )r<   r&   r4   �io�BytesIOrF   r   �openr=   r   �get_curr_device_screen_img)r!   r;   �output�imager@   r#   r#   r$   rK   b   s   

��zAdb.get_curr_device_screen_imgc                 C   sR   z| � � }t|�}t|t�}|W S    td� | � � }t|�}t|t�}| Y S rD   )rK   r   r	   r   r   )r!   �screenr#   r#   r$   �get_cv2_imgs   s   

zAdb.get_cv2_imgc                 C   s*   t �t�| �� �� ��}|�|d � dS )Nz.pngT)r   rJ   rH   rI   r<   rF   �save)r!   �	file_namerM   r#   r#   r$   �save_screen�   s   zAdb.save_screen��������?c           
      C   sR   | � � }t|�}t|t�}t||t�}t|�\}}}}	||kr'|	d |	d fS d S �Nr   rE   )rK   r   r	   r   r
   r   r   )
r!   �img_to_find�
confidence�	pil_image�cv_image�result�min_val�max_val�min_loc�max_locr#   r#   r$   �find_img_cv�   s   
zAdb.find_img_cvN�target�sourcec              
   C   s  z`|d u r.| � � }t|�}|dkr|dd�dd�f }|dkr)|dd�dd	�f }t|t�}| j�|�}t||t�}t|�\}}}	}
||kr^|dkrU|
d d |
d
 fW S |
d |
d
 fW S W d S  t	y� } z| �
d� t��  | �
|� W Y d }~d S d }~ww )N�new_troops_buttonr   iB  i   �   �gem_search_buttoni�  iX  �   rE   z#Error occured when using find_image)rK   r   r	   r   r    �get_file_namer
   r   r   r=   r&   r>   r?   )r!   r_   r`   rV   rW   rU   rY   rZ   r[   r\   r]   �exception_errorr#   r#   r$   �find_img�   s.   

��zAdb.find_imgc           
      C   sD   | j �|�}t||t�}t|�\}}}}	||kr |	d |	d fS d S rT   )r    re   r
   r   r   )
r!   �srcr_   rV   rU   rY   rZ   r[   r\   r]   r#   r#   r$   �find_img_src_conf�   s   zAdb.find_img_src_confc                 C   s:  |d u r| � � }t|�}t|t�}|}| j�|�}|dkr'|dd�dd�f }t||t�}|jd }|jd }	t	|�\}
}}}|}t
||k�}tt|d d d� � �}g }|D ]}t|d �t|d �||	g}|�|� qVg }tt|��D ]'}|dkr�|�|| d d || d f� qt|�|| d || d f� qtg }tt|�d �D ]i}|| d d ||d  d ks�|| d d ||d  d ks�|| d ||d  d k�r|| d d ||d  d k�s|| d d ||d  d k�s|| d ||d  d k�r|�|| � q�|D ]}|�|� �q|S )N�	back_iconr   i�  i�  rb   rE   �����)rK   r   r	   r   r    re   r
   r   �shaper   r   �list�zipr-   �append�range�len�remove)r!   r_   r`   rV   rW   rX   rU   rY   �needle_w�needle_hrZ   r[   r\   r]   �
min_thresh�location�
rectangles�loc�rect�localisations�i�element_to_delete�elementr#   r#   r$   �find_multiple_img�   sJ   


$   ""�zAdb.find_multiple_imgc                 C   s&   d}| � |�}d|v pd|v pd|v S )Nz3dumpsys activity activities | grep mFocusedActivity�
lilithgame�rok�lilithgames��shell)r!   �string�ar#   r#   r$   �is_game_alive�   s   
zAdb.is_game_alivec                 C   s   d|� d|� �}| � |� d S )Nz
input tap rB   r�   )r!   �x�yr�   r#   r#   r$   �click�   s   
z	Adb.clickc                 C   sJ   | � � }z|�|�W S  ty$   tt� td� | ��  | �|� Y S w )N�   )r<   r�   �RuntimeErrorr&   r   r4   )r!   r�   r;   r#   r#   r$   r�   �   s   �z	Adb.shellc              	   C   s,   d|� d|� d|� d|� d�	}| � |� d S )N�input swipe rB   z 420r�   )r!   r�   r�   �x2�y2r�   r#   r#   r$   �swipe  s   
z	Adb.swipec              
   C   s0   d|� d|� d|� d|� d|� �
}| � |� d S )Nr�   rB   r�   )r!   r�   r�   r�   r�   �argr�   r#   r#   r$   �	swipe_arg	  s   "
zAdb.swipe_argc           
      C   s�  zGt � }|d d d� d }t|d � �r)|d d d� d }t�|d � |� � t|� d��}|�� �d�}W d   � n1 sAw   Y  W n   td� Y g }|D ]}d|v rbd|v rbd	|vsjd|v rod
|v ro|�|� qTi }t	dt
|�d�D ]d}|| �d�}|d �dd�|d< |d dd � |d< i |tt
|��< t|d �|tt
|�d � d< |d |tt
|�d � d< ||d  �d�}	|	d �dd�|	d< |	d |tt
|�d � d< qzd S )N�
bluestacks�����z.txt�r�
zsThe pass you provided is wrong ! We are looking for something like : 
 C:\ProgramData\BlueStacks_nxtluestacks.confzbst.instance.Nougat64�adb_port�status�display_namer   r8   z
.adb_port=rE   �"� �   �instancer   z.display_name=r   )r   r   �shutil�copyrJ   �read�splitr&   ro   rp   rq   r.   r   )
r!   r1   r�   �file�data_instance�
liste_infor}   �dico_instancer{   �string2r#   r#   r$   �restart_emulator%  s@   ���
� �zAdb.restart_emulatorc                 C   s   | � d� d S )Nzinput keyevent KEYCODE_HOMEr�   r'   r#   r#   r$   �home_buttonE  s   zAdb.home_button)r   r   )r   )rS   )NrS   )�__name__�
__module__�__qualname__r%   r(   r4   r7   r<   r   r&   rG   rK   rO   rR   r^   r   rg   ri   r~   r�   r�   r�   r�   r�   r�   r�   r#   r#   r#   r$   r      s,    
	
	
%

	9
 r   c                 C   s4   dt j_t j| ddd��dd��dd��dd�}|S )	Nztesseract\tesseract.exe�engz--psm 6)�lang�config�	r�   r�   �)�tess�pytesseract�tesseract_cmd�image_to_stringr.   )rW   rY   r#   r#   r$   �img_to_stringd  s
   �r�   c                 C   s   t | t�}t|||�S r5   )r	   r   r   )rX   �lower�upper�hsvr#   r#   r$   �&img_remove_background_and_enhance_wordl  s   
r�   ))r�   �datetimer   �os.pathr   �timer   �ppadb.clientr   r   r/   r>   �numpyr   r   r   �cv2r	   r
   r   r   r   r   r   rH   r�   r�   �PILr   �utils.Task_utilsr   r   r   r   �LOAD_TRUNCATED_IMAGES�bridge�utils.resourcesr   r   r�   r�   r#   r#   r#   r$   �<module>   s*    $  Q