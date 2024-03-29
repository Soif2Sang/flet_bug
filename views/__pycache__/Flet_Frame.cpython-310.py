o
    �Ud<  �                   @   sj   d dl Zd dlmZ d dlmZ d dlmZmZ G dd� dej	�Z
G dd� dej�ZG d	d
� d
ej�ZdS )�    N)�Logger)�SettingContainer)�get_data�
write_datac                       s2   e Zd Z� fdd�Zdefdd�Zdd� Z�  ZS )�InterfaceSettingsc              	      s�   t � jdi |�� t� }d|vrddd�|d< t|� tjtjtjd|d d � fdd�d�gd	�tjtjd
|d d � fdd�d�gd	�tjtjd|d d � j	d�gd	�gd	�� _
d� _d S )N�	interfaceT)�auto_scrollZauto_refreshzLogger autoscrollr   c                    �
   � � d�S )Nr   ��reverse_keyword��_��self� �cC:\Users\Administrator\Documents\Projets\Rise of kingdom\Bluestacks Version\bot\views\Flet_Frame.py�<lambda>   �   
 z,InterfaceSettings.__init__.<locals>.<lambda>)�label�value�	on_change)�controlszEnable Discord Notifications�discord�enabledc                    r	   )Nr   r
   r   r   r   r   r      r   zYour discord ID�user_idzGeneral Settingsr   )�super�__init__r   r   �ft�Column�Row�Switch�	TextField�submit�content�text)r   �page�kwargs�data��	__class__r   r   r   	   s   (("��
zInterfaceSettings.__init__�keywordc                 C   s�   |dkr5t � }|d |  |d |< t|� |dkr3| jjD ]}|d | | jj| j_q| ��  d S d S t � }|d |  |d |< t|� d S )Nr   r   r   )r   r   r%   �frames�loggerr   �update)r   r*   r'   �framer   r   r   r      s   �z!InterfaceSettings.reverse_keywordc                 C   s"   t � }|jj|d d< t|� d S )Nr   r   )r   �controlr   r   )r   �er'   r   r   r   r"   )   s   zInterfaceSettings.submit)�__name__�
__module__�__qualname__r   �strr   r"   �__classcell__r   r   r(   r   r      s    r   c                       �0   e Zd Zdef� fdd�Zdefdd�Z�  ZS )�Frame�numberc                    sF  t � jdi |�� || _t�� | _d| _d| _t| |�| _	| j
�tj| jdd�� | j
�tj| j	dd�� | j
�t|�� | jj
�tjt|| t|�d�dd�� | jj
�tjt|| t|�d�d	d�� | jj
�tjt|| t|�d
�dd�� t� }|t|� d D ]}t| jj� |t|� d | d r�t|�d | j_ d S q�d S �NTi�  ZSettings)r#   r$   r   �   z	Profile 1�   z	Profile 2�   z	Profile 3�	schedulesr   r   )r   r   r8   r   �Tabs�settings�expand�widthr   r,   �tabs�append�Tabr   r   �intr   r4   �print�selected_index�r   r%   r8   r&   r'   Zprofiler(   r   r   r   /   s(   
&&&��zFrame.__init__�textec                 C   �   | j �|� d S �N�r,   �add_text�r   rI   r   r   r   rM   C   �   zFrame.add_text�r1   r2   r3   r4   r   rM   r5   r   r   r(   r   r7   .   s    r7   c                       r6   )�FrameUpgrader8   c                    sJ  t � jdi |�� || _|| _t�� | _d| _d| _| jj	| _	| j
�tj| jdd�� | j
�tj| j	dd�� | j
�t|�� | jj
�tjt|| t|�d�dd�� | jj
�tjt|| t|�d�d	d�� | jj
�tjt|| t|�d
�dd�� t� }|t|� d D ]}t| jj� |t|� d | d r�t|�d | j_ d S q�d S r9   )r   r   r%   r8   r   r>   r?   r@   rA   r,   rB   rC   rD   r   r   rE   r   r4   rF   rG   rH   r(   r   r   r   I   s*   

&&&��zFrameUpgrade.__init__rI   c                 C   rJ   rK   rL   rN   r   r   r   rM   ^   rO   zFrameUpgrade.add_textrP   r   r   r(   r   rQ   H   s    rQ   )�fletr   Zviews.Flet_Loggerr   Zviews.Flet_Settingr   �utils.Task_utilsr   r   rD   r   r>   r7   rQ   r   r   r   r   �<module>   s    &