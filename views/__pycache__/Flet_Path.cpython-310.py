o
    �Ud�  �                   @   s�   d dl Z d dlZd dlZd dlZd dlmZ dd� Zdd� Zd dlZ	G dd� de	j
�Zd	e	jfd
d�Zedkr?e	jed� dS dS )�    N)�get_pathc                 C   sH   t �| �D ]\}}}|D ]}|�|�}|r t j�||�    S qqd S �N)�os�walk�search�path�join)Zroot_folder�rex�root�dirs�files�f�result� r   �bC:\Users\Administrator\Documents\Projets\Rise of kingdom\Bluestacks Version\bot\views\Flet_Path.py�	find_file	   s   
���r   c                 C   s@   t �| �}t�� �d�d d� D ]}t||� }r|  S qd S )N� �����)�re�compile�win32api�GetLogicalDriveStrings�splitr   )�	file_namer	   �driver   r   r   r   �find_file_in_all_drives   s   
��r   c                       sL   e Zd Z� fdd�Zdd� Zejjfdd�Zdej	fdd	�Z
d
d� Z�  ZS )�	RowFinderc                    s�   t � jdi |�� t� �_|�_�j�d�d �_tjd�j� d�d��_	tj
�j�j�d�d  dd��_tj�jd�� �j�� � tjd	� fd
d�d��_tjd�fdd�d��_�j��j	�j�j�jg� d S )N�\r   zSet z file location��valuei�  )r   �width)�	on_resultzSet file manually...c                    s   � j dd�S )NF)�allow_multiple)�
pick_files)�_)�file_pickerr   r   �<lambda>'   s    z$RowFinder.__init__.<locals>.<lambda>��on_clickzLet the script find it..c                    s
   � � | �S r   )�find��e)�selfr   r   r&   )   s   
 )�textr(   r   )�super�__init__r   �	path_json�motr   Zenhanced_mot�ft�Textr-   �	TextField�entry�
FilePicker�on_dialog_result�controls�append�ElevatedButton�choice�script�extend)r,   r1   �kwargs��	__class__)r%   r,   r   r/      s(   "
�
�
�zRowFinder.__init__c                 C   s   d| j j_| j ��  d S )NF)�page�banner�open�update�r,   r+   r   r   r   �close_banner1   s   
zRowFinder.close_bannerc                 C   sd   t j|t j|d�t jd| jd�gdd�| j_|t jjkr+t j	t j
jt jjdd�| jj_| j��  d S )Nr   �Okr'   T)�bgcolor�content�actionsrC   �(   )�color�size)r2   �Bannerr3   �
TextButtonrF   rA   rB   �colors�	AMBER_100�Icon�icons�WARNING_AMBER_ROUNDED�AMBER�leadingrD   )r,   r-   rL   r   r   r   �
pop_banner5   s   ��
�
zRowFinder.pop_bannerr+   c                 C   s`   t d|jd j� t d|j� |jd j| j| j�d�d < t� | _|jd j| j_| �	�  d S )N�Selected files:r   �Selected file or directory:r   )
�printr   r   r0   r1   r   r   r5   r   rD   rE   r   r   r   r7   E   s   zRowFinder.on_dialog_resultc                 C   s�   t | j� }rB|| j| j�d�d < tdddd��}tj| j|dd� W d   � n1 s-w   Y  || j_| �	d	d
� | �
�  d S | �	d� td� d S )Nr   r   z../path.json�wzUTF-8)�encoding�   )�indent�Success�greenzUnable to locate the file)r   r1   r0   r   rC   �json�dumpr5   r   rW   rD   rZ   )r,   r+   r   r   r   r   r   r)   N   s   �
zRowFinder.find)�__name__�
__module__�__qualname__r/   rF   r2   rP   rQ   rW   �FilePickerResultEventr7   r)   �__classcell__r   r   r?   r   r      s    	r   rA   c                 C   sD   d| _ d| _dtjfdd�}| �td�� | �td�� | ��  d S )N��   i�  r+   c                 S   s   t d| j� t d| j� d S )NrX   rY   )rZ   r   r   r*   r   r   r   r7   ]   s   zmain.<locals>.on_dialog_resultzbluestacks\.confzHD-Player\.exe)�window_height�window_widthr2   rf   �addr   rD   )rA   r7   r   r   r   �mainZ   s   rl   �__main__)�target)ra   r   r   r   �utils.Task_utilsr   r   r   �fletr2   �Rowr   �Pagerl   rc   �appr   r   r   r   �<module>   s    	>�