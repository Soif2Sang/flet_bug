o
    �Ud�  �                   @   s.   d dl Zd dlmZmZ G dd� dej�ZdS )�    N)�get_data�
write_datac                       s$   e Zd Z� fdd�Zdd� Z�  ZS )�FletRowMaterialc                    s�   t � ��  t� �_|�_|�_tjdt�|� d  � d��tj	j
d�tjdddtj�d�tj�d	�tj�d
�tj�d�g�jt�j� d t�j� d� � � � �fdd�d�g�_d S )N�d   �   z	 choice :)�width�content�	alignment�   �F   �Type�leather�stoneZebonyZbones�	schedules�material_choice_c                    s   �� | d� � �t�S )Nr   )�submit�str)�e��i�self� �jC:\Users\Administrator\Documents\Projets\Rise of kingdom\Bluestacks Version\bot\views\Flet_row_material.py�<lambda>   s    z*FletRowMaterial.__init__.<locals>.<lambda>)r   �height�label�options�value�	on_change)�super�__init__r   �data�instance_index�profile_index�ft�	Container�Textr	   �center_right�Dropdown�dropdown�Optionr   �controls)r   �keysr   r"   r#   ��	__class__r   r   r       s0   
�



���
�zFletRowMaterial.__init__c                 C   s�   t � | _|dv r)||jj�| jt| j� |< t| jt| j� | � t| j� d S |dvrC||jj�| jt| j� d t| j� |< nt	|jj�
dd��
dd��| jt| j� d t| j� |< t| j� d S )N)�time_to_wait_loop2�time_to_wait_loop1�API_KEY)�sleep_multiplicator�defeat_barbariansr   �x� zlevel )r   r!   �controlr   r   r"   �printr   r#   �float�replace)r   r   �keyword�methodr   r   r   r   #   s   
,:zFletRowMaterial.submit)�__name__�
__module__�__qualname__r    r   �__classcell__r   r   r-   r   r      s    r   )�fletr$   �utils.Task_utilsr   r   �Rowr   r   r   r   r   �<module>   s    