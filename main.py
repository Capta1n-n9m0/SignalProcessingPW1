import matplotlib.pyplot as plt
import statistics

def main():
    data = list()
    with open("ICE.txt", 'r') as ICE:
        for line in ICE.readlines():
            line_data = line.split("   ")
            line_data.pop(0)
            line_data[12] = line_data[12][:-1]
            for index in range(0, 13):
                line_data[index] = float(line_data[index])
            data.append(line_data)
    # data:
    # [
    #   [year, data, data, data, data, data, data, data, data, data, data, data, data],
    #   [year, data, data, data, data, data, data, data, data, data, data, data, data],
    #   [year, data, data, data, data, data, data, data, data, data, data, data, data],
    #   [year, data, data, data, data, data, data, data, data, data, data, data, data],
    #   [year, data, data, data, data, data, data, data, data, data, data, data, data],
    #   [year, data, data, data, data, data, data, data, data, data, data, data, data],
    #    ...
    # ]


    month_data = list()
    for ii in data:
        for index in range(1, 13):
            time = ii[0] + (1/12)*(index-1)
            month_data.append((time, ii[index]))
    # month_data:
    # [
    #     [year + month, data],
    #     [year + month, data],
    #     [year + month, data],
    #     [year + month, data],
    #     [year + month, data],
    #     [year + month, data],
    #      ...
    # ]
    with open("ICE_MONTH.txt", 'w') as ICE_MONTH:
        for ii in month_data:
            print(f"   {ii[0]:.7e}   {ii[1]:.7e}", file=ICE_MONTH)


    time_axis = [ii[0] for ii in month_data]
    ice_axis  = [ii[1] for ii in month_data]

    ICE_AVG   = statistics.mean(ice_axis)
    ICE_STDV  = statistics.stdev(ice_axis)
    based_ice_axis = [ii[1]-ICE_AVG for ii in month_data]

    plt.figure(figsize=(100, 10))

    plt.plot(time_axis, based_ice_axis)

    plt.show()
    print(ICE_AVG)
    print(ICE_STDV)


if __name__ == '__main__':
    main()
