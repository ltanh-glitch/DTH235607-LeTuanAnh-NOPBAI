from __future__ import annotations

import numpy as np
from sklearn import linear_model

HEIGHT_CM = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
WEIGHT_KG = np.array([49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])


def build_models():
    one = np.ones((HEIGHT_CM.shape[0], 1))
    Xbar = np.concatenate((one, HEIGHT_CM), axis=1)
    A = np.dot(Xbar.T, Xbar)
    b = np.dot(Xbar.T, WEIGHT_KG)
    w = np.dot(np.linalg.pinv(A), b)

    sklearn_model = linear_model.LinearRegression()
    sklearn_model.fit(HEIGHT_CM, WEIGHT_KG)

    return w, sklearn_model


def show_parameters(w: np.ndarray, sklearn_model: linear_model.LinearRegression) -> None:
    print("Manual solution vs scikit-learn:")
    print(
        f"  our solution   : w_1 = {w[1]:.12f}, w_0 = {w[0]:.12f}"
    )
    print(
        f"  scikit-learn   : w_1 = {sklearn_model.coef_[0]:.12f}, w_0 = {sklearn_model.intercept_:.12f}"
    )


def predict_weight(model: linear_model.LinearRegression, height: float) -> float:
    return float(model.coef_[0] * height + model.intercept_)


def prompt_height() -> float | None:
    try:
        raw = input("Nhập chiều cao (cm) hoặc ENTER để kết thúc: ").strip()
        if raw == "":
            return None
        return float(raw)
    except ValueError:
        print("Giá trị không hợp lệ.")
        return None


def main() -> None:
    w, sklearn_model = build_models()
    show_parameters(w, sklearn_model)
    print("(Dựa trên dữ liệu ví dụ, mô hình hồi quy dự đoán cân nặng theo chiều cao.)")
    while True:
        height = prompt_height()
        if height is None:
            print("Kết thúc chương trình.")
            break
        weight = predict_weight(sklearn_model, height)
        print(
            f"Chiều cao {height:.2f} cm => dự đoán cân nặng khoảng {weight:.2f} kg\n"
        )


if __name__ == "__main__":
    main()
