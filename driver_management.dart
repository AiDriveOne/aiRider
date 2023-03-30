// file name: driver_management.dart

void assignDeliveries(List<Driver> drivers, List<Route> routes) {
  for (int i = 0; i < drivers.length; i++) {
    Driver driver = drivers[i];
    Route route = routes[i];

    // Update driver schedule
    driver.schedule.add(route.deliveryTime);

    // Assign deliveries to driver
    for (Order order in route.orders) {
      order.driver = driver;
    }
  }
}
