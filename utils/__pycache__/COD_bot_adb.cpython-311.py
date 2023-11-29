�
    6Ud�6  �                   ��   � d dl Z d dlmZ d dlmZ d dlmZ d dlmZ	 d dl
Z
d dlZd dlmZmZmZ d dlmZmZmZmZmZmZmZ d dlZd dlZd dlmZ d d	lmZmZm Z m!Z! d
e_"        dZ#d dl$T  G d� d�  �        Z%d� Z&d� Z'dS )�    N)�date)�exists)�sleep)�Client)�array�where�ndarray)�cvtColor�matchTemplate�	minMaxLoc�COLOR_BGR2RGB�TM_CCOEFF_NORMED�COLOR_BGR2HSV�inRange)�Image)�current_time�get_data�get_path�writeT)�*c                   �   � e Zd Zdd�Zd� Zdd�Zd� Zdd�Zdefd	�Z	d
� Z
d� Zd� Zd� Zdd�Zd dedefd�Zd� Zdd�Zd� Zd� Zd� Zd� Zd� Zd� Zd� ZdS )!�Adb�	127.0.0.1�  c                 ��   � t          �   �         }t          ||�  �        | _        || _        || _        || _        |t          | j        �  �                 d         | _        t          �   �         | _	        d S )N�name)
r   �PPADBClient�client�host�port�number�strr   �ImageSingleton�images)�selfr!   r   r    �datas        �dC:\Users\Administrator\Documents\Projets\Rise of kingdom\Bluestacks Version\bot\utils\COD_bot_adb.py�__init__zAdb.__init__   s]   � ��z�z��!�$��-�-�����	���	������T�[�)�)�*�6�2��	�$�&�&�����    c                 �d   � t          d| j        � d| j        � ��  �         d| j        � d| j        � �S )NzJsonNumber:z port:)�printr!   r    �r%   s    r'   �__str__zAdb.__str__    s?   � ��:�D�K�:�:�t�y�:�:�;�;�;�;�T�[�;�;��	�;�;�;r)   c                 �"  � t          �   �         }t          �   �         }t          |t          | j        �  �                 d         �  �        | _        |d         �                    dd�  �        � }|� d|� d| j        � �}t          j        |�  �         d S )Nr    �	HD-Player�Playerr   �	 connect �:)	r   r   �intr"   r!   r    �replace�
subprocess�Popen)r%   r   r&   �path�adb_path�cmds         r'   �connect_to_devicezAdb.connect_to_device%   s�   � ��z�z���z�z����S���-�-�.�v�6�7�7��	��;�'�/�/��%�@�@�B���6�6�D�6�6�4�9�6�6���������r)   c                 �4   � | j         �                    �   �         S �N)r   �devicesr,   s    r'   �get_client_deviceszAdb.get_client_devices.   s   � ��{�"�"�$�$�$r)   c                 �  � 	 t          �   �         }t          |t          | j        �  �                 d         �  �        | _        | j        �                    |� d| j        � ��  �        }|��| �                    d�  �         t          �   �         }|d         �                    dd�  �        � }|� d|� d| j        � �}t          j
        |�  �         t          d�  �         |�| �                    �   �         S |S # t          $ �r}t          j        �   �          | �                    d	�  �         t          �   �         }|d         �                    dd�  �        � d
�}t          j
        |�  �         | �                    d�  �         t          d�  �         | �                    d�  �         |d         �                    dd�  �        � }|� d|� d| j        � �}t          j
        |�  �         t          d�  �         | �                    �   �         cY d }~S d }~ww xY w)Nr    r2   z,INFO : Device is None, trying to reconnect..r/   r0   r   r1   �   z&EXCEPTION : Error in connect to devicez start-serverzAdb restarting..�   zConnecting to the device..�   )r   r"   r!   r    r   �devicer+   r   r4   r5   r6   r   �
get_device�	Exception�	traceback�	print_exc)r%   r   r&   rC   r7   r8   r9   �es           r'   rD   zAdb.get_device1   s  � �"	%��:�:�D��D��T�[�!1�!1�2�6�:�;�;�D�I��[�'�'�4�(=�(=�$�)�(=�(=�>�>�F��~��
�
�J�K�K�K��z�z��"�;�/�7�7��%�H�H�J��!�>�>�D�>�>�4�9�>�>��� ��%�%�%��a�����>��?�?�,�,�,��M��� 	%� 	%� 	%���!�!�!��J�J�?�@�@�@��:�:�D��+�&�.�.�x��?�?�N�N�N�C���S�!�!�!��J�J�*�+�+�+��"�I�I�I��J�J�4�5�5�5��{�+�3�3�H�e�D�D�F�H��:�:��:�:�t�y�:�:�C���S�!�!�!��!�H�H�H��?�?�$�$�$�$�$�$�$�$�����#	%���s%   �C-C2 �0C2 �2H�=DH�H�H�textc                 ��   � t          �   �         }t          dt          j        �   �         � dt	          �   �         � d|t          | j        �  �                 d         � d|� ��  �         t          | j        |�  �         d S )Nz[ � z ] [ r   z ] )	r   r+   r   �todayr   r"   r!   r   r   )r%   rI   r&   s      r'   r+   z	Adb.printV   sq   � ��z�z���`�4�:�<�<�`�`�,�.�.�`�`�t�C���<L�<L�7M�f�7U�`�`�Z^�`�`�a�a�a��d�i������r)   c                 ��   � 	 | �                     �   �         �                    �   �         S #  t          d�  �         | �                     �   �         �                    �   �         cY S xY w�N�   )rD   �	screencapr   r,   s    r'   �%get_curr_device_screen_img_byte_arrayz)Adb.get_curr_device_screen_img_byte_array[   sY   � �	1��?�?�$�$�.�.�0�0�0��	1��!�H�H�H��?�?�$�$�.�.�0�0�0�0�0���s	   �%( �7A!c                 �  � 	 | �                     �   �         }|�#t          d�  �         | �                    �   �          t          j        |�                    �   �         �  �        }t          j        |�  �        }|S # t          $ rV}| �                    d�  �         t          d�  �         | �                    �   �          | �
                    �   �         cY d }~S d }~ww xY w)Nz)get_curr_device_screen_img device is nullzEXCEPTION : get_screen_devicerO   )rD   r+   r:   �io�BytesIOrP   r   �openrE   r   �get_curr_device_screen_img)r%   rC   �output�imagerH   s        r'   rV   zAdb.get_curr_device_screen_imgc   s�   � �	5��_�_�&�&�F��~��A�B�B�B��&�&�(�(�(��Z�� 0� 0� 2� 2�3�3�F��J�v�&�&�E��L��� 	5� 	5� 	5��J�J�7�8�8�8��!�H�H�H��"�"�$�$�$��2�2�4�4�4�4�4�4�4�4�����		5���s   �A4A7 �7
C�AC�C�Cc                 �  � 	 | �                     �   �         }t          |�  �        }t          |t          �  �        }|S #  t	          d�  �         | �                     �   �         }t          |�  �        }t          |t          �  �        }|cY S xY wrN   )rV   r   r
   r   r   )r%   �screens     r'   �get_cv2_imgzAdb.get_cv2_imgt   s   � �
	��4�4�6�6�F��6�]�]�F��f�m�4�4�F��M��	��!�H�H�H��4�4�6�6�F��6�]�]�F��f�m�4�4�F��M�M�M���s
   �9< �AB	c                 ��   � t          j        t          j        | �                    �   �         �                    �   �         �  �        �  �        }|�                    |dz   �  �         dS )Nz.pngT)r   rU   rS   rT   rD   rP   �save)r%   �	file_namerX   s      r'   �save_screenzAdb.save_screen�   sM   � ��
�2�:�d�o�o�&7�&7�&A�&A�&C�&C�D�D�E�E���
�
�9�v�%�&�&�&��tr)   ��������?c                 ��   � | �                     �   �         }t          |�  �        }t          |t          �  �        }t	          ||t
          �  �        }t          |�  �        \  }}}}	||k    r|	d         |	d         fS d S �Nr   rO   )rV   r   r
   r   r   r   r   )
r%   �img_to_find�
confidence�	pil_image�cv_image�result�min_val�max_val�min_loc�max_locs
             r'   �find_img_cvzAdb.find_img_cv�   sz   � ��3�3�5�5�	���#�#���H�m�4�4���x��6F�G�G��-6�v�->�->�*���'�7��Z����1�:�w�q�z�)�)��Fr)   N�target�sourcec                 �\  � 	 |�`| �                     �   �         }t          |�  �        }|dk    r|dd�dd�f         }|dk    r|dd�dd	�f         }t          |t          �  �        }| j        �                    |�  �        }t          ||t          �  �        }t          |�  �        \  }}}	}
||k    r)|dk    r|
d         dz   |
d
         fS |
d         |
d
         fS d S # t          $ rH}| �
                    d�  �         t          j        �   �          | �
                    |�  �         Y d }~d S d }~ww xY w)N�new_troops_buttonr   iB  i   �   �gem_search_buttoni�  iX  �   rO   z#Error occured when using find_image)rV   r   r
   r   r$   �get_file_namer   r   r   rE   r+   rF   rG   )r%   rm   rn   rd   re   rc   rg   rh   ri   rj   rk   �exception_errors               r'   �find_imgzAdb.find_img�   sf  � �	(��~� �;�;�=�=�	��y�)�)���0�0�0�#�A�c�E�3�t�8�O�4�F��0�0�0�#�C��G�Q�s�U�N�3�F�!�&�-�8�8���+�3�3�F�;�;�K�"�6�;�8H�I�I�F�1:�6�1B�1B�.�G�W�g�w���#�#��0�0�0�"�1�:��+�W�Q�Z�7�7��q�z�7�1�:�-�-����� 	(� 	(� 	(��J�J�<�=�=�=���!�!�!��J�J��'�'�'�'�'�'�'�'�'�����	(���s   �CC �C �
D+�#=D&�&D+c                 �   � | j         �                    |�  �        }t          ||t          �  �        }t	          |�  �        \  }}}}	||k    r|	d         |	d         fS d S rb   )r$   rt   r   r   r   )
r%   �srcrm   rd   rc   rg   rh   ri   rj   rk   s
             r'   �find_img_src_confzAdb.find_img_src_conf�   sb   � ��k�/�/��7�7���s�K�1A�B�B��-6�v�->�->�*���'�7��Z����1�:�w�q�z�)�)��Fr)   c                 �  � | �                     �   �         }t          |�  �        }t          |t          �  �        }| j        �                    |�  �        }|dk    r|dd�dd�f         }t          ||t          �  �        }|j        d         }|j        d         }t          |�  �        \  }	}
}}|}t          ||k    �  �        }t          t          |d d d�         � �  �        }g }|D ]C}t          |d         �  �        t          |d         �  �        ||g}|�                    |�  �         �Dg }t          t!          |�  �        �  �        D ]j}|dk    r3|�                    ||         d         dz   ||         d         f�  �         �;|�                    ||         d         ||         d         f�  �         �kg }t          t!          |�  �        dz
  �  �        D ]�}||         d         dz   ||dz            d         k    sE||         d         dz
  ||dz            d         k    s!||         d         ||dz            d         k    r�||         d         dz   ||dz            d         k    sE||         d         dz
  ||dz            d         k    s!||         d         ||dz            d         k    r|�                    ||         �  �         ��|D ]}|�                    |�  �         �|S )N�	back_iconr   i�  i�  rq   rO   �����)rV   r   r
   r   r$   rt   r   r   �shaper   r   �list�zipr3   �append�range�len�remove)r%   rm   rd   re   rf   rc   rg   �needle_w�needle_hrh   ri   rj   rk   �
min_thresh�location�
rectangles�loc�rect�localisations�i�element_to_delete�elements                         r'   �find_multiple_imgzAdb.find_multiple_img�   s  � ��3�3�5�5�	���#�#���H�m�4�4�� �k�/�/��7�7���[� � ���#��t�D�y� 0�1�H��x��6F�G�G���$�Q�'���$�Q�'��-6�v�->�->�*���'�7��
���:�-�.�.����X�d�d��d�^�,�-�-�� �
�� 	$� 	$�C���A��K�K��S��V���h��A�D����d�#�#�#�#� ���s�:���'�'� 	K� 	K�A���$�$� �$�$�j��m�A�&6��&=�z�!�}�Q�?O�%P�Q�Q�Q�Q��$�$�j��m�A�&6�
�1��a�8H�%I�J�J�J�J����s�=�)�)�A�-�.�.� 	;� 	;�A�"�1�%�a�(�1�,��a�!�e�0D�Q�0G�G�G�"�1�%�a�(�1�,��a�!�e�0D�Q�0G�G�G�"�1�%�a�(�M�!�a�%�,@��,C�C�C� +�1�-�a�0�1�4��a�!�e�8L�Q�8O�O�O�*�1�-�a�0�1�4��a�!�e�8L�Q�8O�O�O�*�1�-�a�0�M�!�a�%�4H��4K�K�K�!�(�(��q�)9�:�:�:�� )� 	*� 	*�G�� � ��)�)�)�)��r)   c                 �H   � d}| �                     |�  �        }d|v pd|v pd|v S )Nz3dumpsys activity activities | grep mFocusedActivity�
lilithgame�rok�lilithgames��shell)r%   �string�as      r'   �is_game_alivezAdb.is_game_alive�   s6   � �F���J�J�v�����q� �D�E�Q�J�D�-�1�2D�Dr)   c                 �@   � d|� d|� �}| �                     |�  �         d S )Nz
input tap rK   r�   )r%   �x�yr�   s       r'   �clickz	Adb.click�   s.   � �%�a�%�%�!�%�%���
�
�6�����r)   c                 �  � | �                     �   �         }	 |�                    |�  �        S # t          $ rO t          t          �  �         t	          d�  �         | �                    �   �          | �                    |�  �        cY S w xY w)N�   )rD   r�   �RuntimeErrorr+   r   r:   )r%   r�   rC   s      r'   r�   z	Adb.shell�   s�   � ����"�"��	&��<�<��'�'�'��� 	&� 	&� 	&��,�����!�H�H�H��"�"�$�$�$��:�:�f�%�%�%�%�%�		&���s   �+ �AB�Bc           	      �N   � d|� d|� d|� d|� d�	}| �                     |�  �         d S )N�input swipe rK   z 420r�   )r%   r�   r�   �x2�y2r�   s         r'   �swipez	Adb.swipe  sA   � �5��5�5�A�5�5��5�5�R�5�5�5���
�
�6�����r)   c           
      �R   � d|� d|� d|� d|� d|� �
}| �                     |�  �         d S )Nr�   rK   r�   )r%   r�   r�   r�   r�   �argr�   s          r'   �	swipe_argzAdb.swipe_arg	  sF   � �7��7�7�A�7�7��7�7�R�7�7�#�7�7���
�
�6�����r)   c                 ��  � 	 t          �   �         }|d         d d�         dz   }t          |d         � �  �        r0|d         d d�         dz   }t          j        |d         � |� �  �         t	          |� d�  �        5 }|�                    �   �         �                    d�  �        }d d d �  �         n# 1 swxY w Y   n#  t          d�  �         Y nxY wg }|D ]+}d|v rd|v rd	|vsd|v rd
|v r|�                    |�  �         �,i }t          dt          |�  �        d�  �        D �]C}||         �                    d�  �        }|d         �                    dd�  �        |d<   |d         dd �         |d<   i |t          t          |�  �        �  �        <   t          |d         �  �        |t          t          |�  �        dz
  �  �                 d<   |d         |t          t          |�  �        dz
  �  �                 d<   ||dz            �                    d�  �        }	|	d         �                    dd�  �        |	d<   |	d         |t          t          |�  �        dz
  �  �                 d<   ��Ed S )N�
bluestacks�����z.txt�r�
zsThe pass you provided is wrong ! We are looking for something like : 
 C:\ProgramData\BlueStacks_nxtluestacks.confzbst.instance.Nougat64�adb_port�status�display_namer   r@   z
.adb_port=rO   �"� �   �instancer    z.display_name=r   )r   r   �shutil�copyrU   �read�splitr+   r�   r�   r�   r4   r"   )
r%   r7   r�   �file�data_instance�
liste_infor�   �dico_instancer�   �string2s
             r'   �restart_emulatorzAdb.restart_emulator%  s�  � �	I��:�:�D��,�'����,�v�5�F��$�|�,�.�/�/� D��l�+�C�R�C�0�6�9�����\� 2�4�&�l�C�C�C��&�l�C�(�(� 8�D� $�	�	��� 1� 1�$� 7� 7��8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8���� 8� 8� 8� 8���	I�� H�I� I� I� I� I���� �
�$� 	+� 	+�G�)�W�4�4�:��;P�;P�W_�gn�Wn�Wn�,��7�7�n�PW�>W�>W��!�!�'�*�*�*�����q�#�j�/�/�1�-�-� 		L� 		L�A���]�(�(��6�6�F��q�	�)�)�#�r�2�2�F�1�I��q�	�"�#�#��F�1�I�57�M�#�c�-�0�0�1�1�2�EH��PQ��^�^�M�#�c�-�0�0�1�4�5�5�6�z�B�AG���M�#�c�-�0�0�1�4�5�5�6�v�>� ��Q��'�-�-�.>�?�?�G� ���+�+�C��4�4�G�A�J�AH���M�#�c�-�0�0�1�4�5�5�6�v�>�>�		L� 		Ls0   �A8B: �:(B.�"B: �.B2�2B: �5B2�6B: �:Cc                 �0   � | �                     d�  �         d S )Nzinput keyevent KEYCODE_HOMEr�   r,   s    r'   �home_buttonzAdb.home_buttonE  s   � ��
�
�0�1�1�1�1�1r)   )r   r   )r   )r`   )Nr`   )�__name__�
__module__�__qualname__r(   r-   r:   r>   rD   r"   r+   rQ   rV   r[   r_   rl   r	   rv   ry   r�   r�   r�   r�   r�   r�   r�   r�   � r)   r'   r   r      s�  � � � � � �'� '� '� '�<� <� <�
� � � �%� %� %�#%� #%� #%� #%�J�� � � � �
1� 1� 1�5� 5� 5�"� � �� � �
	� 	� 	� 	�(� (�c� (�G� (� (� (� (�:� � �6� 6� 6� 6�pE� E� E�� � �
&� &� &�� � �
� � �8L� L� L�@2� 2� 2� 2� 2r)   r   c                 ��   � dt           j        _        t          j        | dd��  �        �                    dd�  �        �                    dd�  �        �                    dd�  �        }|S )	Nztesseract\tesseract.exe�engz--psm 6)�lang�config�	r�   r�   �)�tess�pytesseract�tesseract_cmd�image_to_stringr4   )re   rg   s     r'   �img_to_stringr�   d  sW   � �%?�D��"��!�)�%�	�J�J�J�	���r�	�	�7�7�4��,�,�W�W�T�2�->�->� ��Mr)   c                 �N   � t          | t          �  �        }t          |||�  �        S r<   )r
   r   r   )rf   �lower�upper�hsvs       r'   �&img_remove_background_and_enhance_wordr�   l  s#   � �
�8�]�
+�
+�C��3��u�%�%�%r)   )(r�   �datetimer   �os.pathr   �timer   �ppadb.clientr   r   r5   rF   �numpyr   r   r	   �cv2r
   r   r   r   r   r   r   rS   r�   r�   �PILr   �utils.Task_utilsr   r   r   r   �LOAD_TRUNCATED_IMAGES�bridge�utils.resourcesr   r�   r�   r�   r)   r'   �<module>r�      s  �� ���� � � � � � � � � � � � � � � � � � � .� .� .� .� .� .� � � � � � � � � '� '� '� '� '� '� '� '� '� '� k� k� k� k� k� k� k� k� k� k� k� k� k� k� k� k� k� k� 	�	�	�	� � � � � � � � � � � D� D� D� D� D� D� D� D� D� D� D� D�"�� �	�� � � � �p2� p2� p2� p2� p2� p2� p2� p2�\
� � �&� &� &� &� &r)   