from season2.module.a.aa import module_AA
a.aa.module_AA.fun_AA()

from a.aa import module_AA
module_AA.fun_AA()

from a.aa.module_AA import fun_AA
fun_AA()

from .. import module_A     # .. ��ʾ�ϼ�Ŀ¼ . ��ʾͬ��Ŀ¼
from . import module_A2     # . ��ʾͬ��Ŀ¼
