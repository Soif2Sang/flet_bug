o
    (%UdV�  �                   @   s�   d dl Z d dlZd dlmZmZ d dlZd dlmZ d dl	m
Z
 d dlmZ d dlmZ d dlmZ d dlmZ d d	lmZ d d
lmZmZ dddd�ZG dd� dej�ZdS )�    N)�ButtonStyle�RoundedRectangleBorder)�Flet_time_allower)�FletRowMaterial)�FletRowPresets)�
FletRowRss)�FletColumnRss)�FletRowTraining)�start)�get_data�
write_data�#3b8ed0�#ba4543�#dec433)�   �   �   c                       s�   e Zd Zdedef� fdd�Zdd� Zdd� Zd	d
� Zdd� Zdd� Z	dd� Z
dd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd � Zd!d"� Zd#d$� Zd%d&� Zd4d(efd)d*�Zd(ed+efd,d-�Zd(ed+efd.d/�Zd0d1� Zd2d3� Z�  ZS )5�SettingContainer�instance_index�profile_indexc                    sX   t � ��  t� | _|| _|| _|| _|| _t| j | _	t
jdddddd�| _| ��  d S )N��  r   r   �,  r   )�height�expand�padding�width�spacing)�super�__init__r   �data�tabs�pager   r   �
color_bank�color_choice�ft�ListView�content�init)�selfr!   �tabr   r   ��	__class__� �eC:\Users\Administrator\Documents\Projets\Rise of kingdom\Bluestacks Version\bot\views\Flet_Setting.pyr      s   
zSettingContainer.__init__c                    s�  � � dd� j� � � dd� j� � �dd� � �dd� � �d	d
� � �dd� � � dd� j� � � dd� j� � �dd� � �dd� � �dd� � �dd� � �dd� � � dd� j� � � dd� j� � � dd � j� � � d!d"� j	� � � d#d$� j
� � jj�t�� � � �d%d&� � �d'd(� � ��  � � d)d*� j� � � d+d,� j� � � d-d.� j� � � d/d0� j� � jj�tjd1� jt� j� d2 � fd3d4�d5�� d S )6N�
gather_gemzGather gems�
gather_rssz
Gather rss�collect_ressourcezCollect city rss�use_enhanced_buffzUse enhanced buff�buy_merchantzBuy merchant�check_donationzAlliance donation�material_productionzMaterial Production�train_troopszTrain troops�claim_daily_vipzClaim VIP Chests�claim_daily_chestzClaim Daily Chests�claim_daily_questszClaim Daily Quests�claim_campaignzClaim Campaign Rewards�alliance_helpzAlliance Help�defeat_barbarianszHunt Barbarians�
start_fortzLaunch Barbarian Rally�	scout_fogz	Clear fog�
heal_troopzTroops healing�transfer_enablezRss Transfer�auto_reconnectzAuto reconnection�auto_captchazResolve captchas�switch_characterzCharacters switching�auto_log_backzLog back from other device�	loop_taskzRe-do Tasks�	schedulerZProfileszCustom API key:�API_KEYc                    �   � � | dt�S )NrF   ��submit�str��e�r(   r,   r-   �<lambda>D   �    z'SettingContainer.init.<locals>.<lambda>��label�value�	on_change)�create_advanced_switch�	page_gems�page_rss�create_normal_switch�page_materials�page_troops�
page_barbs�
page_rally�page_fog�	page_heal�page_transferr&   �controls�appendr$   �Divider�create_slow_mode�page_character�page_logback�	page_redo�page_profile�	TextFieldr   rJ   r   rM   r,   rM   r-   r'   %   s6   6zSettingContainer.initc                 C   s    | j ��  | ��  | j��  d S �N)r&   �cleanr'   r!   �updaterM   r,   r,   r-   �resetF   s   
zSettingContainer.resetc                 C   s�   t � | _|dv r'||jj�| jt| j� |< t| jt| j� | � t| j�S |dvrA||jj�| jt| j� d t| j� |< nt	|jj�
dd��
dd��| jt| j� d t| j� |< t| j� d S )N)�time_to_wait_loop2�time_to_wait_loop1rF   )�sleep_multiplicatorr;   �	schedules�x� zlevel )r   r   �controlrR   rJ   r   �printr   r   �float�replace)r(   rL   �keyword�methodr,   r,   r-   rI   K   s   
,:zSettingContainer.submitc                    sp  t � � _� ��  d� j_tjdddd�� _� jj�	tj
tjtjj� fdd�d�tjd	d
d�gd�� � jj�t�� tjdddd�t�� tjd� jt� j� d t� j� d dtj�d�� fdd�d�t�� tjd� jt� j� d t� j� d dtj�d�� fdd�d�t�� tjd� jt� j� d t� j� d dtj�d�� fdd�d�t�� tjd� jt� j� d t� j� d dtj�d�� fd d�d�t�� tj
t�d!�tjd"� jt� j� d t� j� d# d$tj�d�� fd%d�d�t�d&�tjd'� jt� j� d t� j� d( d)tj�d�� fd*d�d�gd�t�� tj
t�d+�tjd"� jt� j� d t� j� d, d$tj�d�� fd-d�d�t�d&�tjd'� jt� j� d t� j� d. d)tj�d�� fd/d�d�gd�tjd0� j� jt� j� d t� j� d1 �r�dnd2� fd3d�d4�tjd5� j� jt� j� d t� j� d6 �r�dnd2� fd7d�d4�g� � j��  d S )8NTr   r   r   �r   r   r   c                    �   � � � S rh   �rk   ��_rM   r,   r-   rN   b   �    z,SettingContainer.page_gems.<locals>.<lambda>��icon�on_click�Settings�   ��size�r_   z=*REQUIREMENT*
/!\ Pre-configure yellow-lineups with farmers !�   �red�rR   r�   �colorzYour kingdom :ro   �kingdomr   �
   c                    rG   )Nr�   rH   rK   rM   r,   r-   rN   q   rO   )rQ   rR   r   �content_paddingrS   zArea location X coordinates :�city_xc                    rG   )Nr�   �rI   �intrK   rM   r,   r-   rN   w   rO   zArea location Y coordinates :�city_yc                    rG   )Nr�   r�   rK   rM   r,   r-   rN   ~   rO   zScanning radius (km) :�radiusc                    rG   )Nr�   r�   rK   rM   r,   r-   rN   �   rO   zMining duration (mins)�Minimum�gather_gem_duration1�P   c                    rG   )Nr�   r�   rK   rM   r,   r-   rN   �   rO   �~�Maximum�gather_gem_duration2�Z   c                    rG   )Nr�   r�   rK   rM   r,   r-   rN   �   rO   zAvailable troop scan frequency�
gem_check1c                    rG   )Nr�   r�   rK   rM   r,   r-   rN   �   rO   �
gem_check2c                    rG   )Nr�   r�   rK   rM   r,   r-   rN   �   rO   zRestart the game randomly�restart_gameFc                    �
   � � d�S )Nr�   ��reverse_keywordr{   rM   r,   r-   rN   �   �   
 �rQ   �active_track_colorrR   rS   zExperimental feature�gem_experimentalc                    r�   )Nr�   r�   r{   rM   r,   r-   rN   �   r�   )r   r   ri   r    r   r$   r%   r&   r_   r`   �Row�
IconButton�icons�
ARROW_BACK�Text�extendra   rg   rJ   r   r   r   �all�Switchr#   r!   rj   rM   r,   rM   r-   rU   X   s�   
���� 

� 

� 

� 

��

��

����

��

���
�
�
�
��WzSettingContainer.page_gemsc                    s�   t � � _� ��  d� j_tjddtjjdd�d�� _	� j	j
�tjtjtjj� fdd�d	�tjd
dd�gd�� � j	j
�t�� � g d�}|D ]}� j	j
�t|� j� jd�� � j	j
�t�� � qF� j	j
�tjtjjd� fdd�d�� � ��  d S )NTr   r   r�   ��rightrx   c                    ry   rh   rz   r{   rM   r,   r-   rN   �   r}   z.SettingContainer.page_troops.<locals>.<lambda>r~   r�   r�   r�   )ZinfantryZcavalryZarcheryZsiege��keyr   r   �Set Scout camp positionc                    ry   rh   ��show_cords_pager{   rM   r,   r-   rN   �   r}   �r   �textr�   )r   r   ri   r    r   r$   r%   r   �onlyr&   r_   r`   r�   r�   r�   r�   r�   ra   r	   r   r   �OutlinedButton�GPS_FIXED_SHARPrj   �r(   �keysr�   r,   rM   r-   rY   �   s2   
�����
�zSettingContainer.page_troopsc              	      s  t � � _� ��  d� j_tjddtjjdd�d�� _	� j	j
�tjtjtjj� fdd�d	�tjd
dd�gd�� � j	j
�t�� � g d�}t � � _� j	j
�tjd� j� jt� j� d t� j� d rddnd� fdd�d�� |D ]}� j	j
�t|� j� jd�� qp� ��  d S )NTr   r   r�   r�   rx   c                    ry   rh   rz   r{   rM   r,   r-   rN   �   r}   z+SettingContainer.page_rss.<locals>.<lambda>r~   r�   r�   r�   ��First�Second�Third�Fourth�Fifth�Sixth�SeventhzUse Yellow presets as gatherersro   �rss_custom_presetFc                    r�   )Nr�   r�   r{   rM   r,   r-   rN     r�   r�   r�   )r   r   ri   r    r   r$   r%   r   r�   r&   r_   r`   r�   r�   r�   r�   r�   ra   r�   r#   rJ   r   r   r   rj   r�   r,   rM   r-   rV   �   sB   
�����	�
��	zSettingContainer.page_rssc                    s   t � � _� ��  tjddtjjdd�d�� _� jj�	tj
tjtjj� fdd�d�tjd	dd
�gd�t�� tj
t�d�tjd� jt� j� d t� j� d d� fdd�d�t�d�tjd� jt� j� d t� j� d d� fdd�d�gd�t�� tjtjjd� fdd�d�g� � ��  d S )Nr   r   r�   r�   rx   c                    ry   rh   rz   r{   rM   r,   r-   rN     r}   z+SettingContainer.page_fog.<locals>.<lambda>r~   r�   r�   r�   zScout duration (mins)r�   ro   �scout_duration1r�   c                    rG   )Nr�   r�   rK   rM   r,   r-   rN   &  rO   �rQ   rR   r   rS   r�   r�   �scout_duration2r�   c                    rG   )Nr�   r�   rK   rM   r,   r-   rN   -  rO   r�   c                    ry   rh   r�   r{   rM   r,   r-   rN   2  r}   r�   �r   r   ri   r$   r%   r   r�   r&   r_   r�   r�   r�   r�   r�   r�   ra   rg   rJ   r   r   r�   r�   rj   rM   r,   rM   r-   r\     sL   
���	�
��
���
��"zSettingContainer.page_fogc                 C   s<   | j jjt| j� jj�d� tj	t
| j| jfd��
�  d S )NZcity��target�args)r!   �tile_manager�tilesrJ   r   �runner�adbZsave_screen�multiprocessing�Processr
   r   rM   r,   r,   r-   r�   8  s   z SettingContainer.show_cords_pagec                    s�   t � � _� ��  tjddtjjdd�d�� _� jj�	tj
tjtjj� fdd�d�tjd	dd
�gd�t�� tjd� jt� j� d t� j� d d� fdd�d�t�� tjtjjd� fdd�d�g� � ��  d S )Nr   r   r�   r�   rx   c                    ry   rh   rz   r{   rM   r,   r-   rN   F  r}   z,SettingContainer.page_heal.<locals>.<lambda>r~   r�   r�   r�   zHeal batch :ro   �healing_countr   c                    rG   )Nr�   r�   rK   rM   r,   r-   rN   P  rO   r�   zSet Hospital positionc                    ry   rh   r�   r{   rM   r,   r-   rN   T  r}   r�   r�   rM   r,   rM   r-   r]   =  s4   
���	�
�
��zSettingContainer.page_healc              	      s�   t � � _d� j_tjddtjjdd�d�� _� jj	�
tjtjtjj� fdd�d	�tjd
dd�gd�� � jj	�
t�� � g d�}tdd�D ]}� jj	�
t||� j� jd�� qE� ��  d S )NTr   r   r�   r�   rx   c                    ry   rh   rz   r{   rM   r,   r-   rN   c  r}   z1SettingContainer.page_materials.<locals>.<lambda>r~   r�   r�   r�   )r�   r�   r�   r�   r�   r   �   )r�   �ir   r   )r   r   r    r   r$   r%   r   r�   r&   r_   r`   r�   r�   r�   r�   r�   ra   �ranger   r   r   rj   )r(   r�   r�   r,   rM   r-   rX   Z  s(   
����� zSettingContainer.page_materialsc                    s�   t � � _� ��  tjddtjjdd�d�� _� jj�	tj
tjtjj� fdd�d�tjd	dd
�gd�� � jj�	tjdddd�� � jj�	t�� � � jj�	t� j� j�� � jj�	t�� � � jj�	tjtjjd� fdd�d�� � ��  d S )Nr   r   r�   r�   rx   c                    ry   rh   rz   r{   rM   r,   r-   rN   �  r}   z0SettingContainer.page_transfer.<locals>.<lambda>r~   r�   r�   r�   z]/!\ This feature require a custom ApiKey /!\ 
/!\ This feature is on beta and may crash /!\ 
r�   r�   r�   zSet City Positionc                    ry   rh   r�   r{   rM   r,   r-   rN   �  r}   r�   )r   r   ri   r$   r%   r   r�   r&   r_   r`   r�   r�   r�   r�   r�   ra   r   r   r   r�   r�   rj   rM   r,   rM   r-   r^   w  s.   
�����
�zSettingContainer.page_transferc                    s8  t � � _� ��  tjddtjjdd�d�� _� jj�	tj
tjtjj� fdd�d�tjd	dd
�gd�� � jj�	t�� � � jj�tjdddd�t�� tj
tjdd�tjddd� tdd�D �� fdd�� jt� j� d t� j� d d�gdd�t�� tjdd�tj� fdd�tdd�D �d d!d!d"d#�g� � ��  d S )$Nr   r   r�   r�   rx   c                    ry   rh   rz   r{   rM   r,   r-   rN   �  r}   z-SettingContainer.page_barbs.<locals>.<lambda>r~   r�   r�   r�   z�*REQUIREMENT*

/!\ Pre-configure all red slot with PeaceKeeper/!\ 

/!\Avoid AOE to not hit higher barb level/!\ 

/!\The bot is unenable see to the troops health/!\ 

Note this function is not designed for New accounts !r�   r�   r�   zBarbarian Level)rR   �2   c                 S   s   g | ]
}t j�t|���qS r,   )r$   �dropdown�OptionrJ   )�.0r�   r,   r,   r-   �
<listcomp>�  s    �z/SettingContainer.page_barbs.<locals>.<listcomp>r   �8   c                    rG   )N�barbarians_levelrH   rK   rM   r,   r-   rN   �  rO   ro   r�   )r   �optionsrS   rR   r   )r_   r   zPeacekeeper presetsc                    s    g | ]}t � j� jt|���qS r,   )r   r   r   rJ   )r�   Zpreset_indexrM   r,   r-   r�   �  s     �   Tr�   �   )r_   �wrapr   �run_spacingr   )r   r   ri   r$   r%   r   r�   r&   r_   r`   r�   r�   r�   r�   r�   ra   r�   �Dropdownr�   rJ   r   r   �Columnrj   rM   r,   rM   r-   rZ   �  sV   
����
�
 ��
�

���zSettingContainer.page_barbsc                    s�  t � � _� ��  tjddtjjdd�d�� _� jj�	tj
tjtjj� fdd�d�tjd	dd
�gd�� � jj�	t�� � g d�}� jj�tjdddd�tj
tjdt�d�tjjd�tjdddtj�d�tj�d�tj�d�g� jt� j� d t� j� d � fdd�d�gd�tj
tjdt�d�tjjd�tjdddtj�d �tj�d!�tj�d"�g� jt� j� d t� j� d# � fd$d�d�gd�g� � ��  d S )%Nr   r   r�   r�   rx   c                    ry   rh   rz   r{   rM   r,   r-   rN   �  r}   z-SettingContainer.page_rally.<locals>.<lambda>r~   r�   r�   r�   r�   zM*REQUIREMENT*
/!\ Pre-configure first slot of red line-up with rally Leader !r�   r�   r�   �d   zMobilisation time (minutes):)r   r&   �	alignment�   �F   ZMinutes�5�10�30ro   �
rally_timec                    rG   )Nr�   r�   rK   rM   r,   r-   rN   �  rO   �r   r   rQ   r�   rR   rS   zRally type :�Type�cav�infZarchers�
rally_typec                    rG   )Nr�   rH   rK   rM   r,   r-   rN     rO   )r   r   ri   r$   r%   r   r�   r&   r_   r`   r�   r�   r�   r�   r�   ra   r�   �	Containerr�   �center_rightr�   r�   r�   rJ   r   r   rj   )r(   r�   r,   rM   r-   r[   �  sr   
����	�


� 
����


� 
����0zSettingContainer.page_rallyc              	      s�   t � � _� ��  d� j_tjddtjjdd�d�� _	� j	j
�tjtjtjj� fdd�d	�tjd
dd�gd�� � j	j
�t�� � � j	j
�tjd� j� jt� j� d t� j� d r\dnd� fdd�d�� � j��  d S )NTr   r   r�   r�   rx   c                    ry   rh   rz   r{   rM   r,   r-   rN     r}   z1SettingContainer.page_character.<locals>.<lambda>r~   r�   r�   r�   zDRestart the game after switching
to a new character (prevent freeze)ro   �leave_game_switch_characterFc                    r�   )Nr�   r�   r{   rM   r,   r-   rN      r�   r�   )r   r   ri   r    r   r$   r%   r   r�   r&   r_   r`   r�   r�   r�   r�   r�   ra   r�   r#   rJ   r   r   r!   rj   rM   r,   rM   r-   rc   
  s6   
����
�
��	zSettingContainer.page_characterc                    s  t � � _� ��  d� j_tjddtjjdd�d�� _	� j	j
�tjtjtjj� fdd�d	�tjd
dd�gd�t�� tjtjddd�gd�tjtjd� jt� j� d t� j� d d� fdd�d�t�d�tjd� jt� j� d t� j� d d� fdd�d�gd�g� � ��  d S )NTr   r   r�   r�   rx   c                    ry   rh   rz   r{   rM   r,   r-   rN   /  r}   z/SettingContainer.page_logback.<locals>.<lambda>r~   r�   r�   r�   zCTime to wait before the bot log
back from your connection(mins): 

�   r�   ro   �	log_back1r�   c                    rG   )Nr�   r�   rK   rM   r,   r-   rN   B  rO   r�   r�   r�   �	log_back2r�   c                    rG   )Nr�   r�   rK   rM   r,   r-   rN   I  rO   )r   r   ri   r    r   r$   r%   r   r�   r&   r_   r�   r�   r�   r�   r�   r�   ra   rg   rJ   r   r   rj   rM   r,   rM   r-   rd   %  sP   
���	����
��
����&zSettingContainer.page_logbackc                    s�  t � � _� ��  d� j_tjddtjjdd�d�� _	� j	j
�tjtjtjj� fdd�d	�tjd
dd�gd�� � j	j
�t�� � � j	j
�tjtjdd� jt� j� d td� d r\dnd� fdd�d�tjd
� fdd�d�gd�tjtjdd� jt� j� d td� d r�dnd� fdd�d�tjd
� fdd�d�gd�tjtjdd� jt� j� d td� d r�dnd� fdd�d�tjd
� fd d�d�gd�g� � ��  d S )!NTr   r   r�   r�   rx   c                    ry   rh   rz   r{   rM   r,   r-   rN   \  r}   z/SettingContainer.page_profile.<locals>.<lambda>r~   r�   r�   r�   u   Profile n°1r   ro   r   �enabledFc                    �   � � dd�S )Nr�   r   r�   r{   rM   r,   r-   rN   j  �    r�   c                    �   t jtj� jdfd��� S )N�1r�   �r�   r�   r   r
   r   r{   rM   r,   r-   rN   l  s    )r�   r�   u   Profile n°2r   r   c                    r�   )Nr�   r   r�   r{   rM   r,   r-   rN   t  r�   c                    r�   )N�2r�   r�   r{   rM   r,   r-   rN   w  �    �u   Profile n°3r   r   c                    r�   )Nr�   r   r�   r{   rM   r,   r-   rN     r�   c                    r�   )N�3r�   r�   r{   rM   r,   r-   rN   �  r�   )r   r   ri   r    r   r$   r%   r   r�   r&   r_   r`   r�   r�   r�   r�   r�   ra   r�   r�   rJ   r   �ElevatedButtonrj   rM   r,   rM   r-   rf   R  sv   
�����
���
�
�
���
�
���$zSettingContainer.page_profilec                    sJ  t � � _� ��  d� j_tjddtjjdd�d�� _	� j	j
�tjtjtjj� fdd�d	�tjd
dd�gd�� � j	j
�t�� � � j	j
�tjtjdddtjjdd�gd�t�d�tjtjd� jt� j� d d� fdd�d�t�d�tjd� jt� j� d d� fdd�d�gd�tjd� jt� j� d � fdd�d�g� � ��  d S ) NTr   r   r�   r�   rx   c                    ry   rh   rz   r{   rM   r,   r-   rN   �  r}   z,SettingContainer.page_redo.<locals>.<lambda>r~   r�   r�   r�   z"*Randomise it as much as possible*Z
RobotoSlabr�   )r�   �font_family�weightr�   z=Time to wait before
the bot re-do the tasks selected  (mins):r�   rm   r�   c                    rG   )Nrm   r�   rK   rM   r,   r-   rN   �  rO   r�   r�   r�   rl   r�   c                    rG   )Nrl   r�   rK   rM   r,   r-   rN   �  rO   z+Close the game after all the tasks are done�leave_game_loopc                    r�   )Nr   r�   r{   rM   r,   r-   rN   �  r�   rP   )r   r   ri   r    r   r$   r%   r   r�   r&   r_   r`   r�   r�   r�   r�   r�   ra   r�   �
FontWeight�W_400rg   rJ   r   r�   rj   rM   r,   rM   r-   re   �  sb   
��������
�
���
��$zSettingContainer.page_redoNrv   c                 C   s�   |d u r| j }|dvr+| jt| j� d t|� |  | jt| j� d t|� |< n t|| jt| j� | � | jt| j� |  | jt| j� |< t| j� d S )N)rD   rE   r   ro   )r   r   rJ   r   rs   r   )r(   rv   �indexr,   r,   r-   r�   �  s   @&z SettingContainer.reverse_keywordr�   c              	      sZ   t � �_�jj�tj|�j�jt�j	� d t�j
� �  r dnd� �fdd�d�� d S )Nro   TFc                    �
   �� � �S rh   r�   r{   �rv   r(   r,   r-   rN   �  r�   z7SettingContainer.create_normal_switch.<locals>.<lambda>r�   )r   r   r&   r_   r`   r$   r�   r#   rJ   r   r   )r(   rv   r�   r,   r  r-   rW   �  s   ���z%SettingContainer.create_normal_switchc                    s.  t � �_�dvrS�jj�tjtj|�j�jt	�j
� d t	�j� � r&dnd��fdd�d�tjd�jtjj� fd	d�ttjjtd
d�id�d�gtjjd�� d S �jj�tjtj|�j�jt	�j
� � rjdnd��fdd�d�tjd�jtjj� fdd�ttjjtd
d�id�d�gtjjd�� d S )N)rD   rE   ro   TFc                    r  rh   r�   r{   r  r,   r-   rN   �  r�   z9SettingContainer.create_advanced_switch.<locals>.<lambda>r�   r�   c                    �   � � S rh   r,   r{   ��functionr,   r-   rN   �  �    �   )r�   )�shape)r�   �
icon_colorr   r�   �style�r_   r�   c                    r  rh   r�   r{   r  r,   r-   rN   �  r�   c                    r  rh   r,   r{   r  r,   r-   rN     r	  )r   r   r&   r_   r`   r$   r�   r�   r#   rJ   r   r   r�   r�   �SETTINGSr   �MaterialState�DEFAULTr   �MainAxisAlignment�SPACE_BETWEEN)r(   rv   r�   r  r,   )r  rv   r(   r-   rT   �  s\   ��
�����������z'SettingContainer.create_advanced_switchc              
      s`   � j j�tjtjd� j� jt� j	� d t� j
� d rdnd� fdd�d�gtjjd	�� d S )
NzKill barbs with APro   r;   TFc                    r�   )Nr;   r�   r{   rM   r,   r-   rN     r�   z3SettingContainer.create_barbs_row.<locals>.<lambda>r�   r  )r&   r_   r`   r$   r�   r�   r#   r   rJ   r   r   r  r  rM   r,   rM   r-   �create_barbs_row  s   �
��	�z!SettingContainer.create_barbs_rowc                    s�   � j j�tjtjd� j� jt� j	� d t� j
� d rdnd� fdd�d�tjd	d
dtj�d�tj�d�tj�d�tj�d�tj�d�tj�d�tj�d�tj�d�tj�d�g	t� jt� j	� d t� j
� d �d � fdd�d�gtjjd�� d S )Nz	Slow modero   �	slow_modeTFc                    r�   )Nr  r�   r{   rM   r,   r-   rN   $  r�   z3SettingContainer.create_slow_mode.<locals>.<lambda>r�   r�   r�   ZMultiplicatorz1.0xz1.25xz1.5xz1.75xz2.0xz2.25xz2.5xz2.75xz3.0xrn   rp   c                    rG   )Nrn   rH   rK   rM   r,   r-   rN   7  rO   r�   r  )r&   r_   r`   r$   r�   r�   r#   r   rJ   r   r   r�   r�   r�   r  r  rM   r,   rM   r-   rb     sD   �
�








���
���z!SettingContainer.create_slow_moderh   )�__name__�
__module__�__qualname__r�   r   r'   rk   rI   rU   rY   rV   r\   r�   r]   rX   r^   rZ   r[   rc   rd   rf   re   rJ   r�   rW   rT   r  rb   �__classcell__r,   r,   r*   r-   r      s0    !j#+(/K-793r   )r�   �fletr$   �	flet_corer   r   Zviews.Flet_time_allower�viewsr   Zviews.Flet_row_materialr   Zviews.Flet_row_presetsr   Zviews.Flet_row_rssr   Zviews.Flet_col_transferr   Zviews.Flet_row_troopsr	   Zviews.Flet_city_layoutr
   �utils.Task_utilsr   r   r"   r�   r   r,   r,   r,   r-   �<module>   s"    �