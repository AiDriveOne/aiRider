// file name: order_processing.dart

void processOrder(Order order) {
  // Validate customer information
  if (order.customerName.isEmpty || order.customerAddress.isEmpty) {
    throw Exception('Invalid customer information');
  }

  // Update inventory levels
  for (OrderItem item in order.items) {
    int currentQuantity = inventory[item.id] ?? 0;
    if (currentQuantity < item.quantity) {
      throw Exception('Insufficient inventory for item ${item.name}');
    }
    inventory[item.id] = currentQuantity - item.quantity;
  }
}
