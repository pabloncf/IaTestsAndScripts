import tensorflow as tf


# Definir os dados de entrada e saída
x = tf.constant([[0.0, 1.0], [1.0, 0.0]])
y = tf.constant([[1.0, 0.0], [0.0, 1.0]])

# Definir a estrutura da rede neural
input_layer = tf.keras.layers.Input(shape=(2,))
hidden_layer = tf.keras.layers.Dense(4, activation='relu')(input_layer)
output_layer = tf.keras.layers.Dense(2, activation='softmax')(hidden_layer)

# Definir o modelo
model = tf.keras.models.Model(inputs=input_layer, outputs=output_layer)

# Compilar o modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Treinar o modelo
model.fit(x, y, epochs=300)

# Testar o modelo
test_data = tf.constant([[0.0, 1.0], [1.0, 0.0]])
predictions = model.predict(test_data)

print(predictions)
