def calculate_performance(cycles_with, cycles_without):
    if cycles_without > 0:
        improvement = ((cycles_without - cycles_with) / cycles_without) * 100
        return improvement
    else:
        return 0
