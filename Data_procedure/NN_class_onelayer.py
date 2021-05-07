# NN with one layer and one neurons to get the boundary curve

import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_excel(r'files.xlsx')
X = data.iloc[:, [0, 1]]
y = data.iloc[:, -1]
model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(1, activation='sigmoid', input_shape=(X.shape[1],)),
])
adam = tf.keras.optimizers.Adam(learning_rate=5e-3)
model.compile(optimizer='adam',
              loss=tf.losses.BinaryCrossentropy(),
              metrics=[tf.keras.metrics.binary_accuracy])

history = model.fit(x=X, y=y, epochs=1000)
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y)
W, b = model.layers[0].get_weights()
a1 = W[0]
a2 = W[1]
plt.plot(X.iloc[:, 0], (-b - a1 * X.iloc[:, 0]) / a2)
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y)
plt.show()
print('weigth:', W)
print('bias:', b)