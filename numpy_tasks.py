import numpy as np
import matplotlib.pyplot as plt

def sum_prod(matrices, vectors):
    resultVs = []
    for i in range(0, len(matrices)):
        resultVs.append(np.dot(matrices[i], vectors[i]))
    return np.sum(resultVs, axis=0)


def binarize(m, threshold):
    return np.where(m > threshold, 1, 0)


def unique_rows(m):
    return [list(np.unique(row)) for row in m]


class MatrixStatistics:
    def __init__(self, res_m, avg_rows, avg_columns, disp_rows, disp_columns):
        self.res_m = res_m
        self.avg_rows = avg_rows
        self.avg_columns = avg_columns
        self.disp_rows = disp_rows
        self.disp_columns = disp_columns


def matrix_statistics(m, n, loc=0.0, scale=1.0, seed=None):
    if seed is not None:
        np.random.seed(seed)
    res_m = np.random.normal(loc=loc, scale=scale, size=(m, n))
    avg_rows = np.mean(res_m, axis=1)
    avg_columns = np.mean(res_m, axis=0)
    disp_rows = np.var(res_m, axis=1)
    disp_columns = np.var(res_m, axis=0)
    return MatrixStatistics(res_m, avg_rows, avg_columns, disp_rows, disp_columns)


def make_hist(data):
    fig1, axes1 = plt.subplots(1, 2, figsize=(12, 5))
    fig1.canvas.manager.set_window_title("Статистика по строкам")

    axes1[0].hist(data.avg_rows, bins=15, color="red")
    axes1[0].set_title("Среднее значение")
    axes1[1].hist(data.disp_rows, bins=15, color="blue")
    axes1[1].set_title("Дисперсия")
    for ax in axes1:
        ax.set_xlabel("Значение")
        ax.set_ylabel("Частота")

    fig2, axes2 = plt.subplots(1, 2, figsize=(12, 5))
    fig2.canvas.manager.set_window_title("Статистика по столбцам")

    axes2[0].hist(data.avg_columns, bins=15, color="red")
    axes2[0].set_title("Среднее значение")
    axes2[1].hist(data.disp_columns, bins=15, color="blue")
    axes2[1].set_title("Дисперсия")
    for ax in axes2:
        ax.set_xlabel("Значение")
        ax.set_ylabel("Частота")

    plt.show()


def chess(m, n, a, b):
    matr = np.full((m, n), b)
    matr[::2, ::2] = a
    matr[1::2, 1::2] = a
    return matr


def draw_rectangle(m, n, height, width, bg_color, rect_color):
    image = np.zeros((m, n, 3), dtype=np.uint8)
    image[:, :] = bg_color

    y0 = m // 2
    x0 = n // 2
    start_y = y0 - (height // 2)
    end_y = y0 + (height // 2)
    start_x = x0 - (width // 2)
    end_x = x0 + (width // 2)
    image[start_y:end_y, start_x:end_x] = rect_color

    return image


def draw_ellipse(m, n, a, b, bg_color, el_color):
    image = np.zeros((m, n, 3), dtype=np.uint8)
    image[:, :] = bg_color

    y0 = m // 2
    x0 = n // 2
    y, x = np.ogrid[:m, :n]
    check = (x - x0) ** 2 * b ** 2 + (y - y0) ** 2 * a ** 2 <= a ** 2 * b ** 2
    image[check] = el_color
    return image


class TimeSeriesStatistics:
    def __init__(self, expected, disp, std, max_els, min_els, smoothed):
        self.expected = expected
        self.disp = disp
        self.std = std
        self.max_els = max_els
        self.min_els = min_els
        self.smoothed = smoothed


def analyze_time_series(time_row, p):
    data_arr = np.asarray(time_row)

    expected = np.mean(data_arr)
    disp = np.var(data_arr)
    std = np.std(data_arr)

    is_max = (data_arr[1:-1] > data_arr[:-2]) & (data_arr[1:-1] > data_arr[2:])
    is_min = (data_arr[1:-1] < data_arr[:-2]) & (data_arr[1:-1] < data_arr[2:])

    max_els = np.where(is_max)[0] + 1
    min_els = np.where(is_min)[0] + 1

    smoothed = np.convolve(data_arr, np.ones(p)/p, 'valid')

    return TimeSeriesStatistics(expected, disp, std, max_els, min_els, smoothed)


def one_hot(vec, class_count=None):
    v_arr = np.array(vec)
    if class_count is None:
        class_count = np.max(v_arr) + 1
    return np.eye(class_count, dtype=int)[v_arr]

