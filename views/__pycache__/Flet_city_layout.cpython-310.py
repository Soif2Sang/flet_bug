o
    �Ud_  �                   @   sP   d dl Z d dlZd dlmZmZ dejfdd�Zd
dd�Ze	d	kr&e�  dS dS )�    N)�get_data�
write_data�pagec                    s�  t � �d�_d�_d �_ddddddd	d
�� dtf� �fdd���fdd����fdd��dtjf���fdd�}tjtjj	dddddd�}tj
ddd|tjddd�d�}t�� �_t�� �_tj�j�jgd��_tj||gddd�g�j_���j� �jj�tjd�fdd�d �tjd!�fd"d�d �tjd#�fd$d�d �tjd%�fd&d�d �tjd'�fd(d�d �tjd)�fd*d�d �tjd+�fd,d�d �g� ���  d S )-Ni>  i�  r   �   �   �   �   �   �   )�infantry_camp�cavalry_camp�archery_camp�
siege_camp�hospital�
scout_camp�city_transfer�paramc                    s8   | �_ �jjD ]}d|_qd�jj� |   _���  d S )N�blue�red)�current_build�column2�controls�color�update)r   �element)�buttonsr   � �iC:\Users\Administrator\Documents\Projets\Rise of kingdom\Bluestacks Version\bot\views\Flet_city_layout.py�setCurrentBuild   s
   zmain.<locals>.setCurrentBuildc                    s   d� j _� ��  d S )NF)�banner�openr   ��e)r   r   r   �close_banner   s   zmain.<locals>.close_bannerc                    sN   t jt jjt jt jjt jjdd�t j| d�t j	d� d�gdd��_
���  d S )N�(   )r   �size)�value�Ok)�on_clickT)�bgcolor�leading�content�actionsr    )�ft�Banner�colors�	AMBER_100�Icon�icons�WARNING_AMBER_ROUNDED�AMBER�Text�
TextButtonr   r   )�text)r#   r   r   r   �
pop_banner#   s   ���zmain.<locals>.pop_bannerr"   c              
      s�   t | jd | jd � z3t � tt� d tt� � t| jd �t| jd �f� tt� d tt� �j< ��j� d�� W n tyU }  zt	�
�  W Y d } ~ d S d } ~ ww t� � d S )Nr   �	schedulesz successfully set)�print�local_x�local_y�str�sel�profile�intr   �	Exception�	traceback�	print_excr   r!   )�datar   r8   r   r   �on_tap_update1   s   6��zmain.<locals>.on_tap_updatezcity.pngg     �v@g      �@)r)   �left�top�	image_src�height�width�
   )rJ   rI   )�drag_intervalrG   rF   �on_tap_downr+   )r   zSet Infantry campc                    �   � d�S )Nr   r   ��_�r   r   r   �<lambda>N   �    zmain.<locals>.<lambda>)r7   r(   zSet Cavalry campc                    rN   )Nr   r   rO   rQ   r   r   rR   O   rS   zSet Archer campc                    rN   )Nr   r   rO   rQ   r   r   rR   P   rS   zSet Siege campc                    rN   )Nr   r   rO   rQ   r   r   rR   Q   rS   zSet Hospitalc                    rN   )Nr   r   rO   rQ   r   r   rR   R   rS   zSet Scout campc                    rN   )Nr   r   rO   rQ   r   r   rR   S   rS   zSet City to transferc                    rN   )Nr   r   rO   rQ   r   r   rR   T   rS   )r   �window_width�window_heightr   r=   r-   �ControlEvent�	Containerr/   �RED�GestureDetector�ColumnZcolumn1r   �Row�row�Stackr   �add�extend�ElevatedButtonr   )r   rE   �cZgd1r   )r   r#   rD   r   r8   r   r   �main	   sN   �	�

�rb   �1c                 C   s   | a |atjtd� d S )N)�target)r>   r?   r-   �apprb   )�	sel_param�profile_paramr   r   r   �startZ   s   rh   �__main__)rc   rc   )
rB   �fletr-   �utils.Task_utilsr   r   �Pagerb   rh   �__name__r   r   r   r   �<module>   s    
Q
�