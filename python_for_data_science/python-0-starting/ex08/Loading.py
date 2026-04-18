import os


class EstTime:
    def __init__(self):
        self.estimated_time = 0.0
        self.est_min = 0
        self.est_sec = 0
        self.t_min = 0
        self.t_sec = 0


def estimate_time(est, starting_time):
    """Calculate estimated and remaining time"""
    est.est_min = int(est.estimated_time) // 60
    est.est_sec = int(est.estimated_time) % 60
    est.t_min = int(os.times().elapsed - starting_time) // 60
    est.t_sec = int(os.times().elapsed - starting_time) % 60


def fill_bar(width, bar_size):
    """Fills the display bar output"""
    bars = ""
    i = 0
    while i < width:
        if i < round(bar_size):
            bars += "█"
        else:
            bars += " "
        i += 1

    return bars


def ft_tqdm(lst: range) -> None:
    """Tqdm imitation"""
    width = os.get_terminal_size().columns - 40
    bars = ""
    i = 0
    it = 0
    state = 0
    starting_time = os.times().elapsed
    est = EstTime()

    while i < len(lst):
        time = os.times().elapsed
        while os.times().elapsed - time \
                < 0.08 and state < 100 and i < len(lst):
            i += 1
            state = i / len(lst) * 100
            bar_size = i / len(lst) * width
            bars = fill_bar(width, bar_size)
            if it:
                est.estimated_time = (len(lst) - i) / it
                estimate_time(est, starting_time)
            yield i
        it = float(i) / (os.times().elapsed - starting_time)
        print(
            f"{state:.0f}%|{bars}| {i}/{len(lst)} "
            f"[{est.t_min:02d}:{est.t_sec:02d}<"
            f"{est.est_min:02d}:{est.est_sec:02d}, "
            f"{it:.2f}it/s]",
            end="\r"
        )
