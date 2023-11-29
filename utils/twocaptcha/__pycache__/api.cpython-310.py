o
    l��b�
  �                   @   s:   d dl Z G dd� de�ZG dd� de�ZG dd� d�ZdS )�    Nc                   @   �   e Zd ZdS )�NetworkExceptionN��__name__�
__module__�__qualname__� r   r   �gC:\Users\Administrator\Documents\Projets\Rise of kingdom\Bluestacks Version\bot\utils\twocaptcha\api.pyr      �    r   c                   @   r   )�ApiExceptionNr   r   r   r   r	   r   
   r
   r   c                   @   s*   e Zd Zd	dd�Zi fdd�Zdd� ZdS )
�	ApiClient�2captcha.comc                 C   s
   || _ d S )N)�post_url)�selfr   r   r   r	   �__init__   s   
zApiClient.__init__c              
   K   s  zTd| j  d }|r%dd� |�� D �}tj|||d�}dd� |�� D � n.d|v rLt|�d�d	��}tj||d|id�}W d
  � n1 sFw   Y  ntj||d�}W n tjye } zt|��d
}~ww |j	dkrstd|j	� ���|j
�d�}d|v r�t|��|S )a�  
        
        sends POST-request (files and/or params) to solve captcha

        Parameters
        ----------
        files : TYPE, optional
            DESCRIPTION. The default is {}.
        **kwargs : TYPE
            DESCRIPTION.

        Raises
        ------
        NetworkException
            DESCRIPTION.
        ApiException
            DESCRIPTION.

        Returns
        -------
        resp : TYPE
            DESCRIPTION.

        �https://z/in.phpc                 S   s   i | ]
\}}|t |d ��qS )�rb)�open)�.0�key�pathr   r   r	   �
<dictcomp>1   s    z!ApiClient.in_.<locals>.<dictcomp>)�data�filesc                 S   s   g | ]}|� � �qS r   )�close)r   �fr   r   r	   �
<listcomp>6   s    z!ApiClient.in_.<locals>.<listcomp>�filer   N)r   ��   �bad response: �utf-8�ERROR)r   �items�requests�post�valuesr   �pop�RequestExceptionr   �status_code�content�decoder   )r   r   �kwargsZcurrent_url�respr   �er   r   r	   �in_   s>   ��������
zApiClient.in_c              
   K   s|   z,d| j  d }tj||d�}|jdkrtd|j� ���|j�d�}d|v r*t|��W |S  tjy= } zt|��d}~ww )	a|  
        sends additional GET-requests (solved captcha, balance, report etc.)

        Parameters
        ----------
        **kwargs : TYPE
            DESCRIPTION.

        Raises
        ------
        NetworkException
            DESCRIPTION.
        ApiException
            DESCRIPTION.

        Returns
        -------
        resp : TYPE
            DESCRIPTION.

        r   z/res.php)�paramsr   r   r    r!   N)	r   r#   �getr(   r   r)   r*   r   r'   )r   r+   Zcurrent_url_outr,   r-   r   r   r	   �resP   s   
����zApiClient.resN)r   )r   r   r   r   r.   r1   r   r   r   r	   r      s    
=r   )r#   �	Exceptionr   r   r   r   r   r   r	   �<module>   s   