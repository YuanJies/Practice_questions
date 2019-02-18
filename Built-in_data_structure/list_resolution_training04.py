# "0001.abadicddws" 是ID格式，要求ID格式是以点号分割，左边是4位从1开始的整数，
#    右边是10位随机小写英文字母。请依次生成前100个ID的列表
	
# '0001.jkldsrtyij'
# '0002.qazedcvfrt'
# ....
# '0100.olmkijnhub'

# 示例：(Wayne)
import random
['{:04}.{}'.format(n, ''.join([random.choice(bytes(range(97, 123)).decode()) for _ in range(10)])) for n in range(1, 101)]

#--------------------------------------------------------------------------------------------------------------------------

import random
["{:04}.{}".format(i, "".join([chr(random.randint(97, 122)) for j in range(10)])) for i in range(1, 101)]

#--------------------------------------------------------------------------------------------------------------------------

import string
['{:>04}.{}'.format(i, ''.join(random.choice(string.ascii_lowercase) for _ in range(0, 10))) for i in range(1, 101)]

#--------------------------------------------------------------------------------------------------------------------------


# 示例2：(其他)
import random
['0'*(4-len(str(n)))+str(n)+'.'+''.join(['abcdefghijklmnopqrstuvwxyz'[random.randint(0, 25)] for _ in range(10)]) for n in range(1, 101)]

#--------------------------------------------------------------------------------------------------------------------------

import random
import string
[print('{:0>4d}.{}'.format(i, "".join(random.sample(string.ascii_lowercase, 10))), end="\n") for i in range(1, 101)]

#--------------------------------------------------------------------------------------------------------------------------

import random 
['{:04}.{}'.format(i, "".join(random.sample([chr(i) for i in range(97, 123)], 10))) for i in range(1, 101)]

#--------------------------------------------------------------------------------------------------------------------------

import random
alpha_1 = 'abcdefghijklmnopqrstuvwxyz'
id_1 = ['{:04}.{}'.format(i, "".join([random.choice(alpha_1) for _ in range(10)])) for i in range(1, 101)]
print('\n'.join(id_1))
