o
    Ud�  �                   @   s.   d dl Zd dlmZmZ G dd� dej�ZdS )�    N)�get_data�
write_datac                       s$   e Zd Z� fdd�Zdd� Z�  ZS )�FletColumnRssc              
      s   t � ��  t� � _|� _|� _tjd� jt� j� d t� j� d � fdd�tj	�
d�d�tjd� jt� j� d t� j� d	 � fd
d�tj	�
d�d�tjd� jt� j� d t� j� d � fdd�tj	�
d�d�tjd� jt� j� d t� j� d � fdd�tj	�
d�d�g� _d S )NzMillion of Food to transfer :�	schedules�transfer_foodc                    �   � � | dt�S )Nr   ��submit�int��e��self� �jC:\Users\Administrator\Documents\Projets\Rise of kingdom\Bluestacks Version\bot\views\Flet_col_transfer.py�<lambda>   �    z(FletColumnRss.__init__.<locals>.<lambda>�
   )�label�value�	on_change�content_paddingzMillion of Wood to transfer :�transfer_woodc                    r   )Nr   r   r   r   r   r   r      r   zMillion of Stone to transfer :�transfer_stonec                    r   )Nr   r   r   r   r   r   r      r   zMillion of Gold to transfer :�transfer_goldc                    r   )Nr   r   r   r   r   r   r      r   )�super�__init__r   �data�instance_index�profile_index�ft�	TextField�str�padding�all�controls)r   r   r   ��	__class__r   r   r      s*   
 � � � �
�zFletColumnRss.__init__c                 C   sP   t � | _|jjdkr||jj�nd| jt| j� d t| j� |< t| j� d S )N� r   r   )r   r   �controlr   r"   r   r   r   )r   r   �keyword�methodr   r   r   r	       s   :zFletColumnRss.submit)�__name__�
__module__�__qualname__r   r	   �__classcell__r   r   r&   r   r      s    r   )�fletr    �utils.Task_utilsr   r   �Columnr   r   r   r   r   �<module>   s    