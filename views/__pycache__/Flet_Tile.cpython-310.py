o
    �Ud�  �                   @   sV   d dl Z d dlmZ d dlmZ d dlZd dlmZ d dl	m
Z
 G dd� dej�ZdS )�    N)�Frame)�Task)�
TaskRunner)�get_datac                       sj   e Zd Z� fdd�Zdd� Zdd� Zdd� Zd	d
� Zdd� Zde	fdd�Z
dd� Zdde	fdd�Z�  ZS )�Tilec                    s
  t � jdi |�� t� }|� _|� _d� _d� _d � _t� �� _	t
� j	� �� _tj� jjd�� _tjtjjtjj� fdd�d�� _tjtjj� fdd�d�� _tjtjjd� fd	d�d
�� _tj|t|� d dd�� _tjdd�� _� j�� j� j� j� j� jg� d S )NF��targetc                    �   � � � S �N)�select��_��self� �bC:\Users\Administrator\Documents\Projets\Rise of kingdom\Bluestacks Version\bot\views\Flet_Tile.py�<lambda>   �    zTile.__init__.<locals>.<lambda>)�icon�selected_icon�on_clickc                    r	   r
   )�startr   r   r   r   r   "   r   )r   r   Tc                    r	   r
   )�stopr   r   r   r   r   '   r   )r   �disabledr   �name�F   )�value�width� )r   r   )�super�__init__r   �page�number�started�stopped�tasks_processr   Z	main_taskr   �runner�	threading�Thread�run�ft�
IconButton�icons�PAGEVIEW�REMOVE_RED_EYE_OUTLINED�button_select�NOT_STARTED_OUTLINED�button_start�STOP_OUTLINED�button_stop�Text�strZ	text_name�text_status�controls�extend)r   r!   r"   �kwargs�data��	__class__r   r   r       sB   

�
�
�
�zTile.__init__c                 C   sz   | j j��  d| j_t| j j�dkr| j j��  | j| j j	vr+t
| j | j�| j j	| j< | j �| j j	| j � | j ��  d S )NT�   )r!   �tile_manager�unselect_allr/   �selected�lenr7   �popr"   �framesr   �add�updater   r   r   r   r   5   s   zTile.selectc                 C   s`   | j  | _ d| _| j rtjj| j_d| j_n
tjj	| j_d| j_| �
�  | j��  | j��  d S )NF)r#   r$   r*   r,   �PAUSEr1   r   r3   r   r0   �start_tasksrE   r   r   r   r   r   A   s   


z
Tile.startc                 C   sL   | j ��  d| _d| _tjj| j_d| j	_
| j��  | j	��  | �d� d S �NFTr   )r%   �joinr#   r$   r*   r,   r0   r1   r   r3   r   rE   �set_textr   r   r   r   �process_is_aliveN   s   


zTile.process_is_alivec                 C   s>   | j �� stj| jjd�| _ d| j _| j ��  d S td� d S )Nr   TzTask is running)	r%   �is_aliver'   r(   r&   r)   �daemonr   �printr   r   r   r   rG   X   s
   
zTile.start_tasksc                 C   sB   d| _ d| _tjj| j_d| j_| �	d� | j�
�  | j�
�  d S rH   )r#   r$   r*   r,   r0   r1   r   r3   r   rJ   rE   r   r   r   r   r   e   s   

z	Tile.stop�phrasec                 C   s   || j _| j ��  d S r
   )r6   r   rE   )r   rO   r   r   r   rJ   n   s   zTile.set_textc                 C   s   | j jS r
   )r6   r   r   r   r   r   �get_textr   s   zTile.get_textNc                 C   sB   | j | jjvrt| j| j �| jj| j < | jj| j  j�||� d S r
   )r"   r!   rC   r   �logger�add_text)r   rO   �colorr   r   r   rR   u   s   zTile.add_textr
   )�__name__�
__module__�__qualname__r    r   r   rK   rG   r   r5   rJ   rP   rR   �__classcell__r   r   r;   r   r      s    )
	r   )r'   Zviews.Flet_Framer   Z
tasks.Taskr   �fletr*   Ztasks.Task_runnerr   �utils.Task_utilsr   �Rowr   r   r   r   r   �<module>   s    