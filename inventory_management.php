function updateInventory($orderId) {
  $order = getOrder($orderId);
  $items = $order->getItems();

  foreach ($items as $item) {
    $currentQuantity = getInventory($item->getId());
    if ($currentQuantity < $item->getQuantity()) {
      throw new Exception('Insufficient inventory for item ' . $item->getName());
    }
    updateInventoryLevel($item->getId(), $currentQuantity - $item->getQuantity());
  }
}
