from sklearn import metrics
from sklearn.cluster import DBSCAN

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

centers = [[1, 1], [-1, -1], [1, -1]]

# make_blobs = 지정한 중심 주변에 무작위로 점들을 생성
# n_samples = 데이터 포인트 750개
# cluster_std = 중심 주변으로 데이터가 퍼지는 정도. 작을수록 군집이 조밀
# random_state = 실행할 때마다 같은 난수 데이터를 생성하도록 고정

# X = 각 데이터 포인트 좌표가 들어있는 2차원 배열 형태
# labels_true = 각 데이터가 원래 어느 군집(클러스터)에서 생성됬는지를 나타내는 정답 레이블
# - 0은 [1,1], 1은 [-1, -1], 2는 [1, -1]
X, labels_true = make_blobs(
  n_samples=750, centers=centers, cluster_std=0.4, random_state=0
)


"""
# 데이터 표준화
# z = x- μ(mu) / σ(sigma)
# μ = 해당 열의 평균
# σ = 해당 열의 표준편차
"""

# X.mean(axis=0) # 대략 [0,0]
# X.std(axis=0) # 대략 [1,1]

# fit 과 transform 을 연속으로 수행
# - fit은 각 열의 평균과 표준편차 계산
# - transform 은 계산한 값으로 X 변환
X = StandardScaler().fit_transform(X)

# plt.scatter(X[:, 0], X[:, 1])
# plt.show()


"""
# eps = 샘플간 떨어진 거리 / min_samples = 클러스터 내 코어샘플의 개수
# higher min_samples, lower eps need more density
# Core Samples = eps 거리 내에 서로 다른 min_samples 개의 샘플이 존재하는 샘플로 정의
# NonCore Samples = Core Sample의 이웃이지만 그 자체가 Core Sample은 아님
# Outlier
"""

# DBSCAN은 데이터 사이의 거리와 eps를 기준으로 군집을 만들기 때문에, 특성들의 단위나 값의 범위가 다르다면 표준화가 특히 중요
db = DBSCAN(eps=0.3, min_samples=10).fit(X)
labels = db.labels_
print(labels)
# 0, 1, 2, ...: 군집 번호
# -1: 어떤 군집에도 속하지 않은 노이즈


# Number of clusters in labels, ignoring noise if present
# One can access the labels assigend by DBSCAN using the `labels_`
# Noisy samples are given the label -1
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
n_noise = list(labels).count(-1)

print(f"Estimated number of clusters: {n_clusters}")
print(f"Estimated number of noisy points: {n_noise}")
print(f"Homogeneity: {metrics.homogeneity_score(labels_true, labels):.3f}")
print(f"Completeness: {metrics.completeness_score(labels_true, labels):.3f}")
print(f"V-measure: {metrics.v_measure_score(labels_true, labels):.3f}")
print(f"Adjusted Rand Index: {metrics.adjusted_rand_score(labels_true, labels):.3f}")
print(
  "Adjusted Mutual Information:"
  f" {metrics.adjusted_mutual_info_score(labels_true, labels):.3f}"
)
print(f"Silhouette Coefficient: {metrics.silhouette_score(X, labels):.3f}")


unique_labels = set(labels)
core_samples_mask = np.zeros_like(
  labels, dtype=bool
)  # labels와 동일한 크기의 False 배열 생성
core_samples_mask[db.core_sample_indices_] = (
  True  # db.core_sample_indices 는 DBSCAN이 코어 샘플로 판단한 데이터의 인덱스 번호 (indices는 여러 개의 index를 뜻함)
)

colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]


for k, col in zip(unique_labels, colors):
  if k == -1:
    # Black used for noise
    col = [0, 0, 0, 1]

  class_member_mask = (
    labels == k
  )  # 현재 살펴보고 있는 군집 k에 속하는 데이터만 선택하기 위한 불리언 마스크

  xy = X[class_member_mask & core_samples_mask]  # 두 조건을 동시에 만족하는 데이터
  plt.plot(
    xy[:, 0],
    xy[:, 1],
    "o",
    markerfacecolor=tuple(col),
    markeredgecolor="k",
    markersize=14,
  )

  # ~ : bool 값을 반대로 뒤집기
  xy = X[
    class_member_mask & ~core_samples_mask
  ]  # k번 군집에 속하지만 core sample은 아닌 데이터
  # array[row, col]
  # : - 모든 행
  plt.plot(
    xy[:, 0],
    xy[:, 1],
    "o",
    markerfacecolor=tuple(col),
    markeredgecolor="k",
    markersize=6,
  )

plt.title(f"Estimated number of clusters: {n_clusters}")
plt.show()
