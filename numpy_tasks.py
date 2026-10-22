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


def unique_columns(m):
    matr = np.asarray(m)
    return [np.unique(row).tolist() for row in matr.T]


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

#тесты
def test_sum_prod():
    matrices = [np.array([[3, 1], [1, 2]]), np.array([[1, 4], [2, 0]])]
    vectors = [np.array([[2], [5]]), np.array([[4], [1]])]
    expected = np.array([[19], [20]])
    result = sum_prod(matrices, vectors)

    assert np.array_equal(result, expected)
    assert result.shape == (2, 1)

    matrices2 = [np.array([[8, 6], [7, 10]]), np.array([[1, 5], [8, 4]])]
    vectors2 = [np.array([[0], [0]]), np.array([[0], [0]])]

    expected2 = np.array([[0], [0]])
    result2 = sum_prod(matrices2, vectors2)

    assert np.array_equal(result2, expected2)

def test_bin1():
    m = np.array([[2, 2], [2, 2]])
    threshold = 2
    expected = np.array([[0, 0], [0, 0]])
    result = binarize(m, threshold)
    assert np.array_equal(result, expected)

def test_bin2():
    m = np.array([[100, 100], [10, 10]])
    threshold = 5
    expected = np.array([[1, 1], [1, 1]])
    result = binarize(m, threshold)
    assert np.array_equal(result, expected)

def test_bin3():
    m = np.array([[1, 1], [4, 5]])
    threshold = 4
    expected = np.array([[0, 0], [0, 1]])
    result = binarize(m, threshold)
    assert np.array_equal(result, expected)

def test_unique_rows():
    m = np.array([[4, 5, 4], [12, 12, 12], [0, 1, 5]])
    assert unique_rows(m) == [[4, 5], [12], [0, 1, 5]]

def test_unique_col():
    matrix = [[1, 2, 3], [1, 5, 6], [1, 2, 9]]
    assert unique_columns(matrix) == [[1], [2, 5], [3, 6, 9]]

def test_matrix_statistics():
    m, n, seed = 4, 3, 2026
    stats = matrix_statistics(m, n, seed=seed)

    np.random.seed(seed)
    expected_matrix = np.random.normal(loc=0.0, scale=1.0, size=(m, n))
    np.testing.assert_allclose(stats.res_m, expected_matrix)
    np.testing.assert_allclose(stats.avg_rows, np.mean(stats.res_m, axis=1))
    np.testing.assert_allclose(stats.avg_columns, np.mean(stats.res_m, axis=0))
    np.testing.assert_allclose(stats.disp_rows, np.var(stats.res_m, axis=1))
    np.testing.assert_allclose(stats.disp_columns, np.var(stats.res_m, axis=0))

def test_chess():
    assert np.array_equal(chess(3, 3, 1, 0), np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]]))
    assert np.array_equal(chess(1, 1, 3, 2), np.array([[3]]))
    assert np.array_equal(chess(3, 2, 3, 4), np.array([[3, 4], [4, 3], [3, 4]]))

def test_draw_rectangle():
    img = draw_rectangle(8, 8, 4, 4, [0, 0, 255], [255, 255, 255])

    assert img.shape == (8, 8, 3)
    assert np.array_equal(img[0, 0], [0, 0, 255])
    assert np.array_equal(img[7, 7], [0, 0, 255])
    assert np.array_equal(img[4, 4], [255, 255, 255])


def test_draw_ellipse():
    img = draw_ellipse(7, 7, 3, 2, [0, 255, 0], [255, 0, 0])

    assert img.shape == (7, 7, 3)
    assert np.array_equal(img[0, 0], [0, 255, 0])
    assert np.array_equal(img[6, 6], [0, 255, 0])
    assert np.array_equal(img[3, 3], [255, 0, 0])

def test_analyze_time_series_1():
    time_row = [2, 1, 4, 5, 3]
    p = 3
    stats = analyze_time_series(time_row, p)

    assert stats.expected == 3.0
    np.testing.assert_allclose(stats.disp, np.var(time_row))
    np.testing.assert_allclose(stats.std, np.std(time_row))
    assert np.array_equal(stats.min_els, np.array([1]))
    assert np.array_equal(stats.max_els, np.array([3]))
    expected_smoothed = np.array([7 / 3, 10 / 3, 4.0])
    np.testing.assert_allclose(stats.smoothed, expected_smoothed)

def test_analyze_time_series_2():
    time_row = [10, 20, 30, 40, 50]
    p = 3

    stats = analyze_time_series(time_row, p)
    assert stats.expected == 30.0
    assert len(stats.min_els) == 0
    assert len(stats.max_els) == 0
    np.testing.assert_allclose(stats.smoothed, np.array([20.0, 30.0, 40.0]))

def test_one_hot_new_values():
    assert np.array_equal(one_hot([1, 3, 0]), np.array([[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0]]))
    assert np.array_equal(one_hot([2, 0, 2], class_count=5), np.array([[0, 0, 1, 0, 0], [1, 0, 0, 0, 0], [0, 0, 1, 0, 0]]))
    assert np.array_equal(one_hot([1, 1, 0]), np.array([[0, 1], [0, 1], [1, 0]]))
