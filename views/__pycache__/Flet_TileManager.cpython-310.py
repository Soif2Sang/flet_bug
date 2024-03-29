o
    �aUd�+  �                   @   s�   d dl Z d dlZd dlmZ d dlmZ d dlZd dlZd dl	m
Z
mZ d dlmZ d dlmZmZmZmZ G dd� dej�ZG d	d
� d
ej�ZdS )�    N)�exists)�sleep)�ButtonStyle�RoundedRectangleBorder)�Tile)�get_path�get_data�
write_data�get_default_configc                       s   e Zd Z� fdd�Z�  ZS )�NavigationBarc              	      s^   t � jdi |�� |� _tjdtjj� fdd�ttjj	t
dd�id�d�� _� j�� j� d S )	NZRefreshc                    s
   � j �� S �N)�tileManager�refresh)�_��self� �iC:\Users\Administrator\Documents\Projets\Rise of kingdom\Bluestacks Version\bot\views\Flet_TileManager.py�<lambda>   s   
 z(NavigationBar.__init__.<locals>.<lambda>�   )�radius)�shape)�text�icon�on_click�styler   )�super�__init__r   �ft�OutlinedButton�icons�REFRESH_ROUNDEDr   �MaterialState�DEFAULTr   Zbutton_refresh�controls�append)r   �tile_manager�kwargs��	__class__r   r   r      s   ��zNavigationBar.__init__)�__name__�
__module__�__qualname__r   �__classcell__r   r   r(   r   r      s    r   c                       s�   e Zd Z� fdd�Zdefdd�Zdefdd�Zdd	� Zded
efdd�Zdd� Z	dd� Z
dd� Zdd� Zdd� Zdd� Zdd� Z�  ZS )�TileManagerc                    sF   t � jdi |�� || _d| _d| _i | _t| �| _| j�	| j� d S )N��   r   r   )
r   r   �page�height�expand�tilesr   �navigation_barr$   r%   )r   r0   r'   r(   r   r   r      s   
zTileManager.__init__�numberc                 C   s(   t | j|�| j|< | j�| j| � d S r   )r   r0   r3   r$   r%   )r   r5   r   r   r   �add_tile$   s   zTileManager.add_tilec                 C   s2   | j �| j| �}| j �|� | j|= | ��  d S r   )r$   �indexr3   �pop�update)r   r5   r7   r   r   r   �delete_tile)   s   zTileManager.delete_tilec              	   C   s:   | j dd � D ]}zd|j_W |j��  q|j��  w d S )N�   F)r$   Zbutton_select�selectedr9   �r   �tiler   r   r   �unselect_all/   s
   
�zTileManager.unselect_all�phrasec                 C   s   | j | �|� d S r   )r3   �set_text)r   r5   r@   r   r   r   �
set_status6   s   zTileManager.set_statusc                 C   sd   	 | j �� D ]&}|j�� s,d|_d|_tjj|j	_
d|j_|j	��  |j��  |�d� qtd� q)Nr;   FT� )r3   �valuesZtasks_process�is_alive�started�stoppedr   r    �NOT_STARTED_OUTLINEDZbutton_startr   Zbutton_stop�disabledr9   rA   r   r=   r   r   r   �process_is_alive9   s   



��zTileManager.process_is_alivec                 C   s    t j| jd�}d|_|��  d S )N)�targetT)�	threading�ThreadrJ   Zdeamon�start)r   rE   r   r   r   �update_tilesF   s   zTileManager.update_tilesc                 C   st  zIt � }|d d d� d }t|d � �r)|d d d� d }t�|d � |� � t|� ddd��}|�� �d�}W d   � n1 sCw   Y  W n   td��d	d
� }g }|D ]}d|v rgd|v rgd|v sod|v rtd|v rt|�|� qYg }t	dt
|�d�D ]6}	||	d  �d�}|d �d�d }
|d �dd�}||	 �d�d �dd�}t|
�||d�}|�|� q||�S )N�
bluestacks�����z.txt�rzutf-8)�encoding�
zwThe path you provided is wrong ! We are looking for something like : 
 r'C:\ProgramData\BlueStacks_nxt\bluestacks.conf'c                 S   s�   t t| ��D ]b}t t| �d �D ]W}t| | d �t| |d  d �krD| | d | |d  d krC| |d  | | | |< | |d < qt| | d �t| |d  d �krg| |d  | | | |< | |d < qqi }t t| ��D ]
}| | |t|�< qq|S )Nr;   �instance)�range�len�str)�tab�i�yZdicr   r   r   �sort_by_instanceX   s   $"�$"��z7TileManager.get_dic_instances.<locals>.sort_by_instancezbst.instance.Nougat64Zadb_port�status�display_namer   �   r;   z.status.adb_port=�.������"rC   z.display_name=)rU   �port�name)r   r   �shutil�copy�open�read�split�OSErrorr%   rV   rW   �replacerX   )r   �path�string�fileZdata_instancer\   Z
liste_info�elementZtab_instancerZ   rU   rc   r^   Zdico_instancer   r   r   �get_dic_instancesK   sD   ���
��zTileManager.get_dic_instancesc                 C   sF   g }|� � D ]}|| D ]}|dkr|�t|�|| | f� qq|S )Nrd   )�keysr%   rW   )r   �data�names�keyro   r   r   r   �	get_names}   s   ��zTileManager.get_namesc                 C   sR   | � |�}g }t�� D ]}|D ]}|j|d kr|�|� qq|jdd� d� |S )Nr;   c                 S   s   | d S )Nr   r   )�xr   r   r   r   �   s    z3TileManager.get_current_instances.<locals>.<lambda>)rt   )ru   �	pyautogui�getAllWindows�titler%   �sort)r   rr   rs   Zinstances_available�winrd   r   r   r   �get_current_instances�   s   

��z!TileManager.get_current_instancesc                 C   s   | � | �� �S r   )r|   rp   r   r   r   r   �get_all_vms_running�   s   zTileManager.get_all_vms_runningc           	      C   s(  t � }t� }| �� }ddddddddddi d�}i d	g �d
d�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�i d d�d!d�d"d#�d$d#�d%d�d&d�d'd�d(d�d)d�d*d�d+d�d,d�d-d�d.d�d/d0�d1dddddddd2��d3d��i d4d�d5d6�d7d�d8d�d9d:�d;d�d<d�d=d�d>d�d?d�d@d:�dAd�dBdC�dDd�dEd�dFdG�dHd��i dId�dJd�dKd�dLdM�dNdG�dOdP�dQdR�dSd�dTd�dUdV�dWdX�dYdZ�d[d�d\d]�d^d]�d_d]�d`d]��i dad]�dbd�dcd�ddg �deg �dfg �dgg �dhg �dig �djd�dkd�dld�dmd�dndo�dpdo�dqdo�drdo��g dddddds��}tdCd#�D ]	}||dt |< �q7|D ]�}t|�|v�rWtdu� ||t|�< nG|D ]}||t|� v�rn|| |t|� |< �qY|D ]+}tdCd#�D ]"}||t|� dt t|� v�r�|| |t|� dt t|� |< �qy�qr|t|� dv |t|� dv< |t|� dw |t|� dw< t|t|� dx �|t|� dx< �qCt|� | �� }tt	| j
�dC �D ]}| j
��  �q�|D ]%}t|d �| jv �r| j
�| jt|d � � �q�| �t|d �� �q�| ��  d S )yNrC   z	127.0.0.1r   F�<   �n   T)rU   rd   �hostrc   ZAPI_KEYZ	loop_taskZtime_to_wait_loop1Ztime_to_wait_loop2Zleave_game_loopZ	scheduler�	schedulesZtimingZenable_timing�enabledZkingdomZcity_xZcity_yr   �   ZFirst�stoneZSecondZfoodZThird�goldZFourthZwoodZFifthZSixthZSeventhZFirst_levelr   ZSecond_levelZThird_levelZFourth_levelZFifth_levelZSixth_level�   ZSeventh_levelZrss_custom_presetZauto_reconnectZauto_captchaZcheck_donationZuse_enhanced_buffZ
gather_rssZbuy_merchantZclaim_daily_questsZcollect_ressourceZdefeat_barbariansZbarbarians_level�   Zbarbarians_preset)�1�2�3�4�5�6�7Z
gather_gemZ
gem_check1Z
gem_check2�x   Zgem_experimentalZgather_gem_duration1Zgather_gem_duration2�Z   Zrestart_gameZswitch_characterZleave_game_switch_characterZ	scout_fogZscout_duration1Zscout_duration2Z	slow_modeZsleep_multiplicatorr;   Zauto_log_backZ	log_back1Z	log_back2�
   Zclaim_daily_vipZclaim_daily_chestZclaim_campaignZ
start_fortZ
rally_typeZcavZ
rally_timeZrally_radius�   Zrally_countr_   Zmauraudeurs_fortsZ
heal_troopZhealing_building_xi�  Zhealing_building_yi  Zhealing_counti�  Zmaterial_productionZmaterial_choice_1ZleatherZmaterial_choice_2Zmaterial_choice_3Zmaterial_choice_4Zmaterial_choice_5Zalliance_helpZtrain_troopsZinfantry_campZcavalry_campZarchery_campZ
siege_campZhospitalZ
scout_campZinfantry_enableZcavalry_enableZarchery_enableZsiege_enableZinfantry_tier�t1Zcavalry_tierZarchery_tierZ
siege_tier)Zcity_transferZtransfer_enableZtransfer_foodZtransfer_woodZtransfer_stoneZtransfer_goldr�   zDefault config set !rU   rd   rc   )r   r
   rp   rV   rX   �print�intr	   r}   rW   r$   r8   r3   r%   r6   r9   )	r   rr   Zdefault_configZ	instancesZdefault_dicZdefault_profilerZ   rU   rt   r   r   r   r   �   s�  ���������	�
���������������������� �!��)�*�+�,�-�.�/�0�1�2�3�4�5�6�7�8�9�:�;�<�=�>�?�@�A�B�C�D�E�F�G�H�I�J�K�L�M�N�O�P�Q�R�S�T�U�V�W�X�Y�Z�[�\�]�d� ��$zTileManager.refresh)r*   r+   r,   r   rX   r6   r:   r?   rB   rJ   rO   rp   ru   r|   r}   r   r-   r   r   r(   r   r.      s    	2r.   )re   rL   �os.pathr   �timer   �fletr   rw   Z	flet_corer   r   Zviews.Flet_Tiler   �utils.Task_utilsr   r   r	   r
   �Rowr   �ListViewr.   r   r   r   r   �<module>   s    