def min_operations_to_zero(temperature):
    operations = 0
    n = len(temperature)

    # 从右向左遍历
    for i in range(n - 1, -1, -1):
        if temperature[i] > 0:
            # 对于每一个温度，累加操作次数
            operations += temperature[i]
            # 将当前温度降低到 0，并将其影响到前面的温度
            if i > 0:
                temperature[i - 1] = max(temperature[i - 1] - temperature[i], 0)

    return operations


# 测试
n = 3
temperature = [2, 4, 4]
result = min_operations_to_zero(temperature)
print("最小操作数:", result)  # 输出应为 4
