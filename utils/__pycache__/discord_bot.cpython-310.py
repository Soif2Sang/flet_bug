o
    >�Od�  �                   @   s   d dl Z dd� ZdS )�    Nc                    sD   t jt j�� d�� � fdd��� j� ���fdd��}� �d� d S )N)Zintentsc                 �   s.   �� � | �I d H }t|� |�|�I d H  d S )N)�
fetch_user�print�send)�user_id�message�user)�client� �dC:\Users\Administrator\Documents\Projets\Rise of kingdom\Bluestacks Version\bot\utils\discord_bot.py�envoyer_message_utilisateur	   s   �z1send_message.<locals>.envoyer_message_utilisateurc                   �   s,   �t d� ����I d H  � �� I d H  d S )Nu	   Bot prêt)r   �closer	   �r   r   r   r   r	   r
   �on_ready   s   �zsend_message.<locals>.on_readyzHMTEwMDM2MTgyNTQ0MDIzOTY3Ng.GAqJHi.20GKlr5s3l-7i5EptodBcOUs8V1wb6z5VwtASY)�discord�ClientZIntents�default�event�run)r   r   r   r	   r   r
   �send_message   s
   r   )r   r   r	   r	   r	   r
   �<module>   s    