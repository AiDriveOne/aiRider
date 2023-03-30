// file name: customer_service.dart

void updateOrderStatus(Order order, String status) {
  // Update order status
  order.status = status;

  // Notify customer
  String message = 'Your order status has been updated to $status';
  customerService.notifyCustomer(order.customerId, message);
}

void resolveOrderIssue(Order order, String issue) {
  // Update order status
  order.status = 'Issue: $issue';

  // Notify customer
  String message = 'There was an issue with your order: $issue. We apologize for the inconvenience.';
  customerService.notifyCustomer(order.customerId, message);
}
