o
    �Ud�  �                   @   s.   d dl Zd dlmZmZ G dd� dej�ZdS )�    N)�get_data�
write_datac                       s$   e Zd Z� fdd�Zdd� Z�  ZS )�FletRowPresetsc                    sz   t � ��  t� � _|� _|� _|� _tj�	d�� _
tjd|� �� fdd�� jt� j� d t� j� d | d�g� _d S )N�
   zPreset c                    s
   � � | �S )N)�submit)�e��self� �iC:\Users\Administrator\Documents\Projets\Rise of kingdom\Bluestacks Version\bot\views\Flet_row_presets.py�<lambda>   s   
 z)FletRowPresets.__init__.<locals>.<lambda>�	schedules�barbarians_preset)�label�	on_change�value)�super�__init__r   �data�instance_index�profile_index�preset_index�ft�padding�all�content_padding�Checkbox�str�controls)r	   r   r   r   ��	__class__r   r   r      s   

$�
�zFletRowPresets.__init__c                 C   sF   t � | _t|jj�| jt| j� d t| j� d | j< t	| j� d S )Nr   r   )
r   r   �bool�controlr   r   r   r   r   r   )r	   r   r
   r
   r   r      s   0zFletRowPresets.submit)�__name__�
__module__�__qualname__r   r   �__classcell__r
   r
   r   r   r      s    r   )�fletr   �utils.Task_utilsr   r   �Rowr   r
   r
   r
   r   �<module>   s    