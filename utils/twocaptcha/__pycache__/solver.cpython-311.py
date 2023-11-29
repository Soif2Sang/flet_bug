�
    l��b49  �                   �J  � d dl Z d dlZd dlZd dlZd dlmZ 	 ddlmZ n# e$ r	 d dlmZ Y nw xY w G d� de	�  �        Z
 G d� de
�  �        Z G d	� d
e
�  �        Z G d� de
�  �        Z G d� de
�  �        Z G d� d�  �        Zedk    rej        d         Z ee�  �        ZdS dS )�    N)�	b64encode�   )�	ApiClientc                   �   � e Zd ZdS )�SolverExceptionsN��__name__�
__module__�__qualname__� �    �jC:\Users\Administrator\Documents\Projets\Rise of kingdom\Bluestacks Version\bot\utils\twocaptcha\solver.pyr   r      �   � � � � � ��Dr   r   c                   �   � e Zd ZdS )�ValidationExceptionNr   r   r   r   r   r      r   r   r   c                   �   � e Zd ZdS )�NetworkExceptionNr   r   r   r   r   r      r   r   r   c                   �   � e Zd ZdS )�ApiExceptionNr   r   r   r   r   r      r   r   r   c                   �   � e Zd ZdS )�TimeoutExceptionNr   r   r   r   r   r       r   r   r   c                   �   � e Zd Z	 	 	 	 	 	 d d�Zd� Zd� Zd!d�Zd� Zd� Zd� Z	d� Z
d� Zd� Zd� Zd� Zd� Zd"d�Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zd� ZdS )#�
TwoCaptchaN�x   �X  �
   �2captcha.comc                 ��   � || _         || _        || _        || _        || _        || _        t          t          |�  �        ��  �        | _        d| _	        t          | _        d S )N)�post_url�	   )�API_KEY�soft_id�callback�default_timeout�recaptcha_timeout�polling_intervalr   �str�
api_client�	max_filesr   �
exceptions)�self�apiKey�softIdr#   �defaultTimeout�recaptchaTimeout�pollingInterval�servers           r   �__init__zTwoCaptcha.__init__%   s[   � � ������ ���-���!1��� /���#�s�6�{�{�;�;�;������*����r   c                 �N   � | �                     |�  �        } | j        di |�|��}|S )a�  
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
        r   ��
get_method�solve)r+   �file�kwargs�method�results        r   �normalzTwoCaptcha.normal8   s6   � �0 ����&�&�����/�/�f�/��/�/���r   c                 �&   �  | j         d|dd�|��}|S )z�
        Wrapper for solving text captcha 

        Required:
            text
            
        Optional params:
            
            lang
            softId
            callback
        �post)�textr9   r   �r6   )r+   r>   r8   r:   s       r   r>   zTwoCaptcha.textT   s'   � � ���?��f�?�?��?�?���r   �v2r   c                 �B   � ||d||d�|�} | j         dd| j        i|��}|S )a  
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
        �userrecaptcha)�	googlekey�urlr9   �version�
enterprise�timeoutr   )r6   r%   )r+   �sitekeyrD   rE   rF   r8   �paramsr:   s           r   �	recaptchazTwoCaptcha.recaptchae   sO   � �* !��%��$�
� 
� �
�� ���E�E�D�$:�E�f�E�E���r   c                 �(   �  | j         d||dd�|��}|S )af  
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
funcaptcha)�	publickeyrD   r9   r   r?   �r+   rH   rD   r8   r:   s        r   rL   zTwoCaptcha.funcaptcha�   s:   � �$ ��� &�g� #�#/�&� &� %�&� &�� �r   c                 �*   �  | j         d|||dd�|��}|S )aU  
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
        �geetest)�gt�	challengerD   r9   r   r?   )r+   rQ   rR   rD   r8   r:   s         r   rP   zTwoCaptcha.geetest�   s=   � �" ��� &�r�&/� #�#,�&� &� %�	&� &��
 �r   c                 �(   �  | j         d||dd�|��}|S )a*  
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
        �hcaptcha)rH   rD   r9   r   r?   rN   s        r   rT   zTwoCaptcha.hcaptcha�   s:   � �" ��� &�G� #�#-�&� &� %�&� &�� �r   c                 �6   � |||||dd�|�} | j         di |��}|S )ao  
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
keycaptcha)�s_s_c_user_id�s_s_c_session_id�s_s_c_web_server_sign�s_s_c_web_server_sign2rD   r9   r   r?   )	r+   rW   rX   rY   rZ   rD   r8   rI   r:   s	            r   rV   zTwoCaptcha.keycaptcha�   sJ   � �* +� 0�%:�&<��"�
� 
� �
�� ���%�%�f�%�%���r   c                 �(   �  | j         d||dd�|��}|S )a  
        Wrapper for solving capy

        Required:
            sitekey
            url

        Optional params:
            
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
        �capy)�
captchakeyrD   r9   r   r?   rN   s        r   r\   zTwoCaptcha.capy�   s:   � � ��� &�w� #�#)�&� &� %�&� &�� �r   c                 �Z   � | �                     |�  �        }ddi|�|�} | j        di |��}|S )a�  
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
        rJ   r   r   r4   �r+   r7   r8   r9   rI   r:   s         r   �gridzTwoCaptcha.grid  sS   � �* ����&�&�� ��
��
� �
�� ���%�%�f�%�%���r   c                 �   � d|v sd|v st          d�  �        �| �                    |�  �        }ddd�|�|�} | j        di |��}|S )a�  
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
        �hintText�hintImgz,parameters required: hintText and/or hintImgr   )rJ   �canvasr   )r   r5   r6   r_   s         r   rd   zTwoCaptcha.canvas"  s�   � �& �f�$�$�	�V�(;�(;�%�>�@� @� @� ����&�&�� ��
� 
� �
� �	
�� ���%�%�f�%�%���r   c                 �Z   � | �                     |�  �        }ddi|�|�} | j        di |��}|S )aw  
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
        �coordinatescaptchar   r   r4   r_   s         r   �coordinateszTwoCaptcha.coordinatesE  sS   � �" ����&�&�� !�!�
��
� �
�� ���%�%�f�%�%���r   c                 �@  � t          |t          �  �        r-| �                    |�  �        d         } | j        d|dd�|��}|S t          |t          �  �        r!t          |�                    �   �         �  �        }| �                    |�  �        } | j        d|dd�|��}|S )a{  
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
        r7   �rotatecaptcha)r7   r9   )�filesr9   r   )�
isinstancer'   r5   r6   �dict�list�values�extract_files)r+   rj   r8   r7   r:   s        r   �rotatezTwoCaptcha.rotatea  s�   � �$ �e�S�!�!� 	)��?�?�5�)�)�&�1�D��T�Z�L�T�/�L�L�V�L�L�F��M���t�$�$� 	)�������(�(�E��"�"�5�)�)�����J�%��J�J�6�J�J���r   c                 ��   �  | j         di |��}d|i}| j        �Zt          |p| j        �  �        }t	          |p| j        �  �        }| �                    |||�  �        }|�                    d|i�  �         |S )z�
        sends captcha, receives result


        Parameters
        ----------
        timeout : float
        polling_interval : int

        **kwargs : all captcha params

        Returns
        -------
        result : string
        �	captchaIdN�coder   )�sendr#   �floatr$   �intr&   �wait_result�update)r+   rG   r&   r8   �id_r:   �sleeprs   s           r   r6   zTwoCaptcha.solve�  s�   � �" �d�i�!�!�&�!�!���s�#���=� ��G�;�t�';�<�<�G��(�A�D�,A�B�B�E��#�#�C��%�8�8�D��M�M�6�4�.�)�)�)��r   c                 �$  � t          j         �   �         |z   }t          j         �   �         |k     rQ	 | �                    |�  �        S # t          $ r t          j        |�  �         Y nw xY wt          j         �   �         |k     �Qt	          d|� d��  �        �)Nztimeout z	 exceeded)�time�
get_resultr   rz   r   )r+   ry   rG   r&   �max_waits        r   rw   zTwoCaptcha.wait_result�  s�   � ��9�;�;��(���i�k�k�H�$�$�-����s�+�+�+��#� -� -� -��
�+�,�,�,�,�,�-���� �i�k�k�H�$�$� �<�'�<�<�<�=�=�=s   �A �A%�$A%c                 �  � |st          d�  �        �d|vrt          |�  �        dk    rd|d�S |�                    d�  �        r[t          j        |�  �        }|j        dk    rt          d|� ��  �        �dt          |j        �  �        �                    d	�  �        d�S t          j
        �                    |�  �        st          d
|� ��  �        �d|d�S )NzFile required�.�2   �base64)r9   �body�http��   z'File could not be downloaded from url: zutf-8�File not found: r=   )r9   r7   )r   �len�
startswith�requests�get�status_coder   �content�decode�os�path�exists)r+   r7   �img_resps      r   r5   zTwoCaptcha.get_method�  s�   � �� 	7�%�o�6�6�6��d�{�{�s�4�y�y�2�~�~�&��5�5�5��?�?�6�"�"� 	]��|�D�)�)�H��#�s�*�*�)�*Z�TX�*Z�*Z�[�[�[�&�	�(�:J�0K�0K�0R�0R�SZ�0[�0[�\�\�\��w�~�~�d�#�#� 	A�%�&?��&?�&?�@�@�@� �$�/�/�/r   c                 �  � | �                     |�  �        }| �                    |�  �        }| �                    |�  �        \  }} | j        j        dd|i|��}|�                    d�  �        st          d|� ��  �        �|dd �         S )Nrj   �OK|�cannot recognize response �   r   )�default_params�rename_params�check_hint_imgr(   �in_r�   r   )r+   r8   rI   rj   �responses        r   rt   zTwoCaptcha.send�  s�   � ��$�$�V�,�,���#�#�F�+�+���+�+�F�3�3����&�4�?�&�=�=�U�=�f�=�=���"�"�5�)�)� 	H��F�H�F�F�G�G�G�����|�r   c                 ��   � | j         �                    | j        d|��  �        }|dk    rt          �|�                    d�  �        st          d|� ��  �        �|dd �         S )Nr�   ��key�action�id�CAPCHA_NOT_READYr�   r�   r�   )r(   �resr!   r   r�   r   )r+   ry   r�   s      r   r}   zTwoCaptcha.get_result�  sn   � ��?�&�&�4�<��#�&�N�N���)�)�)�"�"��"�"�5�)�)� 	H��F�H�F�F�G�G�G�����|�r   c                 �b   � | j         �                    | j        d��  �        }t          |�  �        S )zZ
        get my balance

        Returns
        -------
        balance : float

        �
getbalance)r�   r�   )r(   r�   r!   ru   )r+   r�   s     r   �balancezTwoCaptcha.balance�  s,   � � �?�&�&�4�<��&�M�M���X���r   c                 �V   � |rdnd}| j         �                    | j        ||��  �         dS )z�
        report of solved captcha: good/bad

        Parameters
        ----------
        id_ : captcha ID
        correct : True/False

        Returns
        -------
        None.

        �
reportgood�	reportbadr�   N)r(   r�   r!   )r+   ry   �correct�reps       r   �reportzTwoCaptcha.report�  s6   � � &�6�l�l�;��������S�S��A�A�A��r   c                 �  �� ddddddddd	d
dddddd�}�fd�|�                     �   �         D �   �         }��                    dd�  �        }|o#|�                    |d         |d         d��  �         |�                    ��  �         |S )N�regsense�min_len�max_len�textinstructions�imginstructions�pageurl�	min_score�textcaptcha�recaptcharows�recaptchacols�
previousID�can_no_answer�
api_serverr"   �pingback)�caseSensitive�minLen�maxLenrb   rc   rD   �scorer>   �rows�cols�
previousId�canSkip�	apiServerr-   r#   c                 �J   �� i | ]\  }}|�v �	|��                     |�  �        �� S r   )�pop)�.0�k�vrI   s      �r   �
<dictcomp>z,TwoCaptcha.rename_params.<locals>.<dictcomp>  s9   �� � 
� 
� 
���1�1��;�;� �v�z�z�!�}�}�+6�;�;r   �proxy� �uri�type)r�   �	proxytype)�itemsr�   rx   )r+   rI   �replace�
new_paramsr�   s    `   r   r�   zTwoCaptcha.rename_params�  s�   �� � (���*�(�� �!�#�#�&�&�%��"�
� 
��$
� 
� 
� 
������
� 
� 
�
�
 �
�
�7�B�'�'��� 	�*�#�#��5�\��v��%
� %
� � ��
 	���&�!�!�!��r   c                 �6  � |�                     d| j        i�  �         |�                    d| j        �  �        }|�                    d| j        �  �        }|r|�                     d|i�  �         |r|�                     d|i�  �         t          |�  �        | _        |S )Nr�   r#   r-   )rx   r!   r�   r#   r"   �bool�has_callback)r+   rI   r#   r"   s       r   r�   zTwoCaptcha.default_params   s�   � ����u�d�l�+�,�,�,��:�:�j�$�-�8�8���*�*�X�t�|�4�4���:�V�]�]�J��#9�:�:�:��6�F�M�M�8�W�"5�6�6�6� ��N�N����r   c                 ��   � t          |�  �        | j        k    rt          d| j        � d��  �        �d� |D �   �         }|rt          d|� ��  �        �d� t          |�  �        D �   �         }|S )NzToo many files (max: �)c                 �P   � g | ]#}t           j        �                    |�  �        �!|��$S r   )r�   r�   r�   )r�   �fs     r   �
<listcomp>z,TwoCaptcha.extract_files.<locals>.<listcomp>4  s+   � �B�B�B�A�r�w�~�~�a�/@�/@�B�a�B�B�Br   r�   c                 �&   � i | ]\  }}d |dz   � �|��S )�file_r   r   )r�   �er�   s      r   r�   z,TwoCaptcha.extract_files.<locals>.<dictcomp>9  s(   � �?�?�?�d�a����1�����?�?�?r   )r�   r)   r   �	enumerate)r+   rj   �
not_existss      r   ro   zTwoCaptcha.extract_files.  s�   � ��u�:�:���&�&�%�9���9�9�9�;� ;� ;� C�B��B�B�B�
�� 	G�%�&E��&E�&E�F�F�F�?�?�i��.>�.>�?�?�?���r   c                 �h  � |�                     dd �  �        }|�                     di �  �        }|s||fS d|vrt          |�  �        dk    r||fS t          j        �                    |�  �        st          d|� ��  �        �|sd|�                     di �  �        i}|�                    d|i�  �         ||fS )Nr�   rj   r�   r�   r�   r7   )r�   r�   r�   r�   r�   r   rx   )r+   rI   �hintrj   s       r   r�   zTwoCaptcha.check_hint_img<  s�   � ��z�z�+�T�2�2���
�
�7�B�'�'��� 	!��5�=� ��d�{�{�s�4�y�y�2�~�~��5�=� ��w�~�~�d�#�#� 	A�%�&?��&?�&?�@�@�@�� 	5��V�Z�Z���3�3�4�E����'��.�/�/�/��u�}�r   )NNr   r   r   r   )r@   r   )r   r   )r	   r
   r   r2   r;   r>   rJ   rL   rP   rT   rV   r\   r`   rd   rg   rp   r6   rw   r5   rt   r}   r�   r�   r�   r�   ro   r�   r   r   r   r   r   $   s�  � � � � � � �� #�"%�!#�(�+� +� +� +�&� � �8� � �"� � � �@� � �0� � �0� � �.� � �B� � �*� � �@!� !� !�F� � �8� � �B� � � �<>� >� >�0� 0� 0�&� � �
� 
� 
�� � �� � �(!� !� !�F� � �� � �� � � � r   r   �__main__)r�   �sysr|   r�   r�   r   �apir   �ImportError�	Exceptionr   r   r   r   r   r   r	   �argvr�   �solr   r   r   �<module>r�      s�  �� �������� ���� ���� � � � � � ����������� � � �������������	� 	� 	� 	� 	�y� 	� 	� 	�	� 	� 	� 	� 	�*� 	� 	� 	�	� 	� 	� 	� 	�'� 	� 	� 	�	� 	� 	� 	� 	�#� 	� 	� 	�	� 	� 	� 	� 	�'� 	� 	� 	�k� k� k� k� k� k� k� k�\ �z���
�(�1�+�C�
�*�S�/�/�C�C�C� �s   � �-�-