// file name: payment_processing.php

function processPayment($paymentInfo) {
  // Verify payment information
  if (!verifyPaymentInfo($paymentInfo)) {
    throw new Exception('Invalid payment information');
  }

  // Process payment
  $paymentResult = processPaymentGateway($paymentInfo);

  // Update payment records
  updatePaymentRecords($paymentInfo, $paymentResult);
}
