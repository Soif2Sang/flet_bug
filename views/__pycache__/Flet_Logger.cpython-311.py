�
    �Ud  �                   �p   � d dl Zd dlmZmZ  G d� dej        �  �        Zd� Z G d� dej        �  �        ZdS )�    N)�get_data�
write_datac                   �,   � � e Zd Z� fd�Zddefd�Z� xZS )�Loggerc                 ��   ��  t          �   �         j        di |�� t          �   �         }d|vrddd�|d<   t          |�  �         |d         d         | _        || _        || _        d S )N�	interfaceT��auto_scroll�auto_refreshr
   � )�super�__init__r   r   r
   �parent�page)�self�framer   �kwargs�data�	__class__s        ��dC:\Users\Administrator\Documents\Projets\Rise of kingdom\Bluestacks Version\bot\views\Flet_Logger.pyr   zLogger.__init__   sx   �� ������"�"�6�"�"�"��z�z���d�"�"�15�� M� M�D����4�����{�+�M�:��������	�	�	�    N�textec                 �8  � |�&t          j        |t           j        j        ��  �        }n&t          j        |t           j        j        |��  �        }| j        �                    |�  �         | j        | j        j        d         k    r| �                    �   �          d S d S �N)�value�weight)r   r   �color�����)	�ft�Text�
FontWeight�W_600�controls�appendr   r   �update�r   r   r   �texts       r   �add_textzLogger.add_text   s�   � ��=��7��b�m�.A�B�B�B�D�D��7��r�}�/B�%�P�P�P�D�����T�"�"�"��;�$�)�,�R�0�0�0��K�K�M�M�M�M�M� 1�0r   �N��__name__�
__module__�__qualname__r   �strr(   �__classcell__�r   s   @r   r   r      sX   �� � � � � �� � � � �� �S� � � � � � � � r   r   c                  �   � d S r)   r   r   r   r   �get_dater2      s   � ��Dr   c                   �,   � � e Zd Z� fd�Zddefd�Z� xZS )�LoggerUpgradec                 �   ��  t          �   �         j        di |�� t          �   �         }d|vrddd�|d<   t          |�  �         d| _        || _        d S )Nr   Tr	   r   )r   r   r   r   r
   r   )r   r   r   r   r   s       �r   r   zLoggerUpgrade.__init__    sg   �� ������"�"�6�"�"�"��z�z���d�"�"�15�� M� M�D����4���������	�	�	r   Nr   c                 �V  � |�&t          j        |t           j        j        ��  �        }n&t          j        |t           j        j        |��  �        }| j        �                    |�  �         t          | j        j        d         t           j        �  �        s| �	                    �   �          d S d S r   )
r   r    r!   r"   r#   r$   �
isinstancer   �Dividerr%   r&   s       r   r(   zLoggerUpgrade.add_text)   s�   � ��=��7��b�m�.A�B�B�B�D�D��7��r�}�/B�%�P�P�P�D�����T�"�"�"��$�)�,�R�0���<�<� 	��K�K�M�M�M�M�M�	� 	r   r)   r*   r0   s   @r   r4   r4      sX   �� � � � � �� � � � �� �S� � � � � � � � r   r4   )	�fletr   �utils.Task_utilsr   r   �ListViewr   r2   r4   r   r   r   �<module>r<      s�   �� � � � � 1� 1� 1� 1� 1� 1� 1� 1�� � � � �R�[� � � �*	� 	� 	�� � � � �B�K� � � � � r   