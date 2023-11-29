o
    l��b49  �                   @   s�   d dl Z d dlZd dlZd dlZd dlmZ zddlmZ W n ey-   d dlmZ Y nw G dd� de	�Z
G dd� de
�ZG d	d
� d
e
�ZG dd� de
�ZG dd� de
�ZG dd� d�Zedkrlejd Zee�ZdS dS )�    N)�	b64encode�   )�	ApiClientc                   @   �   e Zd ZdS )�SolverExceptionsN��__name__�
__module__�__qualname__� r   r   �jC:\Users\Administrator\Documents\Projets\Rise of kingdom\Bluestacks Version\bot\utils\twocaptcha\solver.pyr      �    r   c                   @   r   )�ValidationExceptionNr   r   r   r   r   r      r   r   c                   @   r   )�NetworkExceptionNr   r   r   r   r   r      r   r   c                   @   r   )�ApiExceptionNr   r   r   r   r   r      r   r   c                   @   r   )�TimeoutExceptionNr   r   r   r   r   r       r   r   c                   @   s�   e Zd Z						d8dd�Zdd	� Zd
d� Zd9dd�Zdd� Zdd� Zdd� Z	dd� Z
dd� Zdd� Zdd� Zdd� Zd d!� Zd:d"d#�Zd$d%� Zd&d'� Zd(d)� Zd*d+� Zd,d-� Zd.d/� Zd0d1� Zd2d3� Zd4d5� Zd6d7� ZdS );�
TwoCaptchaN�x   �X  �
   �2captcha.comc                 C   sD   || _ || _|| _|| _|| _|| _tt|�d�| _d| _	t
| _d S )N)�post_url�	   )�API_KEY�soft_id�callback�default_timeout�recaptcha_timeout�polling_intervalr   �str�
api_client�	max_filesr   �
exceptions)�selfZapiKey�softIdr   �defaultTimeoutZrecaptchaTimeout�pollingInterval�serverr   r   r   �__init__%   s   	
zTwoCaptcha.__init__c                 K   s"   | � |�}| jdi |�|��}|S )a�  
        Wrapper for solving normal captcha (image)
        
        Required:
            file                (image, base64, or url)

        Optional params:

            phrase
            numeric
            minLen 
            maxLen 
            phrase 
            caseSensitive
            calc   
            lang
            hintText
            hintImg
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
        Nr   ��
get_method�solve)r#   �file�kwargs�method�resultr   r   r   �normal8   s   
zTwoCaptcha.normalc                 K   s   | j d|dd�|��}|S )z�
        Wrapper for solving text captcha 

        Required:
            text
            
        Optional params:
            
            lang
            softId
            callback
        �post)�textr.   Nr   �r+   )r#   r2   r-   r/   r   r   r   r2   T   s   zTwoCaptcha.text�v2r   c                 K   s.   ||d||d�|�}| j dd| ji|��}|S )a  
        Wrapper for solving recaptcha (v2, v3)

        Required:
            sitekey
            url

        Optional params:
            
            invisible
            version
            enterprise
            action
            score
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
        Zuserrecaptcha)Z	googlekey�urlr.   �version�
enterprise�timeoutNr   )r+   r   )r#   �sitekeyr5   r6   r7   r-   �paramsr/   r   r   r   �	recaptchae   s   ��	zTwoCaptcha.recaptchac                 K   �   | j d||dd�|��}|S )af  
        Wrapper for solving funcaptcha

        Required:
            sitekey
            url

        Optional params:
            
            surl
            userAgent
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
            **{'data[key]': 'anyStringValue'}
        �
funcaptcha)Z	publickeyr5   r.   Nr   r3   �r#   r9   r5   r-   r/   r   r   r   r=   �   s   ��zTwoCaptcha.funcaptchac                 K   s   | j d|||dd�|��}|S )aU  
        Wrapper for solving geetest captcha

        Required:
            gt
            challenge
            url
                        
        Optional params:
            
            apiServer
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
        �geetest)�gt�	challenger5   r.   Nr   r3   )r#   r@   rA   r5   r-   r/   r   r   r   r?   �   s   ��zTwoCaptcha.geetestc                 K   r<   )a*  
        Wrapper for solving hcaptcha

        Required:
            sitekey
            url

        Optional params:

            invisible
            data
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
        �hcaptcha)r9   r5   r.   Nr   r3   r>   r   r   r   rB   �   s   ��zTwoCaptcha.hcaptchac           	      K   s*   |||||dd�|�}| j di |��}|S )ao  
        Wrapper for solving 

        Required:
            s_s_c_user_id
            s_s_c_session_id
            s_s_c_web_server_sign
            s_s_c_web_server_sign2
            url

        Optional params:
            
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
        �
keycaptcha)�s_s_c_user_id�s_s_c_session_id�s_s_c_web_server_sign�s_s_c_web_server_sign2r5   r.   Nr   r3   )	r#   rD   rE   rF   rG   r5   r-   r:   r/   r   r   r   rC   �   s   ��
zTwoCaptcha.keycaptchac                 K   r<   )a  
        Wrapper for solving capy

        Required:
            sitekey
            url

        Optional params:
            
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
        �capy)Z
captchakeyr5   r.   Nr   r3   r>   r   r   r   rH   �   s   ��zTwoCaptcha.capyc                 K   �.   | � |�}ddi|�|�}| jdi |��}|S )a�  
        Wrapper for solving grid captcha (image)
        
        Required:
            file                (image or base64)

        Optional params:
            
            rows      
            cols      
            previousId
            canSkip   
            lang      
            hintImg   
            hintText  
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
        r;   r   Nr   r)   �r#   r,   r-   r.   r:   r/   r   r   r   �grid  s   
���zTwoCaptcha.gridc                 K   sH   d|v sd|v st d��| �|�}ddd�|�|�}| jdi |��}|S )a�  
        Wrapper for solving canvas captcha (image)
        
        Required:
            file                (image or base64)

        Optional params:
            
            previousId
            canSkip   
            lang      
            hintImg   
            hintText  
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
        �hintText�hintImgz,parameters required: hintText and/or hintImgr   )r;   �canvasNr   )r   r*   r+   rJ   r   r   r   rN   "  s   �
���zTwoCaptcha.canvasc                 K   rI   )aw  
        Wrapper for solving coordinates captcha (image)
        
        Required:
            file                (image or base64)

        Optional params:
            
            hintImg   
            hintText  
            lang
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
        Zcoordinatescaptchar   Nr   r)   rJ   r   r   r   �coordinatesE  s   
���zTwoCaptcha.coordinatesc                 K   sl   t |t�r| �|�d }| jd|dd�|��}|S t |t�r$t|�� �}| �|�}| jd|dd�|��}|S )a{  
        Wrapper for solving rotate captcha (image)
        
        Required:
            files               (images)

        Optional params:
            
            angle
            lang
            hintImg   
            hintText  
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
        r,   Zrotatecaptcha)r,   r.   )�filesr.   Nr   )�
isinstancer   r*   r+   �dict�list�values�extract_files)r#   rP   r-   r,   r/   r   r   r   �rotatea  s   


zTwoCaptcha.rotatec                 K   s^   | j di |��}d|i}| jdu r-t|p| j�}t|p| j�}| �|||�}|�d|i� |S )z�
        sends captcha, receives result


        Parameters
        ----------
        timeout : float
        polling_interval : int

        **kwargs : all captcha params

        Returns
        -------
        result : string
        �	captchaIdN�coder   )�sendr   �floatr   �intr   �wait_result�update)r#   r8   r   r-   �id_r/   �sleeprX   r   r   r   r+   �  s   
zTwoCaptcha.solvec                 C   s^   t � � | }t � � |k r'z| �|�W S  ty    t �|� Y nw t � � |k std|� d���)Nztimeout z	 exceeded)�time�
get_resultr   r_   r   )r#   r^   r8   r   Zmax_waitr   r   r   r\   �  s   ��	zTwoCaptcha.wait_resultc                 C   s�   |st d��d|vrt|�dkrd|d�S |�d�r6t�|�}|jdkr+t d|� ���dt|j��d	�d�S t	j
�|�sCt d
|� ���d|d�S )NzFile required�.�2   �base64)r.   �body�http��   z'File could not be downloaded from url: zutf-8�File not found: r1   )r.   r,   )r   �len�
startswith�requests�get�status_coder   �content�decode�os�path�exists)r#   r,   Zimg_respr   r   r   r*   �  s   




zTwoCaptcha.get_methodc                 K   s\   | � |�}| �|�}| �|�\}}| jjdd|i|��}|�d�s(td|� ���|dd � S )NrP   �OK|�cannot recognize response �   r   )�default_params�rename_params�check_hint_imgr    �in_rj   r   )r#   r-   r:   rP   �responser   r   r   rY   �  s   


zTwoCaptcha.sendc                 C   sD   | j j| jd|d�}|dkrt�|�d�std|� ���|dd � S )Nrl   ��key�action�idZCAPCHA_NOT_READYrs   rt   ru   )r    �resr   r   rj   r   )r#   r^   rz   r   r   r   ra   �  s   
zTwoCaptcha.get_resultc                 C   s   | j j| jdd�}t|�S )zZ
        get my balance

        Returns
        -------
        balance : float

        Z
getbalance)r|   r}   )r    r   r   rZ   )r#   rz   r   r   r   �balance�  s   
zTwoCaptcha.balancec                 C   s$   |rdnd}| j j| j||d� dS )z�
        report of solved captcha: good/bad

        Parameters
        ----------
        id_ : captcha ID
        correct : True/False

        Returns
        -------
        None.

        Z
reportgoodZ	reportbadr{   N)r    r   r   )r#   r^   �correct�repr   r   r   �report�  s   zTwoCaptcha.reportc                    s�   ddddddddd	d
dddddd�}� fdd�|� � D �}� �dd�}|o8|�|d |d d�� |�� � |S  |�� � |S )NZregsense�min_len�max_lenZtextinstructions�imginstructionsZpageurlZ	min_scoreZtextcaptchaZrecaptcharowsZrecaptchacolsZ
previousIDZcan_no_answerZ
api_serverr   Zpingback)ZcaseSensitiveZminLenZmaxLenrL   rM   r5   �scorer2   �rows�colsZ
previousIdZcanSkipZ	apiServerr$   r   c                    s$   i | ]\}}|� v r|� � |��qS r   )�pop)�.0�k�v�r:   r   r   �
<dictcomp>  s    
�z,TwoCaptcha.rename_params.<locals>.<dictcomp>�proxy� �uri�type)r�   Z	proxytype)�itemsr�   r]   )r#   r:   �replace�
new_paramsr�   r   r�   r   rw   �  s:   �
��
�
zTwoCaptcha.rename_paramsc                 C   s^   |� d| ji� |�d| j�}|�d| j�}|r|� d|i� |r(|� d|i� t|�| _|S )Nr|   r   r$   )r]   r   r�   r   r   �boolZhas_callback)r#   r:   r   r   r   r   r   rv      s   
zTwoCaptcha.default_paramsc                 C   sV   t |�| jkrtd| j� d���dd� |D �}|r td|� ���dd� t|�D �}|S )NzToo many files (max: �)c                 S   s   g | ]
}t j�|�s|�qS r   )rp   rq   rr   )r�   �fr   r   r   �
<listcomp>4  s    z,TwoCaptcha.extract_files.<locals>.<listcomp>rh   c                 S   s    i | ]\}}d |d � �|�qS )Zfile_r   r   )r�   �er�   r   r   r   r�   9  s     z,TwoCaptcha.extract_files.<locals>.<dictcomp>)ri   r!   r   �	enumerate)r#   rP   Z
not_existsr   r   r   rU   .  s   �zTwoCaptcha.extract_filesc                 C   s�   |� dd �}|� di �}|s||fS d|vr t|�dkr ||fS tj�|�s-td|� ���|s7d|� di �i}|�d|i� ||fS )Nr�   rP   rb   rc   rh   r,   )r�   ri   rp   rq   rr   r   r]   )r#   r:   �hintrP   r   r   r   rx   <  s   zTwoCaptcha.check_hint_img)NNr   r   r   r   )r4   r   )r   r   )r   r	   r
   r(   r0   r2   r;   r=   r?   rB   rC   rH   rK   rN   rO   rV   r+   r\   r*   rY   ra   r�   r�   rw   rv   rU   rx   r   r   r   r   r   $   s>    
�
 ! #
!#r   �__main__)rp   �sysr`   rk   rd   r   �apir   �ImportError�	Exceptionr   r   r   r   r   r   r   �argvr|   Zsolr   r   r   r   �<module>   s.   �    2
�