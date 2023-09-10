import matplotlib.pyplot as plt

def make_graph_pdf(plot_data, hist_data, pdf, file_name, param_name, label_name, ylim = 1.5):
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['font.size'] = 42  # 適当に必要なサイズに
    plt.rcParams['xtick.direction'] = 'in'  # in or out
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['axes.xmargin'] = 0.01
    plt.rcParams['axes.ymargin'] = 0.01
    plt.rcParams["legend.fancybox"] = False  # 丸角OFF
    plt.rcParams["legend.framealpha"] = 1  # 透明度の指定、0で塗りつぶしなし
    plt.rcParams["legend.edgecolor"] = 'black'  # edgeの色を変更
    
    # plt.xlim(0, np.pi * 2)
    
    fig = plt.figure(figsize=(12,10), dpi=72)
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(plot_data, pdf, label=label_name, color = "black", linewidth = 10)
    ax.hist(hist_data, density=True, bins=50, alpha=0.5, label=param_name)
    # plt.show()
    ax.set_ylim(0, ylim)
    ax.legend(fontsize=30)
    ax.set_xlabel("Observed data")
    ax.set_ylabel('Probability of occurrence')
    plt.savefig( file_name + '.svg')