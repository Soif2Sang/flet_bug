o
    �UdK  �                   @   s�   d dl Z d dlmZ d dlZd dlmZmZ dddd�Zde	fd	d
�Z
dd� Zdd� ZG dd� dej�ZG dd� dej�Zdejfdd�Zddd�Zedkrxe�  e� Zed d d d Zee � � � eD ]Zee� eeed  ed �� qfdS dS )�    N)�randint)�get_data�
write_dataz#3b8ed0z#ba4543z#dec433)�   �   �   �timec                 C   sf   t | �dkrdS d| vrdS | �d�\}}t|��� r!t|��� s#dS t|�dks/t|�dkr1dS dS )N�   F�:�   �<   T)�len�split�str�	isnumeric�int)r   �hours�minutes� r   �jC:\Users\Administrator\Documents\Projets\Rise of kingdom\Bluestacks Version\bot\views\Flet_time_allower.py�is_valid_time   s   r   c                 C   s�   dd l }tt|�d��� �\}}}}}t| �rt|�sdS |d | }t| �d�d �d t| �d�d � }	t|�d�d �d t|�d�d � }
|	|  k oT|
k S   S )Nr   �%Y %m %d %H %MFr   r
   r   )r   �mapr   �strftimer   r   ��first�secondr   �year�month�day�hour�min�current�start�endr   r   r   �is_in_frametime   s   ((r%   c                 C   s�   t | �rt |�s
dS dd l}tt|�d��� �\}}}}}|d |d  }t| �d�d �d t| �d�d �d  }	t|�d�d �d t|�d�d �d  }
|
|  kr[|	kr_n n|}	|	| }	|
| }
t|	|
�S )Ni�� r   r   i  r   r
   r   )r   r   r   r   r   r   r   r   r   r   r   �random_time_in_frametime'   s   ,,
r&   c                       s6   e Zd Zd� fdd�	Zdd� Zdd� Zd	d
� Z�  ZS )�RowTimezone�00:00Tc                    s�   t � jdi |�� t� � _|dkr+|dkr+|r+� jt|� d t|� d �ddg� t|�� _t|�� _|� _|� _	|� _
tjd|� fdd�dd�� _tjd	|� fd
d�dd�� _tjtjjddd� fdd�d�� _� j�� j� j� jg� t� j� d S )Nr(   �	schedules�timingZStartc                    �   � � � S �N��sub��_��selfr   r   �<lambda>?   �    z&RowTimezone.__init__.<locals>.<lambda>�2   )�label�value�	on_submit�heightZEndc                    r+   r,   r-   r/   r1   r   r   r3   @   r4   �pink600�(   �Deletec                    s   � j �� �S r,   )�parent�deleter/   r1   r   r   r3   F   s    )�icon�
icon_color�	icon_size�tooltip�on_clickr   )�super�__init__r   �datar   �append�instance�profiler=   r#   �stop�ft�	TextField�field_start�
field_stop�
IconButton�icons�DELETE_FOREVER_ROUNDEDr>   �controls�extendr   )r2   rH   rI   r=   r#   r$   �default�kwargs��	__class__r1   r   rE   5   s(   (


�zRowTimezone.__init__c                 C   s   d| j j_| j ��  d S )NF)�page�banner�open�update)r2   �er   r   r   �close_bannerK   s   
zRowTimezone.close_bannerc                 C   sT   t jt jjt jt jjt jjdd�t j|d�t j	d| j
d�gdd�| j_| j��  d S )Nr;   )�color�size�r7   ZOk)rC   T)�bgcolor�leading�content�actionsrZ   )rK   �Banner�colors�	AMBER_100�IconrP   �WARNING_AMBER_ROUNDED�AMBER�Text�
TextButtonr]   rX   rY   r[   )r2   �textr   r   r   �
pop_bannerO   s   ��
�zRowTimezone.pop_bannerc                 C   s�   t � | _| j| j d | j d �| j| jg�}t| j| j d | j d � | jj	| j
j	g| j| j d | j d |< t| jj	�rHt| j
j	�sO| �d� d S | jj	| j
j	| _| _t| j� d S )Nr)   r*   zWrong format, please fix)r   rF   rH   rI   �indexr#   rJ   �printrM   r7   rN   r   rn   r   )r2   �ir   r   r   r.   \   s   (*zRowTimezone.sub)r(   r(   T)�__name__�
__module__�__qualname__rE   r]   rn   r.   �__classcell__r   r   rV   r   r'   4   s
    r'   c                       sF   e Zd Z� fdd�Zddefdd�Zdd� Zdd
d�Zdd� Z�  Z	S )�ManagerTimezonec              
      s�   t � jdi |�� t� � _t|�� _t|�� _d� _t� j� j d � j d � � j	�
tjdd�� t� � _� j	�
tjtjdtt� j� � jt� j� d t� j� d rXdnd	� fd
d�d�tjd� fdd�tjjd�gdd�� � ��  d S )N�
   r)   r*   z�You can set a frametime to a profile
The only format allowed is 'hours:minutes' also, 02:00 pm -> 14:00
You may want to tune your re-do tasks timings to avoid running the profile twice during the same frametimer`   zEnable profile frametime�enable_timingTFc                    s
   � � d�S )Nrx   )�reverse_keywordr/   r1   r   r   r3   }   s   
 z*ManagerTimezone.__init__.<locals>.<lambda>)r6   �active_track_colorr7   �	on_changezAdd new rulec                    r+   r,   )�add_tiler/   r1   r   r   r3      r4   )rm   rC   r?   r5   )rR   �spacingr   )rD   rE   r   rF   r   rH   rI   r}   rp   rR   rG   rK   rk   �Row�Switch�
color_bankr   �ElevatedButtonrP   �ADD�init)r2   rH   rI   rU   rV   r1   r   rE   j   s2   

�
��
��zManagerTimezone.__init__N�keywordc                 C   sv   |d u r| j }td|�d|�d| j��� | jt| j� d t|� |  | jt| j� d t|� |< t| j� d S )Nz
keyword = z
, index = z, self.instance =r)   )rI   rp   rH   rF   r   r   )r2   r�   ro   r   r   r   ry   �   s    �zManagerTimezone.reverse_keywordc                 C   sr   t | j| j� | j| j d | j d D ]"}t |� t |� |d }|d }| j�t| j| j| ||dd�� qd S )Nr)   r*   r   r   F)r#   r$   rT   )rp   rH   rI   rF   rR   rG   r'   )r2   �tupr#   rJ   r   r   r   r�   �   s   "�zManagerTimezone.initTc                 C   s,   t � | _| j�t| j| j| �� | ��  d S r,   )r   rF   rR   rG   r'   rH   rI   r[   )r2   �refreshr   r   r   r|   �   s   zManagerTimezone.add_tilec                 C   s�   t � | _| j| j d | j d �| j| j d | j d �|j|jg�� tt	| j
��D ]}| j
| |kr>| j
�|�  nq-t| j� | ��  d S )Nr)   r*   )r   rF   rH   rI   �popro   r#   rJ   �ranger   rR   r   r[   )r2   �tilerq   r   r   r   r>   �   s   D�
zManagerTimezone.deleter,   )T)
rr   rs   rt   rE   r   ry   r�   r|   r>   ru   r   r   rV   r   rv   i   s    

rv   rX   c                 C   s<   t � }d| _d| _| �ttt�� dt� d�| _| ��  d S )Ni�  i�  u   Profile n°z configuration)	r   �window_width�window_height�addrv   �selrI   �titler[   )rX   rF   r   r   r   �main�   s   r�   �1c                 C   s   | a |atjtd� d S )N)�target)r�   rI   rK   �appr�   )Z	sel_paramZprofile_paramr   r   r   r#   �   s   r#   �__main__r)   r*   r   )r�   r�   )r   �randomr   �fletrK   �utils.Task_utilsr   r   r�   r   r   r%   r&   r~   r'   �ListViewrv   �Pager�   r#   rr   rF   �timesrp   �tr   r   r   r   �<module>   s2    �5@
	�