o
    �Ud  �                   @   sH   d dl Zd dlmZmZ G dd� dej�Zdd� ZG dd� dej�ZdS )	�    N)�get_data�
write_datac                       �,   e Zd Z� fdd�Zddefdd�Z�  ZS )�Loggerc                    sT   t � jdi |�� t� }d|vrddd�|d< t|� |d d | _|| _|| _d S )N�	interfaceT��auto_scroll�auto_refreshr   � )�super�__init__r   r   r   �parent�page)�self�framer   �kwargs�data��	__class__r
   �dC:\Users\Administrator\Documents\Projets\Rise of kingdom\Bluestacks Version\bot\views\Flet_Logger.pyr      s   
zLogger.__init__N�textec                 C   s^   |d u rt j|t jjd�}n
t j|t jj|d�}| j�|� | j| jjd kr-| ��  d S d S �N)�value�weight)r   r   �color�����)	�ft�Text�
FontWeight�W_600�controls�appendr   r   �update�r   r   r   �textr
   r
   r   �add_text   s   �zLogger.add_text�N��__name__�
__module__�__qualname__r   �strr%   �__classcell__r
   r
   r   r   r      s    
r   c                   C   s   d S r&   r
   r
   r
   r
   r   �get_date   s   r-   c                       r   )�LoggerUpgradec                    sF   t � jdi |�� t� }d|vrddd�|d< t|� d| _|| _d S )Nr   Tr   r
   )r   r   r   r   r   r   )r   r   r   r   r   r
   r   r       s   
zLoggerUpgrade.__init__Nr   c                 C   s`   |d u rt j|t jjd�}n
t j|t jj|d�}| j�|� t| jjd t j�s.| �	�  d S d S r   )
r   r   r   r   r    r!   �
isinstancer   �Dividerr"   r#   r
   r
   r   r%   )   s   �zLoggerUpgrade.add_textr&   r'   r
   r
   r   r   r.      s    	r.   )	�fletr   �utils.Task_utilsr   r   �ListViewr   r-   r.   r
   r
   r
   r   �<module>   s
    