def calib(sensor_gyro):

    # treating image
    img = 0

    # Afficher les données du gyroscope.
    gyro_data = sensor_gyro.get_gyro_data()
    gyro = gyro_data['x'] + gyro_data['y'] + gyro_data['z']

    # treating compass
    compass = 0

    # treating gps
    gps = 0

    return gyro, img, compass, gps
