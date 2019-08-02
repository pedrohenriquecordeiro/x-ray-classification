pip install opencv-python <br />
pip install keras <br />
<br />
<br />
<br />
nano ~/.keras/keras.json<br />
<br />
{<br />
    "epsilon": 1e-07, <br />
    "floatx": "float32", <br />
    "image_data_format": "channels_first", <br />
    "backend": "tensorflow"<br />
}<br />
