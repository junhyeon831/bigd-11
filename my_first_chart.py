import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"
fig, ax = plt.subplots(figsize=(7, 4))
temperature = [26, 21, 20, 17, 21]
days = ['월', '화', '수', '목', '금']
ax.plot(days, temperature)
for i, p in enumerate(temperature):
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points",
    xytext=(0, 2), ha="center")
ax.set_title("이번 주 춘천 최고 온도")
fig.savefig("my_first_chart.png")
 