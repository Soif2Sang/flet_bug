o
    �Vd�  �                   @   s.   d dl Zd dlmZmZ G dd� dej�ZdS )�    N)�get_data�
write_datac                       s$   e Zd Z� fdd�Zdd� Z�  ZS )�
FletRowRssc                    sR  t � ��  t� �_|�_|�_tjdt�� � d��tj	j
d�tjdddtj�d�tj�d�tj�d	�tj�d
�tj�d�g�jt�j� d t�j� � �  � �fdd�d�tjdddtj�d�tj�d�tj�d�tj�d�tj�d�tj�d�tj�d�tj�d�tj�d�g	�jt�j� d t�j� � � d� � �fdd�d�g�_d S )N�d   z	 choice :)�width�content�	alignment�   �F   z	Node Type�food�wood�stone�gold�nothing�	schedulesc                    s   �� | � � t�S )N)�submit�str��e��key�self� �eC:\Users\Administrator\Documents\Projets\Rise of kingdom\Bluestacks Version\bot\views\Flet_row_rss.py�<lambda>   s    z%FletRowRss.__init__.<locals>.<lambda>)r   �height�label�options�value�	on_changez
Node Level�1�2�3�4�5�6�7�8�9�_levelc                    s   �� | � � d�t�S )Nr)   )r   �intr   r   r   r   r   3   s    )�super�__init__r   �data�instance_index�profile_index�ft�	Container�Textr   �center_right�Dropdown�dropdown�Optionr   �controls)r   r   r.   r/   ��	__class__r   r   r,      sT   
�




�"�








���
�zFletRowRss.__init__c                 C   s�   t � | _|dv r)||jj�| jt| j� |< t| jt| j� | � t| j� d S |dvrC||jj�| jt| j� d t| j� |< nt	|jj�
dd��
dd��| jt| j� d t| j� |< t| j� d S )N)�time_to_wait_loop2�time_to_wait_loop1�API_KEY)�sleep_multiplicator�defeat_barbariansr   �x� zlevel )r   r-   �controlr   r   r.   �printr   r/   �float�replace)r   r   �keyword�methodr   r   r   r   7   s   
,:zFletRowRss.submit)�__name__�
__module__�__qualname__r,   r   �__classcell__r   r   r8   r   r      s    0r   )�fletr0   �utils.Task_utilsr   r   �Rowr   r   r   r   r   �<module>   s    