�
    l��b�
  �                   �`   � d dl Z  G d� de�  �        Z G d� de�  �        Z G d� d�  �        ZdS )�    Nc                   �   � e Zd ZdS )�NetworkExceptionN��__name__�
__module__�__qualname__� �    �gC:\Users\Administrator\Documents\Projets\Rise of kingdom\Bluestacks Version\bot\utils\twocaptcha\api.pyr   r      �   � � � � � ��Dr
   r   c                   �   � e Zd ZdS )�ApiExceptionNr   r	   r
   r   r   r   
   r   r
   r   c                   �&   � e Zd Zdd�Zi fd�Zd� ZdS )�	ApiClient�2captcha.comc                 �   � || _         d S )N)�post_url)�selfr   s     r   �__init__zApiClient.__init__   s   � � ����r
   c                 �  � 	 d| j         z   dz   }|rTd� |�                    �   �         D �   �         }t          j        |||��  �        }d� |�                    �   �         D �   �          nod|v rUt          |�                    d�  �        d�  �        5 }t          j        ||d|i��  �        }ddd�  �         n# 1 swxY w Y   nt          j        ||�	�  �        }n&# t          j        $ r}t          |�  �        �d}~ww xY w|j	        d
k    rt          d|j	        � ��  �        �|j
        �                    d�  �        }d|v rt          |�  �        �|S )a�  
        
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

        �https://z/in.phpc                 �6   � i | ]\  }}|t          |d �  �        ��S )�rb)�open)�.0�key�paths      r   �
<dictcomp>z!ApiClient.in_.<locals>.<dictcomp>1   s(   � �N�N�N�9�3���d�4��.�.�N�N�Nr
   )�data�filesc                 �6   � g | ]}|�                     �   �         ��S r	   )�close)r   �fs     r   �
<listcomp>z!ApiClient.in_.<locals>.<listcomp>6   s    � �3�3�3�q������3�3�3r
   �filer   N)r   ��   �bad response: �utf-8�ERROR)r   �items�requests�post�valuesr   �pop�RequestExceptionr   �status_code�content�decoder   )r   r    �kwargs�current_url�respr#   �es          r   �in_zApiClient.in_   s�  � �4	&�$�T�]�2�9�<�K�� 2�N�N������N�N�N���}�[�*0�+0�2� 2� 2�� 4�3�E�L�L�N�N�3�3�3�3�3��6�!�!��&�*�*�V�,�,�d�3�3� <�q�#�=��.4�06��{�<� <� <�D�<� <� <� <� <� <� <� <� <� <� <���� <� <� <� <��  �}�[�*0�2� 2� 2���� �(� 	&� 	&� 	&�"�1�%�%�%�����	&���� ��s�"�"�"�#F�D�4D�#F�#F�G�G�G��|�"�"�7�+�+���d�?�?��t�$�$�$��s<   �B
C �B2�&C �2B6�6C �9B6�:C �C8�$C3�3C8c                 �:  � 	 d| j         z   dz   }t          j        ||��  �        }|j        dk    rt	          d|j        � ��  �        �|j        �                    d�  �        }d|v rt          |�  �        �n&# t          j        $ r}t	          |�  �        �d}~ww xY w|S )	a|  
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

        r   z/res.php)�paramsr&   r'   r(   r)   N)	r   r+   �getr0   r   r1   r2   r   r/   )r   r3   �current_url_outr5   r6   s        r   �reszApiClient.resP   s�   � �.	&�(���6�z�A�O��<���?�?�?�D���3�&�&�&�'J��8H�'J�'J�K�K�K��<�&�&�w�/�/�D��$���"�4�(�(�(� �� �(� 	&� 	&� 	&�"�1�%�%�%�����	&���� �s   �A2A5 �5B�B�BN)r   )r   r   r   r   r7   r<   r	   r
   r   r   r      sQ   � � � � � �!� !� !� !� � ;� ;� ;� ;�z&� &� &� &� &r
   r   )r+   �	Exceptionr   r   r   r	   r
   r   �<module>r>      s�   �� ����	� 	� 	� 	� 	�y� 	� 	� 	�	� 	� 	� 	� 	�9� 	� 	� 	�h� h� h� h� h� h� h� h� h� hr
   