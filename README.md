# Team GAEL - 2024 MATE/NOAA Ocean Exploration Computer Coding Challenge


![GAEL Example](static/demo.gif)

Rohan Vij, Kevin Geng, Shan Kanwar - Dublin High School<br>
Josh Tittiranonda - Stanford Online High School

You can view the Jupyter Notebook for a tutorial on training and inferencing [here](training_and_inference.ipynb).

Documentation (paper, video, spreadsheet, etc) can be found [here](https://drive.google.com/drive/folders/13_QLQmkHtv_PdvRZbzdH0UySW4L2YAw1?usp=sharing).

The trained models (and their associated testing videos) can be found [here](https://drive.google.com/drive/folders/1unqygoG7jHg0SykfKAocx0J4j3OFKjz3?usp=sharing).

<hr>

Note that we had severe limitations with the final capability of the model - we had to use Google Colab due to a lack of home/school training resources and were not able to spend much money to train our models for very long.

YOLOv7's inbuilt calculations recommended a minimum of 171 epochs to train the model on all of the data we provided it - the most we were able to train was 100 epochs (58.4% of the minimum required for decent performance).

When training the model yourself, try to run up to 171 epochs if your compute time and budget allows.

### Acknowledgements
This project would not have been possible without the support of the open-source community and the [creators](https://ieeexplore.ieee.org/document/10204762/authors#authors) of YOLOv7.

### License
This project is licensed under the MIT License. See the [LICENSE](/LICENSE.txt) file for details.
