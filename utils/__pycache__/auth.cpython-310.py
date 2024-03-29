o
    :UdS;  �                
   @   s  d dl Z d dlZd dlZd dlZd dlmZ d dlZd dlZd dl	Z
d dlZd dlZd dlmZ d dlmZ d dlmZmZ ze�� Ze�d� W n" ejjyk Z zee� e�d� e �d� W Y dZ[ndZ[ww G d	d
� d
�ZG dd� d�ZG dd� d�ZdS )�    N)�uuid4)�AES)�SHA256)�pad�unpadzhttps://google.com�   �   c                   @   s�   e Zd Zd Z Z Z ZZd'dd�Zd Z	Z
dZdd� Zd(dd	�Zd
d� Zdd� Zdd� Zdd� Zd)dd�Zdd� Zdd� Zdd� Zdd� Zd*dd�ZG dd � d �ZG d!d"� d"�Ze� Ze� Zd#d$� Zd%d&� ZdS )+�selfApi� Nc                 C   s0   || _ || _|| _|| _|| _|| _| ��  d S �N)�name�ownerid�secret�version�hash_to_check�page�init)�selfr   r   r   r   r   r   � r   �]C:\Users\Administrator\Documents\Projets\Rise of kingdom\Bluestacks Version\bot\utils\auth.py�__init__   s   zselfApi.__init__Fc              	   C   s�  | j dkrtd� t�d� t�d� t�tt	� �d d� �
� ��� }t�tt	� �d d� �
� ��� | _t�d�
� �t�| j| j|�| jt�| j| j|�t�| j�
� �t�| j�
� �|d�}| �|�}|dkrptd	� t�d� t�|| j|�}t�|�}|d
 dkr�|d dkr�td� |d }t�d|� �� t�d� n	td� t�d� |d s�t|d
 � t�d� |d | _ d| _| �|d � d S )Nr
   zYou've already initialized!�   r   �   r   )�type�ver�hash�enckeyr   r   �init_ivZKeyAuth_InvalidzThe application doesn't exist�messageZ
invalidver�downloadzNew Version Availablezstart zIInvalid Version, Contact owner to add download link to latest app version�success�	sessionidT�appinfo)r!   �print�time�sleep�os�_exitr   �new�strr   �encode�	hexdigestr   �binascii�hexlify�
encryption�encryptr   r   r   r   r   �_selfApi__do_request�decrypt�jsond�loads�system�initialized�_selfApi__load_app_data)r   r   �	post_data�response�jsonZdownload_linkr   r   r   r   ,   sD   


 "�






zselfApi.initc              	   C   s�  | � �  |d u rt�� }|d ur| jd u r|| _t�tt� �d d� �� ��	� }t
�d�� �t�|| j|�t�|| j|�t
�| j�� �t
�| j�� �t
�| j�� �|d�}| �|�}t�|| j|�}t�|�}| �d�}	| �d�}
|	dkr}| �d|� |}	|
dkr�|	|kr�| �d|� |}
|	|kr�|
|kr�| jd ur�| �d� td� d	S |d
 r�| �|d � dS | jd ur�| �|d � t|d � d	S )Nr   �login)r   �username�passr!   r   r   r   ZHWID1ZHWID2�Nonez,Hardware id doesn't match, contact the adminzHardware id doesn't matchFr    �infoTr   )�	checkinit�others�get_hwidr   r   r(   r)   r   r*   r+   r,   r-   r.   r/   r   r!   r   r   r0   r1   r2   r3   �getvar�setvar�
pop_bannerr#   �_selfApi__load_user_data)r   �user�password�hwidr   r   r7   r8   r9   Zwid1Zwid2r   r   r   r:   [   sJ    �







zselfApi.loginc                 C   sV   t jt jjt jt jjt jjdd�t j|d�t j	d| j
jd�gdd�| j
_| j
��  d S )N�(   )�color�size)�value�Ok)�on_clickT)�bgcolor�leading�content�actions�open)�ft�Banner�colors�	AMBER_100�Icon�icons�WARNING_AMBER_ROUNDED�AMBER�Text�
TextButtonr   �close_banner�banner�update)r   �textr   r   r   rD   �   s   ��
�zselfApi.pop_bannerc                 C   s�   | � �  t�tt� �d d� �� ��� }t�d�� �t	�
|| j|�t�| j�� �t�| j�� �t�| j�� �|d�}| �|�}t	�|| j|�}t�|�}|d rT|d S t|d � t�d� t�d� d S )Nr   �var)r   Zvaridr!   r   r   r   r    r   �   r   �r?   r   r(   r)   r   r*   r+   r,   r-   r.   r/   r   r!   r   r   r0   r1   r2   r3   r#   r$   r%   r&   r'   )r   r   r   r7   r8   r9   r   r   r   rb   �   s"    �
	

zselfApi.varc                 C   s�   | � �  t�tt� �d d� �� ��� }t�d�� �t	�
|| j|�t�| j�� �t�| j�� �t�| j�� �|d�}| �|�}t	�|| j|�}t�|�}|d rT|d S t|d � dS )Nr   rB   )r   rb   r!   r   r   r   r    r8   r   r=   �r?   r   r(   r)   r   r*   r+   r,   r-   r.   r/   r   r!   r   r   r0   r1   r2   r3   r#   )r   �var_namer   r7   r8   r9   r   r   r   rB   �   s     �

zselfApi.getvarc              	   C   s�   | � �  t�tt� �d d� �� ��� }t�d�� �t	�
|| j|�t	�
|| j|�t�| j�� �t�| j�� �t�| j�� �|d�}| �|�}t	�|| j|�}t�|�}|d rYdS t|d � d S )Nr   rC   )r   rb   �datar!   r   r   r   r    Tr   re   )r   rf   Zvar_datar   r7   r8   r9   r   r   r   rC   �   s     �
	
zselfApi.setvarc           	      C   s�   | � �  t�tt� �d d� �� ��� }t�d�� �t	�
|| j|�t	�
|| j|�t	�
|| j|�t	�
|| j|�t�| j�� �t�| j�� �t�| j�� �|d�	}| �|�}t	�|| j|�}t�|�}|d ri|d S t|d � t�d� t�d� d S )Nr   �webhook)	r   �webid�params�body�conttyper!   r   r   r   r    r   rc   r   rd   )	r   ri   �paramrk   rl   r   r7   r8   r9   r   r   r   rh   �   s(    �


zselfApi.webhookc                 C   s�   | � �  t�tt� �d d� �� ��� }t| j� t	�
d�� �t	�
| j�� �t	�
| j�� �t	�
| j�� �|d�}| �|�}t�|| j|�}t�|�}|d rPdS dS )Nr   �check�r   r!   r   r   r   r    TF)r?   r   r(   r)   r   r*   r+   r#   r   r,   r-   r!   r   r0   r.   r1   r   r2   r3   �r   r   r7   r8   r9   r   r   r   rn   �   s    
�

zselfApi.checkc              	   C   s�   | � �  t�tt� �d d� �� ��� }t�d�� �t	�
t�d�| j|�t	�
|| j|�t�| j�� �t�| j�� �t�| j�� �|d�}| �|� d S )Nr   �logr;   )r   Zpcuserr   r!   r   r   r   )r?   r   r(   r)   r   r*   r+   r,   r-   r.   r/   r&   �getenvr   r!   r   r   r0   )r   r   r   r7   r   r   r   rq     s    �
zselfApi.logc                 C   s�   | � �  td� t�tt� �d d� �� ��� }t�	d�� �t�	| j
�� �t�	| j�� �t�	| j�� �|d�}| �|�}t�|| j|�}t�|�}t|� |d r_t|d �dkr[d S |d S d S )N�testr   �fetchOnlinero   r    �usersr   )r?   r#   r   r(   r)   r   r*   r+   r,   r-   r!   r   r   r0   r.   r1   r   r2   r3   �lenrp   r   r   r   rt      s$    �

zselfApi.fetchOnlinec                 C   s*   | j std� t�d� t�d� d S d S )Nz/Initialize first, in order to use the functionsr   r   )r5   r#   r$   r%   r&   r'   )r   r   r   r   r?   :  s
   
�zselfApi.checkinitr   c                 C   s�   zt jd|dd�}|jW S  tjjy-   |dk r*| jd ur#| �d� td� Y d S Y d S  tjj	yK   |dk rHt
�d� | �||d � Y S Y d S w )Nzhttps://keyauth.win/api/1.0/�   )rg   �timeoutrc   z+Request timed out.. Please wait few minuteszRequest timed outr   )�s�postra   �requests�
exceptions�Timeoutr   rD   r#   �ConnectionErrorr$   r%   r0   )r   r7   �deadstopZrq_outr   r   r   Z__do_request@  s"   �

�
��zselfApi.__do_requestc                   @   s    e Zd Zd Z Z Z ZZdS )zselfApi.application_data_cr
   N)�__name__�
__module__�__qualname__�numUsers�numKeys�app_ver�customer_panel�onlineUsersr   r   r   r   �application_data_cP  s    r�   c                   @   s,   e Zd Zd Z Z Z Z Z Z Z	Z
dS )zselfApi.user_data_cr
   N)r�   r�   r�   r;   �iprH   �expires�
createdate�	lastlogin�subscription�subscriptionsr   r   r   r   �user_data_cU  s    $r�   c                 C   s@   |d | j _|d | j _|d | j _|d | j _|d | j _d S )Nr�   r�   r   ZcustomerPanelLinkZnumOnlineUsers)�app_datar�   r�   r�   r�   r�   �r   rg   r   r   r   Z__load_app_data[  s
   zselfApi.__load_app_datac                 C   st   |d | j _|d | j _|d | j _|d d d | j _|d | j _|d | j _|d d d	 | j _|d | j _d S )
Nr;   r�   rH   r�   r   Zexpiryr�   r�   r�   )	�	user_datar;   r�   rH   r�   r�   r�   r�   r�   r�   r   r   r   Z__load_user_datab  s   zselfApi.__load_user_datar   )NN)r
   r
   )r   )r�   r�   r�   r   r   r   r   r   r   r!   r   r5   r   r:   rD   rb   rB   rC   rh   rn   rq   rt   r?   r0   r�   r�   r�   r�   r6   rE   r   r   r   r   r	      s.    

/2

r	   c                   @   s   e Zd Zedd� �ZdS )r@   c                  C   s�   t �� dkr"td��} | �� }|W  d   � S 1 sw   Y  d S t �� dkr;t�� }t�d |�d }t�|�}|S t �� dkrdt	j
dt	jdd��� d }|�� �d	d
�d
 �dd�}|d
d� }|S d S )N�Linuxz/etc/machine-id�Windowsr   �Darwinz&ioreg -l | grep IOPlatformSerialNumberT)�stdout�shell�=r   � r
   �����)�platformr4   rS   �readr&   �getlogin�win32securityZLookupAccountNameZConvertSidToStringSid�
subprocess�Popen�PIPE�communicate�decode�split�replace)�frH   ZwinuserZsid�output�serialr   r   r   rA   n  s    
$�
�zothers.get_hwidN)r�   r�   r�   �staticmethodrA   r   r   r   r   r@   m  s    r@   c                   @   s<   e Zd Zedd� �Zedd� �Zedd� �Zedd� �Zd	S )
r.   c                 C   s.   t | d�} t�|tj|�}|�| �}t�|�S �N�   )r   r   r(   �MODE_CBCr/   r,   r-   )Z
plain_text�key�iv�aes_instanceZraw_outr   r   r   �encrypt_string�  �   


zencryption.encrypt_stringc                 C   s.   t �| �} t�|tj|�}|�| �} t| d�S r�   )r,   �	unhexlifyr   r(   r�   r1   r   )Zcipher_textr�   r�   r�   r   r   r   �decrypt_string�  r�   zencryption.decrypt_stringc                 C   �t   z*t �|�� ��� d d� }t �|�� ��� d d� }t�| �� |�� |�� ��� W S    td� t�	d� Y d S �N�    r�   zxInvalid Application Information. Long text is secret short text is ownerid. Name is supposed to be app name not usernamer   )
r   r(   r*   r+   r.   r�   r�   r#   r&   r'   �r   Zenc_keyr�   �_keyZ_ivr   r   r   r/   �  �    zencryption.encryptc                 C   r�   r�   )
r   r(   r*   r+   r.   r�   r�   r#   r&   r'   r�   r   r   r   r1   �  r�   zencryption.decryptN)r�   r�   r�   r�   r�   r�   r/   r1   r   r   r   r   r.   �  s    
	
	
r.   ) r&   r9   r2   r$   r,   �uuidr   r�   r�   �fletrT   r{   r�   ZCrypto.Cipherr   ZCrypto.Hashr   ZCrypto.Util.Paddingr   r   �Sessionry   �getr|   �RequestException�er#   r%   r'   r	   r@   r.   r   r   r   r   �<module>   s6    
��  V