class width_search:
    g_dict_states = {}
    # 每个位置可交换的位置集合
    g_dict_shifts = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
                     3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
                     6: [3, 7], 7: [4, 6, 8], 8: [5, 7]}
    def __init__(self, srcState, destState):
        self.srcState = srcState
        self.destState = destState

    # 计算逆序数
    def calSum(self, layout):
        sum = 0
        for i in range(1, 9):  # 1-8
            aSum = 0  # 逆序数和
            for j in range(0, i):
                if layout[j] > layout[i] and layout[i] != '0':
                    aSum += 1
            sum += aSum
        return sum

    # 判断是否可解：判断srcLayout和destLayout逆序值是否同是奇数或偶数
    def hasSolve(self):
        src = self.calSum(self.srcState)
        dest = self.calSum(self.destState)
        return (src % 2 == dest % 2)

    def swap_list(self, a, i, j):
        if i > j:
            i, j = j, i
        # 得到ij交换后的数组
        b = a[:i] + a[j] + a[i + 1:j] + a[i] + a[j + 1:]
        return b

    def search(self):
        # 先进行判断srcLayout和destLayout逆序值是否同是奇数或偶数
        # 这是判断起始状态是否能够到达目标状态，同奇同偶时才是可达
        if self.hasSolve() != True:  # 一个奇数一个偶数，不可达
            return -1, None

        # 初始化字典
        self.g_dict_states[self.srcState] = -1
        stateList = []
        stateList.append(self.srcState)  # 当前状态存入列表

        while len(stateList) > 0:
            curState = stateList.pop(0)  # 出栈
            if curState == self.destState:  # 判断当前状态是否为目标状态
                break
            # 寻找0的位置。
            spacIndex = curState.index("0")
            lst_shifts = self.g_dict_shifts[spacIndex]  # 当前可进行交换的位置集合
            for nShift in lst_shifts:
                newState = self.swap_list(curState, nShift, spacIndex)
                if self.g_dict_states.get(newState) == None:  # 判断交换后的状态是否已经查询过
                    self.g_dict_states[newState] = curState  # g_dict_states[子序列] = 父序列
                    stateList.append(newState)  # 存入集合
        lst_steps = []
        lst_steps.append(curState)
        while self.g_dict_states[curState] != -1:  # 存入路径 直到遍历到起始序列
            curState = self.g_dict_states[curState]  # 递归遍历
            lst_steps.append(curState)
        lst_steps.reverse()  # 反转
        return 0, lst_steps
if __name__ == "__main__":
    # srcState = "541203786"
    # destState = "123804765"
    srcState = "013425786"
    destState = "647850321"
    width = width_search(srcState, destState)
    retCode, lst_steps = width.search()
    if retCode != 0:
        print("未找到路径")
    else:
        print("广度优先算法:已经找到路径")
        for nIndex in range(len(lst_steps)):
            print("step #" + str(nIndex + 1))
            print(lst_steps[nIndex][:3])
            print(lst_steps[nIndex][3:6])
            print(lst_steps[nIndex][6:])
            if nIndex != len(lst_steps) - 1:
                print('->')