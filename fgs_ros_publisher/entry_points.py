# -*- coding: utf-8 -*-
import rclpy

from fgs_publisher import data_loaders, drivers, observers


def test(args=None):
    rclpy.init(args=args)

    loader = data_loaders.TUMRGBImageFileLoader(
        '/Users/fkawata/Desktop/rgbd_dataset_freiburg1_xyz')

    observer_list = [
        observers.CVBridgeObserver('tum'),
        observers.ImagePublisher(),
        ]
    observer_chain = observers.ObservationChain()
    for obs in observer_list:
        observer_chain.add_observer(obs.event)

    driver = drivers.CyclicDriver(
        loader, observer_chain.event, rate_sec=0.033)


    driver.start()
    driver.wait()
