#Alishya Xavier, Libraries Notes

import matplotlib.pyplot as plt
import numpy as np
from faker import faker

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
plt.show()                           # Show the figure.

fake = Faker()

fake.name()
# 'Lucy Cechtelar'

fake.address()
# '426 Jordy Lodge
#  Cartwrightshire, SC 88120-6700'

fake.text()
# 'Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi
#  beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt
#  amet quidem. Iusto deleniti cum autem ad quia aperiam.
#  A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur qui
#  quaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernatur
#  voluptatem sit aliquam. Dolores voluptatum est.
#  Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.
#  Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati.
#  Et sint et. Ut ducimus quod nemo ab voluptatum.'

for _ in range(10):
  print(fake.name())

# 'Adaline Reichel'
# 'Dr. Santa Prosacco DVM'
# 'Noemy Vandervort V'
# 'Lexi O'Conner'
# 'Gracie Weber'
# 'Roscoe Johns'
# 'Emmett Lebsack'
# 'Keegan Thiel'
# 'Wellington Koelpin II'
# 'Ms. Karley Kiehn V'